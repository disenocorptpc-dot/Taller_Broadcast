import sys
import re

file_path = 'c:/Users/rsantarosa/.gemini/antigravity/playground/broadcast-app-clone/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Grid in body
content = content.replace(
'''        body {
            font-family: 'Public Sans', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            height: 100vh;
            display: grid;
            grid-template-columns: 1.2fr 320px 320px;
            grid-template-rows: 70px 1fr 70px;
            overflow: hidden;
        }''',
'''        body {
            font-family: 'Public Sans', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            height: 100vh;
            display: grid;
            grid-template-columns: 1fr 420px;
            grid-template-rows: 70px 1fr 90px;
            overflow: hidden;
            gap: 25px;
            padding: 0 25px 25px 25px;
        }''')

# 2. Update .app-header grid-column
content = content.replace(
'''        .app-header {
            grid-column: 1 / 4;
            grid-row: 1 / 2;
            background-color: var(--marine);
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 40px;
        }''',
'''        .app-header {
            grid-column: 1 / 3;
            grid-row: 1 / 2;
            background-color: var(--marine);
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 40px;
            margin: 0 -25px 0 -25px;
        }''')

# 3. Sidebar
content = content.replace(
'''        #sidebar-1 {
            grid-column: 2 / 3;
            grid-row: 2 / 3;
        }

        #sidebar-2 {
            grid-column: 3 / 4;
            grid-row: 2 / 3;
        }''',
'''        .sidebar {
            grid-column: 2 / 3;
            grid-row: 2 / 3;
        }''')

content = content.replace('.ticker-bar {\\n            grid-column: 1 / 4;', '.ticker-bar {\\n            grid-column: 1 / 3;')

# 4. Body Content Replacement
new_html = \
'''<!-- Header Global -->
    <header class="app-header">
        <div class="header-left">
            <img src="logo.svg" alt="Company Logo" style="height: 30px; margin-left: 15px;">
        </div>
        <div class="header-right">
        </div>
    </header>

    <!-- Left Main Area: Noticias y Recordatorios -->
    <main class="main-content" style="background: var(--glass-bg); backdrop-filter: blur(16px); border: 1px solid var(--glass-border); border-radius: 20px; padding: 40px; justify-content: flex-start; overflow-y: auto;">
        <ul style="list-style: none; font-size: 1.8rem; font-weight: 500; line-height: 1.8; color: var(--text-main); display: flex; flex-direction: column; gap: 10px;">
            <li>Foto reconocimiento</li>
            <li>fecha envíos, MPPC; MPJ; Los Cabos,</li>
            <li>Comunicados Corporativos</li>
            <li>Aviso de Cumpleaños poe calendario</li>
            <li>Foto cumpleañero</li>
            <li>Recordatorios estandares</li>
            <li>Recordatorios Uso equipo de Protección</li>
            <li>Calendario y responsables de tirar basura</li>
            <li>Fotos Hoteles</li>
            <li>Fechas entregas de festividdes, eventos y compromisos calendarizados</li>
        </ul>
        <!-- Hidden video elements to keep JS from throwing errors -->
        <div style="display: none;">
            <div id="video-layer"></div>
            <iframe id="main-video"></iframe>
            <div id="gallery-layer"></div>
            <div id="gallery-author"></div>
            <h1 id="gallery-title"></h1>
            <p id="gallery-desc"></p>
        </div>
    </main>

    <!-- Right Sidebar -->
    <aside class="sidebar">
        <!-- Top Row: Reloj & Clima -->
        <div style="display: flex; gap: 15px;">
            <div class="widget" style="flex: 1; padding: 15px;">
                <h3 style="text-align: center; margin-bottom: 5px;">Reloj</h3>
                <div id="clock" style="font-size: 2rem; margin-bottom: 0px; padding: 5px; text-align: center;">12:00:00</div>
                <div style="display: none;">
                    <div id="cw-merida"></div><div id="wc-merida"></div>
                    <div id="cw-cabos"></div><div id="wc-cabos"></div>
                    <div id="cw-jamaica"></div><div id="wc-jamaica"></div>
                    <div id="cw-punta"></div><div id="wc-punta"></div>
                    <div id="cw-milan"></div><div id="wc-milan"></div>
                </div>
            </div>
            <div class="widget" style="flex: 1; padding: 15px; display: flex; flex-direction: column; justify-content: center;">
                <h3 style="text-align: center; margin-bottom: 5px;">Clima</h3>
                <div class="weather-mini" style="padding: 0; border: none; background: transparent;">
                    <span class="temp" id="weather-temp" style="font-size: 2rem;">--°C</span>
                    <span class="cond" id="weather-cond">Cargando...</span>
                </div>
            </div>
        </div>

        <!-- Middle: Resultados y metas -->
        <div class="widget" style="flex-grow: 1;">
            <h3>Pulse Resultados y metas</h3>
            <div class="stat-grid" style="margin-top: 15px;">
                <div class="stat-box">
                    <div class="label">Meta Mensual</div>
                    <div style="display: flex; align-items: flex-end;">
                        <span class="value">95<span style="font-size: 1.5rem;">%</span></span>
                        <span class="trend">▲ 2%</span>
                    </div>
                </div>
                <div class="stat-box" style="border-left-color: var(--success);">
                    <div class="label">Satisfacción</div>
                    <div style="display: flex; align-items: flex-end;">
                        <span class="value" style="color: var(--success);">4.8</span>
                        <span class="trend" style="opacity: 0.8;">ÓPTIMO</span>
                    </div>
                </div>
            </div>
            
            <div style="display: none;">
                 <!-- Keep JS placeholders -->
                 <ul id="vacation-list"></ul>
                 <ul id="deadline-list"></ul>
                 <ul id="busy-list"></ul>
                 <div id="bday-main"></div><div id="bday-dept"></div>
                 <ul id="bday-next-list"></ul>
            </div>
        </div>

        <!-- Bottom: Avisos de Último Momento -->
        <div class="widget busy-mode" style="background: rgba(220, 38, 38, 0.2); border-color: rgba(220, 38, 38, 0.5);">
            <h3 style="color: white; font-size: 1.2rem; margin-bottom: 15px;">Avisos de último momento</h3>
            <ul style="color: white; list-style: none; font-size: 1.2rem; font-weight: 600; padding: 0;">
                <li style="margin-bottom: 10px; display: flex; align-items: center; gap: 10px;">
                    <span class="status-dot urgent"></span> Avisos de grabación Patiño
                </li>
            </ul>
        </div>
    </aside>

    <!-- Bottom Ticker -->
    <div class="ticker-bar" id="ticker-bar" style="border-radius: 12px; overflow: hidden;">
        <div class="ticker-label" id="ticker-label" style="height: 100%; padding: 0 30px; font-size: 1.5rem;">AVISOS</div>
        <div class="ticker-content" id="ticker-content-box">
            <div class="ticker-text" id="ticker-text" style="animation: none; transform: none; padding-left: 20px; font-size: 1.5rem;">
                <span style="margin-right:0;">Banner Ocupación Hotelera, avisos dias feriados, recordatorios gerenciales y Jefatura y Supervisión</span>
            </div>
        </div>
    </div>

    <!-- Celebration Overlay -->
    <div id="celebration-overlay">
        <div id="celebration-msg">¡FELICIDADES!</div>
    </div>'''

content = re.sub(r'<!-- Header Global -->.*?(?=\s*<script type="module">)', new_html, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Success')
