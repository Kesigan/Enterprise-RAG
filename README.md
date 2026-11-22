# Enterprise RAG

A document-grounded knowledge assistant for enterprise teams.

![Enterprise RAG knowledge workspace](docs/enterprise-rag-ui.png)

## What it does

- Answers natural-language questions with cited source passages.
- Ingests PDF, DOCX, TXT, and Markdown documents.
- Supports access-aware retrieval and human review for sensitive requests.
- Surfaces workspace and guardrail activity in an admin view.

## Architecture

![Enterprise RAG architecture diagram](docs/Enterprise_RAG_Architecture.png)

FastAPI · Amazon S3 · Amazon Bedrock · PostgreSQL · Pinecone