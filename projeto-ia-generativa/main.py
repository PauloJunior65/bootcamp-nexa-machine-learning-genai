#!/usr/bin/env python3
"""
Gerador de Conteúdo com IA Generativa

Ponto de entrada principal da aplicação.
Execute com: python main.py [--demo]
"""
import argparse
import sys

from src.cli import CLI


def main():
    """Função principal da aplicação."""
    parser = argparse.ArgumentParser(
        description="Gerador de Conteúdo com IA Generativa"
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Executar em modo demonstração (sem usar API real)"
    )
    
    args = parser.parse_args()
    
    try:
        cli = CLI(demo_mode=args.demo)
        cli.run()
    except KeyboardInterrupt:
        print("\n\n👋 Aplicação encerrada pelo usuário.")
        sys.exit(0)


if __name__ == "__main__":
    main()
