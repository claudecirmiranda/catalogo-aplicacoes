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
│   │   getcatalog.py        # Consulta APIs do Azure DevOps e extrai dados do POM
│   │   web.py               # Aplicação Flask principal
│   │   __init__.py
│   │
│   ├───static
│   │       tree_data.json   # JSON gerado para alimentar a árvore
│   │
│   ├───templates
│   │       index.html       # Frontend com jsTree + Bootstrap
│   │
│   └───__pycache__
│           getcatalog.cpython-310.pyc
│
├───K8S
│       k8s-deploy.yaml  # Deployment + volume + secret
│       service.yaml     # Service NodePort para expor a aplicação
```

------

Este é projeto **bem estruturado** para atender de forma **genérica e reutilizável** a catalogação de aplicações **Java com `pom.xml` no Azure DevOps**, com as seguintes características que reforçam isso:

* * *

### ✅ **Por que ele é genérico e reutilizável?**

#### 1. **Consulta dinâmica à API do Azure DevOps**

*   Utiliza `get_projects()` e `get_pipelines()` para buscar _todos os projetos e pipelines_, independentemente de nomes ou estrutura.
    
*   Isso permite adicionar novos projetos ao Azure DevOps sem alterar o código.

#### 2. **Extração robusta de `pom.xml`**

*   O método `get_pom_data()` faz parse XML genérico baseado no [namespace oficial do Maven](http://maven.apache.org/POM/4.0.0), o que cobre praticamente todos os projetos Java padrão.
    
*   Pega dados como: `groupId`, `artifactId`, `version`, `dependencies`, `plugins`, versão Java e Spring Boot — que são comuns à maioria dos projetos Java modernos.
    

#### 3. **Exibição baseada em estrutura**

*   A exibição via `jsTree` é baseada em:
    *   Projeto
        
    *   Pasta (folder)
        
    *   Pipeline
        
    *   Informações do `pom.xml`
        
*   Ou seja, você pode aplicar o sistema a qualquer repositório Java que use Maven (`pom.xml`) e esteja versionado no Azure DevOps.
    

* * *

### 🔁 **O que ele _não_ faz (mas pode ser estendido para fazer)**

1.  **Suporte a outros tipos de projeto**
    *   Atualmente funciona apenas com Maven (`pom.xml`). Não suporta:
        *   Gradle (`build.gradle`)
            
        *   Projetos .NET (`.csproj`)
            
        *   Projetos Node.js (`package.json`)
            
2.  **Filtragem por tecnologia ou tags**
    *   Não há tags, labels ou filtros avançados. Isso poderia ser adicionado via leitura de YAML ou arquivos específicos no repositório.
        
3.  **Detecção de múltiplos módulos**
    *   Projetos multi-module com `pom.xml` pai + filhos ainda não são explicitamente tratados como hierarquia (a menos que estejam em repositórios separados).
        

* * *

### ✅ **Conclusão**

Este projeto **é genérico o suficiente para catalogar qualquer repositório Java com `pom.xml` hospedado no Azure DevOps**, desde que:
*   A estrutura do `pom.xml` esteja de acordo com o Maven padrão.
    
*   Os projetos estejam acessíveis via Azure DevOps API (o token tem permissão).
    
Com pequenas melhorias, podemos ampliar para outras linguagens ou ferramentas de build.


## 📄 Licença
Projeto privado / interno. Para uso sob autorização.

