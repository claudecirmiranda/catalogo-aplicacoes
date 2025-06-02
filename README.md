# Catálogo de Aplicações (Azure DevOps)

Este projeto Flask gera e exibe um catálogo visual de aplicações com base nos pipelines e repositórios do Azure DevOps, utilizando jsTree para visualização hierárquica.

## Funcionalidades
- Leitura dos projetos, pipelines e arquivos `pom.xml` do Azure DevOps
- Extração de informações como `groupId`, `artifactId`, `versão`, `dependências`, etc.
- Interface com árvore interativa e botão de atualização

## Instalação local
```bash
git clone https://github.com/claudecirmiranda/catalogo-aplicacoes.git
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
Veja manifesto `K8S/k8s-deploy.yaml` para deploy em Oracle Kubernetes Engine (OKE).

### Criar Secret para PAT:

```
kubectl create secret generic azure-pat --from-literal=pat='<SEU_PAT_AQUI>'
```

### Subir para o OKE:

```
kubectl apply -f K8S/k8s-deploy.yaml
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

