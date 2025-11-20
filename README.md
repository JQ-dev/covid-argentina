# Medical Coding RAG System

A Retrieval-Augmented Generation (RAG) system that provides accurate medical codes (ICD-10-CM/PCS, CPT, HCPCS) for specific medical events, conditions, and procedures.

## Overview

This system helps healthcare professionals quickly identify the correct codes for medical conditions and procedures. For example:
- Input: "COPD level 3"
- Output: ICD-10-CM code, procedure codes, and relevant coding guidelines

## Features

- **Multi-Code System Support**: ICD-10-CM, ICD-10-PCS, CPT, HCPCS Level II
- **Intelligent Search**: Natural language queries to find appropriate codes
- **Official Guidelines**: Integrated with CDC/NCHS and CMS official coding guidelines
- **Context-Aware**: Provides location-specific and procedure-specific code recommendations

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

```bash
# Interactive mode
python src/main.py

# Single query
python src/main.py --query "COPD level 3"
```

### Python API

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
