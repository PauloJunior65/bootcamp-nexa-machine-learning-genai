"""
Módulo de interface de linha de comando.
"""
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.text import Text

from .generator import ContentGenerator
from .config import Config


class CLI:
    """Interface de linha de comando para o gerador de conteúdo."""
    
    def __init__(self, demo_mode: bool = False):
        """
        Inicializa a CLI.
        
        Args:
            demo_mode: Se True, força o modo demonstração.
        """
        self.console = Console()
        self.generator = ContentGenerator(demo_mode=demo_mode)
    
    def show_header(self):
        """Exibe o cabeçalho da aplicação."""
        title = Text("🤖 Gerador de Conteúdo com IA Generativa", style="bold cyan")
        self.console.print(Panel(title, expand=False))
        
        if self.generator.demo_mode:
            self.console.print(
                "[yellow]⚠️  Modo demonstração ativado (sem API key configurada)[/yellow]\n"
            )
        else:
            self.console.print(
                "[green]✅ API OpenAI configurada[/green]\n"
            )
    
    def show_menu(self) -> int:
        """
        Exibe o menu principal e retorna a opção escolhida.
        
        Returns:
            Número da opção escolhida.
        """
        menu_text = """
[bold]? Escolha uma opção:[/bold]

  [cyan]1.[/cyan] 📝 Gerar texto criativo
  [cyan]2.[/cyan] 💡 Gerar ideias para projeto
  [cyan]3.[/cyan] 📦 Gerar descrição de produto
  [cyan]4.[/cyan] 🎯 Gerar título/headline
  [cyan]5.[/cyan] ❌ Sair
"""
        self.console.print(menu_text)
        
        choice = IntPrompt.ask(
            "[bold]> Sua escolha[/bold]",
            choices=["1", "2", "3", "4", "5"],
            default=5
        )
        return choice
    
    def show_result(self, title: str, content: str):
        """
        Exibe o resultado gerado.
        
        Args:
            title: Título do resultado.
            content: Conteúdo gerado.
        """
        self.console.print()
        self.console.print(Panel(content, title=title, expand=False, border_style="green"))
        self.console.print()
    
    def run(self):
        """Executa o loop principal da aplicação."""
        self.show_header()
        
        while True:
            choice = self.show_menu()
            
            if choice == 5:
                self.console.print("\n[cyan]👋 Até logo![/cyan]\n")
                break
            
            if choice == 1:
                topic = Prompt.ask("\n[bold]> Tema do texto[/bold]")
                with self.console.status("[cyan]Gerando texto...[/cyan]"):
                    result = self.generator.generate_creative_text(topic)
                self.show_result("📝 Texto Gerado", result)
            
            elif choice == 2:
                topic = Prompt.ask("\n[bold]> Tema para ideias[/bold]")
                with self.console.status("[cyan]Gerando ideias...[/cyan]"):
                    result = self.generator.generate_project_ideas(topic)
                self.show_result("💡 Ideias de Projeto", result)
            
            elif choice == 3:
                product = Prompt.ask("\n[bold]> Nome do produto[/bold]")
                with self.console.status("[cyan]Gerando descrição...[/cyan]"):
                    result = self.generator.generate_product_description(product)
                self.show_result("📦 Descrição do Produto", result)
            
            elif choice == 4:
                topic = Prompt.ask("\n[bold]> Tema para títulos[/bold]")
                with self.console.status("[cyan]Gerando títulos...[/cyan]"):
                    result = self.generator.generate_headline(topic)
                self.show_result("🎯 Títulos Sugeridos", result)
            
            # Perguntar se quer continuar
            continue_prompt = Prompt.ask(
                "[bold]Deseja continuar?[/bold]",
                choices=["s", "n"],
                default="s"
            )
            if continue_prompt.lower() == "n":
                self.console.print("\n[cyan]👋 Até logo![/cyan]\n")
                break
            
            self.console.print("\n" + "─" * 50 + "\n")
