CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE documents (
    document_id INT PRIMARY KEY,
    owner_id INT,
    title VARCHAR(255),
    content TEXT
);

CREATE TABLE document_versions (
    version_id INT PRIMARY KEY,
    document_id INT,
    content TEXT,
    created_at TIMESTAMP
);
