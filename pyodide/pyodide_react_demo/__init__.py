import math, js
from pyodide_react_demo.react.components import div, p, Button
from pyodide_react_demo.react import use_state
from pyodide_react_demo.react.decorator import component


@component
def App(*children, **props):
    print(children)
    print(props)
    k, set_k = use_state(1)
    n, set_n = use_state(1)
    disabled, set_disabled = use_state(True)

    def increase_k(event):
        set_k(k + 1)
        set_disabled(k + 1 >= n)

    def increase_n(event):
        set_n(n + 1)
        set_disabled(k >= n + 1)

    return div()(
        p[f"{n} choose {k} = {math.comb(n, k)}"],
        Button(on_click=increase_n, variant="contained", color="secondary")[
            'Increase n'
        ],
        Button(on_click=increase_k, variant="contained", disabled=disabled, color="primary")[
            'Increase k'
        ],
    )