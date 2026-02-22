\# AIRMAN AI Agent Assessment



\## Overview



This project implements an AI-assisted dispatch system for flight training operations.



The system performs:



\- Automated ingestion of roster inputs

\- Draft roster generation

\- Weather-aware GO / NO\_GO dispatch decisions

\- Automatic SIM substitution when weather is below minima

\- Explainable decisions (reasons + citations)

\- Evaluation harness

\- Replanning signal (Level-2 fast-track)



---



\## Architecture



Ingestion Layer

↓

Database (SQLite)

↓

Scheduler Engine

↓

Weather Tool

↓

Dispatch Decisions

↓

Evaluation Harness





\### High-Level Flow



1\. Ingestion loads JSON data into SQL tables.

2\. Scheduler generates draft roster assignments.

3\. Weather tool evaluates minima conditions.

4\. Dispatch decisions convert flights to SIM if needed.

5\. Decisions include reasons and citations.

6\. Evaluation endpoint exposes quality metrics.



---



\## Project Structure



airman-ai-agent/

│

├── app/

│ ├── api/

│ ├── db/

│ ├── ingestion/

│ ├── scheduler/

│ ├── weather/

│ ├── dispatch/

│ └── rag/

│

├── data/

├── tests/

├── Dockerfile

├── docker-compose.yml

├── README.md

├── PLAN.md

├── CUTS.md

├── POSTMORTEM.md

└── requirements.txt





---



\## API Endpoints



\### Ingestion



\- `POST /ingest/run`



Loads input data into database tables with idempotent behavior.



---



\### Roster Generation



\- `POST /roster/generate`



Generates draft roster with:



\- weather-aware decisions

\- SIM fallback

\- scoring

\- replanning trigger



---



\### Evaluation



\- `POST /eval/run`



Returns evaluation metrics:



\- hard constraint violations

\- coverage

\- citation coverage



---



\## Level-2 Features (Fast Track)



Implemented lightweight Level-2 signals:



\- scoring-based dispatch evaluation

\- replanning trigger (`needs\_replan`)

\- decision reasoning summary



These demonstrate agent-style orchestration behavior.



---



\## Run Locally



```bash

uvicorn app.main:app --reload



\## Open:



http://127.0.0.1:8000/docs



\## Run with Docker



docker compose up --build



\## Design Tradeoffs



To focus on core dispatch logic:



* simplified scheduling logic (greedy approach)
* mock weather service instead of live API
* static rule citations (no full RAG pipeline)
* minimal evaluation scenarios



\## Future Improvements



* Full RAG grounding over rules documents
* Advanced constraint solver (OR-Tools)
* Dynamic disruption handling
* Roster versioning \& audit trail
* LangGraph-based orchestration workflow



