#!/usr/bin/env python3
"""
Verify all loaded medical code systems.
Shows comprehensive statistics across ICD-10-CM, HCPCS, and Revenue codes.
"""

import pandas as pd
from pathlib import Path


def verify_all_code_systems():
    """Verify all loaded code systems."""
    data_dir = Path(__file__).parent.parent / "data"

    print("=" * 80)
    print("MEDICAL CODING SYSTEM - COMPREHENSIVE VERIFICATION")
    print("=" * 80)

    total_codes = 0
    code_systems = {}

    # 1. ICD-10-CM Diagnosis Codes
    icd10cm_path = data_dir / "icd10cm" / "icd10cm_codes.csv"
    if icd10cm_path.exists():
        df_icd = pd.read_csv(icd10cm_path)
        code_systems['ICD-10-CM'] = df_icd
        total_codes += len(df_icd)

        print(f"\n📋 ICD-10-CM (Diagnosis Codes)")
        print(f"   Location: {icd10cm_path}")
        print(f"   Total codes: {len(df_icd):,}")
        print(f"   Chapters: {df_icd['chapter'].nunique()}")
        print(f"   Sample: {df_icd['code'].iloc[0]} - {df_icd['description'].iloc[0][:50]}...")
    else:
        print(f"\n❌ ICD-10-CM codes not found")

    # 2. HCPCS Level II Codes
    hcpcs_path = data_dir / "hcpcs" / "hcpcs_codes.csv"
    if hcpcs_path.exists():
        df_hcpcs = pd.read_csv(hcpcs_path)
        code_systems['HCPCS Level II'] = df_hcpcs
        total_codes += len(df_hcpcs)

        print(f"\n💊 HCPCS Level II (Procedures, Supplies, Equipment)")
        print(f"   Location: {hcpcs_path}")
        print(f"   Total codes: {len(df_hcpcs):,}")
        print(f"   Categories: {df_hcpcs['category'].nunique()}")
        print(f"   Sample: {df_hcpcs['code'].iloc[0]} - {df_hcpcs['description'].iloc[0][:50]}...")
    else:
        print(f"\n❌ HCPCS codes not found")

    # 3. Revenue Codes
    revenue_path = data_dir / "revenue_codes" / "revenue_codes.csv"
    if revenue_path.exists():
        df_revenue = pd.read_csv(revenue_path)
        code_systems['Revenue Codes'] = df_revenue
        total_codes += len(df_revenue)

        print(f"\n🏥 UB-04 Revenue Codes (Hospital Billing)")
        print(f"   Location: {revenue_path}")
        print(f"   Total codes: {len(df_revenue):,}")
        print(f"   Categories: {df_revenue['category'].nunique()}")
        print(f"   Sample: {df_revenue['code'].iloc[0]} - {df_revenue['description'].iloc[0][:50]}...")
    else:
        print(f"\n❌ Revenue codes not found")

    # Summary
    print("\n" + "=" * 80)
    print(f"TOTAL MEDICAL CODES LOADED: {total_codes:,}")
    print("=" * 80)

    print(f"\nCode Systems Breakdown:")
    for system, df in code_systems.items():
        print(f"  • {system}: {len(df):,} codes")

    # Example Queries
    print("\n" + "=" * 80)
    print("EXAMPLE QUERIES")
    print("=" * 80)

    if 'ICD-10-CM' in code_systems:
        df = code_systems['ICD-10-CM']

        # COPD Example (User's request)
        print(f"\n🔍 Query: 'COPD' (Chronic Obstructive Pulmonary Disease)")
        copd = df[df['description'].str.contains('COPD|chronic obstructive', case=False, na=False)]
        print(f"   Found {len(copd)} codes:")
        for _, row in copd.head(5).iterrows():
            print(f"      {row['code']}: {row['description']}")

        # Diabetes
        print(f"\n🔍 Query: 'Diabetes'")
        diabetes = df[df['description'].str.contains('diabetes', case=False, na=False)]
        print(f"   Found {len(diabetes)} codes:")
        for _, row in diabetes.head(3).iterrows():
            print(f"      {row['code']}: {row['description']}")

        # Heart attack / MI
        print(f"\n🔍 Query: 'Myocardial Infarction' (Heart Attack)")
        mi = df[df['description'].str.contains('myocardial infarction', case=False, na=False)]
        print(f"   Found {len(mi)} codes:")
        for _, row in mi.head(3).iterrows():
            print(f"      {row['code']}: {row['description']}")

    if 'HCPCS Level II' in code_systems:
        df = code_systems['HCPCS Level II']

        print(f"\n🔍 Query: 'Oxygen Equipment' (HCPCS)")
        oxygen = df[df['description'].str.contains('oxygen|CPAP', case=False, na=False)]
        print(f"   Found {len(oxygen)} codes:")
        for _, row in oxygen.iterrows():
            print(f"      {row['code']}: {row['description']}")

    if 'Revenue Codes' in code_systems:
        df = code_systems['Revenue Codes']

        print(f"\n🔍 Query: 'Emergency Room' (Revenue Codes)")
        er = df[df['description'].str.contains('emergency', case=False, na=False)]
        print(f"   Found {len(er)} codes:")
        for _, row in er.iterrows():
            print(f"      {row['code']}: {row['description']}")

    # Use Case Example
    print("\n" + "=" * 80)
    print("EXAMPLE USE CASE: Patient with COPD receiving oxygen therapy")
    print("=" * 80)

    if 'ICD-10-CM' in code_systems:
        df_icd = code_systems['ICD-10-CM']
        copd_codes = df_icd[df_icd['code'].str.startswith('J44', na=False)]
        print(f"\n✓ Diagnosis Code (ICD-10-CM):")
        if not copd_codes.empty:
            row = copd_codes.iloc[0]
            print(f"   {row['code']}: {row['description']}")

    if 'HCPCS Level II' in code_systems:
        df_hcpcs = code_systems['HCPCS Level II']
        oxygen_codes = df_hcpcs[df_hcpcs['description'].str.contains('oxygen', case=False, na=False)]
        print(f"\n✓ Equipment/Procedure Code (HCPCS):")
        if not oxygen_codes.empty:
            row = oxygen_codes.iloc[0]
            print(f"   {row['code']}: {row['description']}")

    if 'Revenue Codes' in code_systems:
        df_rev = code_systems['Revenue Codes']
        resp_codes = df_rev[df_rev['description'].str.contains('respiratory|oxygen', case=False, na=False)]
        print(f"\n✓ Billing Code (Revenue):")
        if not resp_codes.empty:
            row = resp_codes.iloc[0]
            print(f"   {row['code']}: {row['description']}")
        else:
            # Use pharmacy or supplies
            supply_codes = df_rev[df_rev['category'] == 'Supplies']
            if not supply_codes.empty:
                row = supply_codes.iloc[0]
                print(f"   {row['code']}: {row['description']}")

    print("\n" + "=" * 80)
    print("✓ VERIFICATION COMPLETE")
    print("=" * 80)
    print(f"\nAll {total_codes:,} medical codes are loaded and ready for use!")
    print("\nNext step: Build vector database with:")
    print("  python src/build_index.py")


if __name__ == "__main__":
    verify_all_code_systems()
