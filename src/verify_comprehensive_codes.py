#!/usr/bin/env python3
"""
Comprehensive verification of ALL medical code systems.
Shows statistics for ICD-10-CM, HCPCS, CPT, and Revenue codes.
"""

import pandas as pd
from pathlib import Path


def verify_comprehensive_system():
    """Verify all loaded code systems."""
    data_dir = Path(__file__).parent.parent / "data"

    print("=" * 80)
    print("COMPREHENSIVE MEDICAL CODING SYSTEM - FULL VERIFICATION")
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
        print(f"   Total codes: {len(df_icd):,}")
        print(f"   Chapters: {df_icd['chapter'].nunique()}")
        print(f"   Code types: {', '.join(df_icd['code_type'].unique()[:4])}")

    # 2. HCPCS Level II Codes
    hcpcs_path = data_dir / "hcpcs" / "hcpcs_codes_comprehensive.csv"
    if hcpcs_path.exists():
        df_hcpcs = pd.read_csv(hcpcs_path)
        code_systems['HCPCS Level II'] = df_hcpcs
        total_codes += len(df_hcpcs)

        print(f"\n💊 HCPCS Level II (Procedures, Supplies, Equipment)")
        print(f"   Total codes: {len(df_hcpcs):,}")
        print(f"   Categories: {df_hcpcs['category'].nunique()}")
        print(f"   Top categories: {', '.join(df_hcpcs['category'].value_counts().head(3).index.tolist()[:2])}")

    # 3. CPT Codes
    cpt_path = data_dir / "cpt" / "cpt_codes.csv"
    if cpt_path.exists():
        df_cpt = pd.read_csv(cpt_path)
        code_systems['CPT'] = df_cpt
        total_codes += len(df_cpt)

        print(f"\n🏥 CPT (Current Procedural Terminology)")
        print(f"   Total codes: {len(df_cpt):,}")
        print(f"   Categories: {df_cpt['category'].nunique()}")
        print(f"   Note: CPT codes are copyrighted by AMA")

    # 4. Revenue Codes
    revenue_path = data_dir / "revenue_codes" / "revenue_codes.csv"
    if revenue_path.exists():
        df_revenue = pd.read_csv(revenue_path)
        code_systems['Revenue Codes'] = df_revenue
        total_codes += len(df_revenue)

        print(f"\n💰 UB-04 Revenue Codes (Hospital Billing)")
        print(f"   Total codes: {len(df_revenue):,}")
        print(f"   Categories: {df_revenue['category'].nunique()}")

    # Summary
    print("\n" + "=" * 80)
    print(f"TOTAL MEDICAL CODES LOADED: {total_codes:,}")
    print("=" * 80)

    print(f"\nCode System Breakdown:")
    for system, df in code_systems.items():
        percentage = (len(df) / total_codes * 100) if total_codes > 0 else 0
        print(f"  • {system:<25} {len(df):>6,} codes ({percentage:>5.1f}%)")

    # Example Queries
    print("\n" + "=" * 80)
    print("EXAMPLE COMPREHENSIVE QUERIES")
    print("=" * 80)

    # Example 1: COPD
    print(f"\n🔍 EXAMPLE 1: COPD (Chronic Obstructive Pulmonary Disease)")

    if 'ICD-10-CM' in code_systems:
        df = code_systems['ICD-10-CM']
        copd = df[df['description'].str.contains('COPD|chronic obstructive', case=False, na=False)]
        print(f"\n   Diagnosis Codes (ICD-10-CM): {len(copd)} codes")
        for _, row in copd.head(3).iterrows():
            print(f"      {row['code']}: {row['description'][:65]}")

    if 'HCPCS Level II' in code_systems:
        df = code_systems['HCPCS Level II']
        oxygen = df[df['description'].str.contains('oxygen|pulmonary|respiratory', case=False, na=False)]
        print(f"\n   Equipment/Procedures (HCPCS): {len(oxygen)} codes")
        for _, row in oxygen.head(3).iterrows():
            print(f"      {row['code']}: {row['description'][:65]}")

    if 'CPT' in code_systems:
        df = code_systems['CPT']
        pulm = df[df['subcategory'].str.contains('Pulmonary', case=False, na=False)]
        print(f"\n   Procedures (CPT): {len(pulm)} codes")
        for _, row in pulm.head(2).iterrows():
            print(f"      {row['code']}: {row['description'][:65]}")

    if 'Revenue Codes' in code_systems:
        df = code_systems['Revenue Codes']
        resp = df[df['description'].str.contains('respiratory|oxygen', case=False, na=False)]
        print(f"\n   Billing (Revenue): {len(resp)} codes")
        for _, row in resp.head(2).iterrows():
            print(f"      {row['code']}: {row['description'][:65]}")

    # Example 2: Diabetes
    print(f"\n🔍 EXAMPLE 2: Diabetes Management")

    if 'ICD-10-CM' in code_systems:
        df = code_systems['ICD-10-CM']
        diabetes = df[df['description'].str.contains('diabetes', case=False, na=False)]
        print(f"\n   Diagnosis Codes (ICD-10-CM): {len(diabetes)} codes")
        for _, row in diabetes.head(3).iterrows():
            print(f"      {row['code']}: {row['description'][:65]}")

    if 'HCPCS Level II' in code_systems:
        df = code_systems['HCPCS Level II']
        diabetic = df[df['description'].str.contains('glucose|insulin|diabetic', case=False, na=False)]
        print(f"\n   Equipment/Supplies (HCPCS): {len(diabetic)} codes")
        for _, row in diabetic.head(3).iterrows():
            print(f"      {row['code']}: {row['description'][:65]}")

    if 'CPT' in code_systems:
        df = code_systems['CPT']
        diab_procs = df[(df['category'] == 'Pathology and Laboratory') &
                        (df['description'].str.contains('glucose', case=False, na=False))]
        if len(diab_procs) > 0:
            print(f"\n   Lab Tests (CPT): {len(diab_procs)} codes")
            for _, row in diab_procs.head(2).iterrows():
                print(f"      {row['code']}: {row['description'][:65]}")

    # Complete Use Case
    print("\n" + "=" * 80)
    print("COMPLETE USE CASE: Emergency Room Visit for COPD with Oxygen Therapy")
    print("=" * 80)

    use_case = {
        'Diagnosis (ICD-10-CM)': 'J44.1 - COPD with acute exacerbation',
        'Procedure (CPT)': '94640 - Pressurized or nonpressurized inhalation treatment',
        'Equipment (HCPCS)': 'E0424 - Stationary compressed oxygen system, rental',
        'ER Visit (Revenue)': '0450 - Emergency Room - General',
        'Oxygen Supply (Revenue)': '0277 - Medical/Surgical Supplies - Oxygen Take Home',
        'Lab Test (CPT)': '82803 - Blood gases, arterial oxygen saturation'
    }

    for code_type, example in use_case.items():
        print(f"\n   {code_type}:")
        print(f"      {example}")

    # Statistics by category
    print("\n" + "=" * 80)
    print("TOP CATEGORIES BY CODE COUNT")
    print("=" * 80)

    if 'HCPCS Level II' in code_systems:
        df = code_systems['HCPCS Level II']
        print(f"\nHCPCS Top 5 Categories:")
        for i, (cat, count) in enumerate(df['category'].value_counts().head(5).items(), 1):
            print(f"   {i}. {cat}: {count:,} codes")

    if 'CPT' in code_systems:
        df = code_systems['CPT']
        print(f"\nCPT Top 5 Categories:")
        for i, (cat, count) in enumerate(df['category'].value_counts().head(5).items(), 1):
            print(f"   {i}. {cat}: {count:,} codes")

    print("\n" + "=" * 80)
    print("✓ COMPREHENSIVE VERIFICATION COMPLETE")
    print("=" * 80)
    print(f"\nAll {total_codes:,} medical codes are loaded and ready for use!")
    print("\nNext step: Build vector database with:")
    print("  python src/build_index.py")
    print("\nThis will enable semantic search across all code systems!")


if __name__ == "__main__":
    verify_comprehensive_system()
