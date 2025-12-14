import json
from urllib import request, error

BASE = "http://127.0.0.1:8000"

def req(method, path, data=None):
    url = BASE + path
    headers = {"Content-Type": "application/json"}
    data_bytes = None
    if data is not None:
        data_bytes = json.dumps(data).encode('utf-8')
    req = request.Request(url, data=data_bytes, headers=headers, method=method)
    try:
        with request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode('utf-8')
            status = resp.getcode()
            return status, json.loads(body) if body else None
    except error.HTTPError as e:
        body = e.read().decode('utf-8')
        print(f"HTTP {e.code} on {method} {path}: {body}")
        return e.code, None
    except Exception as e:
        print(f"Error on {method} {path}: {e}")
        return None, None

def test_usuario():
    print('\n--- Testing Usuario CRUD')
    # Create
    payload = {"nome":"Teste","email":"teste@example.com","senha":"senha","papel":"atleta"}
    s, body = req('POST', '/usuarios/', payload)
    print('POST /usuarios/ ->', s, body)
    uid = body.get('id') if body else None

    # List
    s, body = req('GET', '/usuarios/')
    print('GET /usuarios/ ->', s, body)

    # Get
    s, body = req('GET', f'/usuarios/{uid}')
    print(f'GET /usuarios/{uid} ->', s, body)

    # Update
    payload2 = {"nome":"Teste2","email":"teste2@example.com","senha":"nova","papel":"atleta"}
    s, body = req('PUT', f'/usuarios/{uid}', payload2)
    print(f'PUT /usuarios/{uid} ->', s, body)

    # Delete
    s, body = req('DELETE', f'/usuarios/{uid}')
    print(f'DELETE /usuarios/{uid} ->', s, body)

def test_equipe_atleta():
    print('\n--- Testing Equipe and Atleta CRUD')
    # Create treinador user
    t_payload = {"nome":"Treinador","email":"treinador@example.com","senha":"t","papel":"treinador"}
    s, body = req('POST', '/usuarios/', t_payload)
    tid = body.get('id') if body else None
    print('Created treinador id', tid)

    # Create equipe
    e_payload = {"nome":"Equipe A","categoria":"juvenil","treinador_id": tid}
    s, body = req('POST', '/equipes/', e_payload)
    eid = body.get('id') if body else None
    print('POST /equipes/ ->', s, body)

    # Create atleta
    a_payload = {"nome":"Atleta1","email":"atleta1@example.com","nascimento":"2005-01-01","posicao":"ala","equipe_id": eid}
    s, body = req('POST', '/atletas/', a_payload)
    aid = body.get('id') if body else None
    print('POST /atletas/ ->', s, body)

    # List equipes and atletas
    s, body = req('GET', '/equipes/')
    print('GET /equipes/ ->', s, body)
    s, body = req('GET', '/atletas/')
    print('GET /atletas/ ->', s, body)

    # Update equipe
    e_update = {"nome":"Equipe B","categoria":"senior","treinador_id": tid}
    s, body = req('PUT', f'/equipes/{eid}', e_update)
    print(f'PUT /equipes/{eid} ->', s, body)

    # Update atleta
    a_update = {"nome":"Atleta1-up","email":"atleta1-up@example.com","nascimento":"2005-01-01","posicao":"pivô","equipe_id": eid}
    s, body = req('PUT', f'/atletas/{aid}', a_update)
    print(f'PUT /atletas/{aid} ->', s, body)

    # Cleanup: delete atleta, equipe, treinador
    s, body = req('DELETE', f'/atletas/{aid}')
    print(f'DELETE /atletas/{aid} ->', s)
    s, body = req('DELETE', f'/equipes/{eid}')
    print(f'DELETE /equipes/{eid} ->', s)
    s, body = req('DELETE', f'/usuarios/{tid}')
    print(f'DELETE /usuarios/{tid} ->', s)

if __name__ == '__main__':
    test_usuario()
    test_equipe_atleta()
