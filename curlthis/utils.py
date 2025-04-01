"""
Utility module for curlthis CLI styling and output functions.

This module provides standardized styling functions for the curlthis CLI
using the Rich library. It follows the Pokemon-themed function naming convention
with Fighting-type Pokemon for system operations.

Author: David Diaz (https://github.com/alfdav)
Version: 1.0.0
"""
from typing import Optional, Any, List, Dict, Union
import sys
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.theme import Theme
from rich.rule import Rule
from rich.markdown import Markdown
import platform
import subprocess
import sys
import os

# Install Rich traceback handler for global exception beautification
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Define custom theme matching standards
custom_theme = Theme({
    # Base colors
    "info": "blue",
    "warning": "yellow",
    "error": "red",
    "success": "green",
    "header": "cyan bold",
    
    # Additional styles
    "code": "cyan",
    "command": "cyan bold",
    "filename": "cyan",
    "path": "cyan",
    "url": "blue underline",
    "dim": "dim",
    "bold": "bold",
    "italic": "italic",
    "underline": "underline",
    "strike": "strike",
    "highlight": "black on yellow",
    "title": "cyan bold"
})

# Main console instance
console = Console(theme=custom_theme)

# Error console (stderr)
error_console = Console(stderr=True, theme=custom_theme)

# Status indicators dictionary with standardized styling
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}


def hitmonchan_show_banner(title: str = "curlthis v1.0.0",
                         description: str = "Transform raw HTTP requests into curl one-liners",
                         author: str = "David Diaz (https://github.com/alfdav)",
                         version: str = "1.0.0") -> None:
    """Display application banner with standardized styling.
    
    Creates a styled banner with the application title, description, version,
    and author information using Rich panels.
    
    Args:
        title: The title to display in the banner
        description: The description to display in the banner
        author: The author name to display in the banner subtitle
        version: The version to display in the banner
    """
    # Format content with description and version
    content = f"[bold]{title}[/bold] - [italic]{description}[/italic]\n\n"
    content += f"[dim]Version: {version}[/dim]"
    
    # Create banner panel with standardized styling
    banner = Panel(
        content,
        border_style="blue",
        subtitle=f"By {author}" if author else None,
        expand=False
    )
    console.print(banner)


def primeape_show_error(message: str, exception: Optional[Exception] = None) -> None:
    """Display error message with optional exception details.
    
    Shows a styled error panel with the provided message and optionally
    displays exception details if provided.
    
    Args:
        message: The error message to display
        exception: Optional exception to display details for
    """
    # Create error panel with standardized styling
    error_panel = Panel(
        f"[bold red]ERROR:[/bold red] {message}",
        border_style="red", 
        title="Error"
    )
    error_console.print(error_panel)
    
    # Show exception details if available
    if exception and str(exception):
        error_console.print(f"[dim]{str(exception)}[/dim]")


def primeape_show_warning(message: str, title: str = "Warning", multiline: bool = False) -> None:
    """Display warning message in a styled panel.
    
    Shows a yellow-bordered panel with the warning message to
    draw attention to potential issues.
    
    Args:
        message: The warning message to display
        title: The title of the warning panel
        multiline: Whether the message contains multiple lines that should be preserved
    """
    # Format the message based on whether it's multiline or not
    if multiline:
        # For multiline messages, preserve formatting but add styling
        formatted_message = message.replace("\n", "\n")
        content = Markdown(formatted_message)
    else:
        # For single-line messages, use simple styling
        content = f"[bold yellow]WARNING:[/bold yellow] {message}"
    
    # Create warning panel with standardized styling
    warning_panel = Panel(
        content,
        border_style="yellow", 
        title=title,
        expand=True
    )
    console.print(warning_panel)


def hitmonchan_show_success(message: str) -> None:
    """Display success message with a checkmark indicator.
    
    Shows a green checkmark followed by the success message.
    
    Args:
        message: The success message to display
    """
    console.print(f"{STATUS['success']} {message}")


def hitmonchan_show_progress(message: str, spinner: bool = False, 
                           total: Optional[float] = None) -> Optional[Progress]:
    """Display progress message or create a progress bar.
    
    Shows a simple progress message, a spinner animation, or a full progress bar
    depending on the parameters provided.
    
    Args:
        message: The progress message to display
        spinner: Whether to show a spinner animation
        total: Optional total for progress tracking (None for indeterminate)
        
    Returns:
        Progress object if total is provided, None otherwise
    """
    if spinner:
        # Create spinner with standardized styling
        with Progress(
            SpinnerColumn(),
            TextColumn("[blue]{task.description}[/blue]"),
            transient=True
        ) as progress:
            progress.add_task(message, total=None)
        return None
    elif total is not None:
        # Create progress bar with standardized columns
        progress = Progress(
            SpinnerColumn(),
            TextColumn("[blue]{task.description}[/blue]"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        )
        task_id = progress.add_task(message, total=total)
        return progress
    else:
        # Simple progress message
        console.print(f"{STATUS['info']} {message}")
        return None


def create_table(title: str, style: str = "header", 
                show_header: bool = True, box_style: box = box.ROUNDED) -> Table:
    """Create a table with the given title and standardized styling.
    
    Args:
        title: The title of the table
        style: The style to apply to the title
        show_header: Whether to show the header
        box_style: The box style to use
        
    Returns:
        A Rich Table object with standardized styling
    """
    table = Table(
        title=title, 
        title_style=style, 
        box=box_style,
        show_header=show_header,
        header_style="bold cyan"
    )
    return table


def create_section(title: str, style: str = "cyan") -> None:
    """Create a section header with a rule.
    
    Args:
        title: The title of the section
        style: The style to apply to the rule
    """
    console.print(Rule(title=f"[bold {style}]{title}[/bold {style}]", style=style))


def kadabra_display_code(code: str, language: str = "bash", title: str = "Generated code", line_numbers: bool = True) -> None:
    """Display code with syntax highlighting in a panel.
    
    Kadabra's transformation abilities make it perfect for formatting and
    displaying code with proper syntax highlighting.
    
    Args:
        code: The code to display
        language: The language for syntax highlighting
        title: The title of the panel
        line_numbers: Whether to display line numbers (default: True)
    """
    panel = Panel(
        Syntax(code, language, theme="monokai", word_wrap=True, line_numbers=line_numbers),
        title=f"[bold]{title}[/bold]",
        border_style="green",
        expand=False
    )
    console.print(panel)

def display_code(code: str, language: str = "bash", theme: str = "monokai",
                 title: str = "Generated code", border_style: str = "green") -> None:
    """Display code with syntax highlighting in a panel.
    
    Note: This function is maintained for backward compatibility.
    For new code, use kadabra_display_code() instead.
    
    Args:
        code: The code to display
        language: The language for syntax highlighting
        theme: The color theme for syntax highlighting
        title: The title of the panel
        border_style: The color of the panel border
    """
    # Create syntax-highlighted code with standardized styling
    syntax = Syntax(
        code,
        language,
        theme=theme,
        word_wrap=True,
        line_numbers=False,
        code_width=100
    )
    
    # Create panel with standardized styling
    panel = Panel(
        syntax,
        title=f"[bold]{title}[/bold]",
        border_style=border_style,
        expand=False
    )
    console.print(panel)


def meowth_copy_to_clipboard(text: str) -> tuple[bool, str]:
    """Copy text to clipboard with cross-platform support.
    
    This function provides a more robust clipboard handling mechanism with
    platform-specific implementations and clear error messages.
    
    Args:
        text: The text to copy to clipboard
        
    Returns:
        A tuple containing (success_status, message)
    """
    system = platform.system().lower()
    
    # Check for SSH session (where clipboard access typically fails)
    is_ssh_session = False
    try:
        # Check common SSH environment variables
        is_ssh_session = bool(os.environ.get('SSH_CLIENT') or os.environ.get('SSH_TTY') or 
                             os.environ.get('SSH_CONNECTION'))
    except Exception:
        pass
    
    # For SSH sessions on Linux, provide immediate guidance
    if is_ssh_session and system == "linux":
        try:
            import tempfile
            
            # Save to file as the primary method for SSH sessions
            fd, path = tempfile.mkstemp(suffix=".txt", prefix="curlthis_")
            with os.fdopen(fd, 'w') as tmp:
                tmp.write(text)
            
            ssh_msg = (
                "**SSH Session Detected**\n\n"
                "Clipboard operations are not available in SSH sessions without X11 forwarding.\n"
                "Options:\n"
                "1. Use the saved command file\n"
                "2. Enable X11 forwarding with 'ssh -X' or 'ssh -Y' when connecting\n"
                "3. Use the '--no-clipboard' flag to disable clipboard attempts\n\n"
                f"Command saved to: {path}"
            )
            return False, ssh_msg
        except Exception:
            # If file saving fails, just return the SSH message
            ssh_msg = (
                "**SSH Session Detected**\n\n"
                "Clipboard operations are not available in SSH sessions without X11 forwarding.\n"
                "Options:\n"
                "1. Enable X11 forwarding with 'ssh -X' or 'ssh -Y' when connecting\n"
                "2. Use the '--no-clipboard' flag to disable clipboard attempts"
            )
            return False, ssh_msg
    
    # Always try pyperclip first (maintain it as primary clipboard mechanism)
    try:
        import pyperclip
        pyperclip.copy(text)
        return True, "Copied to clipboard (ready to use)"
    except ImportError:
        # Pyperclip not installed
        return False, "Pyperclip not installed. Install with 'pip install pyperclip'."
    except Exception as e:
        # Pyperclip failed, provide better error messages and fallbacks
        error_msg = str(e)
        
        # For Linux systems, provide specific guidance
        if system == "linux":
            # Check if the DISPLAY environment variable is set
            if not os.environ.get('DISPLAY'):
                display_msg = (
                    "**X11 Display Not Available**\n\n"
                    "Clipboard operations on Linux require X11 display access.\n"
                    "The DISPLAY environment variable is not set.\n\n"
                    "Options:\n"
                    "1. Run in a local desktop environment\n"
                    "2. Use X11 forwarding with 'ssh -X' or 'ssh -Y'\n"
                    "3. Use the '--no-clipboard' flag to disable clipboard attempts"
                )
                
                # Try to save to file as fallback
                try:
                    import tempfile
                    
                    fd, path = tempfile.mkstemp(suffix=".txt", prefix="curlthis_")
                    with os.fdopen(fd, 'w') as tmp:
                        tmp.write(text)
                    
                    fallback_msg = f"{display_msg}\n\nCommand saved to: {path}"
                    return False, fallback_msg
                except Exception:
                    return False, display_msg
            
            # Standard Linux clipboard utilities message
            install_msg = (
                "**Clipboard Access Failed**\n\n"
                "Clipboard operations on Linux require xclip or xsel.\n"
                "1. Install with: sudo apt install xclip\n"
                "2. Or: sudo apt install xsel\n\n"
                "After installation, you may need to log out and log back in,\n"
                "or restart your terminal session for pyperclip to detect them."
            )
            
            # Try to save to file as fallback
            try:
                import tempfile
                
                fd, path = tempfile.mkstemp(suffix=".txt", prefix="curlthis_")
                with os.fdopen(fd, 'w') as tmp:
                    tmp.write(text)
                
                fallback_msg = f"{install_msg}\n\nCommand saved to: {path}"
                return False, fallback_msg
            except Exception:
                return False, install_msg
                
        # For macOS, try pbcopy as fallback
        if system == "darwin":
            try:
                process = subprocess.Popen('pbcopy', stdin=subprocess.PIPE, close_fds=True)
                process.communicate(input=text.encode('utf-8'))
                if process.returncode == 0:
                    return True, "Copied to clipboard using pbcopy"
            except Exception:
                pass
                
        # For Windows, try clip.exe as fallback
        elif system == "windows":
            try:
                process = subprocess.Popen('clip', stdin=subprocess.PIPE, close_fds=True)
                process.communicate(input=text.encode('utf-8'))
                if process.returncode == 0:
                    return True, "Copied to clipboard using clip.exe"
            except Exception:
                pass
        
        # If all methods failed, save to file as fallback
        try:
            import tempfile
            
            fd, path = tempfile.mkstemp(suffix=".txt", prefix="curlthis_")
            with os.fdopen(fd, 'w') as tmp:
                tmp.write(text)
            
            fallback_msg = f"Clipboard access failed. Command saved to: {path}"
            return False, fallback_msg
        except Exception:
            # Last resort: just return the error
            return False, f"Clipboard error: {error_msg}"