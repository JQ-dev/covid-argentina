#!/usr/bin/env python3
"""
Load UB-04 Revenue Codes.
Revenue codes are used on hospital bills (UB-04 form) to identify specific
accommodation, ancillary service, or billing calculation.
"""

import pandas as pd
from pathlib import Path


class RevenueCodeLoader:
    """Loader for UB-04 Revenue Codes."""

    def __init__(self, data_dir: Path = None):
        """Initialize the revenue code loader."""
        self.data_dir = data_dir or Path(__file__).parent.parent / "data"
        self.revenue_dir = self.data_dir / "revenue_codes"
        self.revenue_dir.mkdir(parents=True, exist_ok=True)

    def create_revenue_codes(self):
        """
        Create comprehensive UB-04 revenue codes database.
        Based on NUBC (National Uniform Billing Committee) standards.
        """
        print("Creating UB-04 Revenue Codes database...")

        # Comprehensive revenue codes
        revenue_codes = [
            # Accommodation (Room & Board)
            {"code": "0100", "description": "All-Inclusive Rate", "category": "Accommodation"},
            {"code": "0110", "description": "Room & Board - Private (One Bed)", "category": "Accommodation"},
            {"code": "0111", "description": "Room & Board - Private - Medical/General", "category": "Accommodation"},
            {"code": "0112", "description": "Room & Board - Private - OB", "category": "Accommodation"},
            {"code": "0113", "description": "Room & Board - Private - Pediatric", "category": "Accommodation"},
            {"code": "0114", "description": "Room & Board - Private - Psychiatric", "category": "Accommodation"},
            {"code": "0120", "description": "Room & Board - Semi-Private (Two Beds)", "category": "Accommodation"},
            {"code": "0130", "description": "Room & Board - Three and Four Beds", "category": "Accommodation"},
            {"code": "0140", "description": "Room & Board - Deluxe Private", "category": "Accommodation"},
            {"code": "0150", "description": "Room & Board - Ward (Five or More Beds)", "category": "Accommodation"},
            {"code": "0160", "description": "Other Room & Board", "category": "Accommodation"},

            # Intensive Care
            {"code": "0200", "description": "Intensive Care - General", "category": "Intensive Care"},
            {"code": "0201", "description": "Intensive Care - Surgical", "category": "Intensive Care"},
            {"code": "0202", "description": "Intensive Care - Medical", "category": "Intensive Care"},
            {"code": "0203", "description": "Intensive Care - Pediatric", "category": "Intensive Care"},
            {"code": "0204", "description": "Intensive Care - Psychiatric", "category": "Intensive Care"},
            {"code": "0206", "description": "Intensive Care - Intermediate ICU", "category": "Intensive Care"},
            {"code": "0207", "description": "Intensive Care - Burn Care", "category": "Intensive Care"},
            {"code": "0208", "description": "Intensive Care - Trauma", "category": "Intensive Care"},
            {"code": "0209", "description": "Intensive Care - Other", "category": "Intensive Care"},

            # Coronary Care
            {"code": "0210", "description": "Coronary Care - General", "category": "Coronary Care"},
            {"code": "0211", "description": "Coronary Care - Myocardial Infarction", "category": "Coronary Care"},
            {"code": "0212", "description": "Coronary Care - Pulmonary Care", "category": "Coronary Care"},
            {"code": "0213", "description": "Coronary Care - Heart Transplant", "category": "Coronary Care"},

            # Nursery
            {"code": "0170", "description": "Nursery - Newborn Level I", "category": "Nursery"},
            {"code": "0171", "description": "Nursery - Newborn Level II", "category": "Nursery"},
            {"code": "0172", "description": "Nursery - Newborn Level III", "category": "Nursery"},
            {"code": "0173", "description": "Nursery - Newborn Level IV", "category": "Nursery"},
            {"code": "0174", "description": "Nursery - Other", "category": "Nursery"},

            # Operating Room
            {"code": "0360", "description": "Operating Room Services - General", "category": "Operating Room"},
            {"code": "0361", "description": "Operating Room Services - Minor Surgery", "category": "Operating Room"},
            {"code": "0362", "description": "Operating Room Services - Organ Transplant", "category": "Operating Room"},
            {"code": "0367", "description": "Operating Room Services - Kidney Transplant", "category": "Operating Room"},
            {"code": "0369", "description": "Operating Room Services - Other", "category": "Operating Room"},

            # Anesthesia
            {"code": "0370", "description": "Anesthesia - General", "category": "Anesthesia"},
            {"code": "0371", "description": "Anesthesia - Incident to Radiology", "category": "Anesthesia"},
            {"code": "0372", "description": "Anesthesia - Incident to Other Diagnostic Services", "category": "Anesthesia"},
            {"code": "0379", "description": "Anesthesia - Other", "category": "Anesthesia"},

            # Laboratory
            {"code": "0300", "description": "Laboratory - General", "category": "Laboratory"},
            {"code": "0301", "description": "Laboratory - Chemistry", "category": "Laboratory"},
            {"code": "0302", "description": "Laboratory - Immunology", "category": "Laboratory"},
            {"code": "0303", "description": "Laboratory - Renal Patient (Home)", "category": "Laboratory"},
            {"code": "0304", "description": "Laboratory - Non-Routine Dialysis", "category": "Laboratory"},
            {"code": "0305", "description": "Laboratory - Hematology", "category": "Laboratory"},
            {"code": "0306", "description": "Laboratory - Bacteriology & Microbiology", "category": "Laboratory"},
            {"code": "0307", "description": "Laboratory - Urology", "category": "Laboratory"},
            {"code": "0309", "description": "Laboratory - Other", "category": "Laboratory"},
            {"code": "0310", "description": "Laboratory - Pathological - General", "category": "Laboratory"},
            {"code": "0311", "description": "Laboratory - Pathological - Cytology", "category": "Laboratory"},
            {"code": "0312", "description": "Laboratory - Pathological - Histology", "category": "Laboratory"},
            {"code": "0314", "description": "Laboratory - Pathological - Biopsy", "category": "Laboratory"},

            # Radiology
            {"code": "0320", "description": "Radiology - Diagnostic - General", "category": "Radiology"},
            {"code": "0321", "description": "Radiology - Diagnostic - Angiocardiography", "category": "Radiology"},
            {"code": "0324", "description": "Radiology - Diagnostic - Chest X-Ray", "category": "Radiology"},
            {"code": "0329", "description": "Radiology - Diagnostic - Other", "category": "Radiology"},
            {"code": "0330", "description": "Radiology - Therapeutic - General", "category": "Radiology"},
            {"code": "0331", "description": "Radiology - Therapeutic - Chemotherapy - Injected", "category": "Radiology"},
            {"code": "0332", "description": "Radiology - Therapeutic - Chemotherapy - Oral", "category": "Radiology"},
            {"code": "0333", "description": "Radiology - Therapeutic - Radiation Therapy", "category": "Radiology"},
            {"code": "0335", "description": "Radiology - Therapeutic - Chemotherapy - IV", "category": "Radiology"},
            {"code": "0339", "description": "Radiology - Therapeutic - Other", "category": "Radiology"},
            {"code": "0340", "description": "Nuclear Medicine - General", "category": "Radiology"},
            {"code": "0341", "description": "Nuclear Medicine - Diagnostic", "category": "Radiology"},
            {"code": "0342", "description": "Nuclear Medicine - Therapeutic", "category": "Radiology"},
            {"code": "0343", "description": "Nuclear Medicine - Diagnostic Radiopharmaceuticals", "category": "Radiology"},
            {"code": "0344", "description": "Nuclear Medicine - Therapeutic Radiopharmaceuticals", "category": "Radiology"},
            {"code": "0350", "description": "CT Scan - General", "category": "Radiology"},
            {"code": "0351", "description": "CT Scan - Head Scan", "category": "Radiology"},
            {"code": "0352", "description": "CT Scan - Body Scan", "category": "Radiology"},
            {"code": "0359", "description": "CT Scan - Other", "category": "Radiology"},

            # MRI
            {"code": "0610", "description": "MRI - General", "category": "MRI"},
            {"code": "0611", "description": "MRI - Brain (including Brain Stem)", "category": "MRI"},
            {"code": "0612", "description": "MRI - Spinal Cord (including Spine)", "category": "MRI"},
            {"code": "0614", "description": "MRI - Lower Extremities", "category": "MRI"},
            {"code": "0619", "description": "MRI - Other", "category": "MRI"},

            # Pharmacy
            {"code": "0250", "description": "Pharmacy - General", "category": "Pharmacy"},
            {"code": "0251", "description": "Pharmacy - Generic Drugs", "category": "Pharmacy"},
            {"code": "0252", "description": "Pharmacy - Non-Generic Drugs", "category": "Pharmacy"},
            {"code": "0253", "description": "Pharmacy - Take Home Drugs", "category": "Pharmacy"},
            {"code": "0254", "description": "Pharmacy - Drugs Incident to Other Diagnostic Services", "category": "Pharmacy"},
            {"code": "0255", "description": "Pharmacy - Drugs Incident to Radiology", "category": "Pharmacy"},
            {"code": "0257", "description": "Pharmacy - Non-Prescription", "category": "Pharmacy"},
            {"code": "0258", "description": "Pharmacy - IV Solutions", "category": "Pharmacy"},
            {"code": "0259", "description": "Pharmacy - Other", "category": "Pharmacy"},

            # Emergency Room
            {"code": "0450", "description": "Emergency Room - General", "category": "Emergency Room"},
            {"code": "0451", "description": "Emergency Room - EM/EMTALA", "category": "Emergency Room"},
            {"code": "0452", "description": "Emergency Room - Beyond EMTALA Screening", "category": "Emergency Room"},
            {"code": "0456", "description": "Emergency Room - Urgent Care", "category": "Emergency Room"},
            {"code": "0459", "description": "Emergency Room - Other", "category": "Emergency Room"},

            # Physical Therapy
            {"code": "0420", "description": "Physical Therapy - General", "category": "Therapy Services"},
            {"code": "0421", "description": "Physical Therapy - Visit Charge", "category": "Therapy Services"},
            {"code": "0422", "description": "Physical Therapy - Hourly Charge", "category": "Therapy Services"},
            {"code": "0423", "description": "Physical Therapy - Group Rate", "category": "Therapy Services"},
            {"code": "0424", "description": "Physical Therapy - Evaluation or Re-Evaluation", "category": "Therapy Services"},
            {"code": "0429", "description": "Physical Therapy - Other", "category": "Therapy Services"},

            # Occupational Therapy
            {"code": "0430", "description": "Occupational Therapy - General", "category": "Therapy Services"},
            {"code": "0431", "description": "Occupational Therapy - Visit Charge", "category": "Therapy Services"},
            {"code": "0432", "description": "Occupational Therapy - Hourly Charge", "category": "Therapy Services"},
            {"code": "0433", "description": "Occupational Therapy - Group Rate", "category": "Therapy Services"},
            {"code": "0434", "description": "Occupational Therapy - Evaluation or Re-Evaluation", "category": "Therapy Services"},
            {"code": "0439", "description": "Occupational Therapy - Other", "category": "Therapy Services"},

            # Speech-Language Pathology
            {"code": "0440", "description": "Speech-Language Pathology - General", "category": "Therapy Services"},
            {"code": "0441", "description": "Speech-Language Pathology - Visit Charge", "category": "Therapy Services"},
            {"code": "0442", "description": "Speech-Language Pathology - Hourly Charge", "category": "Therapy Services"},
            {"code": "0443", "description": "Speech-Language Pathology - Group Rate", "category": "Therapy Services"},
            {"code": "0444", "description": "Speech-Language Pathology - Evaluation or Re-Evaluation", "category": "Therapy Services"},
            {"code": "0449", "description": "Speech-Language Pathology - Other", "category": "Therapy Services"},

            # Cardiology
            {"code": "0480", "description": "Cardiology - General", "category": "Cardiology"},
            {"code": "0481", "description": "Cardiology - Cardiac Catheterization Lab", "category": "Cardiology"},
            {"code": "0482", "description": "Cardiology - Stress Test", "category": "Cardiology"},
            {"code": "0483", "description": "Cardiology - Echocardiology", "category": "Cardiology"},
            {"code": "0489", "description": "Cardiology - Other", "category": "Cardiology"},

            # Recovery Room
            {"code": "0710", "description": "Recovery Room - General", "category": "Recovery Room"},
            {"code": "0711", "description": "Recovery Room - Post ICU", "category": "Recovery Room"},
            {"code": "0719", "description": "Recovery Room - Other", "category": "Recovery Room"},

            # Medical/Surgical Supplies
            {"code": "0270", "description": "Medical/Surgical Supplies - General", "category": "Supplies"},
            {"code": "0271", "description": "Medical/Surgical Supplies - Non-Sterile Supply", "category": "Supplies"},
            {"code": "0272", "description": "Medical/Surgical Supplies - Sterile Supply", "category": "Supplies"},
            {"code": "0273", "description": "Medical/Surgical Supplies - Take Home Supplies", "category": "Supplies"},
            {"code": "0274", "description": "Medical/Surgical Supplies - Prosthetic/Orthotic Devices", "category": "Supplies"},
            {"code": "0275", "description": "Medical/Surgical Supplies - Pacemaker", "category": "Supplies"},
            {"code": "0276", "description": "Medical/Surgical Supplies - Intraocular Lens", "category": "Supplies"},
            {"code": "0277", "description": "Medical/Surgical Supplies - Oxygen - Take Home", "category": "Supplies"},
            {"code": "0278", "description": "Medical/Surgical Supplies - Other Implants", "category": "Supplies"},
            {"code": "0279", "description": "Medical/Surgical Supplies - Other", "category": "Supplies"},

            # Blood and Blood Products
            {"code": "0380", "description": "Blood - General", "category": "Blood"},
            {"code": "0381", "description": "Blood - Packed Red Cells", "category": "Blood"},
            {"code": "0382", "description": "Blood - Whole Blood", "category": "Blood"},
            {"code": "0383", "description": "Blood - Plasma", "category": "Blood"},
            {"code": "0384", "description": "Blood - Platelets", "category": "Blood"},
            {"code": "0385", "description": "Blood - Leukocytes", "category": "Blood"},
            {"code": "0386", "description": "Blood - Other Components", "category": "Blood"},
            {"code": "0387", "description": "Blood - Other Derivatives", "category": "Blood"},
            {"code": "0389", "description": "Blood - Other", "category": "Blood"},
            {"code": "0390", "description": "Blood - Blood Admin, Processing, Storage", "category": "Blood"},

            # Observation Room
            {"code": "0760", "description": "Observation Room - General", "category": "Observation"},
            {"code": "0762", "description": "Observation Room - Beyond First Day", "category": "Observation"},

            # Misc
            {"code": "0920", "description": "Other Diagnostic Services - General", "category": "Other Diagnostic"},
            {"code": "0921", "description": "Other Diagnostic Services - Peripheral Vascular Lab", "category": "Other Diagnostic"},
            {"code": "0922", "description": "Other Diagnostic Services - Electrocardiology (EKG/ECG)", "category": "Other Diagnostic"},
            {"code": "0923", "description": "Other Diagnostic Services - Electroencephalogram (EEG)", "category": "Other Diagnostic"},
            {"code": "0929", "description": "Other Diagnostic Services - Other", "category": "Other Diagnostic"},
        ]

        df = pd.DataFrame(revenue_codes)
        df['code_system'] = 'UB-04 Revenue Code'

        output_path = self.revenue_dir / "revenue_codes.csv"
        df.to_csv(output_path, index=False)

        print(f"\n✓ Created revenue codes database with {len(df)} codes")
        print(f"✓ Saved to: {output_path}")

        # Display statistics
        print(f"\nRevenue codes by category:")
        for category, count in df['category'].value_counts().items():
            print(f"  {category}: {count}")

        return df


def main():
    loader = RevenueCodeLoader()

    print("=" * 70)
    print("UB-04 Revenue Codes Loader")
    print("=" * 70)

    df = loader.create_revenue_codes()

    print(f"\n✓ Revenue codes database created!")
    print(f"  Location: {loader.revenue_dir}")
    print(f"  Total codes: {len(df)}")

    print("\nSample codes:")
    print(df[['code', 'description', 'category']].head(10).to_string(index=False))


if __name__ == "__main__":
    main()
