#!/usr/bin/env python3
"""
Main entry point for the Medical Coding RAG System.
Provides both CLI and interactive interfaces for querying medical codes.
"""

import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from dotenv import load_dotenv

from rag_system import MedicalCodingRAG

# Load environment variables
load_dotenv()

console = Console()


def display_result(result: dict):
    """Display query results in a formatted way."""
    if "error" in result:
        console.print(f"[bold red]Error:[/bold red] {result['error']}")
        return

    console.print("\n[bold cyan]Medical Coding Results[/bold cyan]\n")

    if "primary_code" in result:
        console.print(Panel(
            f"[bold]Code:[/bold] {result['primary_code']}\n"
            f"[bold]Description:[/bold] {result.get('description', 'N/A')}\n"
            f"[bold]Code System:[/bold] {result.get('code_system', 'N/A')}",
            title="Primary Code",
            border_style="green"
        ))

    if "related_codes" in result and result["related_codes"]:
        console.print("\n[bold]Related Codes:[/bold]")
        for i, code in enumerate(result["related_codes"][:5], 1):
            console.print(f"  {i}. {code.get('code', 'N/A')} - {code.get('description', 'N/A')}")

    if "guidelines" in result and result["guidelines"]:
        console.print(Panel(
            result["guidelines"],
            title="Coding Guidelines",
            border_style="yellow"
        ))

    if "confidence" in result:
        console.print(f"\n[bold]Confidence:[/bold] {result['confidence']:.2%}")


@click.group()
def cli():
    """Medical Coding RAG System - Query ICD-10 and other medical codes."""
    pass


@cli.command()
@click.option('--query', '-q', help='Medical condition or procedure to query')
@click.option('--code-system', '-c', default='icd10cm',
              type=click.Choice(['icd10cm', 'icd10pcs', 'all']),
              help='Code system to search')
def query(query: Optional[str], code_system: str):
    """Query for medical codes."""
    try:
        rag = MedicalCodingRAG()

        if query:
            # Single query mode
            result = rag.query(query, code_system=code_system)
            display_result(result)
        else:
            # Interactive mode
            console.print(Panel(
                "[bold]Medical Coding RAG System[/bold]\n\n"
                "Enter medical conditions or procedures to get coding information.\n"
                "Type 'exit' or 'quit' to exit.",
                border_style="blue"
            ))

            while True:
                user_query = Prompt.ask("\n[bold cyan]Enter query[/bold cyan]")

                if user_query.lower() in ['exit', 'quit', 'q']:
                    console.print("[yellow]Goodbye![/yellow]")
                    break

                if not user_query.strip():
                    continue

                with console.status("[bold green]Searching medical codes..."):
                    result = rag.query(user_query, code_system=code_system)

                display_result(result)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        sys.exit(1)


@cli.command()
def info():
    """Display system information and data status."""
    from pathlib import Path

    console.print(Panel("[bold]Medical Coding RAG System Info[/bold]", border_style="blue"))

    data_dir = Path(__file__).parent.parent / "data"

    # Check data directories
    icd10cm_dir = data_dir / "icd10cm"
    icd10pcs_dir = data_dir / "icd10pcs"
    vector_db_dir = data_dir / "vector_db"

    console.print("\n[bold]Data Status:[/bold]")
    console.print(f"  ICD-10-CM: {'✓' if icd10cm_dir.exists() else '✗'} {icd10cm_dir}")
    console.print(f"  ICD-10-PCS: {'✓' if icd10pcs_dir.exists() else '✗'} {icd10pcs_dir}")
    console.print(f"  Vector DB: {'✓' if vector_db_dir.exists() else '✗'} {vector_db_dir}")

    console.print("\n[bold]Next Steps:[/bold]")
    if not icd10cm_dir.exists() or not icd10pcs_dir.exists():
        console.print("  1. Run: [cyan]python src/data_loader.py --download-all[/cyan]")
    if not vector_db_dir.exists():
        console.print("  2. Run: [cyan]python src/build_index.py[/cyan]")
    if icd10cm_dir.exists() and vector_db_dir.exists():
        console.print("  ✓ System is ready! Run: [cyan]python src/main.py query[/cyan]")


if __name__ == "__main__":
    cli()
