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
@click.argument('term')
def decode(term: str):
    """Decode a medical term into its components (prefix + root + suffix)."""
    try:
        rag = MedicalCodingRAG()
        result = rag.decode_medical_term(term)

        if "error" in result:
            console.print(f"[bold red]Error:[/bold red] {result['error']}")
            return

        console.print(Panel(
            f"[bold]Medical Term:[/bold] {result['term']}",
            title="Medical Term Decoder",
            border_style="cyan"
        ))

        if result.get('breakdown'):
            console.print("\n[bold green]Component Breakdown:[/bold green]")
            for comp in result['breakdown']:
                console.print(
                    f"\n  [bold]{comp['type'].upper()}:[/bold] {comp['component']}\n"
                    f"  Meaning: {comp['meaning']}\n"
                    f"  Example: {comp['example']}"
                )

            if result.get('constructed_meaning'):
                console.print(Panel(
                    result['constructed_meaning'],
                    title="Constructed Meaning",
                    border_style="green"
                ))
        else:
            console.print(f"\n[yellow]{result.get('message', 'No breakdown available')}[/yellow]")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        sys.exit(1)


@cli.command()
@click.argument('abbreviation')
def abbrev(abbreviation: str):
    """Look up a medical abbreviation."""
    try:
        rag = MedicalCodingRAG()
        result = rag.lookup_abbreviation(abbreviation)

        if "error" in result:
            console.print(f"[bold red]Error:[/bold red] {result['error']}")
            return

        if "message" in result:
            console.print(f"\n[yellow]{result['message']}[/yellow]")
            return

        console.print(Panel(
            f"[bold]Abbreviation:[/bold] {result['abbreviation']}\n"
            f"[bold]Meaning:[/bold] {result['meaning']}\n"
            f"[bold]Usage:[/bold] {result['usage']}\n"
            f"[bold]Example:[/bold] {result['example']}",
            title="Medical Abbreviation",
            border_style="blue"
        ))

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        sys.exit(1)


@cli.command()
def terminology():
    """Display medical terminology statistics."""
    try:
        rag = MedicalCodingRAG()
        stats = rag.get_terminology_stats()

        if "error" in stats:
            console.print(f"[bold red]Error:[/bold red] {stats['error']}")
            return

        console.print(Panel(
            "[bold]Medical Terminology Database Statistics[/bold]",
            border_style="cyan"
        ))

        console.print(f"\n[bold]Total Entries:[/bold] {stats['total_entries']:,}")
        console.print(f"  • Prefixes: {stats['prefixes']}")
        console.print(f"  • Suffixes: {stats['suffixes']}")
        console.print(f"  • Root Words: {stats['root_words']}")
        console.print(f"  • Abbreviations: {stats['abbreviations']}")

        console.print("\n[bold]Top Usage Categories:[/bold]")
        for usage, count in list(stats['by_usage'].items())[:10]:
            console.print(f"  • {usage}: {count}")

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
    hcpcs_dir = data_dir / "hcpcs"
    cpt_dir = data_dir / "cpt"
    revenue_dir = data_dir / "revenue_codes"
    terminology_dir = data_dir / "medical_terminology"
    vector_db_dir = data_dir / "vector_db"

    console.print("\n[bold]Data Status:[/bold]")
    console.print(f"  ICD-10-CM: {'✓' if icd10cm_dir.exists() else '✗'} {icd10cm_dir}")
    console.print(f"  HCPCS: {'✓' if hcpcs_dir.exists() else '✗'} {hcpcs_dir}")
    console.print(f"  CPT: {'✓' if cpt_dir.exists() else '✗'} {cpt_dir}")
    console.print(f"  Revenue Codes: {'✓' if revenue_dir.exists() else '✗'} {revenue_dir}")
    console.print(f"  Medical Terminology: {'✓' if terminology_dir.exists() else '✗'} {terminology_dir}")
    console.print(f"  Vector DB: {'✓' if vector_db_dir.exists() else '✗'} {vector_db_dir}")

    console.print("\n[bold]Next Steps:[/bold]")
    if not vector_db_dir.exists():
        console.print("  1. Run: [cyan]python src/build_index.py[/cyan]")
    else:
        console.print("  ✓ System is ready!")
        console.print("\n[bold]Available Commands:[/bold]")
        console.print("  • [cyan]query[/cyan] - Query medical codes")
        console.print("  • [cyan]decode[/cyan] - Decode medical terms")
        console.print("  • [cyan]abbrev[/cyan] - Look up abbreviations")
        console.print("  • [cyan]terminology[/cyan] - View terminology stats")


if __name__ == "__main__":
    cli()
