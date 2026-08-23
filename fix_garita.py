import os

file_path = r"c:\Users\Leonar\OneDrive - ylsolutionsperu.com\YL SOLUTIONS\GRUPO AURICA\Proyectos\FlotaVechicular\flota-frontend\garita.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replacement 1: CSS
old_css = """        .grid-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; width: 100%; }
        @media (max-width: 992px) {
            .grid-layout { grid-template-columns: 1fr; }
        }"""
new_css = """        /* Estilos de Tabs para Garita */
        .garita-tabs { display: flex; gap: 15px; margin-bottom: 25px; width: 100%; }
        .garita-tab-btn { flex: 1; padding: 18px 25px; font-size: 18px; font-weight: 800; border-radius: var(--radius-md); background: white; border: 2px solid var(--aurica-gray-light); color: var(--text-muted); cursor: pointer; transition: 0.3s; display: flex; align-items: center; justify-content: center; gap: 12px; box-shadow: var(--shadow-sm); }
        .garita-tab-btn:hover { border-color: var(--aurica-blue-light); color: var(--aurica-blue); transform: translateY(-2px); }
        .garita-tab-btn.active { background: var(--aurica-blue); color: white; border-color: var(--aurica-blue); box-shadow: var(--shadow-md); }
        .garita-panel { display: none; width: 100%; }
        .garita-panel.active { display: block; animation: fadeIn 0.3s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        @media (max-width: 768px) {
            .garita-tabs { flex-direction: column; }
        }"""
content = content.replace(old_css, new_css)

# Replacement 2: Structure before Salida
old_html_salida = """            <div class="page-content">
                <div class="grid-layout">
    
    <!-- PANEL DE SALIDA -->
    <div class="card">"""
new_html_salida = """            <div class="page-content">
                <div class="garita-tabs">
                    <button type="button" class="garita-tab-btn active" id="btnTabSalida" onclick="switchGaritaTab('salida')">
                        <i class="fa-solid fa-rocket"></i> Registro de Salida
                    </button>
                    <button type="button" class="garita-tab-btn" id="btnTabRetorno" onclick="switchGaritaTab('retorno')">
                        <i class="fa-solid fa-flag-checkered"></i> Registro de Retorno
                    </button>
                </div>
                
                <div class="garita-panel active" id="panelSalida">
    <!-- PANEL DE SALIDA -->
    <div class="card">"""
content = content.replace(old_html_salida, new_html_salida)

# Replacement 3: Structure before Retorno
old_html_retorno = """    <!-- PANEL DE RETORNO -->
    <div class="card">"""
new_html_retorno = """                </div>
                
                <div class="garita-panel" id="panelRetorno">
    <!-- PANEL DE RETORNO -->
    <div class="card">"""
# Be careful: there's only one "<!-- PANEL DE RETORNO -->"
content = content.replace(old_html_retorno, new_html_retorno)

# Replacement 4: Structure at end of grid
old_html_end = """        </form>
    </div>
</div>

<!-- MODAL DE COMBUSTIBLE INTERACTIVO -->"""
new_html_end = """        </form>
    </div>
                </div>
</div>

<!-- MODAL DE COMBUSTIBLE INTERACTIVO -->"""
content = content.replace(old_html_end, new_html_end)

# Replacement 5: JS Script
old_js = """    const API_URL = "https://flota-backend-xecu.onrender.com";
    let memoriaVehiculos = [];"""
new_js = """    const API_URL = "https://flota-backend-xecu.onrender.com";

    function switchGaritaTab(tab) {
        document.getElementById('btnTabSalida').classList.remove('active');
        document.getElementById('btnTabRetorno').classList.remove('active');
        document.getElementById('panelSalida').classList.remove('active');
        document.getElementById('panelRetorno').classList.remove('active');
        
        if (tab === 'salida') {
            document.getElementById('btnTabSalida').classList.add('active');
            document.getElementById('panelSalida').classList.add('active');
        } else {
            document.getElementById('btnTabRetorno').classList.add('active');
            document.getElementById('panelRetorno').classList.add('active');
        }
    }

    let memoriaVehiculos = [];"""
content = content.replace(old_js, new_js)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("done")
