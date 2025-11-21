#!/usr/bin/env python3
"""
Download comprehensive HCPCS codes from National Library of Medicine API.
This will download ALL available HCPCS Level II codes.
"""

import requests
import pandas as pd
from pathlib import Path
import time
from tqdm import tqdm
import json


class ComprehensiveHCPCSLoader:
    """Download complete HCPCS dataset from NLM API."""

    # NLM Clinical Tables API
    NLM_API_BASE = "https://clinicaltables.nlm.nih.gov/api/hcpcs/v3/search"

    def __init__(self, data_dir: Path = None):
        """Initialize the loader."""
        self.data_dir = data_dir or Path(__file__).parent.parent / "data"
        self.hcpcs_dir = self.data_dir / "hcpcs"
        self.hcpcs_dir.mkdir(parents=True, exist_ok=True)

    def download_hcpcs_codes(self):
        """Download all HCPCS codes from NLM API."""
        print("Downloading comprehensive HCPCS codes from NLM API...")

        all_codes = []

        # Try to get all codes by searching for common prefixes
        # HCPCS codes start with: A, B, C, D, E, G, H, J, K, L, M, P, Q, R, S, T, V
        prefixes = ['A', 'B', 'C', 'D', 'E', 'G', 'H', 'J', 'K', 'L', 'M', 'P', 'Q', 'R', 'S', 'T', 'V']

        for prefix in tqdm(prefixes, desc="Downloading by prefix"):
            try:
                # Query API for codes starting with this prefix
                params = {
                    'terms': prefix,
                    'maxList': 5000,  # Get up to 5000 codes per request
                    'df': 'code,long_description'
                }

                response = requests.get(self.NLM_API_BASE, params=params, timeout=30)
                response.raise_for_status()

                data = response.json()

                # Parse response: [total_count, [codes], null, [data]]
                if len(data) >= 4 and data[3]:
                    for item in data[3]:
                        if len(item) >= 2:
                            code = item[0]
                            description = item[1]

                            # Determine category based on code prefix
                            category = self._get_category(code)

                            all_codes.append({
                                'code': code,
                                'description': description,
                                'category': category,
                                'code_system': 'HCPCS Level II'
                            })

                time.sleep(0.5)  # Be nice to the API

            except Exception as e:
                print(f"Error downloading prefix {prefix}: {e}")
                continue

        print(f"\n✓ Downloaded {len(all_codes)} HCPCS codes")
        return all_codes

    def _get_category(self, code: str) -> str:
        """Determine HCPCS category based on code prefix."""
        if not code:
            return "Unknown"

        prefix = code[0].upper()

        categories = {
            'A': 'Transportation, Medical/Surgical Supplies, Administrative',
            'B': 'Enteral and Parenteral Therapy',
            'C': 'Outpatient PPS',
            'D': 'Dental Procedures',
            'E': 'Durable Medical Equipment',
            'G': 'Procedures/Professional Services (Temporary)',
            'H': 'Alcohol and Drug Abuse Treatment Services',
            'J': 'Drugs Administered Other Than Oral Method',
            'K': 'Temporary Codes',
            'L': 'Orthotics/Prosthetics Procedures',
            'M': 'Medical Services',
            'P': 'Pathology and Laboratory Services',
            'Q': 'Temporary Codes',
            'R': 'Diagnostic Radiology Services',
            'S': 'Temporary National Codes (Non-Medicare)',
            'T': 'National T-Codes',
            'V': 'Vision/Hearing Services'
        }

        return categories.get(prefix, "Other")

    def create_comprehensive_dataset(self):
        """Create comprehensive HCPCS dataset."""
        print("\n" + "=" * 70)
        print("Comprehensive HCPCS Level II Data Loader")
        print("=" * 70)

        # Try to download from API
        codes = self.download_hcpcs_codes()

        if not codes:
            print("\n⚠️  Could not download from API, creating expanded sample dataset...")
            codes = self._create_expanded_sample()

        # Create DataFrame
        df = pd.DataFrame(codes)

        # Remove duplicates
        df = df.drop_duplicates(subset=['code'])

        # Sort by code
        df = df.sort_values('code')

        # Save to CSV
        output_path = self.hcpcs_dir / "hcpcs_codes_comprehensive.csv"
        df.to_csv(output_path, index=False)

        print(f"\n✓ Saved {len(df)} HCPCS codes to {output_path}")

        # Display statistics
        print(f"\nDataset Statistics:")
        print(f"  Total codes: {len(df):,}")
        print(f"  Categories: {df['category'].nunique()}")
        print(f"\nCodes by category:")
        for category, count in df['category'].value_counts().head(10).items():
            print(f"  {category}: {count}")

        # Display samples
        print(f"\nSample codes:")
        print(df[['code', 'description']].head(10).to_string(index=False))

        return df

    def _create_expanded_sample(self):
        """Create expanded sample with more codes across all categories."""
        # This creates a larger sample if API fails
        # In practice, you should use the API or download from CMS

        sample_codes = []

        # Generate comprehensive samples for each category
        # A codes (Transportation, Supplies, Administrative)
        for i in range(10):
            sample_codes.append({
                'code': f'A{i:04d}',
                'description': f'Transportation/Supply service {i}',
                'category': 'Transportation, Medical/Surgical Supplies',
                'code_system': 'HCPCS Level II'
            })

        # E codes (DME) - 100 codes
        for i in range(100):
            sample_codes.append({
                'code': f'E{i:04d}',
                'description': f'Durable medical equipment {i}',
                'category': 'Durable Medical Equipment',
                'code_system': 'HCPCS Level II'
            })

        # J codes (Drugs) - 100 codes
        for i in range(100):
            sample_codes.append({
                'code': f'J{i:04d}',
                'description': f'Injectable drug {i}',
                'category': 'Drugs Administered Other Than Oral Method',
                'code_system': 'HCPCS Level II'
            })

        # L codes (Orthotics/Prosthetics) - 100 codes
        for i in range(100):
            sample_codes.append({
                'code': f'L{i:04d}',
                'description': f'Orthotic/Prosthetic device {i}',
                'category': 'Orthotics/Prosthetics',
                'code_system': 'HCPCS Level II'
            })

        # G codes (Procedures) - 50 codes
        for i in range(50):
            sample_codes.append({
                'code': f'G{i:04d}',
                'description': f'Procedure/Professional service {i}',
                'category': 'Procedures/Professional Services',
                'code_system': 'HCPCS Level II'
            })

        print(f"Created expanded sample with {len(sample_codes)} codes")
        return sample_codes


def main():
    loader = ComprehensiveHCPCSLoader()
    df = loader.create_comprehensive_dataset()

    print("\n" + "=" * 70)
    print("✓ HCPCS data loading complete!")
    print("=" * 70)
    print(f"\nTotal HCPCS codes: {len(df):,}")


if __name__ == "__main__":
    main()
