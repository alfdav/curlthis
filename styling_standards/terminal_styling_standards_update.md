# CLI Framework Implementation (Typer vs Click)

This section extends the existing terminal styling standards to provide specific guidance on CLI framework implementation.

## Recommended CLI Framework: Typer

While both Click and Typer are supported CLI frameworks, **Typer is the recommended framework** for all new CLI applications. Typer provides several advantages over Click:

1. **Built-in Rich Formatting**: Typer has built-in support for Rich formatting in help text via the `rich_markup_mode="rich"` parameter.
2. **Type Annotations**: Typer uses Python type annotations for parameters, making the code more readable and self-documenting.
3. **Command Groups**: Typer has built-in support for command groups, making it easier to organize complex CLIs.
4. **Help Text Formatting**: Typer's help text is automatically formatted with Rich, eliminating the need for custom help command classes.
5. **Cleaner Implementation**: Typer requires less boilerplate code for the same functionality.

## Typer Implementation

For Typer-based CLI applications, use the following pattern:

```python
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box
from rich.traceback import install as install_rich_traceback

# Install Rich traceback handler
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Create console for rich output
console = Console()

# Status indicators - STANDARDIZED FORMAT
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}

# Create Typer app with rich formatting
app = typer.Typer(
    help="Application description",
    add_completion=True,
    rich_markup_mode="rich"  # Enable rich markup in help text
)

# Command implementation with Pokemon naming
@app.command()
def machamp_process_file(
    file_path: str = typer.Argument(..., help="Path to the file to process"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output")
) -> None:
    """
    Process a file with detailed analysis.
    
    This command demonstrates how to structure a Typer command with
    the Pokemon naming convention while maintaining clean help output.
    """
    # Implementation...
```

## Click Implementation (Legacy)

For existing Click-based CLI applications, use the following pattern:

```python
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box
from rich.traceback import install as install_rich_traceback

# Install Rich traceback handler
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Create console for rich output
console = Console()

# Status indicators - STANDARDIZED FORMAT
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}

# Custom help command class
class RichHelpCommand(click.Command):
    """Custom click.Command that displays help using Rich styling."""
    
    def format_help(self, ctx, formatter):
        # Use Rich for help display instead of the default formatter
        hitmonchan_show_banner(author="David Diaz (https://github.com/alfdav)")
        
        # Command description with rule
        create_section("Description")
        console.print(f"{self.help}\n")
        
        # Usage section with rule
        usage_text = self.collect_usage(ctx)
        create_section("Usage")
        console.print(f"{usage_text}\n")
        
        # Options table with rule
        options = self.collect_options(ctx)
        if options:
            create_section("Options")
            options_table = create_table("", "")
            options_table.add_column("Option", style="bold")
            options_table.add_column("Description")
            
            for opt in options:
                options_table.add_row(opt["name"], opt["help"])
            
            console.print(options_table)
            console.print()

# Command implementation with Pokemon naming
@click.command(cls=RichHelpCommand, context_settings={"help_option_names": ["-h", "--help"]})
@click.option("-f", "--file", type=click.File("r"), help="Input file path")
@click.option("-v", "--verbose", is_flag=True, help="Show verbose output")
def machamp_process_file(file, verbose):
    """Process a file with detailed analysis."""
    # Implementation...
```

## Reference Implementations

For complete reference implementations, see:

1. **Typer Template**: `styling_standards/python_terminal_styling/typer_template.py`
2. **Typer Styling Guide**: `styling_standards/typer_styling_guide.md`
3. **Click Template**: Original implementation in the terminal styling template

## Migration Guide

For existing Click-based applications, consider migrating to Typer using the following steps:

1. Replace Click imports with Typer imports
2. Replace Click decorators with Typer decorators
3. Add type annotations to function parameters
4. Remove custom help command classes
5. Add `rich_markup_mode="rich"` to the Typer app

For detailed migration instructions, see the Typer documentation: https://typer.tiangolo.com/tutorial/using-click/

## Compliance Verification

The standards compliance verification tool has been updated to check for Typer implementation. To verify compliance, run:

```python
from utils.standards import mewtwo_verify_standards_compliance

results = mewtwo_verify_standards_compliance()
if results['passed']:
    print("Project meets all terminal styling standards!")
else:
    print("Project does not meet all standards. See details:")
    for check_name, check_result in results['checks'].items():
        if not check_result['passed']:
            print(f"- {check_name}: {check_result['message']}")