from pyodide_js import loadPackage
from js import ReactDOM
import js

await loadPackage('/pyodide_react_demo-0.1.0-py3-none-any.whl')

from pyodide_react_demo import App

if __name__ == '__main__':
    dom_container = js.document.createElement('div')
    js.document.body.appendChild(dom_container)
    root = ReactDOM.createRoot(dom_container)
    root.render(App()())