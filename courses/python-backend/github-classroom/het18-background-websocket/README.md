# 18. hét – Background Tasks és WebSocket

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## Feladat

### 18.1 – Background Task ⭐⭐
Adj háttérfeladatot egy végponthoz: a `POST /termekek` után háttérben logoljon egy fájlba (`app.log`).

### 18.2 – WebSocket echo ⭐⭐
Készíts `/ws` WebSocket végpontot, amely visszaküldi a kapott üzeneteket "Echo: " prefixszel.

### 18.3 – WebSocket teszt ⭐⭐
Írj pytest tesztet a WebSocket végpontra.

### 18.4 – Chat ⭐⭐⭐
Készíts `/ws/chat` végpontot `ConnectionManager`-rel: több kliens csatlakozhat, az üzenetek mindenkihez eljutnak (broadcast).

---

## Dokumentáció

- [Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
- [WebSockets](https://fastapi.tiangolo.com/advanced/websockets/)

## Beadás

1. `main.py` legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
