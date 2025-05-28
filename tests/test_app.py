import os
import tempfile
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    # Crée un dossier temporaire pour les fichiers
    temp_dir = tempfile.TemporaryDirectory()
    app.FILES_DIR = temp_dir.name

    # Ajoute un fichier test dedans
    test_file_path = os.path.join(temp_dir.name, "test.txt")
    with open(test_file_path, "w") as f:
        f.write("contenu test")

    with app.test_client() as client:
        yield client

    temp_dir.cleanup()

def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"test.txt" in rv.data

def test_api_files(client):
    rv = client.get("/api/files")
    assert rv.status_code == 200
    assert b"test.txt" in rv.data

def test_download(client):
    rv = client.get("/download/test.txt")
    assert rv.status_code == 200
    assert rv.data == b"contenu test"
    
def test_api_files(client):
    rv = client.get("/api/files")
    assert rv.status_code == 200
    data = rv.get_json()
    assert isinstance(data, list)
    assert any(f["name"] == "test.txt" for f in data)

def test_api_download(client):
    rv = client.get("/api/download/test.txt")
    assert rv.status_code == 200
    assert rv.data == b"contenu test"
    
def test_api_download_not_found(client):
    rv = client.get("/api/download/fichier_inexistant.txt")
    assert rv.status_code == 404



