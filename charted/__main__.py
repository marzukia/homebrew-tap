"""CLI entry point for charted."""

import argparse
import sys
from pathlib import Path

from .cli.create import create_command
from .cli.batch import batch_command


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="charted",
        description="Generate SVG charts from the command line",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Create subcommand
    create_parser = subparsers.add_parser("create", help="Create a new chart")
    create_parser.add_argument("chart_type", choices=["bar", "column", "line", "pie", "scatter"])
    create_parser.add_argument("output", help="Output SVG file path")
    create_parser.add_argument("--data", "-d", help="Data file (CSV or JSON)")
    create_parser.add_argument("--config", "-c", help="Config file path")
    create_parser.set_defaults(func=create_command)
    
    # Batch subcommand
    batch_parser = subparsers.add_parser("batch", help="Generate multiple charts from a directory")
    batch_parser.add_argument("input_dir", help="Input directory containing data files")
    batch_parser.add_argument("output_dir", help="Output directory for SVG files")
    batch_parser.add_argument("--config", "-c", help="Config file path")
    batch_parser.set_defaults(func=batch_command)
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == "__main__":
    main()
