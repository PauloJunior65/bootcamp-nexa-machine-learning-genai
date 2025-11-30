"""
Módulo de configuração da aplicação.
"""
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


class Config:
    """Configurações da aplicação."""
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    @classmethod
    def is_api_configured(cls) -> bool:
        """Verifica se a API key está configurada."""
        return bool(cls.OPENAI_API_KEY and cls.OPENAI_API_KEY != "sua-chave-aqui")
