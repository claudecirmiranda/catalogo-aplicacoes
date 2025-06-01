# Catálogo de Aplicações (Azure DevOps)

Este projeto Flask gera e exibe um catálogo visual de aplicações com base nos pipelines e repositórios do Azure DevOps, utilizando jsTree para visualização hierárquica.

## Funcionalidades
- Leitura dos projetos, pipelines e arquivos `pom.xml` do Azure DevOps
- Extração de informações como `groupId`, `artifactId`, `versão`, `dependências`, etc.
- Interface com árvore interativa e botão de atualização

## Instalação local
```bash
git clone https://github.com/seuusuario/catalogo-aplicacoes.git
cd catalogo-aplicacoes
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python app/web.py
```

## Configuração
No arquivo `getcatalog.py`, substitua a variável `PAT` pelo seu token pessoal de acesso ao Azure DevOps:
```python
PAT = "<SEU_PAT_AQUI>"
```

## Executando via Docker
```bash
docker build -t catalogo-aplicacoes .
docker run -p 5000:5000 catalogo-aplicacoes
```

## Atualizar Catálogo
Através do botão "Atualizar Catálogo" na interface, o backend acessa o Azure DevOps e atualiza os dados.

## Deploy no OKE
Veja manifesto `k8s-deploy.yaml` para deploy em Oracle Kubernetes Engine (OKE).