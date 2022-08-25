import app

v = app.Vartotojas(vardas='v', el_pastas='a@a.lt', nuotrauka='a', slaptazodis='a')

token = v.get_reset_token()

verified_token = app.Vartotojas.verify_reset_token(token)

