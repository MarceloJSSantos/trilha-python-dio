salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(f"Salário antes do bônus: {salario}")  # Salário antes do bônus: 2000
salario_bonus(500)  # 2500
print(f"Salário depois do bônus: {salario}")  # Salário depois do bônus: 2500
