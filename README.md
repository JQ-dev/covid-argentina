# Medical Coding RAG System

A Retrieval-Augmented Generation (RAG) system that provides accurate medical codes (ICD-10-CM/PCS, CPT, HCPCS) for specific medical events, conditions, and procedures.

## Overview

This system helps healthcare professionals quickly identify the correct codes for medical conditions and procedures. For example:
- Input: "COPD level 3"
- Output: ICD-10-CM code J44.x, HCPCS oxygen equipment codes, revenue codes, and relevant coding guidelines

## Currently Loaded: 29,872 Medical Codes + 175 Medical Terms

### Medical Codes
- **ICD-10-CM**: 12,542 diagnosis codes (all 21 chapters)
- **HCPCS Level II**: 13,593 procedure, equipment, and supply codes
- **CPT**: 3,595 current procedural terminology codes
- **UB-04 Revenue Codes**: 142 hospital billing codes

### Medical Terminology Database
- **175 medical terminology entries**:
  - 43 Prefixes (hyper-, hypo-, brady-, tachy-, etc.)
  - 43 Suffixes (-itis, -ectomy, -osis, -pathy, etc.)
  - 52 Root Words organized by body system (cardi/o, gastr/o, nephr/o, etc.)
  - 37 Common Abbreviations (COPD, MI, CHF, DVT, etc.)

## Features

- **Multi-Code System Support**: ICD-10-CM, HCPCS Level II, CPT, UB-04 Revenue Codes
- **Intelligent Search**: Natural language queries to find appropriate codes
- **Medical Terminology Database**: Professional terminology support
  - Decode medical terms (prefix + root + suffix breakdown)
  - Look up medical abbreviations with examples
  - 175 entries covering all major body systems
  - Integrated with RAG responses for professional explanations
- **Official Coding Guidelines**: Comprehensive ICD-10-CM coding guidelines and conventions
- **Exam Preparation**: Designed to help pass CPC (AAPC) and CCS (AHIMA) certification exams
  - 28 Multiple Choice Questions covering ICD-10-CM, CPT, and HCPCS
  - 5 Medical Record Coding Cases (inpatient, outpatient, ED, surgical, procedural)
  - Complete answer keys with detailed rationales
  - Coverage of common exam topics: COPD, diabetes, MI, injuries, E&M coding
  - Medical terminology fundamentals for professional coding
- **Context-Aware**: Provides diagnosis, procedure, and billing codes for complete coding scenarios
- **Real Use Cases**: Examples include COPD with oxygen therapy, diabetes management, emergency room visits

## Data Sources

The system uses official data from:

1. **ICD-10-CM/PCS Code Sets**:
   - CDC/NCHS: https://www.cdc.gov/nchs/icd/icd-10-cm.htm
   - CMS: https://www.cms.gov/medicare/coding-billing/icd-10-codes

2. **Official Coding Guidelines**:
   - Published annually by CDC/NCHS and CMS
   - Included in code set downloads

3. **AHA Coding Clinic**:
   - Official U.S. clearinghouse for coding advice
   - Quarterly guidance on ICD-10-CM/PCS and HCPCS
   - Access: https://www.codingclinicadvisor.com/

4. **CMS ICD-10 Coordination and Maintenance**:
   - ICD-10-CM: https://www.cdc.gov/nchs/icd/icd10_maintenance.htm
   - ICD-10-PCS: https://www.cms.gov/medicare/coding-billing/icd-10-codes

5. **CMS MLN Fact Sheet on Code Sets**:
   - https://www.cms.gov/files/document/mln900943-health-care-code-sets.pdf

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd covid-argentina

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Setup

### 1. Download ICD Code Data

```bash
python src/data_loader.py --download-all
```

This will download the latest ICD-10-CM and ICD-10-PCS code sets from official sources.

## CPC/CCS Exam Preparation Materials

This system includes comprehensive materials to help you prepare for and pass medical coding certification exams:

### Official Coding Guidelines
📘 **docs/ICD10CM_Coding_Guidelines_Summary.md**
- Complete summary of ICD-10-CM Official Coding Guidelines
- Section I: Conventions, General, and Chapter-Specific Guidelines
- Section II: Selection of Principal Diagnosis (Inpatient)
- Section III: Reporting Additional Diagnoses
- Section IV: Outpatient Coding Guidelines
- Key conventions: NEC, NOS, Excludes1, Excludes2, 7th characters
- Chapter-specific guidelines for all 21 chapters
- Common coding scenarios with explanations

### Multiple Choice Questions
📝 **docs/CPC_CCS_Exam_Prep_MCQs.md**
- **28 Multiple Choice Questions** covering:
  - ICD-10-CM Coding Conventions (Q1-Q3)
  - COPD & Respiratory Diseases (Q4-Q6)
  - Diabetes Mellitus (Q7-Q9)
  - Injuries & External Causes (Q10-Q12)
  - Signs, Symptoms & General Guidelines (Q13-Q15)
  - Sequencing & Principal Diagnosis (Q16-Q18)
  - Combination Codes (Q19-Q20)
  - CPT E&M Coding (Q21-Q23)
  - CPT Modifiers (Q24-Q25)
  - HCPCS Level II (Q26-Q28)
- Complete answer key with detailed explanations
- Rationale for each answer
- Study tips for CPC/CCS exams

### Medical Record Coding Cases
🏥 **docs/Medical_Record_Coding_Cases.md**
- **5 Complete Medical Record Coding Cases**:
  1. **Inpatient**: COPD Exacerbation with Respiratory Failure (ICU admission, complex sequencing)
  2. **Outpatient**: New Patient Visit for Diabetes (multiple complications, E&M coding)
  3. **Emergency Department**: Acute MI/STEMI (time-sensitive, critical care)
  4. **Inpatient Surgery**: Hip Fracture (injury coding, external causes, ICD-10-PCS)
  5. **Outpatient Procedure**: Screening Colonoscopy (preventive, pathology findings)
- Each case includes:
  - Complete patient history and documentation
  - Physical exam findings
  - Diagnostic studies
  - Assessment and plan
  - Coding assignment questions
  - Complete answer keys with detailed rationales
  - Common coding errors to avoid

### Medical Terminology Fundamentals
📚 **docs/Medical_Terminology_Fundamentals.md**
- **Comprehensive Medical Terminology Guide**:
  - 100+ prefixes (quantity, position, condition, negation)
  - 75+ suffixes (diagnostic, procedural, descriptive)
  - 50+ root words organized by body system
  - 50+ common medical abbreviations
  - Anatomical terminology and directional terms
  - Practical decoding examples
  - Integration with medical coding practice

### How to Use for Exam Prep

1. **Master Medical Terminology** (docs/Medical_Terminology_Fundamentals.md)
   - Learn prefixes, suffixes, and root words
   - Practice decoding medical terms
   - Memorize common abbreviations
2. **Study the Guidelines** (docs/ICD10CM_Coding_Guidelines_Summary.md)
   - Understand conventions (NEC, NOS, Excludes1/2)
   - Learn chapter-specific rules
3. **Take the MCQ Quiz** (docs/CPC_CCS_Exam_Prep_MCQs.md)
   - Answer without looking at keys
   - Check your work and understand rationale
4. **Code the Medical Records** (docs/Medical_Record_Coding_Cases.md)
   - Time yourself (real exam conditions)
   - Code all 5 cases completely
5. **Review Answer Keys** - learn from mistakes
6. **Use the CLI Tools** for practice:
   - `python src/main.py decode [term]` - decode medical terms
   - `python src/main.py abbrev [abbrev]` - look up abbreviations
   - `python src/main.py query -q "[condition]"` - find codes
7. **Repeat daily** until exam day

### Download Official Guidelines

Download the official ICD-10-CM Guidelines PDF from:
- **CDC FTP**: https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2025/
- **CMS**: https://www.cms.gov/files/document/fy-2025-icd-10-cm-coding-guidelines.pdf

### 2. Build the Vector Database

```bash
python src/build_index.py
```

This creates the vector embeddings for efficient semantic search.

### 3. Configure API Keys

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
# or
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

### Command Line Interface

#### Query Medical Codes
```bash
# Interactive mode
python src/main.py query

# Single query
python src/main.py query -q "COPD level 3"

# Filter by code system
python src/main.py query -q "diabetes" -c icd10cm
```

#### Medical Terminology Commands
```bash
# Decode a medical term
python src/main.py decode tachycardia
# Output: tachy- (fast) + cardi/o (heart) + -ia (condition) = fast heart condition

# Look up an abbreviation
python src/main.py abbrev COPD
# Output: Chronic Obstructive Pulmonary Disease

# View terminology statistics
python src/main.py terminology

# System information
python src/main.py info
```

### Python API

#### Query Codes
```python
from src.rag_system import MedicalCodingRAG

# Initialize the system
rag = MedicalCodingRAG()

# Query for codes
result = rag.query("COPD level 3 with acute exacerbation")

print(f"Primary Code: {result['primary_code']}")
print(f"Description: {result['description']}")
print(f"Guidelines: {result['guidelines']}")
print(f"Related Codes: {result['related_codes']}")
```

#### Medical Terminology API
```python
from src.rag_system import MedicalCodingRAG

rag = MedicalCodingRAG()

# Decode medical term
decoded = rag.decode_medical_term("gastroenteritis")
print(decoded['constructed_meaning'])  # stomach + intestine + inflammation

# Look up abbreviation
abbrev = rag.lookup_abbreviation("MI")
print(abbrev['meaning'])  # Myocardial Infarction

# Get terminology statistics
stats = rag.get_terminology_stats()
print(f"Total entries: {stats['total_entries']}")
```

## Project Structure

```
.
├── src/
│   ├── main.py              # Main application entry point
│   ├── rag_system.py        # Core RAG implementation
│   ├── data_loader.py       # Download and process ICD codes
│   ├── build_index.py       # Build vector database
│   ├── embeddings.py        # Embedding generation
│   └── utils.py             # Utility functions
├── data/
│   ├── icd10cm/             # ICD-10-CM codes and guidelines
│   ├── icd10pcs/            # ICD-10-PCS codes and guidelines
│   └── vector_db/           # Vector database storage
├── docs/
│   └── guidelines/          # Cached coding guidelines
├── tests/
│   └── test_rag.py          # Unit tests
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Technologies Used

- **LangChain**: RAG framework and orchestration
- **ChromaDB/FAISS**: Vector database for semantic search
- **OpenAI/Anthropic**: LLM for query understanding and response generation
- **Sentence Transformers**: Medical domain embeddings
- **BeautifulSoup/Requests**: Data fetching and parsing

## Contributing

Contributions are welcome! Please ensure:
- All code changes include appropriate tests
- Documentation is updated for new features
- Code follows PEP 8 style guidelines

## License

MIT License

## Disclaimer

This tool is for informational and educational purposes only. Always verify codes with official coding manuals and guidelines. Consult certified medical coders for production use in healthcare settings.

## Resources

- [CDC ICD-10-CM Official Guidelines](https://www.cdc.gov/nchs/icd/icd-10-cm.htm)
- [CMS ICD-10 Resources](https://www.cms.gov/medicare/coding-billing/icd-10-codes)
- [AHA Coding Clinic](https://www.codingclinicadvisor.com/)
- [CMS Code Sets Overview](https://www.cms.gov/files/document/mln900943-health-care-code-sets.pdf)
