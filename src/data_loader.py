#!/usr/bin/env python3
"""
Data loader for downloading and processing ICD-10 codes and guidelines.
Downloads official code sets from CDC/NCHS and CMS.
"""

import os
import zipfile
from pathlib import Path
from typing import List, Dict, Optional
import xml.etree.ElementTree as ET

import click
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm


class ICDDataLoader:
    """Loader for ICD-10-CM and ICD-10-PCS data."""

    # Official data sources
    ICD10CM_BASE_URL = "https://www.cdc.gov/nchs/icd/icd-10-cm.htm"
    ICD10PCS_BASE_URL = "https://www.cms.gov/medicare/coding-billing/icd-10-codes"

    # Direct download URLs (these may need to be updated annually)
    ICD10CM_DOWNLOAD_URL = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2024/icd10cm-tabular-2024.xml"
    ICD10CM_GUIDELINES_URL = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2024/icd10cm-guidelines-2024.pdf"

    def __init__(self, data_dir: Optional[Path] = None):
        """Initialize the data loader."""
        self.data_dir = data_dir or Path(__file__).parent.parent / "data"
        self.icd10cm_dir = self.data_dir / "icd10cm"
        self.icd10pcs_dir = self.data_dir / "icd10pcs"

        # Create directories
        self.icd10cm_dir.mkdir(parents=True, exist_ok=True)
        self.icd10pcs_dir.mkdir(parents=True, exist_ok=True)

    def download_file(self, url: str, output_path: Path) -> bool:
        """
        Download a file with progress bar.

        Args:
            url: URL to download from
            output_path: Path to save the file

        Returns:
            True if successful, False otherwise
        """
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))

            with open(output_path, 'wb') as f, tqdm(
                desc=output_path.name,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) as pbar:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))

            return True

        except Exception as e:
            print(f"Error downloading {url}: {e}")
            return False

    def download_icd10cm(self) -> bool:
        """
        Download ICD-10-CM codes and guidelines.

        Returns:
            True if successful
        """
        print("\n[ICD-10-CM] Downloading data...")

        # Download tabular XML
        xml_path = self.icd10cm_dir / "icd10cm_tabular.xml"
        if not xml_path.exists():
            print("Downloading ICD-10-CM tabular data...")
            success = self.download_file(self.ICD10CM_DOWNLOAD_URL, xml_path)
            if not success:
                print("⚠️  Failed to download ICD-10-CM data. You may need to manually download from:")
                print(f"   {self.ICD10CM_BASE_URL}")
                return False
        else:
            print(f"✓ ICD-10-CM data already exists at {xml_path}")

        # Download guidelines PDF
        guidelines_path = self.icd10cm_dir / "icd10cm_guidelines.pdf"
        if not guidelines_path.exists():
            print("Downloading ICD-10-CM guidelines...")
            self.download_file(self.ICD10CM_GUIDELINES_URL, guidelines_path)

        return True

    def download_icd10pcs(self) -> bool:
        """
        Download ICD-10-PCS codes and guidelines.

        Returns:
            True if successful
        """
        print("\n[ICD-10-PCS] Downloading data...")
        print("⚠️  ICD-10-PCS data must be manually downloaded from:")
        print(f"   {self.ICD10PCS_BASE_URL}")
        print(f"   Save the files to: {self.icd10pcs_dir}")

        return True

    def parse_icd10cm_xml(self, xml_path: Optional[Path] = None) -> List[Dict]:
        """
        Parse ICD-10-CM XML file into structured data.

        Args:
            xml_path: Path to XML file

        Returns:
            List of code dictionaries
        """
        xml_path = xml_path or self.icd10cm_dir / "icd10cm_tabular.xml"

        if not xml_path.exists():
            raise FileNotFoundError(f"XML file not found: {xml_path}")

        print(f"\nParsing ICD-10-CM data from {xml_path}...")

        codes = []
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Parse chapters and codes
        for chapter in tqdm(root.findall('.//chapter'), desc="Processing chapters"):
            chapter_name = chapter.find('desc').text if chapter.find('desc') is not None else ""

            # Find all diagnosis codes in this chapter
            for diag in chapter.findall('.//diag'):
                code_elem = diag.find('name')
                desc_elem = diag.find('desc')

                if code_elem is not None and desc_elem is not None:
                    code = code_elem.text
                    description = desc_elem.text

                    # Extract includes/excludes notes
                    includes = []
                    excludes = []

                    for inc in diag.findall('.//includes/note'):
                        if inc.text:
                            includes.append(inc.text)

                    for exc in diag.findall('.//excludes1/note'):
                        if exc.text:
                            excludes.append(exc.text)

                    codes.append({
                        'code': code,
                        'description': description,
                        'chapter': chapter_name,
                        'includes': includes,
                        'excludes': excludes,
                        'code_system': 'ICD-10-CM'
                    })

        print(f"✓ Parsed {len(codes)} ICD-10-CM codes")
        return codes

    def save_codes_to_csv(self, codes: List[Dict], output_path: Path):
        """
        Save codes to CSV file.

        Args:
            codes: List of code dictionaries
            output_path: Path to save CSV
        """
        df = pd.DataFrame(codes)
        df.to_csv(output_path, index=False)
        print(f"✓ Saved codes to {output_path}")

    def process_all(self):
        """Download and process all ICD data."""
        print("=" * 60)
        print("Medical Coding Data Loader")
        print("=" * 60)

        # Download ICD-10-CM
        self.download_icd10cm()

        # Parse and save ICD-10-CM
        try:
            codes = self.parse_icd10cm_xml()
            csv_path = self.icd10cm_dir / "icd10cm_codes.csv"
            self.save_codes_to_csv(codes, csv_path)
        except Exception as e:
            print(f"Error processing ICD-10-CM: {e}")

        # Note about ICD-10-PCS
        self.download_icd10pcs()

        print("\n" + "=" * 60)
        print("Data loading complete!")
        print("=" * 60)
        print(f"\nData saved to: {self.data_dir}")
        print("\nNext steps:")
        print("1. Review the downloaded data")
        print("2. Run: python src/build_index.py")


@click.command()
@click.option('--download-all', is_flag=True, help='Download all available data')
@click.option('--icd10cm-only', is_flag=True, help='Download only ICD-10-CM')
@click.option('--parse-only', is_flag=True, help='Parse existing downloaded files')
@click.option('--data-dir', type=click.Path(), help='Custom data directory')
def main(download_all, icd10cm_only, parse_only, data_dir):
    """Download and process ICD-10 medical codes."""
    loader = ICDDataLoader(data_dir=Path(data_dir) if data_dir else None)

    if parse_only:
        codes = loader.parse_icd10cm_xml()
        csv_path = loader.icd10cm_dir / "icd10cm_codes.csv"
        loader.save_codes_to_csv(codes, csv_path)
    elif icd10cm_only:
        loader.download_icd10cm()
    elif download_all:
        loader.process_all()
    else:
        # Default: process all
        loader.process_all()


if __name__ == "__main__":
    main()
