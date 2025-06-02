# 📚 Catálogo de Aplicações (Azure DevOps)

Projeto web em Flask que gera um catálogo visual interativo com base em pipelines e repositórios do Azure DevOps, organizados em estrutura de árvore usando jsTree.

## ✨ Funcionalidades

 - 🔍 Leitura automática de projetos, pipelines e arquivos pom.xml do Azure DevOps.
 - 📦 Extração de informações como:

    - groupId, artifactId, version
    - dependencies e plugins
    - Versões de Java e Spring Boot
 - 🌳 Interface com árvore interativa (jsTree) e botão para atualização dinâmica do catálogo.

## 🚀 Instalação Local

```
bash
git clone https://github.com/claudecirmiranda/catalogo-aplicacoes.git
cd catalogo-aplicacoes
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python app/web.py
```

## ⚙️ Configuração
No arquivo app/getcatalog.py, substitua a variável PAT pelo seu Personal Access Token (PAT) do Azure DevOps:
```
python
PAT = "<SEU_PAT_AQUI>"
```

**⚠ Importante: Para ambientes de produção, utilize um secret em vez de deixar o PAT no código-fonte.**

# 🐳 Executando com Docker
```bash
docker build -t catalogo-aplicacoes .
docker run -p 5000:5000 catalogo-aplicacoes
```

#🔁 Atualização do Catálogo

A aplicação possui um botão "Atualizar Catálogo" que aciona uma rota Flask (/atualizar) para buscar e reconstruir o JSON com os dados mais recentes do Azure DevOps.
☁️ Deploy no Oracle Kubernetes Engine (OKE)
 1. Criar Secret com PAT
```
bash
kubectl create secret generic azure-pat --from-literal=pat='<SEU_PAT_AQUI>'
```

 2. Build e push da imagem para seu container registry
```bash
docker build -t <seu-registry>/catalogo-aplicacoes:latest .
docker push <seu-registry>/catalogo-aplicacoes:latest
```

 3. Aplicar os manifests Kubernetes
```bash
kubectl apply -f K8S/k8s-deploy.yaml
kubectl apply -f K8S/service.yaml
```

**Nota**: Certifique-se de que seu cluster tenha acesso à internet e permissões para pull da imagem.

## 📁 Estrutura do Projeto
```
bash

CATALOGO-APLICACOES
│   .gitignore
│   Dockerfile
│   README.md
│   requirements.txt
│
├───app
│   │   getcatalog.py    # Consulta APIs do Azure DevOps e extrai dados do POM
│   │   web.py           # Aplicação Flask principal
│   │   __init__.py
│
├───static
│   │   tree_data.json   # JSON gerado para alimentar a árvore
│
└───templates
│   │   index.html       # Frontend com jsTree + Bootstrap
│
└───K8S
    │   k8s-deploy.yaml  # Deployment + volume + secret
    │   service.yaml     # Service NodePort para expor a aplicação
```

## 📄 Licença
Projeto privado / interno. Para uso sob autorização.