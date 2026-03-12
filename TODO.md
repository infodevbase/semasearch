# TODO List - Progetto Piattaforma di Ricerca Semantica

## 📌 Legenda
- [ ] Task da fare
- [x] Task completato
- 🔧 In corso
- 🚀 Priorità alta
- 📌 Priorità media
- 💡 Priorità bassa

---

## 🗃️ FR1 - Upload e Gestione Documenti

### [ ] FR1.1 - Upload documenti testuali (.txt)
- [ ] Implementare interfaccia frontend per upload (drag-and-drop o selezione file).
- [ ] Creare endpoint backend `/api/documents/upload` per ricevere e salvare i file.
- [ ] Validare il formato del file (solo `.txt`).
- [ ] Salvare il file in PostgreSQL con metadati: `id`, `user_id`, `filename`, `upload_date`, `content`.
- [ ] 🚀 **Priorità alta**

### [ ] FR1.2 - Modifica documenti (no eliminazione)
- [ ] Aggiungere pulsante "Modifica" nella vista documento (frontend).
- [ ] Implementare endpoint backend `/api/documents/{id}` per aggiornare il contenuto.
- [ ] Validare che l'utente sia il proprietario del documento.
- [ ] 📌 **Priorità media**

---

## 🔍 FR2 - Ricerca Semantica

### [ ] FR2.1 - Ricerca per frasi e filtri avanzati
- [ ] Creare barra di ricerca nel frontend per input testuali.
- [ ] Sviluppare endpoint backend `/api/search` per:
  - Preprocessare il testo (tokenizzazione, rimozione stopwords).
  - Generare embedding vettoriali per query e documenti.
  - Calcolare similarità coseno tra query e documenti.
  - Restituire documenti ordinati per rilevanza.
- [ ] Usare modello pre-addestrato `all-MiniLM-L6-v2`.
- [ ] 🚀 **Priorità alta**

### [ ] FR2.2 - Supporto sinonimi e similarità
- [ ] Integrare libreria per sinonimi (es. `WordNet`).
- [ ] Modificare funzione di ricerca per includere sinonimi.
- [ ] 📌 **Priorità media**

### [ ] FR2.3 - Punteggio di rilevanza
- [ ] Aggiungere campo `relevance_score` nella risposta API.
- [ ] Visualizzare punteggio nel frontend (es. barra colorata).
- [ ] 💡 **Priorità bassa**

### [ ] FR2.4 - Ricerche salvate e alert
- [ ] Aggiungere pulsante "Salva ricerca" nella pagina dei risultati.
- [ ] Creare tabella `saved_searches` nel database.
- [ ] Implementare sistema di alert asincrono (usare `Celery`).
- [ ] 📌 **Priorità media**

---

## 👥 FR3 - Gestione Utenti

### [ ] FR3.1 - Ruoli e permessi (admin/user)
- [ ] Definire ruoli `admin` e `user` nel database.
- [ ] Implementare sistema di autorizzazione (RBAC).
- [ ] 🚀 **Priorità alta**

### [ ] FR3.2 - Autenticazione 2FA e SSO Google
- [ ] Integrare sistema di autenticazione (es. `Firebase Auth`).
- [ ] Abilitare 2FA via email/SMS.
- [ ] Configurare SSO con Google (usare `Google OAuth 2.0`).
- [ ] 🚀 **Priorità alta**

### [ ] FR3.3 - Condivisione documenti (stesso gruppo)
- [ ] Aggiungere pulsante "Condividi" nella vista documento.
- [ ] Implementare endpoint `/api/documents/{id}/share` per condividere documenti.
- [ ] Validare che il destinatario appartenga allo stesso gruppo.
- [ ] 📌 **Priorità media**

---

## 🔔 FR4 - Notifiche Asincrone

### [ ] FR4.1 - Trigger notifiche
- [ ] Identificare eventi trigger (nuovo documento, modifiche, ricerche salvate).
- [ ] Implementare listener asincrono (usare `Celery`).
- [ ] 💡 **Priorità bassa**

### [ ] FR4.2 - Invio notifiche (email + push)
- [ ] Sviluppare servizio di notifica per invio email (usare `SendGrid`).
- [ ] Implementare push notification (usare `Firebase Cloud Messaging`).
- [ ] Filtrare destinatari in base al gruppo.
- [ ] 💡 **Priorità bassa**

---

## 📅 Schedulazione Consigliata

### Fase 1 (MVP - 4 settimane)
- FR1.1, FR2.1, FR3.1, FR3.2

### Fase 2 (2 settimane)
- FR1.2, FR2.2, FR2.4, FR3.3

### Fase 3 (1 settimana)
- FR2.3, FR4.1, FR4.2
