# ER Diagram – Distributed Document Editor

USERS
- user_id (PK)
- name

DOCUMENTS
- document_id (PK)
- owner_id (FK)
- title
- content

DOCUMENT_VERSIONS
- version_id (PK)
- document_id (FK)
- content
- created_at

Relationship:

User 1 → N Documents  
Document 1 → N Versions
