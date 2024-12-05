from chemlib import Compound

#1.Formación de un compuesto
def create_compound(formula):
    """
    Crea un compuesto químico a partir de su fórmula.
    """
    return Compound(formula)
  
  #2.Masa molar
def calculate_molar_mass(compound):
    """
    Calcula la masa molar de un compuesto.
    """
    return compound.molar_mass()

water = create_compound("H2O")
glucose = create_compound("C6H12O6")
print(f"Masa molar de H2O: {calculate_molar_mass(water)} g/mol")
print(f"Masa molar de C6H12O6: {calculate_molar_mass(glucose)} g/mol")
#3.Composición porcentual en masa
from chemlib import Compound

def percentage_composition(formula):
    """
    Calcula la composición porcentual en masa de un compuesto.
    """
    compound = Compound(formula)
    return compound.mass_percent()

formula = "C2H5OH"  # Etanol
percentages = percentage_composition(formula)
print(f"Composición porcentual en masa de {formula}:")
for element, percent in percentages.items():
  print(f"{element}: {percent:.2f}%")
  
#4.Estequiometría
from chemlib import Reaction

def stoichiometry(reactants, products):
    """
    Calcula los coeficientes estequiométricos para balancear una reacción química.

    :param reactants: Diccionario con los reactivos y sus cantidades iniciales.
    :param products: Diccionario con los productos y sus cantidades iniciales.
    :return: Fórmula de la reacción balanceada y los coeficientes.
    """
    reaction = Reaction(reactants, products)
    reaction.balance()
    return reaction.formula, reaction.coefficients

reactants = {"H2": 2, "O2": 1}
products = {"H2O": 2}
formula, coefficients = stoichiometry(reactants, products)
print(f"Reacción balanceada: {formula}")
print(f"Coeficientes: {coefficients}")






