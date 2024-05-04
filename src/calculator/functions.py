import sympy

def evaluate_expression(expr):
    """Evaluate the mathematical expression using sympy with custom local variables."""
    if not expr:
        return ""  # Return empty string if expression is empty
    try:
        evaluated_expr = sympy.sympify(
            expr,
            locals={
                'π': sympy.pi,
                'e': sympy.E,
                'factorial': sympy.factorial,
                'ln': sympy.log,  # Natural logarithm (base e)
                'log': lambda x: sympy.log(x, 10)  # Common logarithm (base 10)
            }
        )
        return str(float(evaluated_expr))
    except Exception as exc:
        return "Error: " + str(exc)
