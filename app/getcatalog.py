import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import quote
import xml.etree.ElementTree as ET
import html

# === CONFIGURAÇÕES ===
ORGANIZATION = "TI-Desenvolvimento"
PAT = "FCSZaifCeD9b6cGjWXEUlN4SPU0WEm5xIpfQ0fZeMJkHTacFFFpKJQQJ99BEACAAAAAsgxOaAAASAZDO3fFG"
API_VERSION = "7.0"
BASE_URL = f"https://dev.azure.com/{ORGANIZATION}"
auth = HTTPBasicAuth('', PAT)
NAMESPACE = {'m': 'http://maven.apache.org/POM/4.0.0'}

def get_projects():
    url = f"{BASE_URL}/_apis/projects?api-version={API_VERSION}"
    response = requests.get(url, auth=auth)
    response.raise_for_status()
    return response.json()['value']

def get_pipelines(project_id):
    url = f"{BASE_URL}/{project_id}/_apis/pipelines?api-version={API_VERSION}"
    response = requests.get(url, auth=auth)
    response.raise_for_status()
    return response.json()['value']

def get_pom_data(project_id, repo_name, path='/pom.xml'):
    encoded_path = quote(path, safe='')
    url = f"{BASE_URL}/{project_id}/_apis/git/repositories/{repo_name}/items?path={path}&includeContent=true&api-version={API_VERSION}"
    response = requests.get(url, auth=auth)
    if response.status_code != 200:
        return None
    try:
        content = response.content.decode("utf-8")
    except UnicodeDecodeError:
        content = response.content.decode("latin-1")
    try:
        return parse_pom(content)
    except ET.ParseError:
        print(f"Erro ao fazer parse do XML no pipeline: {repo_name}")
        return None

def parse_pom(xml_content):
    root = ET.fromstring(xml_content)

    def get_text(tag):
        elem = root.find(f'm:{tag}', NAMESPACE)
        return elem.text if elem is not None else ''

    def get_parent_text(tag):
        elem = root.find(f'm:parent/m:{tag}', NAMESPACE)
        return elem.text if elem is not None else ''

    def get_property(key):
        elem = root.find(f'm:properties/m:{key}', NAMESPACE)
        return elem.text if elem is not None else ''

    def get_dependencies():
        return [
            f"{dep.find('m:groupId', NAMESPACE).text}:{dep.find('m:artifactId', NAMESPACE).text}"
            for dep in root.findall('m:dependencies/m:dependency', NAMESPACE)
            if dep.find('m:groupId', NAMESPACE) is not None and dep.find('m:artifactId', NAMESPACE) is not None
        ]

    def get_plugins():
        return [
            f"{plugin.find('m:groupId', NAMESPACE).text}:{plugin.find('m:artifactId', NAMESPACE).text}"
            for plugin in root.findall('m:build/m:plugins/m:plugin', NAMESPACE)
            if plugin.find('m:groupId', NAMESPACE) is not None and plugin.find('m:artifactId', NAMESPACE) is not None
        ]

    return {
        'name': get_text('name'),
        'description': html.unescape(get_text('description')),
        'groupId': get_text('groupId'),
        'artifactId': get_text('artifactId'),
        'version': get_text('version'),
        'java_version': get_property('java.version'),
        'spring_boot_version': get_parent_text('version'),
        'dependencies': get_dependencies(),
        'plugins': get_plugins()
    }
