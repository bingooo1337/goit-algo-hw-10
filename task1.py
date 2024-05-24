from pulp import LpMaximize, LpProblem, LpVariable, value


model = LpProblem(name="Optimization_Problem", sense=LpMaximize)

Lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
Fruit_Juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")


model += 2 * Lemonade + Fruit_Juice <= 100, "Вода"
model += 1 * Lemonade <= 50, "Цукор"
model += 1 * Lemonade <= 30, "Лимонний сік"
model += 2 * Fruit_Juice <= 40, "Фруктове пюре"


model += Lemonade + Fruit_Juice

model.solve()


print(f"Лимонад: {value(Lemonade)}")
print(f"Фруктовий сік: {value(Fruit_Juice)}")
