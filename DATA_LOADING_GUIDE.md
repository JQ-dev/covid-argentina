# Data Loading Guide

This document explains how to load ICD-10 medical codes into the RAG system.

## Current Status

✅ **12,542 ICD-10-CM codes loaded successfully!**

## What's Loaded

- **Total Codes**: 12,542
- **Code Types**:
  - Subcategory codes: 10,196
  - Category codes: 2,050
  - Block codes: 274
  - Chapter codes: 22
- **Coverage**: All 21 ICD-10-CM chapters

### Sample Data

**COPD Codes (6 codes)**:
- `J44`: Other chronic obstructive pulmonary disease
- `J44.0`: COPD with acute lower respiratory infection
- `J44.1`: COPD with acute exacerbation, unspecified
- `J44.8`: Other specified COPD
- `J44.9`: COPD, unspecified

**Diabetes Codes (70 codes)**:
- `E10-E14`: Diabetes mellitus
- `E10`: Type 1 diabetes mellitus
- `E11`: Type 2 diabetes mellitus
- And 65+ more specific subcategories

**By System**:
- Respiratory: 290 codes
- Circulatory: 468 codes
- Infectious diseases: 1,000+ codes
- And more...

## How to Load the Data

### Step 1: Extract ICD-10 Codes

```bash
python src/extract_icd_data.py
```

This script:
- Uses the `simple-icd-10` Python package
- Extracts all 12,542 ICD-10-CM codes
- Saves to `data/icd10cm/icd10cm_codes.csv`

### Step 2: Verify the Data

```bash
python src/verify_data.py
```

This shows:
- Total codes loaded
- Statistics by code type and chapter
- Sample queries for common conditions (COPD, diabetes, etc.)

### Step 3: Build Vector Database (Next Step)

Once dependencies are installed:

```bash
python src/build_index.py
```

This will:
- Create embeddings for all codes
- Build a searchable vector database
- Enable semantic search (e.g., "COPD level 3" → finds J44.x codes)

## Data Source

The codes are extracted from the `simple-icd-10` Python package, which provides:
- Official ICD-10-CM codes
- Standard descriptions
- Hierarchical structure (chapters → blocks → categories → subcategories)

## File Locations

- **CSV Data**: `data/icd10cm/icd10cm_codes.csv` (12,542 codes, ~2.5MB)
- **Vector DB**: `data/vector_db/` (created after running build_index.py)

## Next Steps

1. ✅ Data extracted and verified
2. ⏳ Install ML dependencies (in progress)
3. ⏳ Build vector database
4. ⏳ Test RAG queries

## Example Queries (After Vector DB is Built)

```bash
# Interactive mode
python src/main.py query

# Single query
python src/main.py query -q "COPD level 3"
python src/main.py query -q "Type 2 diabetes with complications"
python src/main.py query -q "Acute myocardial infarction"
```

## Troubleshooting

**If data file is missing:**
```bash
python src/extract_icd_data.py
```

**If you need to re-extract:**
```bash
rm data/icd10cm/icd10cm_codes.csv
python src/extract_icd_data.py
```

**To verify data integrity:**
```bash
python src/verify_data.py
```
