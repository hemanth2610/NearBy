import subprocess
import sys
import typer
from rich.console import Console

console = Console()


def reset_admin_command(
    email: str = typer.Option("admin@nearbyapp.com", "--email", "-e", help="Admin account email address"),
    password: str = typer.Option("Admin@Nearby2026!Secure", "--password", "-p", help="New admin password"),
    name: str = typer.Option("System Administrator", "--name", "-n", help="Admin display name"),
    list_users: bool = typer.Option(False, "--list", "-l", help="List all accounts in the database")
):
    """🔑 Reset admin password or create an administrator account."""
    cmd = [sys.executable, "scripts/reset_admin_password.py"]
    if list_users:
        cmd.append("--list")
    else:
        cmd.extend(["--email", email, "--password", password, "--name", name])

    try:
        subprocess.run(cmd, check=True)
    except Exception as e:
        console.print(f"[red]Reset admin command failed: {str(e)}[/red]")
