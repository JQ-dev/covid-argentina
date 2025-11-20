"""
Utility functions for the Medical Coding RAG system.
"""

from pathlib import Path
from typing import Dict, List, Any, Optional
import re


def normalize_code(code: str) -> str:
    """
    Normalize medical code format.

    Args:
        code: Medical code (e.g., "J441", "J44.1")

    Returns:
        Normalized code with proper formatting
    """
    # Remove whitespace
    code = code.strip().upper()

    # Add decimal point if missing for ICD-10 codes
    if re.match(r'^[A-Z]\d{3,}$', code):
        # Insert decimal after first 3 characters for ICD-10-CM
        code = code[:3] + '.' + code[3:]

    return code


def validate_icd10_code(code: str) -> bool:
    """
    Validate ICD-10 code format.

    Args:
        code: ICD-10 code to validate

    Returns:
        True if valid format
    """
    # ICD-10-CM format: Letter followed by 2 digits, optional decimal and 1-4 more digits
    pattern = r'^[A-Z]\d{2}(\.\d{1,4})?$'
    return bool(re.match(pattern, code.upper()))


def extract_codes_from_text(text: str) -> List[str]:
    """
    Extract medical codes from text.

    Args:
        text: Text containing medical codes

    Returns:
        List of extracted codes
    """
    # Pattern for ICD-10 codes
    pattern = r'\b[A-Z]\d{2}\.?\d{0,4}\b'
    matches = re.findall(pattern, text.upper())

    # Normalize and validate
    codes = []
    for match in matches:
        normalized = normalize_code(match)
        if validate_icd10_code(normalized):
            codes.append(normalized)

    return list(set(codes))  # Remove duplicates


def format_code_description(code: str, description: str, max_length: int = 80) -> str:
    """
    Format code and description for display.

    Args:
        code: Medical code
        description: Code description
        max_length: Maximum length for description

    Returns:
        Formatted string
    """
    if len(description) > max_length:
        description = description[:max_length - 3] + "..."

    return f"{code}: {description}"


def parse_icd_chapter(code: str) -> Optional[str]:
    """
    Determine ICD-10-CM chapter from code.

    Args:
        code: ICD-10 code

    Returns:
        Chapter name or None
    """
    # ICD-10-CM chapter ranges (simplified)
    chapters = {
        'A': 'Infectious and Parasitic Diseases',
        'B': 'Infectious and Parasitic Diseases',
        'C': 'Neoplasms',
        'D': 'Diseases of Blood/Neoplasms',
        'E': 'Endocrine, Nutritional and Metabolic Diseases',
        'F': 'Mental, Behavioral and Neurodevelopmental Disorders',
        'G': 'Diseases of the Nervous System',
        'H': 'Diseases of Eye/Ear',
        'I': 'Diseases of the Circulatory System',
        'J': 'Diseases of the Respiratory System',
        'K': 'Diseases of the Digestive System',
        'L': 'Diseases of the Skin',
        'M': 'Diseases of the Musculoskeletal System',
        'N': 'Diseases of the Genitourinary System',
        'O': 'Pregnancy, Childbirth and the Puerperium',
        'P': 'Perinatal Period Conditions',
        'Q': 'Congenital Malformations',
        'R': 'Symptoms, Signs and Abnormal Findings',
        'S': 'Injury, Poisoning',
        'T': 'Injury, Poisoning',
        'V': 'External Causes of Morbidity',
        'W': 'External Causes of Morbidity',
        'X': 'External Causes of Morbidity',
        'Y': 'External Causes of Morbidity',
        'Z': 'Factors Influencing Health Status',
    }

    if code and len(code) > 0:
        return chapters.get(code[0].upper())

    return None


def get_project_root() -> Path:
    """
    Get the project root directory.

    Returns:
        Path to project root
    """
    return Path(__file__).parent.parent


def ensure_data_directories():
    """Create necessary data directories if they don't exist."""
    root = get_project_root()
    directories = [
        root / "data" / "icd10cm",
        root / "data" / "icd10pcs",
        root / "data" / "vector_db",
        root / "docs" / "guidelines",
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def load_config() -> Dict[str, Any]:
    """
    Load configuration from environment variables.

    Returns:
        Configuration dictionary
    """
    import os
    from dotenv import load_dotenv

    load_dotenv()

    config = {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "anthropic_api_key": os.getenv("ANTHROPIC_API_KEY"),
        "llm_provider": os.getenv("LLM_PROVIDER", "openai"),
        "model_name": os.getenv("MODEL_NAME"),
        "embedding_provider": os.getenv("EMBEDDING_PROVIDER", "sentence-transformers"),
    }

    return config
