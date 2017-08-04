from sympy import *
from library import *

def mrsolve(*equations):
    items = []
    for i in equations:
        items.append(Eq(i[0], i[1]))
    return latexoutput(solve(items, check=False))

def mrprint(val):
    print latexoutput(val)
def latexoutput(val):
    return "<div class='problems'>" + latex(val) + "</div>"
    
def mrsolvecontext():
    return solve(denklemler)
