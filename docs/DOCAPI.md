

# Documentazione API - Piattaforma di Ricerca Semantica

Questa documentazione descrive le API esposte dal backend Flask per la piattaforma di ricerca semantica. Tutte le API restituiscono risposte in formato JSON.

---

## 📌 Informazioni Generali
```
### Base URL
`http://localhost:5000/api`

### Autenticazione
- Le API che richiedono autenticazione utilizzano un token JWT inviato nell'header `Authorization`:
  ```
  Authorization: Bearer <token>
  ```

### Codici di Stato
- `200 OK`: Richiesta completata con successo.
- `201 Created`: Risorsa creata con successo.
- `400 Bad Request`: Richiesta malformattata.
- `401 Unauthorized`: Autenticazione fallita.
- `403 Forbidden`: Utente non autorizzato.
- `404 Not Found`: Risorsa non trovata.
- `500 Internal Server Error`: Errore del server.

---
```
## 📤 Endpoint per la Gestione Documenti

### 1. Upload di un Documento
**Endpoint:** `POST /documents/upload`

**Descrizione:** Carica un documento testuale (.txt) associato all'utente autenticato.

```
**Headers:**
- `Authorization: Bearer <token>`
- `Content-Type: multipart/form-data`

**Body:**
| Campo      | Tipo     | Descrizione                     |
|------------|----------|---------------------------------|
| document   | file     | File di testo (.txt) da caricare. |
```

**Risposta (Successo):**
```json
{
  "status": "success",
  "document_id": "123e4567-e89b-12d3-a456-426614174000",
  "message": "Documento caricato con successo."
}
```

**Risposta (Errore):**
```json
{
  "status": "error",
  "message": "Formato file non valido. Solo .txt è permesso."
}
```

---

### 2. Modifica di un Documento
**Endpoint:** `PUT /documents/{document_id}`

**Descrizione:** Modifica il contenuto di un documento esistente.

**Headers:**
- `Authorization: Bearer <token>`
- `Content-Type: application/json`

**Body:**
| Campo      | Tipo     | Descrizione                     |
|------------|----------|---------------------------------|
| content    | string   | Nuovo contenuto del documento.   |

**Risposta (Successo):**
```json
{
  "status": "success",
  "message": "Documento aggiornato con successo."
}
```

**Risposta (Errore):**
```json
{
  "status": "error",
  "message": "Non sei autorizzato a modificare questo documento."
}
```

---

## 🔍 Endpoint per la Ricerca Semantica

### 3. Ricerca Semantica
**Endpoint:** `GET /search`

**Descrizione:** Esegue una ricerca semantica sui documenti caricati.

**Headers:**
- `Authorization: Bearer <token>`

**Query Parameters:**
| Parametro | Tipo     | Descrizione                                      |
|-----------|----------|--------------------------------------------------|
| q         | string   | Query di ricerca (es. "relazione tra A e B").   |

**Risposta (Successo):**
```json
{
  "status": "success",
  "results": [
    {
      "document_id": "123e4567-e89b-12d3-a456-426614174000",
      "title": "Documento 1",
      "content": "Contenuto del documento...",
      "relevance_score": 0.95,
      "highlight": "relazione tra A e B trovata in questa sezione..."
    },
    {
      "document_id": "223e4567-e89b-12d3-a456-426614174001",
      "title": "Documento 2",
      "content": "Altro contenuto...",
      "relevance_score": 0.87,
      "highlight": "relazione tra A e B menzionata qui..."
    }
  ]
}
```

**Risposta (Errore):**
```json
{
  "status": "error",
  "message": "Nessun documento trovato per la query specificata."
}
```

---

### 4. Salva una Ricerca
**Endpoint:** `POST /search/save`

**Descrizione:** Salva una query di ricerca per l'utente autenticato.

**Headers:**
- `Authorization: Bearer <token>`
- `Content-Type: application/json`

**Body:**
| Campo      | Tipo     | Descrizione                     |
|------------|----------|---------------------------------|
| query      | string   | Query di ricerca da salvare.     |

**Risposta (Successo):**
```json
{
  "status": "success",
  "saved_search_id": "323e4567-e89b-12d3-a456-426614174002",
  "message": "Ricerca salvata con successo."
}
```

---

## 👥 Endpoint per la Gestione Utenti

### 5. Condivisione di un Documento
**Endpoint:** `POST /documents/{document_id}/share`

**Descrizione:** Condivide un documento con un altro utente dello stesso gruppo.

**Headers:**
- `Authorization: Bearer <token>`
- `Content-Type: application/json`

**Body:**
| Campo      | Tipo     | Descrizione                     |
|------------|----------|---------------------------------|
| user_id    | string   | ID dell'utente con cui condividere. |

**Risposta (Successo):**
```json
{
  "status": "success",
  "message": "Documento condiviso con successo."
}
```

**Risposta (Errore):**
```json
{
  "status": "error",
  "message": "L'utente specificato non appartiene al tuo gruppo."
}
```

---

## 🔔 Endpoint per le Notifiche

### 6. Ottieni Notifiche
**Endpoint:** `GET /notifications`

**Descrizione:** Recupera le notifiche per l'utente autenticato.

**Headers:**
- `Authorization: Bearer <token>`

**Risposta (Successo):**
```json
{
  "status": "success",
  "notifications": [
    {
      "notification_id": "423e4567-e89b-12d3-a456-426614174003",
      "type": "new_document",
      "message": "Nuovo documento 'Documento 3' caricato da Mario Rossi.",
      "date": "2026-02-18T10:00:00Z",
      "is_read": false
    }
  ]
}
```

---

## 📌 Esempi di Utilizzo

### Esempio di Upload di un Documento
```bash
curl -X POST http://localhost:5000/api/documents/upload \
  -H "Authorization: Bearer <token>" \
  -F "document=@documento.txt"
```

### Esempio di Ricerca Semantica
```bash
curl -X GET "http://localhost:5000/api/search?q=relazione%20tra%20A%20e%20B" \
  -H "Authorization: Bearer <token>"
```

---

## 📄 Note per lo Sviluppo Frontend

- **Autenticazione:** Assicurarsi di includere il token JWT in ogni richiesta che richiede autenticazione.
- **Gestione Errori:** Gestire i codici di stato HTTP per fornire feedback appropriati all'utente.
- **Formati:** Assicurarsi che i file caricati siano solo `.txt`.
- **Embedding:** La ricerca semantica utilizza modelli di embedding pre-addestrati. Assicurarsi che le query siano ben formulate per ottenere risultati rilevanti.

---


