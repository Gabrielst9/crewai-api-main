import requests
from crewai.tools import BaseTool
import os
from typing import Dict, Any
import json

class FetchConteudoEducacionalTool(BaseTool):
    name: str = "Busca de Recursos Educacionais"
    description: str = (
        "Busca recursos educacionais online (vídeos, artigos, planos de aula) "
        "relacionados ao tema especificado. Retorna resultados categorizados."
    )

    def _run(self, tema: str) -> str:
        #executa busca em múltiplas fontes e formata os resultados
        resultados = {
            "wikipedia": self._buscar_wikipedia(tema),
            "duckduckgo": self._buscar_ddg(tema),
            "youtube": self._buscar_youtube(tema),
            "nova_escola": self._buscar_portal_educacional(tema)
        }
        
        return self._formatar_resultados(resultados)

    def _buscar_wikipedia(self, tema: str) -> Dict[str, Any]:
        #busca conteúdo na Wikipedia
        try:
            url = f"https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&explaintext&titles={tema}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            pages = data.get("query", {}).get("pages", {})
            
            if pages:
                page_id = next(iter(pages))
                page_data = pages[page_id]
                if 'extract' in page_data:
                    return {
                        "conteudo": page_data['extract'][:500] + "...",
                        "url": f"https://pt.wikipedia.org/wiki/{tema.replace(' ', '_')}"
                    }
            return {}
        except Exception as e:
            print(f"Erro na busca Wikipedia: {str(e)}")
            return {}

    def _buscar_ddg(self, tema: str) -> Dict[str, Any]:
        #busca na API do DuckDuckGo
        try:
            url = f"{os.getenv('DUCKDUCKGO_API_URL')}?q={tema}&format=json&no_html=1"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return {
                "conteudo": data.get("AbstractText", ""),
                "url": data.get("AbstractURL", "")
            }
        except Exception as e:
            print(f"Erro na busca DuckDuckGo: {str(e)}")
        return {}

    def _buscar_youtube(self, tema: str) -> Dict[str, Any]:
        #busca vídeos educacionais no YouTube
        try:
            api_key = os.getenv("YOUTUBE_API_KEY")
            if not api_key:
                return {}
                
            url = f"{os.getenv('YOUTUBE_API_URL')}?part=snippet&maxResults=1&q={tema}+educação&type=video&key={api_key}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if data.get("items"):
                video = data["items"][0]
                return {
                    "titulo": video["snippet"]["title"],
                    "url": f"https://youtube.com/watch?v={video['id']['videoId']}"
                }
        except Exception as e:
            print(f"Erro na busca YouTube: {str(e)}")
        return {}

    def _buscar_portal_educacional(self, tema: str) -> Dict[str, Any]:
        #simula busca no portal Nova Escola
        try:
            return {
                "conteudo": f"Planos de aula e atividades sobre {tema}",
                "url": f"https://novaescola.org.br/busca?q={tema}"
            }
        except Exception as e:
            print(f"Erro na busca Portal Educacional: {str(e)}")
        return {}

    def _formatar_resultados(self, resultados: Dict[str, Any]) -> str:
        #formata os resultados para exibição
        output = []
        
        if resultados["wikipedia"]:
            output.append(f"📚 Wikipedia: {resultados['wikipedia']['conteudo']}")
            output.append(f"🔗 {resultados['wikipedia']['url']}\n")
        
        if resultados["duckduckgo"] and resultados["duckduckgo"]["conteudo"]:
            output.append(f"🔍 DuckDuckGo: {resultados['duckduckgo']['conteudo']}")
            output.append(f"🔗 {resultados['duckduckgo']['url']}\n")
        
        if resultados["youtube"]:
            output.append(f"🎬 YouTube: {resultados['youtube']['titulo']}")
            output.append(f"🔗 {resultados['youtube']['url']}\n")
        
        if resultados["nova_escola"]:
            output.append(f"🏫 Portal Educacional: {resultados['nova_escola']['conteudo']}")
            output.append(f"🔗 {resultados['nova_escola']['url']}\n")
        
        return "\n".join(output) if output else "Nenhum recurso educacional encontrado para este tema."