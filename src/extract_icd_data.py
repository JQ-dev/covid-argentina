#!/usr/bin/env python3
"""
Extract ICD-10 codes from simple_icd_10 package and create CSV database.
"""

import pandas as pd
from pathlib import Path
import simple_icd_10 as icd10
from tqdm import tqdm

def extract_all_icd10_codes():
    """Extract all ICD-10 codes with descriptions."""
    print("Extracting ICD-10-CM codes from simple_icd_10 package...")

    # Get all valid ICD-10 codes
    all_codes = icd10.get_all_codes()

    print(f"Found {len(all_codes)} ICD-10 codes")

    # Extract details for each code
    codes_data = []

    for code in tqdm(all_codes, desc="Processing codes"):
        try:
            description = icd10.get_description(code)

            # Determine chapter
            chapter = ""
            if code:
                first_char = code[0].upper()
                chapter_map = {
                    'A': 'Infectious and Parasitic Diseases (A00-B99)',
                    'B': 'Infectious and Parasitic Diseases (A00-B99)',
                    'C': 'Neoplasms (C00-D49)',
                    'D': 'Diseases of Blood and Immune System / Neoplasms (D50-D89)',
                    'E': 'Endocrine, Nutritional and Metabolic Diseases (E00-E89)',
                    'F': 'Mental, Behavioral and Neurodevelopmental Disorders (F01-F99)',
                    'G': 'Diseases of the Nervous System (G00-G99)',
                    'H': 'Diseases of Eye/Ear and Adnexa (H00-H95)',
                    'I': 'Diseases of the Circulatory System (I00-I99)',
                    'J': 'Diseases of the Respiratory System (J00-J99)',
                    'K': 'Diseases of the Digestive System (K00-K95)',
                    'L': 'Diseases of the Skin and Subcutaneous Tissue (L00-L99)',
                    'M': 'Diseases of the Musculoskeletal System (M00-M99)',
                    'N': 'Diseases of the Genitourinary System (N00-N99)',
                    'O': 'Pregnancy, Childbirth and the Puerperium (O00-O9A)',
                    'P': 'Certain Conditions Originating in the Perinatal Period (P00-P96)',
                    'Q': 'Congenital Malformations, Deformations (Q00-Q99)',
                    'R': 'Symptoms, Signs and Abnormal Clinical Findings (R00-R99)',
                    'S': 'Injury, Poisoning (S00-T88)',
                    'T': 'Injury, Poisoning (S00-T88)',
                    'V': 'External Causes of Morbidity (V00-Y99)',
                    'W': 'External Causes of Morbidity (V00-Y99)',
                    'X': 'External Causes of Morbidity (V00-Y99)',
                    'Y': 'External Causes of Morbidity (V00-Y99)',
                    'Z': 'Factors Influencing Health Status (Z00-Z99)',
                }
                chapter = chapter_map.get(first_char, "")

            # Determine if it's a category, subcategory, or leaf
            code_type = ""
            if icd10.is_chapter(code):
                code_type = "chapter"
            elif icd10.is_block(code):
                code_type = "block"
            elif icd10.is_category(code):
                code_type = "category"
            elif icd10.is_subcategory(code):
                code_type = "subcategory"
            elif icd10.is_leaf(code):
                code_type = "leaf"

            codes_data.append({
                'code': code,
                'description': description,
                'chapter': chapter,
                'code_type': code_type,
                'includes': '',  # Will be empty for this source
                'excludes': '',  # Will be empty for this source
                'code_system': 'ICD-10-CM'
            })

        except Exception as e:
            print(f"Error processing code {code}: {e}")
            continue

    return codes_data


def main():
    # Extract codes
    codes_data = extract_all_icd10_codes()

    # Create DataFrame
    df = pd.DataFrame(codes_data)

    # Save to CSV
    output_dir = Path(__file__).parent.parent / "data" / "icd10cm"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "icd10cm_codes.csv"
    df.to_csv(output_path, index=False)

    print(f"\n✓ Successfully saved {len(df)} ICD-10-CM codes to {output_path}")

    # Display statistics
    print("\nDataset Statistics:")
    print(f"  Total codes: {len(df)}")
    print(f"  Chapters: {df['chapter'].nunique()}")
    print(f"  Code types:")
    for code_type, count in df['code_type'].value_counts().items():
        print(f"    {code_type}: {count}")

    # Show sample
    print("\nSample codes:")
    print(df[['code', 'description', 'chapter']].head(10).to_string(index=False))


if __name__ == "__main__":
    main()
