from chemlib import Reaction

def balance_equation(reactants, products):
    """
    Balancea una ecuación química a partir de los reactivos y productos dados.

    :param reactants: Diccionario con los reactivos y sus cantidades iniciales.
    :param products: Diccionario con los productos y sus cantidades iniciales.
    :return: Fórmula de la ecuación balanceada.
    """
    reaction = Reaction(reactants, products)
    reaction.balance()
    return reaction.formula

reactants = {"CH4": 1, "O2": 2}
products = {"CO2": 1, "H2O": 2}
balanced_equation = balance_equation(reactants, products)
print(f"Ecuación balanceada: {balanced_equation}")
