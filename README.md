# AI-Powered Employee Shuttle Reliability Platform

A privacy-first shuttle management platform for scheduled employee transport between a metro station and office.

## Goals
- Prevent early departures and missed pickups
- Verify driver arrival without continuous location tracking
- Notify employees and HR about trip status and exceptions
- Provide operational analytics
- Add AI-assisted delay prediction, anomaly detection, and HR insights

## MVP scope
- 2 cabs
- Metro <-> Office routes
- Driver, Employee, and HR roles
- Scheduled trips
- Event-based GPS verification
- Trip status and alerts
- HR dashboard
- Audit history

## Planned stack
- Backend: Python, FastAPI, PostgreSQL
- Frontend: React + TypeScript
- Cache/events: Redis (as needed)
- AI: LLM service + Python ML service
- Infrastructure: Docker, GitLab CI/CD

See `docs/requirements.md` and `docs/architecture.md`.
