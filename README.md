# ⚽ Estadísticas LaLiga EA Sports 2023/24

**Trabajo Práctico:** Gestión Colaborativa, Control de Versiones y Organización Empresarial  
**Cátedra:** Organización Empresarial — UTN TUP a Distancia  
**Año Lectivo:** 2026  
**Escenario elegido:** D — Estadísticas de Resultados Deportivos

---

## 👥 Integrantes del Equipo

| Rol | Integrante | Responsabilidad |
|-----|-----------|----------------|
| P1 — Líder y Organizador | Juan Ignacio Ortiz | Gobernanza del repositorio, estructura de carpetas y README |
| P2 — Desarrolladora Técnica | Lucía Caramuti | Script de análisis estadístico en Python |
| P3 — Revisora QA | Lucía Caramuti | Peer Review, documentación y cierre de Pull Requests |

---

## 📋 Descripción del Proyecto

Este proyecto analiza la tabla final de la **LaLiga EA Sports 2023/24**, temporada en la que el Real Madrid se consagró campeón con 95 puntos. El script Python genera estadísticas básicas del torneo: tabla de posiciones completa, indicadores de rendimiento por equipo y un gráfico comparativo.

### Indicadores calculados

- Tabla de posiciones completa (PJ, PG, PE, PP, GF, GC, DG, Pts)
- Diferencia de goles y porcentaje de victorias por equipo
- Promedio de goles por partido del torneo
- Gráfico comparativo: rendimiento y puntos totales con clasificación europea destacada

---

## 📁 Estructura del Repositorio

```
repo-proyecto/
│
├── datos/
│   └── laliga_2023_24.csv         # Dataset con estadísticas finales de los 20 equipos
│
├── scripts/
│   └── analisis_laliga.py         # Script principal de análisis
│
├── resultados/
│   ├── grafico_laliga_2324.png    # Gráfico comparativo (generado por el script)
│   └── tabla_posiciones_laliga.csv
│
├── README.md
└── .gitignore
```

---

## 📊 Dataset Utilizado

**Archivo:** `datos/laliga_2023_24.csv`  
**Fuente:** Datos oficiales de LaLiga EA Sports — Temporada 2023/24 (dominio público).  
**Formato:** CSV  
**Registros:** 20 equipos — 38 jornadas — 380 partidos totales

**Columnas:**

| Campo | Descripción |
|-------|-------------|
| `posicion` | Posición final en la tabla |
| `equipo` | Nombre del equipo |
| `PJ` | Partidos jugados |
| `PG` | Partidos ganados |
| `PE` | Partidos empatados |
| `PP` | Partidos perdidos |
| `GF` | Goles a favor |
| `GC` | Goles en contra |
| `Pts` | Puntos totales |

---

## ▶️ Instrucciones para Ejecutar el Script

### En Google Colab

```python
# 1. Clonar el repositorio
!git clone https://github.com/USUARIO/REPO.git
%cd REPO

# 2. Las dependencias ya están disponibles en Colab (pandas, matplotlib)

# 3. Ejecutar el script
!python scripts/analisis_laliga.py
```

### En entorno local

```bash
git clone https://github.com/USUARIO/REPO.git
cd REPO
pip install pandas matplotlib
python scripts/analisis_laliga.py
```

---

## 🔗 Trazabilidad con Jira

| Issue | Responsable | Descripción |
|-------|-------------|-------------|
| PROY-1 | Juan Ignacio Ortiz (P1) | Inicialización del repositorio y estructura de carpetas |
| PROY-2 | Lucía Caramuti (P2) | Desarrollo del script de análisis estadístico |
| PROY-3 | Lucía Caramuti (P3) | Revisión de código, documentación y merge del PR |

---

## 🔒 Seguridad

- Los Personal Access Tokens (PAT) **nunca** se almacenan en el repositorio.
- El archivo `.gitignore` excluye archivos temporales, checkpoints y logs.
