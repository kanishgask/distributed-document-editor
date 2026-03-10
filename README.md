# 📝 Distributed Document Editor

System Design Project – Real-Time Collaborative Editing

This project demonstrates the architecture of a distributed document editor similar to Google Docs.

---

# Problem Statement

Design a system where multiple users can edit a document simultaneously and see updates in real time.

---

# Functional Requirements

- Create document
- Edit document
- Real-time collaboration
- View document history
- Multiple users editing

---

# Non Functional Requirements

- Low latency updates
- Conflict resolution
- High availability
- Horizontal scalability

---

# Key Concepts

• Operational Transformation (OT)  
• Conflict-free Replicated Data Types (CRDT)  
• WebSocket communication  
• Event-driven updates  

---

# High Level Architecture

Client
 ↓
API Gateway
 ↓
Collaboration Service
 ↓
Document Service
 ↓
Database
