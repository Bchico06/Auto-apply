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


## Troubleshooting (Windows + Docker Desktop)
Si ves errores como:
- `the attribute version is obsolete`
- `open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified`

Haz lo siguiente:
1. Asegúrate de tener Docker Desktop instalado y **abierto**.
2. Verifica que el engine Linux esté corriendo:
   ```powershell
   docker version
   docker info
   ```
3. Si falla, reinicia Docker Desktop y espera a que diga "Engine running".
4. Luego ejecuta:
   ```powershell
   docker compose up --build
   ```

Nota: el warning de `version` ya no aplica con este archivo actualizado.
