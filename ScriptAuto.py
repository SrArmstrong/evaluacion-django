import requests

# Credenciales del usuario administrador
LOGIN_URL = "http://127.0.0.1:8000/api/token/"
REFRESH_URL = "http://127.0.0.1:8000/api/token/refresh/"
API_URL = "http://127.0.0.1:8000/api/peliculas/"

# Usuario y contraseña
credentials = {
    "username": "sergio",
    "password": "sergio"
}

# Obtener TOKEN JWT
response = requests.post(LOGIN_URL, json=credentials)
if response.status_code == 200:
    tokens = response.json()
    access_token = tokens["access"]
    refresh_token = tokens["refresh"]
    print("Token obtenido correctamente.")
else:
    print("Error en la autenticación.")
    exit()

# Función para obtener datos con autenticación
def get_peliculas(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:  # catch para marcar error en caso de que el token no funcione
        return refresh_access_token()
    else:
        print(f" Error: {response.status_code}")
        return None

# Funcion dedicada a refresca el TOKEN en caso de que no funcione correctamente
def refresh_access_token():
    global access_token
    response = requests.post(REFRESH_URL, json={"refresh": refresh_token})
    
    if response.status_code == 200:
        new_tokens = response.json()
        access_token = new_tokens["access"]
        print("Token refrescado correctamente.")
        return get_peliculas(access_token)
    else:
        print("No se pudo refrescar el token. Vuelve a iniciar sesión.")
        exit()

# Llamar a la API automáticamente con autenticación
peliculas = get_peliculas(access_token)
if peliculas:
    print("Películas obtenidas:")
    print(peliculas)
