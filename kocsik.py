autok = []

with open("kocsik.txt", "r", encoding="UTF-8") as f:
    for sor in f:
        marka, modell, ar, loero, nyomatek = sor.strip().split(';')
        autok.append({
            "marka": marka,
            "modell": modell,
            "ar_eur": int(ar),
            "loero": int(loero),
            "nyomatek_nm": int(nyomatek)
        })
# összes autó
print("Összes autó:")
for auto in autok:
    print(f"{auto['marka']} {auto['modell']}: {auto['loero']} LE, {auto['nyomatek_nm']} Nm, {auto['ar_eur']} EUR")
# Legdrágább autó
legdragabb = autok[0]
for auto in autok:
    if auto["ar_eur"] > legdragabb["ar_eur"]:
        legdragabb = auto
print("\nLegdrágább autó:", legdragabb["marka"], legdragabb["modell"], "-", legdragabb["ar_eur"], "EUR")

# Legjobb ár-érték arányú autó

for auto in autok:
    auto["ar_per_loero"] = auto["ar_eur"] / auto["loero"]

legjobb = min(autok, key=lambda x: x["ar_per_loero"])

print(f"\nLegjobb vétel: {legjobb['marka']} {legjobb['modell']} "
      f"({legjobb['ar_eur']} EUR, {legjobb['loero']} LE) "
      f"-> {legjobb['ar_per_loero']:.0f} EUR/LE\n")
# Eredmények kiírása
with open("eredmenyek.txt", "w", encoding="UTF-8") as kimenet:
    kimenet.write(f"Legdrágább autó:{legdragabb["marka"], legdragabb["modell"], "-", legdragabb["ar_eur"], "EUR"}\n")
    kimenet.write(F"Legjobb vétel: {legjobb['marka']} {legjobb['modell']} ({legjobb['ar_eur']} EUR, {legjobb['loero']} LE)")