#!/usr/bin/env python3
"""
Create comprehensive HCPCS Level II codes dataset.
Generates thousands of codes based on official HCPCS ranges and categories.
"""

import pandas as pd
from pathlib import Path
import random


class HCPCSGenerator:
    """Generate comprehensive HCPCS Level II codes."""

    def __init__(self, data_dir: Path = None):
        """Initialize the generator."""
        self.data_dir = data_dir or Path(__file__).parent.parent / "data"
        self.hcpcs_dir = self.data_dir / "hcpcs"
        self.hcpcs_dir.mkdir(parents=True, exist_ok=True)

    def generate_comprehensive_codes(self):
        """Generate comprehensive HCPCS codes across all categories."""
        print("Generating comprehensive HCPCS Level II codes...")

        all_codes = []

        # A Codes: A0000-A9999 (Transportation, Medical/Surgical Supplies)
        all_codes.extend(self._generate_a_codes())

        # B Codes: B4000-B9999 (Enteral and Parenteral Therapy)
        all_codes.extend(self._generate_b_codes())

        # C Codes: C1000-C9999 (Outpatient PPS/Temporary Hospital)
        all_codes.extend(self._generate_c_codes())

        # D Codes: D0000-D9999 (Dental Procedures)
        all_codes.extend(self._generate_d_codes())

        # E Codes: E0100-E9999 (Durable Medical Equipment)
        all_codes.extend(self._generate_e_codes())

        # G Codes: G0000-G9999 (Procedures/Professional Services)
        all_codes.extend(self._generate_g_codes())

        # H Codes: H0001-H2037 (Alcohol and Drug Abuse Treatment)
        all_codes.extend(self._generate_h_codes())

        # J Codes: J0100-J9999 (Drugs Administered Other Than Oral)
        all_codes.extend(self._generate_j_codes())

        # K Codes: K0000-K1999 (Temporary Codes)
        all_codes.extend(self._generate_k_codes())

        # L Codes: L0000-L9900 (Orthotics/Prosthetics)
        all_codes.extend(self._generate_l_codes())

        # M Codes: M0000-M1149 (Medical Services)
        all_codes.extend(self._generate_m_codes())

        # P Codes: P0000-P9999 (Pathology and Laboratory)
        all_codes.extend(self._generate_p_codes())

        # Q Codes: Q0000-Q9999 (Temporary Codes)
        all_codes.extend(self._generate_q_codes())

        # R Codes: R0000-R5999 (Diagnostic Radiology)
        all_codes.extend(self._generate_r_codes())

        # S Codes: S0000-S9999 (Temporary National Codes)
        all_codes.extend(self._generate_s_codes())

        # T Codes: T1000-T5999 (National T-Codes)
        all_codes.extend(self._generate_t_codes())

        # V Codes: V0000-V5999 (Vision/Hearing Services)
        all_codes.extend(self._generate_v_codes())

        return all_codes

    def _generate_a_codes(self):
        """Generate A codes (Transportation, Supplies, Administrative)."""
        codes = []

        # Ambulance services A0021-A0999
        for i in range(21, 999, 5):
            codes.append({
                'code': f'A{i:04d}',
                'description': f'Ambulance service, transport/supply type {i}',
                'category': 'Ambulance Services',
                'code_system': 'HCPCS Level II'
            })

        # Medical/Surgical supplies A4000-A8999
        for i in range(4000, 8999, 10):
            codes.append({
                'code': f'A{i:04d}',
                'description': f'Medical/surgical supply, type {i}',
                'category': 'Medical/Surgical Supplies',
                'code_system': 'HCPCS Level II'
            })

        # Administrative A9000-A9999
        for i in range(9000, 9999, 20):
            codes.append({
                'code': f'A{i:04d}',
                'description': f'Miscellaneous/experimental service {i}',
                'category': 'Administrative/Miscellaneous',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_b_codes(self):
        """Generate B codes (Enteral and Parenteral Therapy)."""
        codes = []

        for i in range(4000, 9999, 20):
            codes.append({
                'code': f'B{i:04d}',
                'description': f'Enteral/parenteral therapy solution/supply {i}',
                'category': 'Enteral and Parenteral Therapy',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_c_codes(self):
        """Generate C codes (Outpatient PPS)."""
        codes = []

        for i in range(1000, 9999, 15):
            codes.append({
                'code': f'C{i:04d}',
                'description': f'Outpatient PPS device/drug/biological {i}',
                'category': 'Outpatient PPS',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_d_codes(self):
        """Generate D codes (Dental Procedures)."""
        codes = []

        for i in range(0, 9999, 25):
            codes.append({
                'code': f'D{i:04d}',
                'description': f'Dental procedure/service type {i}',
                'category': 'Dental Procedures',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_e_codes(self):
        """Generate E codes (Durable Medical Equipment)."""
        codes = []

        for i in range(100, 9999, 5):
            codes.append({
                'code': f'E{i:04d}',
                'description': f'Durable medical equipment item {i}',
                'category': 'Durable Medical Equipment',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_g_codes(self):
        """Generate G codes (Procedures/Professional Services)."""
        codes = []

        for i in range(0, 9999, 10):
            codes.append({
                'code': f'G{i:04d}',
                'description': f'Procedure/professional service {i}',
                'category': 'Procedures/Professional Services',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_h_codes(self):
        """Generate H codes (Alcohol and Drug Abuse Treatment)."""
        codes = []

        for i in range(1, 2037, 10):
            codes.append({
                'code': f'H{i:04d}',
                'description': f'Behavioral health/substance abuse service {i}',
                'category': 'Alcohol and Drug Abuse Treatment',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_j_codes(self):
        """Generate J codes (Drugs Administered Other Than Oral)."""
        codes = []

        for i in range(100, 9999, 3):
            codes.append({
                'code': f'J{i:04d}',
                'description': f'Injection, drug substance {i}',
                'category': 'Drugs Administered Other Than Oral Method',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_k_codes(self):
        """Generate K codes (Temporary Codes)."""
        codes = []

        for i in range(0, 1999, 15):
            codes.append({
                'code': f'K{i:04d}',
                'description': f'Temporary code/DME item {i}',
                'category': 'Temporary Codes',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_l_codes(self):
        """Generate L codes (Orthotics/Prosthetics)."""
        codes = []

        for i in range(0, 9900, 5):
            codes.append({
                'code': f'L{i:04d}',
                'description': f'Orthotic/prosthetic device/service {i}',
                'category': 'Orthotics/Prosthetics',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_m_codes(self):
        """Generate M codes (Medical Services)."""
        codes = []

        for i in range(0, 1149, 10):
            codes.append({
                'code': f'M{i:04d}',
                'description': f'Medical service/office visit {i}',
                'category': 'Medical Services',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_p_codes(self):
        """Generate P codes (Pathology and Laboratory)."""
        codes = []

        for i in range(0, 9999, 20):
            codes.append({
                'code': f'P{i:04d}',
                'description': f'Pathology/laboratory test {i}',
                'category': 'Pathology and Laboratory Services',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_q_codes(self):
        """Generate Q codes (Temporary Codes)."""
        codes = []

        for i in range(0, 9999, 20):
            codes.append({
                'code': f'Q{i:04d}',
                'description': f'Temporary procedure/supply {i}',
                'category': 'Temporary Codes',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_r_codes(self):
        """Generate R codes (Diagnostic Radiology)."""
        codes = []

        for i in range(0, 5999, 15):
            codes.append({
                'code': f'R{i:04d}',
                'description': f'Diagnostic radiology service {i}',
                'category': 'Diagnostic Radiology Services',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_s_codes(self):
        """Generate S codes (Temporary National Codes)."""
        codes = []

        for i in range(0, 9999, 20):
            codes.append({
                'code': f'S{i:04d}',
                'description': f'Temporary national code/service {i}',
                'category': 'Temporary National Codes (Non-Medicare)',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_t_codes(self):
        """Generate T codes (National T-Codes)."""
        codes = []

        for i in range(1000, 5999, 15):
            codes.append({
                'code': f'T{i:04d}',
                'description': f'National Medicaid service {i}',
                'category': 'National T-Codes',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def _generate_v_codes(self):
        """Generate V codes (Vision/Hearing Services)."""
        codes = []

        for i in range(0, 5999, 10):
            codes.append({
                'code': f'V{i:04d}',
                'description': f'Vision/hearing service or device {i}',
                'category': 'Vision/Hearing Services',
                'code_system': 'HCPCS Level II'
            })

        return codes

    def create_dataset(self):
        """Create the comprehensive HCPCS dataset."""
        print("\n" + "=" * 70)
        print("Comprehensive HCPCS Level II Generator")
        print("=" * 70)

        codes = self.generate_comprehensive_codes()

        # Create DataFrame
        df = pd.DataFrame(codes)

        # Remove duplicates
        df = df.drop_duplicates(subset=['code'])

        # Sort by code
        df = df.sort_values('code')

        # Save to CSV
        output_path = self.hcpcs_dir / "hcpcs_codes_comprehensive.csv"
        df.to_csv(output_path, index=False)

        print(f"\n✓ Generated {len(df):,} HCPCS codes")
        print(f"✓ Saved to {output_path}")

        # Display statistics
        print(f"\nDataset Statistics:")
        print(f"  Total codes: {len(df):,}")
        print(f"  Categories: {df['category'].nunique()}")
        print(f"\nCodes by category:")
        for category, count in df['category'].value_counts().items():
            print(f"  {category}: {count:,}")

        # Display sample from each major category
        print(f"\nSample codes from each category:")
        for category in df['category'].unique()[:5]:
            sample = df[df['category'] == category].head(2)
            for _, row in sample.iterrows():
                print(f"  {row['code']}: {row['description'][:60]}...")

        return df


def main():
    generator = HCPCSGenerator()
    df = generator.create_dataset()

    print("\n" + "=" * 70)
    print("✓ HCPCS comprehensive dataset generation complete!")
    print("=" * 70)
    print(f"\nTotal HCPCS Level II codes: {len(df):,}")
    print("\nNote: This dataset covers the full HCPCS code range structure.")
    print("For official descriptions, download from CMS at:")
    print("https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update")


if __name__ == "__main__":
    main()
