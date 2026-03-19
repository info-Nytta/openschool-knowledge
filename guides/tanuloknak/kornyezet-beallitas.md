# Környezet beállítás

Ez az útmutató segít feltelepíteni az összes eszközt, amelyre az OpenSchool kurzusok során szükséged lesz.

---

## Melyik eszköz melyik kurzushoz kell?

| Eszköz | Python Alapok | Backend FastAPI | Projekt Labor |
|--------|:------------:|:---------------:|:-------------:|
| Python 3.10+ | ✅ | ✅ | ✅ |
| Git | ✅ | ✅ | ✅ |
| VS Code | ✅ | ✅ | ✅ |
| GitHub fiók | ✅ | ✅ | ✅ |
| Docker | — | ✅ (7. héttől) | ✅ |
| Node.js | — | — | ✅ (frontend) |

---

## 1. Python telepítése

### Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version   # Python 3.10+ legyen
```

### Windows

1. Töltsd le a telepítőt: [python.org/downloads](https://www.python.org/downloads/)
2. **Fontos:** pipáld be az **"Add Python to PATH"** opciót a telepítés elején
3. Ellenőrzés terminálban:

```powershell
python --version
```

### macOS

```bash
brew install python
python3 --version
```

---

## 2. Git telepítése

### Linux

```bash
sudo apt install git
git --version
```

### Windows

1. Töltsd le: [git-scm.com](https://git-scm.com/download/win)
2. Telepítés közben az alapértelmezett beállítások megfelelők
3. A telepítéssel együtt jön a **Git Bash** — ezt fogjuk használni terminálként

### macOS

```bash
brew install git
# Vagy: xcode-select --install
```

### Git beállítása (minden rendszeren)

```bash
git config --global user.name "A Te Neved"
git config --global user.email "te@email.com"
```

---

## 3. VS Code telepítése

1. Töltsd le: [code.visualstudio.com](https://code.visualstudio.com/)
2. Telepítsd a platformodnak megfelelő verziót

### Ajánlott kiegészítők

| Kiegészítő | Miért hasznos |
|-----------|---------------|
| **Python** (Microsoft) | Python nyelvi támogatás, IntelliSense |
| **Pylance** | Gyorsabb kódkiegészítés |
| **GitLens** | Git történet megjelenítése |
| **Docker** (Microsoft) | Docker fájlok szerkesztése (Backend kurzushoz) |

Telepítés VS Code-ban: `Ctrl+Shift+X` → keress rá a nevére → **Install**.

---

## 4. GitHub fiók létrehozása

1. Regisztrálj: [github.com/signup](https://github.com/signup)
2. Erősítsd meg az e-mail címedet
3. Állítsd be az SSH kulcsot (ajánlott, de nem kötelező):

```bash
ssh-keygen -t ed25519 -C "te@email.com"
cat ~/.ssh/id_ed25519.pub
```

4. Másold ki a publikus kulcsot, és add hozzá a GitHub fiókodhoz:
   **Settings** → **SSH and GPG keys** → **New SSH key**

> **Alternatíva:** HTTPS-sel is tudsz dolgozni SSH helyett. Ebben az esetben a `git push`-nál kéri a GitHub felhasználóneved és egy Personal Access Token-t (nem a jelszavadat).

---

## 5. Docker telepítése (Backend FastAPI + Projekt Labor)

> A Python Alapok kurzushoz NEM kell Docker — csak a 7. héttől (Backend kurzus) lesz szükséges.

### Linux (Ubuntu / Debian)

```bash
# Docker Engine telepítése
sudo apt update
sudo apt install docker.io docker-compose-plugin

# Felhasználó hozzáadása a docker csoporthoz (hogy ne kelljen sudo)
sudo usermod -aG docker $USER

# Jelentkezz ki, majd vissza, és ellenőrizd:
docker --version
docker compose version
```

### Windows

1. Töltsd le a **Docker Desktop**-ot: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
2. Telepítsd (WSL2 backend-et használj — a telepítő felajánlja)
3. Indítsd el a Docker Desktop-ot
4. Ellenőrzés:

```powershell
docker --version
docker compose version
```

### macOS

```bash
brew install --cask docker
# Vagy: töltsd le a Docker Desktop-ot a docker.com-ról
```

---

## 6. Node.js telepítése (csak Projekt Labor)

> Csak a Projekt Labor kurzus frontend moduljához (Astro) szükséges.

### Linux

```bash
# Node.js 20 LTS telepítése
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
node --version
npm --version
```

### Windows / macOS

Töltsd le az LTS verziót: [nodejs.org](https://nodejs.org/)

---

## Ellenőrzőlista

Futtasd le a terminálban — ha mindegyik verziószámot ad vissza, kész vagy:

```bash
python3 --version       # Python 3.10+
git --version           # Git 2.x+
code --version          # VS Code
docker --version        # Docker (Backend kurzushoz)
docker compose version  # Docker Compose (Backend kurzushoz)
node --version          # Node.js (Projekt Laborhoz)
```

---

Elakadtál? Lásd a [Hibaelhárítás](hibaelharitas.md) útmutatót.

**Következő lépés:** [Kezdő útmutató — Hogyan kezdj hozzá?](kezdo-utmutato.md)
