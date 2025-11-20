#!/usr/bin/env python3
"""
Download HCPCS codes from CMS official source.
HCPCS (Healthcare Common Procedure Coding System) includes:
- Level I: CPT codes (copyrighted by AMA, not freely available)
- Level II: National codes (A-V codes, publicly available from CMS)
"""

import os
import zipfile
import requests
from pathlib import Path
from io import BytesIO
import pandas as pd
from tqdm import tqdm


class HCPCSDataLoader:
    """Loader for HCPCS Level II codes from CMS."""

    # CMS HCPCS file URLs (updated quarterly)
    # These URLs are for the Alpha-Numeric HCPCS files
    CMS_HCPCS_BASE = "https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system"

    def __init__(self, data_dir: Path = None):
        """Initialize the HCPCS data loader."""
        self.data_dir = data_dir or Path(__file__).parent.parent / "data"
        self.hcpcs_dir = self.data_dir / "hcpcs"
        self.hcpcs_dir.mkdir(parents=True, exist_ok=True)

    def create_sample_hcpcs_data(self):
        """
        Create sample HCPCS Level II codes.
        Note: Full HCPCS data should be downloaded from CMS.
        This creates a representative sample for demonstration.
        """
        print("Creating sample HCPCS Level II codes...")

        # Sample HCPCS codes (real codes, sample data)
        sample_codes = [
            # Durable Medical Equipment (E codes)
            {"code": "E0100", "description": "Cane, includes canes of all materials, adjustable or fixed, with tip", "category": "Durable Medical Equipment"},
            {"code": "E0130", "description": "Walker, rigid (pickup), adjustable or fixed height", "category": "Durable Medical Equipment"},
            {"code": "E0163", "description": "Commode chair, mobile or stationary, with detachable arms", "category": "Durable Medical Equipment"},
            {"code": "E0601", "description": "Continuous positive airway pressure (CPAP) device", "category": "Durable Medical Equipment"},

            # Ambulance Services (A codes)
            {"code": "A0425", "description": "Ground mileage, per statute mile", "category": "Ambulance Services"},
            {"code": "A0428", "description": "Ambulance service, basic life support, non-emergency transport (BLS)", "category": "Ambulance Services"},
            {"code": "A0429", "description": "Ambulance service, basic life support, emergency transport (BLS-emergency)", "category": "Ambulance Services"},
            {"code": "A0433", "description": "Advanced life support, level 2 (ALS 2)", "category": "Ambulance Services"},

            # Drugs (J codes)
            {"code": "J0129", "description": "Injection, abatacept, 10 mg", "category": "Drugs Administered Other Than Oral Method"},
            {"code": "J0178", "description": "Injection, aflibercept, 1 mg", "category": "Drugs Administered Other Than Oral Method"},
            {"code": "J1644", "description": "Injection, heparin sodium, per 1000 units", "category": "Drugs Administered Other Than Oral Method"},
            {"code": "J1817", "description": "Injection, insulin for administration through DME (insulin pump) per 50 units", "category": "Drugs Administered Other Than Oral Method"},
            {"code": "J2001", "description": "Injection, lidocaine HCl for intravenous infusion, 10 mg", "category": "Drugs Administered Other Than Oral Method"},
            {"code": "J3420", "description": "Injection, vitamin B-12 cyanocobalamin, up to 1000 mcg", "category": "Drugs Administered Other Than Oral Method"},

            # Lab/Pathology (G codes)
            {"code": "G0101", "description": "Cervical or vaginal cancer screening; pelvic and clinical breast examination", "category": "Procedures/Professional Services"},
            {"code": "G0103", "description": "Prostate cancer screening; prostate specific antigen test (PSA)", "category": "Procedures/Professional Services"},
            {"code": "G0106", "description": "Colorectal cancer screening; alternative to G0105, screening colonoscopy, barium enema", "category": "Procedures/Professional Services"},
            {"code": "G0180", "description": "Physician certification for Medicare-covered home health services", "category": "Procedures/Professional Services"},
            {"code": "G0202", "description": "Screening mammography, bilateral (2-view film study of each breast)", "category": "Procedures/Professional Services"},

            # Prosthetics/Orthotics (L codes)
            {"code": "L0112", "description": "Cranial cervical orthosis, congenital torticollis type", "category": "Orthotics"},
            {"code": "L0220", "description": "Thoracic rib belt, custom fabricated", "category": "Orthotics"},
            {"code": "L1680", "description": "Knee ankle foot orthosis (KAFO), single upright, free knee", "category": "Orthotics"},
            {"code": "L5000", "description": "Partial foot, shoe insert with longitudinal arch, toe filler", "category": "Prosthetics"},
            {"code": "L5100", "description": "Below knee, molded socket, shin, SACH foot", "category": "Prosthetics"},

            # Supplies (A codes - supplies)
            {"code": "A4206", "description": "Syringe with needle, sterile, 1 cc or less, each", "category": "Medical Supplies"},
            {"code": "A4211", "description": "Supplies for self-administered injections", "category": "Medical Supplies"},
            {"code": "A4233", "description": "Replacement battery, alkaline (other than J cell), for use with medically necessary home blood glucose monitor", "category": "Medical Supplies"},
            {"code": "A4253", "description": "Blood glucose test or reagent strips for home blood glucose monitor, per 50 strips", "category": "Medical Supplies"},
            {"code": "A4554", "description": "Disposable underpads, all sizes", "category": "Medical Supplies"},

            # Oxygen and Related Supplies (E codes - oxygen)
            {"code": "E0424", "description": "Stationary compressed gaseous oxygen system, rental", "category": "Oxygen and Equipment"},
            {"code": "E0431", "description": "Portable gaseous oxygen system, rental", "category": "Oxygen and Equipment"},
            {"code": "E0445", "description": "Oximeter device for measuring blood oxygen levels non-invasively", "category": "Oxygen and Equipment"},

            # Vision/Hearing (V codes)
            {"code": "V2020", "description": "Frames, purchases", "category": "Vision Services"},
            {"code": "V2100", "description": "Sphere, single vision, plano to plus or minus 4.00, per lens", "category": "Vision Services"},
            {"code": "V2627", "description": "Slab off prism, glass or plastic, per lens", "category": "Vision Services"},
            {"code": "V5008", "description": "Hearing screening", "category": "Hearing Services"},
            {"code": "V5014", "description": "Repair/modification of a hearing aid", "category": "Hearing Services"},

            # Dental (D codes - note: limited in HCPCS, mainly in CDT)
            {"code": "D0120", "description": "Periodic oral evaluation - established patient", "category": "Dental Services"},
            {"code": "D0150", "description": "Comprehensive oral evaluation - new or established patient", "category": "Dental Services"},

            # Temporary Codes (C codes)
            {"code": "C1713", "description": "Anchor/screw for opposing bone-to-bone or soft tissue-to-bone", "category": "Outpatient PPS"},
            {"code": "C1725", "description": "Catheter, transluminal angioplasty, non-laser", "category": "Outpatient PPS"},
            {"code": "C9145", "description": "Injection, aprepitant, 1 mg", "category": "Outpatient PPS"},

            # Additional common codes
            {"code": "Q0091", "description": "Screening Papanicolaou smear; obtaining, preparing and conveyance of cervical or vaginal smear to laboratory", "category": "Temporary Codes"},
            {"code": "Q4081", "description": "Injection, epoetin alfa, 100 units (for ESRD on dialysis)", "category": "Temporary Codes"},
            {"code": "S0630", "description": "Removal of sutures by a physician other than the physician who originally closed the wound", "category": "Non-Medicare"},
        ]

        df = pd.DataFrame(sample_codes)
        df['code_system'] = 'HCPCS Level II'

        output_path = self.hcpcs_dir / "hcpcs_codes.csv"
        df.to_csv(output_path, index=False)

        print(f"\n✓ Created sample HCPCS data with {len(df)} codes")
        print(f"✓ Saved to: {output_path}")

        # Display statistics
        print(f"\nSample by category:")
        for category, count in df['category'].value_counts().items():
            print(f"  {category}: {count}")

        return df

    def download_official_cms_data(self):
        """
        Instructions for downloading official CMS HCPCS data.
        Note: Direct download URLs change quarterly.
        """
        print("\n" + "="*70)
        print("To download official HCPCS Level II codes from CMS:")
        print("="*70)
        print("\n1. Visit: https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update")
        print("\n2. Download the latest Alpha-Numeric HCPCS File (ZIP)")
        print("\n3. Extract the files to:", self.hcpcs_dir)
        print("\n4. Look for files like 'HCPC####_CONTR_ANWEB.xlsx'")
        print("\n5. Convert to CSV and save as 'hcpcs_codes_official.csv'")
        print("\n" + "="*70)


def main():
    loader = HCPCSDataLoader()

    print("=" * 70)
    print("HCPCS Level II Data Loader")
    print("=" * 70)

    # Create sample data
    df = loader.create_sample_hcpcs_data()

    # Show download instructions
    loader.download_official_cms_data()

    print("\n✓ Sample HCPCS data created!")
    print(f"  Location: {loader.hcpcs_dir}")
    print(f"  Total codes: {len(df)}")

    print("\nNote: This is a sample dataset. For complete HCPCS data,")
    print("download from CMS using the instructions above.")


if __name__ == "__main__":
    main()
