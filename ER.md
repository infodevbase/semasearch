# Entity Relation per Database PG

```
-- Creazione del database (se non esiste già)
CREATE DATABASE semantic_search;

-- Connessione al database
\c semantic_search;

-- Tabella per gli utenti
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'user')),
    deleted INT,
    owners INT[],
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabella per i gruppi
CREATE TABLE groups (
    group_id SERIAL PRIMARY KEY,
    group_owner INT REFERENCES users(user_id) ON DELETE CASCADE,
    group_name VARCHAR(100) NOT NULL
);

-- Tabella di associazione tra utenti e gruppi
CREATE TABLE user_groups (
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    group_id INT REFERENCES groups(group_id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, group_id)
);

-- Tabella per i documenti
CREATE TABLE documents (
    document_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabella per la condivisione dei documenti
CREATE TABLE shared_documents (
    share_id SERIAL PRIMARY KEY,
    document_id UUID REFERENCES documents(document_id) ON DELETE CASCADE,
    owner_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    shared_with_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    shared_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_shared_document UNIQUE (document_id, shared_with_id)
);

-- Tabella per le ricerche salvate
CREATE TABLE saved_searches (
    search_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    query TEXT NOT NULL,
    search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabella per le notifiche
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB
);

-- Tabella per i log delle azioni
CREATE TABLE action_logs (
    log_id BIGSERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE SET NULL,
    action_type VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    entity_id VARCHAR(255) NOT NULL,
    old_value JSONB,
    new_value JSONB,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    user_agent TEXT
);

-- Indici per ottimizzare le query
CREATE INDEX idx_documents_user_id ON documents(user_id);
CREATE INDEX idx_shared_documents_document_id ON shared_documents(document_id);
CREATE INDEX idx_shared_documents_shared_with_id ON shared_documents(shared_with_id);
CREATE INDEX idx_saved_searches_user_id ON saved_searches(user_id);
CREATE INDEX idx_notifications_user_id ON notifications(user_id);
CREATE INDEX idx_notifications_is_read ON notifications(is_read);
CREATE INDEX idx_action_logs_user_id ON action_logs(user_id);
CREATE INDEX idx_action_logs_entity_id ON action_logs(entity_id);
CREATE INDEX idx_action_logs_action_timestamp ON action_logs(action_timestamp);


```