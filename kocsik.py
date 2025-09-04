autok = []

with open('autok.txt', 'r', encoding='utf-8') as f:
    for sor in f:
        marka, modell, ar, loero, nyomatek = sor.strip().split(';')
        autok.append({
            "marka": marka,
            "modell": modell,
            "ar_eur": int(ar),
            "loero": int(loero),
            "nyomatek_nm": int(nyomatek)
        })

for auto in autok:
    print(f"{auto['marka']} {auto['modell']}: {auto['loero']} LE, {auto['nyomatek_nm']} Nm, {auto['ar_eur']} EUR")
