import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Definir los datos de la malla curricular
data = {
    'Semestre': [
        '1º Semestre', '2º Semestre', '3º Semestre', '4º Semestre', '5º Semestre', 
        '6º Semestre', '7º Semestre', '8º Semestre', '9º Semestre', '10º Semestre'
    ],
    'Asignaturas': [
        ['Introducción a la Microeconomía', 'Matemática I', 'Ética General', 'Tecnologías de la Información', 'Inglés I', 'Habilidades de Aprendizaje I'],
        ['Introducción a la Administración I', 'Matemática II', 'Historia Económica y de la Empresa', 'Inglés II', 'Habilidades de Aprendizaje II', 'Contabilidad I'],
        ['Microeconomía I', 'Matemática III', 'Estadística I', 'Personas y Organizaciones', 'Inglés III', 'Habilidades de Aprendizaje III'],
        ['Microeconomía II', 'Matemática para la Economía', 'Estadística II', 'Gestión de Personas I', 'Inglés IV', 'Habilidades de Aprendizaje IV'],
        ['Macroeconomía I', 'Contabilidad II', 'Finanzas I', 'Marketing I', 'Formación Complementaria', 'Habilidades Profesionales I'],
        ['Microeconomía III', 'Macroeconomía II', 'Finanzas II', 'Marketing II', 'Formación Complementaria', 'Habilidades Profesionales II'],
        ['Macroeconomía III', 'Econometría', 'Gestión de Personas II', 'Organización Industrial', 'Formación Complementaria', 'Habilidades Profesionales III'],
        ['Economía Internacional', 'Econometría para la Gestión', 'Estrategia', 'Gestión de Operaciones', 'Formación Complementaria', 'Habilidades Profesionales IV'],
        ['Evaluación de Proyectos', 'Teoría de Juegos', 'Política Económica', 'Gestión de la Innovación', 'Formación Complementaria', 'Habilidades Profesionales V'],
        ['Regulación y Competencia', 'Desarrollo Económico', 'Juego de Negocios', 'Consultoría', 'Taller de Titulación', 'Ética en los Negocios y en la Economía']
    ]
}

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data)

# Expandir el DataFrame para que cada asignatura tenga su propia fila
df_expanded = df.explode('Asignaturas')

# Crear la figura interactiva
fig = go.Figure()

for semestre in df['Semestre']:
    sem_df = df_expanded[df_expanded['Semestre'] == semestre]
    fig.add_trace(go.Scatter(
        x=[semestre]*len(sem_df),
        y=sem_df['Asignaturas'],
        mode='markers+text',
        text=sem_df['Asignaturas'],
        textposition='top center',
        marker=dict(size=10)
    ))

fig.update_layout(
    title="Malla Curricular de Ingeniería Comercial",
    xaxis_title="Semestre",
    yaxis_title="Asignaturas",
    xaxis=dict(tickmode='array', tickvals=df['Semestre']),
    yaxis=dict(automargin=True),
    showlegend=False,
    height=800,
    margin=dict(l=100, r=100, t=100, b=100)
)

# Mostrar la figura
fig.show()
