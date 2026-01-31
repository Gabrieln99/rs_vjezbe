import hashlib
from aiohttp import web

korisnici = [
    {"korisnicko_ime": "admin", "lozinka_hash": "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"},  # lozinka = "lozinka123"
    {"korisnicko_ime": "markoMaric", "lozinka_hash": "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"},  # lozinka = "markoKralj123"
    {"korisnicko_ime": "ivanHorvat", "lozinka_hash": "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"},  # lozinka = "lllllllllllozinka_123"
    {"korisnicko_ime": "Nada000", "lozinka_hash": "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"}  # lozinka = "blablabla"
]


def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


async def register(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "Neispravan JSON format"}, status=400)

    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    if not korisnicko_ime or not lozinka:
        return web.json_response({"error": "Korisnicko ime i lozinka su obavezni"}, status=400)

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            return web.json_response({"error": "Korisnik vec postoji"}, status=409)

    novi_korisnik = {
        "korisnicko_ime": korisnicko_ime,
        "lozinka_hash": hash_data(lozinka)
    }
    korisnici.append(novi_korisnik)

    return web.json_response({"message": "Korisnik uspjesno registriran"}, status=201)


async def login(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "Neispravan JSON format"}, status=400)

    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    if not korisnicko_ime or not lozinka:
        return web.json_response({"error": "Korisnicko ime i lozinka su obavezni"}, status=400)

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            if korisnik["lozinka_hash"] == hash_data(lozinka):
                return web.json_response({"uspjesno": True}, status=200)
            else:
                return web.json_response({"uspjesno": False}, status=401)

    return web.json_response({"uspjesno": False}, status=404)


app = web.Application()
app.router.add_post("/register", register)
app.router.add_post("/login", login)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=9000)
