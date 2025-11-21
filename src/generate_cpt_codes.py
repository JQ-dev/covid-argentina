#!/usr/bin/env python3
"""
Generate CPT (Current Procedural Terminology) codes dataset.

NOTE: CPT codes are copyrighted by the American Medical Association (AMA).
This generates a comprehensive sample based on CPT code structure and ranges.
For official CPT codes, purchase from: https://www.ama-assn.org/
"""

import pandas as pd
from pathlib import Path


class CPTGenerator:
    """Generate comprehensive CPT codes across all categories."""

    def __init__(self, data_dir: Path = None):
        """Initialize the generator."""
        self.data_dir = data_dir or Path(__file__).parent.parent / "data"
        self.cpt_dir = self.data_dir / "cpt"
        self.cpt_dir.mkdir(parents=True, exist_ok=True)

    def generate_comprehensive_codes(self):
        """Generate comprehensive CPT codes across all categories."""
        print("Generating comprehensive CPT codes...")

        all_codes = []

        # Evaluation and Management (E/M): 99201-99499
        all_codes.extend(self._generate_eval_mgmt_codes())

        # Anesthesia: 00100-01999, 99100-99150
        all_codes.extend(self._generate_anesthesia_codes())

        # Surgery: 10000-69990
        all_codes.extend(self._generate_surgery_codes())

        # Radiology: 70000-79999
        all_codes.extend(self._generate_radiology_codes())

        # Pathology and Laboratory: 80047-89398
        all_codes.extend(self._generate_lab_codes())

        # Medicine: 90281-99607
        all_codes.extend(self._generate_medicine_codes())

        # Category II (Performance Measurement): 0001F-9007F
        all_codes.extend(self._generate_category_ii_codes())

        # Category III (Emerging Technology): 0016T-0999T
        all_codes.extend(self._generate_category_iii_codes())

        return all_codes

    def _generate_eval_mgmt_codes(self):
        """Generate Evaluation and Management codes."""
        codes = []

        # Office visits
        for i in range(99201, 99220, 1):
            codes.append({
                'code': str(i),
                'description': f'Office/outpatient visit, evaluation and management',
                'category': 'Evaluation and Management',
                'subcategory': 'Office Visits',
                'code_system': 'CPT'
            })

        # Hospital visits
        for i in range(99221, 99240, 1):
            codes.append({
                'code': str(i),
                'description': f'Hospital inpatient/observation care',
                'category': 'Evaluation and Management',
                'subcategory': 'Hospital Visits',
                'code_system': 'CPT'
            })

        # Consultations
        for i in range(99241, 99260, 1):
            codes.append({
                'code': str(i),
                'description': f'Consultation services',
                'category': 'Evaluation and Management',
                'subcategory': 'Consultations',
                'code_system': 'CPT'
            })

        # Emergency department
        for i in range(99281, 99292, 1):
            codes.append({
                'code': str(i),
                'description': f'Emergency department services',
                'category': 'Evaluation and Management',
                'subcategory': 'Emergency Department',
                'code_system': 'CPT'
            })

        # Critical care
        for i in range(99291, 99293, 1):
            codes.append({
                'code': str(i),
                'description': f'Critical care services',
                'category': 'Evaluation and Management',
                'subcategory': 'Critical Care',
                'code_system': 'CPT'
            })

        # Other E/M
        for i in range(99304, 99500, 5):
            codes.append({
                'code': str(i),
                'description': f'E/M service type {i}',
                'category': 'Evaluation and Management',
                'subcategory': 'Other',
                'code_system': 'CPT'
            })

        return codes

    def _generate_anesthesia_codes(self):
        """Generate Anesthesia codes."""
        codes = []

        # Anesthesia procedures
        for i in range(100, 1999, 10):
            codes.append({
                'code': f'{i:05d}',
                'description': f'Anesthesia for procedure {i}',
                'category': 'Anesthesia',
                'subcategory': 'Anesthesia Services',
                'code_system': 'CPT'
            })

        # Anesthesia modifiers/add-ons
        for i in range(99100, 99151, 5):
            codes.append({
                'code': str(i),
                'description': f'Anesthesia add-on service {i}',
                'category': 'Anesthesia',
                'subcategory': 'Add-on Services',
                'code_system': 'CPT'
            })

        return codes

    def _generate_surgery_codes(self):
        """Generate Surgery codes."""
        codes = []

        # Integumentary System (10000-19999)
        for i in range(10000, 20000, 25):
            codes.append({
                'code': str(i),
                'description': f'Integumentary system procedure {i}',
                'category': 'Surgery',
                'subcategory': 'Integumentary System',
                'code_system': 'CPT'
            })

        # Musculoskeletal System (20000-29999)
        for i in range(20000, 30000, 25):
            codes.append({
                'code': str(i),
                'description': f'Musculoskeletal system procedure {i}',
                'category': 'Surgery',
                'subcategory': 'Musculoskeletal System',
                'code_system': 'CPT'
            })

        # Respiratory System (30000-32999)
        for i in range(30000, 33000, 25):
            codes.append({
                'code': str(i),
                'description': f'Respiratory system procedure {i}',
                'category': 'Surgery',
                'subcategory': 'Respiratory System',
                'code_system': 'CPT'
            })

        # Cardiovascular System (33000-37799)
        for i in range(33000, 37800, 25):
            codes.append({
                'code': str(i),
                'description': f'Cardiovascular system procedure {i}',
                'category': 'Surgery',
                'subcategory': 'Cardiovascular System',
                'code_system': 'CPT'
            })

        # Digestive System (40000-49999)
        for i in range(40000, 50000, 25):
            codes.append({
                'code': str(i),
                'description': f'Digestive system procedure {i}',
                'category': 'Surgery',
                'subcategory': 'Digestive System',
                'code_system': 'CPT'
            })

        # Urinary System (50000-53899)
        for i in range(50000, 53900, 25):
            codes.append({
                'code': str(i),
                'description': f'Urinary system procedure {i}',
                'category': 'Surgery',
                'subcategory': 'Urinary System',
                'code_system': 'CPT'
            })

        # Nervous System (61000-64999)
        for i in range(61000, 65000, 25):
            codes.append({
                'code': str(i),
                'description': f'Nervous system procedure {i}',
                'category': 'Surgery',
                'subcategory': 'Nervous System',
                'code_system': 'CPT'
            })

        # Eye and Ocular Adnexa (65091-68899)
        for i in range(65091, 68900, 25):
            codes.append({
                'code': str(i),
                'description': f'Eye and ocular procedure {i}',
                'category': 'Surgery',
                'subcategory': 'Eye and Ocular Adnexa',
                'code_system': 'CPT'
            })

        return codes

    def _generate_radiology_codes(self):
        """Generate Radiology codes."""
        codes = []

        # Diagnostic Radiology (70000-76499)
        for i in range(70000, 76500, 25):
            codes.append({
                'code': str(i),
                'description': f'Diagnostic radiology procedure {i}',
                'category': 'Radiology',
                'subcategory': 'Diagnostic Radiology',
                'code_system': 'CPT'
            })

        # Diagnostic Ultrasound (76506-76999)
        for i in range(76506, 77000, 20):
            codes.append({
                'code': str(i),
                'description': f'Diagnostic ultrasound {i}',
                'category': 'Radiology',
                'subcategory': 'Diagnostic Ultrasound',
                'code_system': 'CPT'
            })

        # Radiation Oncology (77000-77799)
        for i in range(77000, 77800, 20):
            codes.append({
                'code': str(i),
                'description': f'Radiation oncology treatment {i}',
                'category': 'Radiology',
                'subcategory': 'Radiation Oncology',
                'code_system': 'CPT'
            })

        # Nuclear Medicine (78000-79999)
        for i in range(78000, 80000, 25):
            codes.append({
                'code': str(i),
                'description': f'Nuclear medicine procedure {i}',
                'category': 'Radiology',
                'subcategory': 'Nuclear Medicine',
                'code_system': 'CPT'
            })

        return codes

    def _generate_lab_codes(self):
        """Generate Pathology and Laboratory codes."""
        codes = []

        # Organ/Disease panels (80047-80081)
        for i in range(80047, 80082, 1):
            codes.append({
                'code': str(i),
                'description': f'Organ or disease-oriented panel {i}',
                'category': 'Pathology and Laboratory',
                'subcategory': 'Organ/Disease Panels',
                'code_system': 'CPT'
            })

        # Drug assays (80150-80377)
        for i in range(80150, 80378, 5):
            codes.append({
                'code': str(i),
                'description': f'Drug testing/assay {i}',
                'category': 'Pathology and Laboratory',
                'subcategory': 'Drug Assays',
                'code_system': 'CPT'
            })

        # Chemistry tests (82000-84999)
        for i in range(82000, 85000, 20):
            codes.append({
                'code': str(i),
                'description': f'Chemistry test {i}',
                'category': 'Pathology and Laboratory',
                'subcategory': 'Chemistry',
                'code_system': 'CPT'
            })

        # Hematology tests (85002-85999)
        for i in range(85002, 86000, 20):
            codes.append({
                'code': str(i),
                'description': f'Hematology test {i}',
                'category': 'Pathology and Laboratory',
                'subcategory': 'Hematology',
                'code_system': 'CPT'
            })

        # Immunology tests (86000-86849)
        for i in range(86000, 86850, 20):
            codes.append({
                'code': str(i),
                'description': f'Immunology test {i}',
                'category': 'Pathology and Laboratory',
                'subcategory': 'Immunology',
                'code_system': 'CPT'
            })

        # Microbiology tests (87001-87999)
        for i in range(87001, 88000, 20):
            codes.append({
                'code': str(i),
                'description': f'Microbiology test {i}',
                'category': 'Pathology and Laboratory',
                'subcategory': 'Microbiology',
                'code_system': 'CPT'
            })

        return codes

    def _generate_medicine_codes(self):
        """Generate Medicine codes."""
        codes = []

        # Immunizations (90281-90749)
        for i in range(90281, 90750, 10):
            codes.append({
                'code': str(i),
                'description': f'Immunization/vaccine {i}',
                'category': 'Medicine',
                'subcategory': 'Immunizations',
                'code_system': 'CPT'
            })

        # Psychiatry (90785-90899)
        for i in range(90785, 90900, 5):
            codes.append({
                'code': str(i),
                'description': f'Psychiatric diagnostic/therapeutic procedure {i}',
                'category': 'Medicine',
                'subcategory': 'Psychiatry',
                'code_system': 'CPT'
            })

        # Dialysis (90935-90999)
        for i in range(90935, 91000, 5):
            codes.append({
                'code': str(i),
                'description': f'Dialysis service {i}',
                'category': 'Medicine',
                'subcategory': 'Dialysis',
                'code_system': 'CPT'
            })

        # Cardiology (92950-93799)
        for i in range(92950, 93800, 20):
            codes.append({
                'code': str(i),
                'description': f'Cardiovascular service {i}',
                'category': 'Medicine',
                'subcategory': 'Cardiology',
                'code_system': 'CPT'
            })

        # Pulmonary (94002-94799)
        for i in range(94002, 94800, 20):
            codes.append({
                'code': str(i),
                'description': f'Pulmonary service {i}',
                'category': 'Medicine',
                'subcategory': 'Pulmonary',
                'code_system': 'CPT'
            })

        # Physical Medicine (97010-97799)
        for i in range(97010, 97800, 10):
            codes.append({
                'code': str(i),
                'description': f'Physical medicine/rehabilitation service {i}',
                'category': 'Medicine',
                'subcategory': 'Physical Medicine',
                'code_system': 'CPT'
            })

        return codes

    def _generate_category_ii_codes(self):
        """Generate Category II (Performance Measurement) codes."""
        codes = []

        for i in range(1, 9008, 50):
            codes.append({
                'code': f'{i:04d}F',
                'description': f'Performance measure {i}F',
                'category': 'Category II - Performance Measures',
                'subcategory': 'Quality Measurement',
                'code_system': 'CPT'
            })

        return codes

    def _generate_category_iii_codes(self):
        """Generate Category III (Emerging Technology) codes."""
        codes = []

        for i in range(16, 1000, 10):
            codes.append({
                'code': f'{i:04d}T',
                'description': f'Emerging technology procedure {i}T',
                'category': 'Category III - Emerging Technology',
                'subcategory': 'Investigational',
                'code_system': 'CPT'
            })

        return codes

    def create_dataset(self):
        """Create the comprehensive CPT dataset."""
        print("\n" + "=" * 70)
        print("Comprehensive CPT Code Generator")
        print("=" * 70)
        print("\nNOTE: CPT codes are copyrighted by the American Medical Association.")
        print("This is a sample dataset based on CPT code structure.")
        print("For official codes, purchase from: https://www.ama-assn.org/")

        codes = self.generate_comprehensive_codes()

        # Create DataFrame
        df = pd.DataFrame(codes)

        # Remove duplicates
        df = df.drop_duplicates(subset=['code'])

        # Sort by code
        df = df.sort_values('code')

        # Save to CSV
        output_path = self.cpt_dir / "cpt_codes.csv"
        df.to_csv(output_path, index=False)

        print(f"\n✓ Generated {len(df):,} CPT codes")
        print(f"✓ Saved to {output_path}")

        # Display statistics
        print(f"\nDataset Statistics:")
        print(f"  Total codes: {len(df):,}")
        print(f"  Categories: {df['category'].nunique()}")
        print(f"\nCodes by category:")
        for category, count in df['category'].value_counts().items():
            print(f"  {category}: {count:,}")

        # Display sample from each major category
        print(f"\nSample codes:")
        for category in ['Evaluation and Management', 'Surgery', 'Radiology', 'Pathology and Laboratory', 'Medicine'][:5]:
            if category in df['category'].values:
                sample = df[df['category'] == category].head(2)
                for _, row in sample.iterrows():
                    print(f"  {row['code']}: {row['description']}")

        return df


def main():
    generator = CPTGenerator()
    df = generator.create_dataset()

    print("\n" + "=" * 70)
    print("✓ CPT code generation complete!")
    print("=" * 70)
    print(f"\nTotal CPT codes: {len(df):,}")


if __name__ == "__main__":
    main()
