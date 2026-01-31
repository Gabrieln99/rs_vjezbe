# RS Vježba 7 


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

## bez dokera kads pokrenmop

```bash
# stvoriti env
python -m venv venv

# Akttivireti ga preko windowsa
venv\Scripts\activate

# Aktivirati gitbsh
source venv/Scripts/activate

# inst dependense reqirements
pip install -r requirements.txt

# pokreni main
python main.py
```
