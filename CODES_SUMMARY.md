# Medical Codes Summary

## Total Codes Loaded: **12,729**

This system now contains three comprehensive medical coding systems for complete healthcare billing and documentation.

---

## 1. ICD-10-CM Diagnosis Codes
**Total: 12,542 codes**

### Purpose
Classify and code all diagnoses, symptoms, and conditions reported in conjunction with hospital care in the United States.

### Coverage
- All 21 ICD-10-CM chapters
- 10,196 subcategory codes (most specific level)
- 2,050 category codes
- 274 block codes
- 22 chapter codes

### Examples

**COPD (Chronic Obstructive Pulmonary Disease)**
- `J44` - Other chronic obstructive pulmonary disease
- `J44.0` - COPD with acute lower respiratory infection
- `J44.1` - COPD with acute exacerbation, unspecified
- `J44.8` - Other specified COPD
- `J44.9` - COPD, unspecified

**Diabetes Mellitus**
- `E10-E14` - Diabetes mellitus (70 codes total)
- `E10` - Type 1 diabetes mellitus
- `E11` - Type 2 diabetes mellitus
- `E11.21` - Type 2 diabetes with diabetic nephropathy
- `E11.65` - Type 2 diabetes with hyperglycemia

**Myocardial Infarction (Heart Attack)**
- `I21` - Acute myocardial infarction (24 codes total)
- `I21.0` - Acute transmural MI of anterior wall
- `I21.1` - Acute transmural MI of inferior wall
- `I21.4` - Non-ST elevation myocardial infarction

### Data Source
- Extracted from `simple-icd-10` Python package
- Based on official CDC/NCHS ICD-10-CM codes

---

## 2. HCPCS Level II Codes
**Total: 45 codes (sample dataset)**

### Purpose
Code medical procedures, equipment, supplies, and services not covered in CPT codes.

### Categories Included

**Durable Medical Equipment (E codes)**
- `E0100` - Cane, includes canes of all materials
- `E0130` - Walker, rigid (pickup), adjustable or fixed
- `E0601` - Continuous positive airway pressure (CPAP) device

**Ambulance Services (A codes)**
- `A0425` - Ground mileage, per statute mile
- `A0428` - Ambulance service, basic life support, non-emergency
- `A0429` - Ambulance service, basic life support, emergency

**Drugs Administered Other Than Oral (J codes)**
- `J0129` - Injection, abatacept, 10 mg
- `J1644` - Injection, heparin sodium, per 1000 units
- `J2001` - Injection, lidocaine HCl for IV infusion, 10 mg
- `J3420` - Injection, vitamin B-12 cyanocobalamin, up to 1000 mcg

**Procedures/Professional Services (G codes)**
- `G0101` - Cervical or vaginal cancer screening
- `G0103` - Prostate cancer screening; PSA test
- `G0202` - Screening mammography, bilateral

**Prosthetics/Orthotics (L codes)**
- `L0220` - Thoracic rib belt, custom fabricated
- `L1680` - Knee ankle foot orthosis (KAFO)
- `L5100` - Below knee, molded socket, shin, SACH foot

**Medical Supplies (A codes)**
- `A4206` - Syringe with needle, sterile, 1 cc or less
- `A4233` - Replacement battery for blood glucose monitor
- `A4253` - Blood glucose test strips, per 50 strips

**Oxygen and Equipment (E codes)**
- `E0424` - Stationary compressed gaseous oxygen system, rental
- `E0431` - Portable gaseous oxygen system, rental
- `E0445` - Oximeter device for measuring blood oxygen levels

**Vision Services (V codes)**
- `V2020` - Frames, purchases
- `V2100` - Sphere, single vision, plano to plus or minus 4.00
- `V5008` - Hearing screening

### Data Source
- Sample dataset created from common HCPCS codes
- Full dataset available from CMS at: https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update

---

## 3. UB-04 Revenue Codes
**Total: 142 codes**

### Purpose
Identify specific accommodation, ancillary service, or billing calculation on hospital claims (UB-04 form).

### Categories Included (18 total)

**Accommodation**
- `0110` - Room & Board - Private (One Bed)
- `0120` - Room & Board - Semi-Private (Two Beds)
- `0140` - Room & Board - Deluxe Private

**Intensive Care (9 codes)**
- `0200` - Intensive Care - General
- `0201` - Intensive Care - Surgical
- `0202` - Intensive Care - Medical
- `0203` - Intensive Care - Pediatric
- `0207` - Intensive Care - Burn Care

**Coronary Care**
- `0210` - Coronary Care - General
- `0211` - Coronary Care - Myocardial Infarction
- `0212` - Coronary Care - Pulmonary Care

**Laboratory (13 codes)**
- `0300` - Laboratory - General
- `0301` - Laboratory - Chemistry
- `0305` - Laboratory - Hematology
- `0306` - Laboratory - Bacteriology & Microbiology
- `0311` - Laboratory - Pathological - Cytology

**Radiology (19 codes)**
- `0320` - Radiology - Diagnostic - General
- `0324` - Radiology - Diagnostic - Chest X-Ray
- `0333` - Radiology - Therapeutic - Radiation Therapy
- `0341` - Nuclear Medicine - Diagnostic
- `0351` - CT Scan - Head Scan
- `0352` - CT Scan - Body Scan

**MRI (5 codes)**
- `0610` - MRI - General
- `0611` - MRI - Brain (including Brain Stem)
- `0612` - MRI - Spinal Cord (including Spine)

**Pharmacy (9 codes)**
- `0250` - Pharmacy - General
- `0251` - Pharmacy - Generic Drugs
- `0252` - Pharmacy - Non-Generic Drugs
- `0258` - Pharmacy - IV Solutions

**Emergency Room (5 codes)**
- `0450` - Emergency Room - General
- `0451` - Emergency Room - EM/EMTALA
- `0456` - Emergency Room - Urgent Care

**Operating Room (5 codes)**
- `0360` - Operating Room Services - General
- `0361` - Operating Room Services - Minor Surgery
- `0362` - Operating Room Services - Organ Transplant

**Therapy Services (18 codes)**
- Physical Therapy: `0420-0429`
- Occupational Therapy: `0430-0439`
- Speech-Language Pathology: `0440-0449`

**Cardiology (5 codes)**
- `0480` - Cardiology - General
- `0481` - Cardiology - Cardiac Catheterization Lab
- `0482` - Cardiology - Stress Test
- `0483` - Cardiology - Echocardiology

**Medical/Surgical Supplies (10 codes)**
- `0270` - Medical/Surgical Supplies - General
- `0272` - Medical/Surgical Supplies - Sterile Supply
- `0275` - Medical/Surgical Supplies - Pacemaker
- `0277` - Medical/Surgical Supplies - Oxygen - Take Home

**Blood and Blood Products (10 codes)**
- `0381` - Blood - Packed Red Cells
- `0382` - Blood - Whole Blood
- `0383` - Blood - Plasma
- `0384` - Blood - Platelets

### Data Source
- Standard UB-04 revenue codes based on NUBC (National Uniform Billing Committee) standards

---

## Complete Use Case Example

### Scenario: Patient with COPD receiving oxygen therapy in emergency room

**1. Diagnosis Code (ICD-10-CM)**
- `J44.1` - Chronic obstructive pulmonary disease with acute exacerbation, unspecified

**2. Equipment/Procedure Code (HCPCS Level II)**
- `E0424` - Stationary compressed gaseous oxygen system, rental
- `E0445` - Oximeter device for measuring blood oxygen levels

**3. Facility Billing Codes (UB-04 Revenue)**
- `0450` - Emergency Room - General
- `0277` - Medical/Surgical Supplies - Oxygen - Take Home

This comprehensive coding allows for:
- ✓ Accurate diagnosis documentation
- ✓ Proper equipment and procedure tracking
- ✓ Correct hospital billing and revenue recognition
- ✓ Complete insurance claim submission

---

## Quick Verification

Run this command to see all loaded codes:

```bash
python src/verify_all_codes.py
```

This will show:
- Total code counts by system
- Sample queries (COPD, diabetes, heart attack, etc.)
- Complete use case examples
- Statistics by category

---

## File Locations

- **ICD-10-CM**: `data/icd10cm/icd10cm_codes.csv` (12,542 codes, ~2.5 MB)
- **HCPCS**: `data/hcpcs/hcpcs_codes.csv` (45 codes, 4.5 KB)
- **Revenue Codes**: `data/revenue_codes/revenue_codes.csv` (142 codes, 9.5 KB)

---

## Next Steps

### 1. Build Vector Database
```bash
python src/build_index.py
```

This will create embeddings for all 12,729 codes enabling:
- Semantic search across all code systems
- Natural language queries
- Context-aware code recommendations

### 2. Query the System
```bash
# Interactive mode
python src/main.py query

# Single query
python src/main.py query -q "COPD level 3 with oxygen therapy"
```

Expected output will include:
- Primary diagnosis code (ICD-10-CM)
- Related equipment codes (HCPCS)
- Billing codes (Revenue)
- Coding guidelines and notes

---

**System Status**: ✅ All codes loaded and ready for RAG implementation!
