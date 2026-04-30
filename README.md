# AutoApply

Plataforma web moderna para automatizar postulaciones laborales desde una sola interfaz.

## Stack
- Frontend: React + Tailwind + Vite
- Backend: FastAPI + SQLAlchemy + JWT
- Base de datos: PostgreSQL (docker-compose)
- Automatización: Playwright (estructura inicial)

## Ejecutar con Docker
```bash
docker compose up --build
```

Frontend: http://localhost:5173  
Backend: http://localhost:8000/docs

## Estructura
- `frontend/`: UI SaaS moderna (tema oscuro), dashboard y formularios principales.
- `backend/`: API REST con auth JWT, perfil, filtros, jobs y aplicaciones.
- `automation/`: esqueleto para motores de auto-postulación por plataforma.
