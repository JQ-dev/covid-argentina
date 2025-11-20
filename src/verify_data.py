#!/usr/bin/env python3
"""
Verify that ICD-10 data is loaded correctly.
"""

import pandas as pd
from pathlib import Path


def verify_icd10_data():
    """Verify the ICD-10 data."""
    data_path = Path(__file__).parent.parent / "data" / "icd10cm" / "icd10cm_codes.csv"

    if not data_path.exists():
        print(f"❌ Data file not found: {data_path}")
        return False

    # Load data
    df = pd.read_csv(data_path)

    print("=" * 70)
    print("ICD-10-CM Data Verification")
    print("=" * 70)

    print(f"\n✓ Data file found: {data_path}")
    print(f"✓ Total codes loaded: {len(df):,}")

    # Statistics by chapter
    print(f"\n📊 Statistics:")
    print(f"  Unique chapters: {df['chapter'].nunique()}")
    print(f"  Code types:")
    for code_type, count in df['code_type'].value_counts().items():
        print(f"    - {code_type}: {count:,}")

    # Sample queries
    print(f"\n🔍 Sample Queries:")

    # COPD
    copd_codes = df[df['description'].str.contains('COPD|chronic obstructive', case=False, na=False)]
    print(f"\n  COPD-related codes ({len(copd_codes)} found):")
    for _, row in copd_codes.head(5).iterrows():
        print(f"    {row['code']}: {row['description']}")

    # Diabetes
    diabetes_codes = df[df['description'].str.contains('diabetes', case=False, na=False)]
    print(f"\n  Diabetes-related codes ({len(diabetes_codes)} found):")
    for _, row in diabetes_codes.head(5).iterrows():
        print(f"    {row['code']}: {row['description']}")

    # Respiratory
    respiratory = df[df['chapter'].str.contains('Respiratory', case=False, na=False)]
    print(f"\n  Respiratory system codes: {len(respiratory):,}")

    # Cardiovascular
    cardio = df[df['chapter'].str.contains('Circulatory', case=False, na=False)]
    print(f"  Circulatory system codes: {len(cardio):,}")

    print("\n" + "=" * 70)
    print("✓ Data verification complete!")
    print("=" * 70)

    return True


if __name__ == "__main__":
    verify_icd10_data()
