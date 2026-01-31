# RS Vježba 7 - Kontejnerizacija mikroservisa


## zadatak 1.8
## authAPI (aiohttp - port 9000)
Mikroservis za autentifikaciju korisnika.

## socialAPI (FastAPI - port 3500)
Mikroservis za objave na društvenoj mreži.

---

## Pokretanje s Dockerom

```bash
# authAPI
cd authAPI
docker build -t authapi .
docker run -d -p 9000:9000 authapi

# socialAPI
cd socialAPI
docker build -t socialapi .
docker run -d -p 3500:3500 socialapi
```

## Lokalno pokretanje (bez Dockera)

```bash
# Kreiraj virtual environment
python -m venv venv

# Aktiviraj (Windows)
venv\Scripts\activate

# Aktiviraj (Git Bash)
source venv/Scripts/activate

# Instaliraj dependencies
pip install -r requirements.txt

# Pokreni
python main.py
```
