# GitHub Repository Activity Tracker

A full-stack system that tracks **GitHub repository activity** using **GitHub Webhooks**, stores events in **MongoDB**, and displays updates on a **polling-based frontend UI**.

This project was developed as part of a **technical job interview assignment**.

---

## Problem Statement

Build a system that:

- Listens to GitHub repository events:
  - **Push**
  - **Pull Request**
  - **Merge**
- Stores event data in MongoDB using a fixed schema
- Displays repository activity on a frontend UI
- Automatically updates the UI every **15 seconds**

---

## Architecture Overview
```
GitHub Repository
│
│ Webhooks (push / pull_request)
▼
FastAPI Backend
│
│ Normalized Events
▼
MongoDB
│
│ Poll every 15 seconds
▼
Frontend (Browser)
```
---

## Design Decisions

- **Webhook-based ingestion**: GitHub pushes events instead of polling GitHub APIs
- **Schema-first MongoDB design**: Only raw facts are stored; UI messages are derived
- **Polling frontend**: Simple, reliable, and sufficient for near-real-time updates
- **Clear separation of concerns**:
  - Backend → ingestion & persistence
  - Frontend → presentation only

---

## Project structure
```
github-event-tracker/
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── webhook.py
│ │ ├── database.py
│ │ └── formatter.py
│ └── requirements.txt
│
└── frontend/
├── index.html
└── app.js
```

## 🗄️ MongoDB Schema

All events are stored using the following schema:

```json
{
  "request_id": "string",
  "author": "string",
  "action": "PUSH | PULL_REQUEST | MERGE",
  "from_branch": "string | null",
  "to_branch": "string",
  "timestamp": "ISO-8601 string"
}
```

Display messages are not stored in MongoDB.
They are generated dynamically when serving data to the frontend.

<img width="1920" height="1018" alt="image" src="https://github.com/user-attachments/assets/ebf430c4-f4be-4814-9bcb-113110cd614d" />
