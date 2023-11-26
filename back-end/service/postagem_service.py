import os
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

#Extrair caminho relativo para variável de ambiente
caminho_relativo_json_postagens = Path('back-end/input_files/json/postagens.json')
caminho_relativo_jinja_template = Path('front-end/jinja_templates')
caminho_arquivo_index_html = 'index.html'

def obter_caminho_absoluto_pelo_relativo(caminho_relativo):
    caminho_absoluto = Path.cwd() / caminho_relativo
    return caminho_absoluto

def ler_json_pelo_caminho_absoluto(caminho_absoluto):
    with open(caminho_absoluto, 'r', encoding='utf-8') as arquivo:
        lista_objetos = json.load(arquivo)
    return lista_objetos

def configurar_template_jinja(caminho_relativo_jinja_template):
    
    caminho_absoluto_jinja_template = obter_caminho_absoluto_pelo_relativo(caminho_relativo_jinja_template)
    
    jinja_env = Environment(loader = FileSystemLoader(caminho_absoluto_jinja_template))
    

    jinja_template = jinja_env.get_template('index-template.html')
    return jinja_template
    
def renderizar_dados_template(jinja_template, json, caminho_arquivo_saida):
    
    html_saida = jinja_template.render(lista_postagens = json)
    
    with open(caminho_arquivo_saida, 'w', encoding='utf-8') as saida_html:
        saida_html.write(html_saida)
    return saida_html

def deletar_index_antigo():
    if os.path.exists(caminho_arquivo_index_html):
        os.remove(caminho_arquivo_index_html)

def parsear_json_para_html():
    
    deletar_index_antigo()
    
    caminho_absoluto_json_postagens = obter_caminho_absoluto_pelo_relativo(caminho_relativo_json_postagens)
    
    lista_postagens = ler_json_pelo_caminho_absoluto(caminho_absoluto_json_postagens)
    
    jinja_template = configurar_template_jinja(caminho_relativo_jinja_template)
    
    renderizar_dados_template(jinja_template, lista_postagens, caminho_arquivo_index_html)

parsear_json_para_html()
    
    






