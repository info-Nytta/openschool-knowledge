"""
Discord webhook üzenetküldő – heti bejelentések és emlékeztetők automatizálása.

Használat:
    # Bejelentés küldése:
    python discord-webhook.py bejelentes --kurzus python10 --het 3 --tema "Feltételes elágazások"

    # Házi feladat emlékeztető:
    python discord-webhook.py emlekezteto --kurzus backend13 --het 7 --hatarido "2026-03-15"

    # Szabad üzenet küldése:
    python discord-webhook.py uzenet --webhook-url URL --uzenet "Szabad szöveg"

Előfeltételek:
    - Discord webhook URL-ek környezeti változókban:
        DISCORD_WEBHOOK_KOZLEMENYEK   → #közlemények csatorna
        DISCORD_WEBHOOK_PYTHON10      → #python10-segítség csatorna
        DISCORD_WEBHOOK_BACKEND13     → #backend13-segítség csatorna
    - Vagy .env fájl a projekt gyökerében

Webhook létrehozása:
    Discord → Csatorna beállítások → Integrations → Webhooks → New Webhook
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error


def load_env():
    """Betölti a .env fájlt ha létezik."""
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    if not os.path.isfile(env_path):
        return
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def get_webhook_url(name):
    """Visszaadja a webhook URL-t környezeti változóból."""
    key = f"DISCORD_WEBHOOK_{name.upper()}"
    url = os.environ.get(key)
    if not url:
        print(f"HIBA: A '{key}' környezeti változó nincs beállítva.")
        print("Állítsd be a .env fájlban vagy a terminálban:")
        print(f'  Linux/macOS:  export {key}="https://discord.com/api/webhooks/..."')
        print(f'  Windows:      set {key}=https://discord.com/api/webhooks/...')
        sys.exit(1)
    return url


def send_webhook(webhook_url, content=None, embeds=None, username="Kurzus Bot"):
    """Üzenet küldése Discord webhookon keresztül."""
    payload = {"username": username}
    if content:
        payload["content"] = content
    if embeds:
        payload["embeds"] = embeds

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 204:
                print("✅ Üzenet elküldve.")
            else:
                print(f"Válasz: {response.status}")
    except urllib.error.HTTPError as e:
        print(f"HIBA: {e.code} – {e.read().decode()}")
        sys.exit(1)


KURZUS_EMOJIK = {
    "python10": "🐍",
    "backend13": "⚡",
}

KURZUS_NEVEK = {
    "python10": "Python 10",
    "backend13": "Backend FastAPI 13",
}


def cmd_bejelentes(args):
    """Heti bejelentés küldése a #közlemények csatornára."""
    webhook_url = get_webhook_url("KOZLEMENYEK")
    emoji = KURZUS_EMOJIK.get(args.kurzus, "📚")
    nev = KURZUS_NEVEK.get(args.kurzus, args.kurzus)

    embed = {
        "title": f"{emoji} {nev} – {args.het}. hét: {args.tema}",
        "description": (
            f"**Téma:** {args.tema}\n"
            f"**Hét:** {args.het}\n\n"
            f"A heti feladat elérhető a GitHub Classroom-on.\n"
            f"Kérdéseket a `#{args.kurzus}-segítség` csatornán tedd fel "
            f"az aktuális hét szálában."
        ),
        "color": 0x2ECC71 if args.kurzus == "python10" else 0x3498DB,
    }

    if args.hatarido:
        embed["description"] += f"\n\n⏰ **Határidő:** {args.hatarido}"

    if args.megjegyzes:
        embed["description"] += f"\n\n📝 {args.megjegyzes}"

    send_webhook(webhook_url, embeds=[embed])


def cmd_emlekezteto(args):
    """Házi feladat emlékeztető küldése."""
    webhook_url = get_webhook_url("KOZLEMENYEK")
    emoji = KURZUS_EMOJIK.get(args.kurzus, "📚")
    nev = KURZUS_NEVEK.get(args.kurzus, args.kurzus)

    content = (
        f"⏰ {emoji} **{nev} – Emlékeztető**\n\n"
        f"A **{args.het}. heti** házi feladat határideje: **{args.hatarido}**\n\n"
        f"Ne felejtsd el pusholni a megoldásodat a GitHub-ra! "
        f"Az autograding automatikusan lefut push után."
    )

    send_webhook(webhook_url, content=content)


def cmd_szal(args):
    """Heti szál nyitó üzenet küldése a kurzus segítség csatornájára."""
    webhook_url = get_webhook_url(args.kurzus)
    emoji = KURZUS_EMOJIK.get(args.kurzus, "📚")

    content = (
        f"**{args.ev} – {args.het}. hét – {args.tema}** {emoji}\n\n"
        f"Ebben a szálban kérdezzetek a(z) {args.het}. heti anyaggal kapcsolatban.\n"
        f"Használjatok kódblokkot (\\`\\`\\`python) a kód formázásához!"
    )

    send_webhook(webhook_url, content=content)
    print(f"💡 Tipp: Discordon kattints az üzenetre → 'Create Thread' → "
          f"nevezd el: \"{args.ev} – {args.het}. hét – {args.tema}\"")


def cmd_uzenet(args):
    """Szabad szöveges üzenet küldése megadott webhook URL-re."""
    send_webhook(args.webhook_url, content=args.uzenet)


def main():
    load_env()

    parser = argparse.ArgumentParser(
        description="Discord webhook üzenetküldő – kurzus bejelentések és emlékeztetők"
    )
    subparsers = parser.add_subparsers(dest="parancs", required=True)

    # --- bejelentes ---
    p_bej = subparsers.add_parser("bejelentes", help="Heti bejelentés küldése")
    p_bej.add_argument("--kurzus", required=True, choices=["python10", "backend13"])
    p_bej.add_argument("--het", required=True, type=int, help="Hét száma (0-12 vagy 0-24)")
    p_bej.add_argument("--tema", required=True, help="Heti téma neve")
    p_bej.add_argument("--hatarido", help="Házi feladat határideje (pl. 2026-03-15)")
    p_bej.add_argument("--megjegyzes", help="Extra megjegyzés")
    p_bej.set_defaults(func=cmd_bejelentes)

    # --- emlekezteto ---
    p_eml = subparsers.add_parser("emlekezteto", help="Házi feladat emlékeztető")
    p_eml.add_argument("--kurzus", required=True, choices=["python10", "backend13"])
    p_eml.add_argument("--het", required=True, type=int)
    p_eml.add_argument("--hatarido", required=True, help="Határidő dátum")
    p_eml.set_defaults(func=cmd_emlekezteto)

    # --- szal ---
    p_szal = subparsers.add_parser("szal", help="Heti szál nyitó üzenet")
    p_szal.add_argument("--kurzus", required=True, choices=["python10", "backend13"])
    p_szal.add_argument("--het", required=True, type=int)
    p_szal.add_argument("--tema", required=True, help="Heti téma neve")
    p_szal.add_argument("--ev", default="2026", help="Tanév (alapértelmezett: 2026)")
    p_szal.set_defaults(func=cmd_szal)

    # --- uzenet ---
    p_uz = subparsers.add_parser("uzenet", help="Szabad szöveges üzenet")
    p_uz.add_argument("--webhook-url", required=True)
    p_uz.add_argument("--uzenet", required=True)
    p_uz.set_defaults(func=cmd_uzenet)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
