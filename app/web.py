from flask import Flask, render_template, jsonify
import json
from getcatalog import get_pipelines, get_pom_data, get_projects 

app = Flask(__name__)

def gerar_tree_data():
    # === GERAÇÃO DO JSON PARA jsTree COM AGRUPAMENTO POR FOLDER, IGNORANDO Nós vazios ===

    tree_data = []

    for project in get_projects():
        project_node = {
            "text": f"Projeto: {project['name']}",
            "children": []
        }

        # Agrupar pipelines por folder
        grupo_por_pasta = {}
        for pipeline in get_pipelines(project['id']):
            folder = pipeline.get('folder', 'Outros')
            if folder not in grupo_por_pasta:
                grupo_por_pasta[folder] = []
            grupo_por_pasta[folder].append(pipeline)

        for folder, pipelines_grupo in grupo_por_pasta.items():
            # Cria o nó da pasta, só se tiver pipelines nesse grupo
            if not pipelines_grupo:
                continue  # Pula pastas vazias

            folder_node = {
                "text": f"Folder: {folder}",
                "children": []
            }

            for pipeline in pipelines_grupo:
                # Opcional: ignorar pipelines sem detalhes
                # ou pipelines que geraram apenas o nó de pasta vazio
                pipeline_node = {
                    "text": f"Pipeline: {pipeline['name']}",
                    "children": []
                }

                # Buscar detalhes do pom_data
                pom_data = get_pom_data(project['id'], pipeline['name'])
                if pom_data:
                    info_fields = [
                        ("Nome", pom_data['name']),
                        ("Descrição", pom_data['description']),
                        ("GroupId", pom_data['groupId']),
                        ("ArtifactId", pom_data['artifactId']),
                        ("Versão", pom_data['version']),
                        ("Java", pom_data['java_version']),
                        ("Spring Boot", pom_data['spring_boot_version'])
                    ]
                    for label, value in info_fields:
                        if value:
                            pipeline_node["children"].append({
                                "text": f"{label}: {value}",
                                "icon": "jstree-file"
                            })

                    if pom_data['dependencies']:
                        deps = {
                            "text": "Dependências",
                            "children": [{"text": dep, "icon": "jstree-file"} for dep in pom_data['dependencies']]
                        }
                        pipeline_node["children"].append(deps)

                    if pom_data['plugins']:
                        plugins = {
                            "text": "Plugins",
                            "children": [{"text": plugin, "icon": "jstree-file"} for plugin in pom_data['plugins']]
                        }
                        pipeline_node["children"].append(plugins)

                # Só adiciona pipeline se tiver filhos
                if pipeline_node["children"]:
                    folder_node["children"].append(pipeline_node)

            # Só adiciona pasta se tiver pipelines (filhos)
            if folder_node["children"]:
                project_node["children"].append(folder_node)

        # Adiciona o projeto só se tiver pastas/ pipelines
        if project_node["children"]:
            tree_data.append(project_node)

    # Salvar em arquivo
    with open("static/tree_data.json", "w", encoding="utf-8") as f:
        json.dump(tree_data, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    # Apenas exibe a página
    return render_template('index.html')

@app.route('/atualizar', methods=['POST'])
def atualizar():
    # Executa a geração do JSON
    gerar_tree_data()
    # Retorna sucesso
    return jsonify({"status": "ok"})

# Se desejar, na inicialização, gerar o JSON uma primeira vez
if __name__ == '__main__':
    gerar_tree_data()
    app.run(debug=True)