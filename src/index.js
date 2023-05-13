import './index.css';
import reportWebVitals from './reportWebVitals';
import script from './loader.py';

async function main() {
    const pyodide = await window.loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.22.1/full/"
    });

    const scriptText = await (await fetch(script)).text();
    pyodide.runPythonAsync(scriptText);
}
main();

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
