"""
Unit tests for utility functions.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import (
    normalize_code,
    validate_icd10_code,
    extract_codes_from_text,
    parse_icd_chapter
)


class TestCodeNormalization:
    """Tests for code normalization."""

    def test_normalize_code_adds_decimal(self):
        """Test that decimal is added correctly."""
        assert normalize_code("J441") == "J44.1"
        assert normalize_code("E119") == "E11.9"

    def test_normalize_code_preserves_decimal(self):
        """Test that existing decimal is preserved."""
        assert normalize_code("J44.1") == "J44.1"
        assert normalize_code("E11.9") == "E11.9"

    def test_normalize_code_uppercase(self):
        """Test that code is converted to uppercase."""
        assert normalize_code("j44.1") == "J44.1"
        assert normalize_code("e11.9") == "E11.9"


class TestCodeValidation:
    """Tests for code validation."""

    def test_validate_valid_codes(self):
        """Test validation of valid ICD-10 codes."""
        assert validate_icd10_code("J44.1") is True
        assert validate_icd10_code("E11.9") is True
        assert validate_icd10_code("A00") is True

    def test_validate_invalid_codes(self):
        """Test validation rejects invalid codes."""
        assert validate_icd10_code("123.45") is False
        assert validate_icd10_code("ABC") is False
        assert validate_icd10_code("J") is False


class TestCodeExtraction:
    """Tests for code extraction from text."""

    def test_extract_codes_from_text(self):
        """Test extraction of codes from text."""
        text = "Patient has J44.1 and E11.9"
        codes = extract_codes_from_text(text)
        assert "J44.1" in codes
        assert "E11.9" in codes

    def test_extract_codes_without_decimal(self):
        """Test extraction of codes without decimal."""
        text = "Diagnosis: J441 and E119"
        codes = extract_codes_from_text(text)
        assert "J44.1" in codes
        assert "E11.9" in codes


class TestChapterParsing:
    """Tests for chapter parsing."""

    def test_parse_respiratory_chapter(self):
        """Test parsing respiratory disease chapter."""
        chapter = parse_icd_chapter("J44.1")
        assert "Respiratory" in chapter

    def test_parse_endocrine_chapter(self):
        """Test parsing endocrine disease chapter."""
        chapter = parse_icd_chapter("E11.9")
        assert "Endocrine" in chapter


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
