# =============================================================================
# PROY-2: Script de Análisis — Estadísticas LaLiga EA Sports 2023/24
# Autor: P2 - Desarrolladora Técnica (Lucía Caramuti)
# Descripción: Procesa la tabla final de LaLiga 2023/24 y genera estadísticas
#              básicas del torneo: tabla de posiciones, rendimiento por equipo
#              y gráficos comparativos.
# =============================================================================

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Backend sin pantalla, necesario en Google Colab / entornos sin GUI
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# ─────────────────────────────────────────────────────────────────────────────
# 1. CARGA DE DATOS
# Usamos os.path para construir rutas relativas, garantizando que el script
# funcione correctamente tanto en Google Colab como en entornos locales.
# ─────────────────────────────────────────────────────────────────────────────

base = os.path.dirname(os.path.abspath(__file__))
ruta_datos = os.path.join(base, '..', 'datos', 'laliga_2023_24.csv')

df = pd.read_csv(ruta_datos)

print("=" * 60)
print("     LALIGA EA SPORTS 2023/24 — ANÁLISIS ESTADÍSTICO")
print("=" * 60)
print(f"\n✅ Dataset cargado: {len(df)} equipos\n")

# ─────────────────────────────────────────────────────────────────────────────
# 2. INDICADORES CALCULADOS
# Calculamos métricas adicionales útiles para el análisis:
#   - Diferencia de goles (DG): mide la solidez ofensiva/defensiva
#   - Promedio de goles a favor (GF_prom): eficacia ofensiva por partido
#   - Promedio de goles en contra (GC_prom): solidez defensiva por partido
#   - % de victorias: proporción de partidos ganados sobre el total jugados
# ─────────────────────────────────────────────────────────────────────────────

df['DG']      = df['GF'] - df['GC']
df['GF_prom'] = (df['GF'] / df['PJ']).round(2)
df['GC_prom'] = (df['GC'] / df['PJ']).round(2)
df['pct_vic'] = ((df['PG'] / df['PJ']) * 100).round(1)

# Cálculo del promedio general de goles por partido del torneo
# Dividimos el total de goles (suma de todos los GF) entre los partidos totales.
# Nota: cada partido genera GF para un equipo y GC para el otro,
# por eso usamos solo la suma de GF (evita doble conteo).
total_goles   = df['GF'].sum()
total_partidos = (df['PJ'].sum()) // 2   # cada partido cuenta dos veces en PJ
promedio_goles = round(total_goles / total_partidos, 2)

# ─────────────────────────────────────────────────────────────────────────────
# 3. TABLA DE POSICIONES
# ─────────────────────────────────────────────────────────────────────────────

print("TABLA DE POSICIONES FINAL")
print("-" * 60)
cols_mostrar = ['posicion', 'equipo', 'PJ', 'PG', 'PE', 'PP', 'GF', 'GC', 'DG', 'Pts']
print(df[cols_mostrar].to_string(index=False))
print("-" * 60)
print(f"\n⚽ Total de goles del torneo : {total_goles}")
print(f"🏟️  Total de partidos         : {total_partidos}")
print(f"📊 Promedio de goles/partido  : {promedio_goles}")
print(f"\n🏆 Campeón: {df.iloc[0]['equipo']} ({df.iloc[0]['Pts']} puntos)")
print(f"⬇️  Descensos: {', '.join(df.tail(3)['equipo'].tolist())}\n")

# ─────────────────────────────────────────────────────────────────────────────
# 4. GENERACIÓN DE GRÁFICOS
# Creamos un panel de 2 gráficos:
#   - Izquierda: barras apiladas de PG / PE / PP para cada equipo
#   - Derecha:   puntos totales con línea de promedio de la liga
# Ordenamos por posición para que el líder quede primero (izquierda).
# ─────────────────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle('LaLiga EA Sports 2023/24 — Rendimiento por Equipo',
             fontsize=15, fontweight='bold', y=1.01)

equipos = df['equipo']
x = range(len(df))

# ── Panel izquierdo: victorias, empates y derrotas ──────────────────────────
ax1 = axes[0]
ancho = 0.25
ax1.bar([i - ancho for i in x], df['PG'], width=ancho, label='Victorias',  color='#27ae60')
ax1.bar(list(x),                df['PE'], width=ancho, label='Empates',    color='#f39c12')
ax1.bar([i + ancho for i in x], df['PP'], width=ancho, label='Derrotas',   color='#e74c3c')

ax1.set_title('Victorias, Empates y Derrotas', fontsize=12, fontweight='bold')
ax1.set_xticks(list(x))
ax1.set_xticklabels(equipos, rotation=45, ha='right', fontsize=8)
ax1.set_ylabel('Cantidad de partidos')
ax1.legend(loc='upper right')
ax1.grid(axis='y', alpha=0.3)

# ── Panel derecho: puntos totales ────────────────────────────────────────────
ax2 = axes[1]
# Coloreamos diferente los 4 clasificados a Champions, los descensos y el resto
colores_barras = []
for pos in df['posicion']:
    if pos <= 4:
        colores_barras.append('#1a5276')   # Champions — azul oscuro
    elif pos >= 18:
        colores_barras.append('#922b21')   # Descenso — rojo
    else:
        colores_barras.append('#2980b9')   # Resto — azul normal

barras = ax2.bar(equipos, df['Pts'], color=colores_barras, alpha=0.88)

# Línea de promedio de puntos de la liga
promedio_pts = df['Pts'].mean()
ax2.axhline(promedio_pts, color='gray', linestyle='--', linewidth=1.2,
            label=f'Promedio liga: {promedio_pts:.1f} pts')

# Etiqueta de puntos encima de cada barra
for barra, pts in zip(barras, df['Pts']):
    ax2.text(barra.get_x() + barra.get_width() / 2,
             barra.get_height() + 0.5,
             str(pts), ha='center', va='bottom', fontsize=7.5, fontweight='bold')

ax2.set_title('Puntos Totales por Equipo', fontsize=12, fontweight='bold')
ax2.set_xticks(range(len(equipos)))
ax2.set_xticklabels(equipos, rotation=45, ha='right', fontsize=8)
ax2.set_ylabel('Puntos')
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

# Leyenda de colores
patch_ch  = mpatches.Patch(color='#1a5276', label='Champions League (Top 4)')
patch_re  = mpatches.Patch(color='#2980b9', label='Resto')
patch_des = mpatches.Patch(color='#922b21', label='Descenso (18°-20°)')
ax2.legend(handles=[patch_ch, patch_re, patch_des], fontsize=8, loc='upper right')

plt.tight_layout()

# ─────────────────────────────────────────────────────────────────────────────
# 5. EXPORTACIÓN DE RESULTADOS
# Guardamos el gráfico y la tabla con métricas en /resultados.
# Usamos rutas relativas para que funcione en cualquier entorno.
# ─────────────────────────────────────────────────────────────────────────────

ruta_grafico = os.path.join(base, '..', 'resultados', 'grafico_laliga_2324.png')
ruta_tabla   = os.path.join(base, '..', 'resultados', 'tabla_posiciones_laliga.csv')

plt.savefig(ruta_grafico, dpi=150, bbox_inches='tight')
df.to_csv(ruta_tabla, index=False)

print(f"✅ Gráfico guardado en: resultados/grafico_laliga_2324.png")
print(f"✅ Tabla exportada en : resultados/tabla_posiciones_laliga.csv")
