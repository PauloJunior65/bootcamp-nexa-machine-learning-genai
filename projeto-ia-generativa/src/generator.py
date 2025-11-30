"""
Módulo de geração de conteúdo com IA.
"""
import random
from typing import Optional

from .config import Config


class ContentGenerator:
    """Gerador de conteúdo usando IA Generativa."""
    
    def __init__(self, demo_mode: bool = False):
        """
        Inicializa o gerador.
        
        Args:
            demo_mode: Se True, usa respostas simuladas ao invés da API real.
        """
        self.demo_mode = demo_mode or not Config.is_api_configured()
        self.client = None
        
        if not self.demo_mode:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
            except ImportError:
                self.demo_mode = True
    
    def _generate_with_api(self, prompt: str, system_prompt: str) -> str:
        """Gera conteúdo usando a API da OpenAI."""
        if self.client is None:
            return self._generate_demo(prompt)
        
        response = self.client.chat.completions.create(
            model=Config.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content or ""
    
    def _generate_demo(self, prompt: str) -> str:
        """Gera conteúdo simulado para modo demonstração."""
        demo_responses = {
            "texto": [
                f"Este é um texto criativo gerado sobre '{prompt}'. "
                "A Inteligência Artificial está revolucionando a forma como criamos conteúdo. "
                "Com modelos de linguagem avançados, podemos gerar textos que parecem escritos por humanos, "
                "abrindo novas possibilidades para criadores de conteúdo, escritores e desenvolvedores.",
                
                f"Explorando o tema '{prompt}', podemos observar que a tecnologia de IA Generativa "
                "está transformando diversos setores. Desde a criação de arte até a programação, "
                "essas ferramentas estão se tornando cada vez mais sofisticadas e acessíveis.",
            ],
            "ideias": [
                f"💡 Ideias de projeto sobre '{prompt}':\n\n"
                "1. **Chatbot Inteligente**: Crie um assistente virtual que responda perguntas\n"
                "2. **Gerador de Imagens**: Desenvolva uma aplicação que crie arte com IA\n"
                "3. **Analisador de Sentimentos**: Ferramenta para análise de textos\n"
                "4. **Tradutor Automático**: Sistema de tradução em tempo real\n"
                "5. **Resumidor de Textos**: Aplicação que resume documentos longos",
            ],
            "produto": [
                f"📦 **{prompt}**\n\n"
                "Descubra a revolução em tecnologia! Este produto inovador combina "
                "design elegante com funcionalidade excepcional. Desenvolvido com os mais "
                "altos padrões de qualidade, oferece uma experiência única que supera todas "
                "as expectativas. Ideal para quem busca excelência e inovação no dia a dia.",
            ],
            "titulo": [
                f"🎯 Títulos sugeridos para '{prompt}':\n\n"
                "• \"Descubra o Futuro: Uma Jornada Incrível\"\n"
                "• \"Transformando Ideias em Realidade\"\n"
                "• \"O Guia Definitivo para o Sucesso\"\n"
                "• \"Inovação que Inspira, Resultados que Impressionam\"\n"
                "• \"Além dos Limites: Explorando Novas Fronteiras\"",
            ],
        }
        return random.choice(demo_responses.get("texto", demo_responses["texto"]))
    
    def generate_creative_text(self, topic: str) -> str:
        """
        Gera um texto criativo sobre o tema fornecido.
        
        Args:
            topic: Tema do texto a ser gerado.
            
        Returns:
            Texto criativo gerado.
        """
        if self.demo_mode:
            return self._generate_demo(topic)
        
        system_prompt = (
            "Você é um escritor criativo e envolvente. "
            "Escreva textos interessantes e bem estruturados em português brasileiro."
        )
        prompt = f"Escreva um texto criativo e envolvente sobre: {topic}"
        return self._generate_with_api(prompt, system_prompt)
    
    def generate_project_ideas(self, topic: str) -> str:
        """
        Gera ideias de projetos relacionadas ao tema.
        
        Args:
            topic: Tema para geração de ideias.
            
        Returns:
            Lista de ideias de projetos.
        """
        if self.demo_mode:
            demo_responses = [
                f"💡 Ideias de projeto sobre '{topic}':\n\n"
                "1. **Chatbot Inteligente**: Crie um assistente virtual que responda perguntas\n"
                "2. **Gerador de Imagens**: Desenvolva uma aplicação que crie arte com IA\n"
                "3. **Analisador de Sentimentos**: Ferramenta para análise de textos\n"
                "4. **Tradutor Automático**: Sistema de tradução em tempo real\n"
                "5. **Resumidor de Textos**: Aplicação que resume documentos longos",
            ]
            return random.choice(demo_responses)
        
        system_prompt = (
            "Você é um consultor de tecnologia criativo. "
            "Sugira ideias inovadoras de projetos de software em português brasileiro."
        )
        prompt = f"Sugira 5 ideias criativas de projetos de programação sobre: {topic}"
        return self._generate_with_api(prompt, system_prompt)
    
    def generate_product_description(self, product: str) -> str:
        """
        Gera uma descrição de produto.
        
        Args:
            product: Nome ou descrição do produto.
            
        Returns:
            Descrição de marketing do produto.
        """
        if self.demo_mode:
            return (
                f"📦 **{product}**\n\n"
                "Descubra a revolução em tecnologia! Este produto inovador combina "
                "design elegante com funcionalidade excepcional. Desenvolvido com os mais "
                "altos padrões de qualidade, oferece uma experiência única que supera todas "
                "as expectativas. Ideal para quem busca excelência e inovação no dia a dia."
            )
        
        system_prompt = (
            "Você é um copywriter especializado em descrições de produtos. "
            "Crie descrições persuasivas e envolventes em português brasileiro."
        )
        prompt = f"Crie uma descrição de marketing atraente para o produto: {product}"
        return self._generate_with_api(prompt, system_prompt)
    
    def generate_headline(self, topic: str) -> str:
        """
        Gera títulos e headlines.
        
        Args:
            topic: Tema para geração de títulos.
            
        Returns:
            Lista de títulos sugeridos.
        """
        if self.demo_mode:
            return (
                f"🎯 Títulos sugeridos para '{topic}':\n\n"
                "• \"Descubra o Futuro: Uma Jornada Incrível\"\n"
                "• \"Transformando Ideias em Realidade\"\n"
                "• \"O Guia Definitivo para o Sucesso\"\n"
                "• \"Inovação que Inspira, Resultados que Impressionam\"\n"
                "• \"Além dos Limites: Explorando Novas Fronteiras\""
            )
        
        system_prompt = (
            "Você é um especialista em marketing e copywriting. "
            "Crie títulos impactantes e chamativos em português brasileiro."
        )
        prompt = f"Crie 5 títulos/headlines criativos e impactantes sobre: {topic}"
        return self._generate_with_api(prompt, system_prompt)
