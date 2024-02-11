import os 
from rich.console import Console

console = Console()
console.print(os.path.dirname(__file__))