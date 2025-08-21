# Lista: disciplinas que o aluno já cursou (pode ter repetição acidental)
disciplinas_cursadas = ["Algoritmos", "Matemática Discreta", "Python Básico", "Python Básico"]
print("Disciplinas já cursadas pelo aluno:")
print(disciplinas_cursadas)

# Conjunto: disciplinas eletivas disponíveis no semestre (sem duplicatas)
disciplinas_eletivas = {"Visão Computacional", "Computação Gráfica", "IA Generativa", "Segurança da Informação", "IA Generativa"}
print("\n Disciplinas eletivas disponíveis:")
print(disciplinas_eletivas)

# Dicionário: nome da disciplina como chave e carga horária como valor
carga_horaria = {
    "Algoritmos": 60,
    "Matemática Discreta": 60,
    "Python Básico": 80,
    "Visão Computacional": 40,
    "Computação Gráfica": 40,
    "IA Generativa": 60,
    "Segurança da Informação": 50
}
print("\n Carga horária das disciplinas (em horas):")
for nome, horas in carga_horaria.items():
    print(f"{nome}: {horas}h")

# Exemplo de lógica: calcular a carga horária total já cursada
total_cursada = sum([carga_horaria[disc] for disc in disciplinas_cursadas if disc in carga_horaria])
print(f"\n Carga horária total já cursada: {total_cursada}h")

# Remover duplicatas da lista de disciplinas cursadas
disciplinas_sem_duplicatas = list(set(disciplinas_cursadas))
print("\n Disciplinas cursadas (sem duplicatas):")
print(disciplinas_sem_duplicatas)

# Adicionar uma nova disciplina cursada
nova_disciplina = "Segurança da Informação"
disciplinas_cursadas.append(nova_disciplina)
print(f"\n '{nova_disciplina}' adicionada como cursada:")
print(disciplinas_cursadas)

# Verificar se uma disciplina está nas eletivas
consulta = "IA Generativa"
if consulta in disciplinas_eletivas:
    print(f"\n '{consulta}' está disponível como disciplina eletiva neste semestre.")