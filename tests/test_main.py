from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_criar_e_listar_animal():
    novo_animal = {
        "nome": "Thor",
        "especie": "Canino",
        "porte": "Médio",
        "temperamento": "Dócil e brincalhão",
        "castrado": True,
        "vacinas_em_dia": True,
        "foto_url": "https://example.com/thor.jpg"
    }
    post_res = client.post("/api/animais", json=novo_animal)
    assert post_res.status_code == 201
    animal_data = post_res.json()
    assert animal_data["nome"] == "Thor"
    animal_id = animal_data["id"]

    get_res = client.get("/api/animais?especie=Canino")
    assert get_res.status_code == 200
    animais = get_res.json()
    assert any(a["id"] == animal_id for a in animais)

def test_submissao_candidatura():
    post_animal = client.post("/api/animais", json={
        "nome": "Mia",
        "especie": "Felino",
        "porte": "Pequeno",
        "temperamento": "Tranquila",
        "castrado": True,
        "vacinas_em_dia": True,
        "foto_url": "https://example.com/mia.jpg"
    })
    animal_id = post_animal.json()["id"]

    candidatura = {
        "animal_id": animal_id,
        "nome_candidato": "Lucas Silveira",
        "email_candidato": "lucas@example.com",
        "telefone_whatsapp": "(11) 98765-4321",
        "tipo_moradia": "Apartamento",
        "possui_telas_protecao": True
    }
    post_cand = client.post("/api/candidaturas", json=candidatura)
    assert post_cand.status_code == 201
    assert post_cand.json()["status_triagem"] == "Em Análise"
