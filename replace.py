import re

with open('index.html', 'r', encoding='utf-8') as f:
    original = f.read()

# Extract script module (starting around line 648)
script_match = re.search(r'<script type="module">.*?</script>', original, re.DOTALL)
if script_match:
    script_content = script_match.group(0)
else:
    print("Could not find script module!")
    exit(1)

new_html = r"""<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Company Broadcast Dashboard</title>
<!-- Tailwind CSS v3 CDN -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<!-- Google Fonts for Public Sans -->
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet"/>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

<script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brandBlue: '#254D6E',
            brandCream: '#EDECE4',
            brandTan: '#B88F69',
            brandGrey: '#E0E5E5',
            brandDark: '#1a364d',
          },
          fontFamily: {
            sans: ['Public Sans', 'sans-serif'],
          },
          borderRadius: {
            'custom': '8px',
          }
        }
      }
    }
</script>

<style data-purpose="layout-styles">
    :root {
        --marine: #254D6E;
        --gold: #B88F69;
        --text-muted: rgba(37, 77, 110, 0.7);
        --danger: #ff0055;
        --glass-border: rgba(37, 77, 110, 0.15);
    }
    
    body {
      background-color: #EDECE4;
      color: #254D6E;
      font-family: 'Public Sans', sans-serif;
      overflow: hidden;
      height: 100vh;
      display: flex;
      flex-direction: column;
    }
    .glass-panel {
      background: rgba(224, 229, 229, 0.4);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(184, 143, 105, 0.2);
    }
    .main-grid {
      display: grid;
      grid-template-columns: 1.4fr 1fr 1fr;
      gap: 1.5rem;
      padding: 1.5rem;
      flex-grow: 1;
    }
</style>

<style data-purpose="component-styles">
    .metric-card {
      border-left: 4px solid #B88F69;
    }
    .clock-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 0.75rem;
    }
    .clock-item {
      border: 1px solid #B88F69;
      transition: all 0.3s ease;
    }
    .clock-item.working {
        background-color: #254D6E;
        color: #EDECE4;
        border-color: #254D6E;
    }
    .clock-item.off-hours {
        background-color: rgba(255,255,255,0.4);
        border-color: #e0e5e5;
        color: rgba(37, 77, 110, 0.7);
    }
    
    .ticker-container {
      height: 60px;
      background-color: #254D6E;
    }
    .ticker-label {
      background-color: #B88F69;
      color: #EDECE4;
    }
    .ticker-container.alert-mode {
        background-color: #ff0055;
    }
    .ticker-container.alert-mode .ticker-label {
        background-color: white;
        color: #ff0055;
    }
    
    .abstract-bg {
      background: linear-gradient(135deg, #254D6E 0%, #B88F69 100%);
      position: relative;
      overflow: hidden;
    }
    .abstract-bg::after {
      content: "";
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle, rgba(237,236,228,0.1) 0%, transparent 70%);
      animation: rotate 20s linear infinite;
    }
    @keyframes rotate {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

	/* CSS para Animaciones Antiguas (Marquee JS, Overlay, busy alert) */
    .ticker-manager-alert {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
        font-size: 1.5rem;
        font-weight: 700;
        color: white;
        animation: pulse 2s infinite;
    }
	.ticker-text span {
        margin-right: 50px;
    }
    .ticker-text .highlight {
        color: #B88F69;
        font-weight: 600;
    }
    .ticker-text .alert {
        color: #ff0055;
        font-weight: 600;
    }
	@keyframes ticker {
        0% { transform: translate3d(0, 0, 0); }
        100% { transform: translate3d(-100%, 0, 0); }
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
	#celebration-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.85);
        backdrop-filter: blur(10px);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 40px;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.5s ease;
    }
    #celebration-overlay.active {
        opacity: 1;
        pointer-events: all;
    }
    #celebration-msg {
        font-family: 'Public Sans', sans-serif;
        font-size: 7.5rem;
        font-weight: 900;
        color: #fff;
        text-align: center;
        text-transform: uppercase;
        text-shadow: 0 0 50px rgba(0, 240, 255, 0.8), 0 0 100px rgba(255, 0, 85, 0.8);
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards, pulseCelebration 0.8s 0.5s infinite alternate ease-in-out;
        transform: scale(0.1);
        background: -webkit-linear-gradient(45deg, #00f0ff, #fff, #ff0055);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    @keyframes popIn {
        to { transform: scale(1); }
    }
    @keyframes pulseCelebration {
        0% { transform: scale(1); filter: drop-shadow(0 0 20px rgba(255, 0, 85, 0.8)); }
        100% { transform: scale(1.15) rotate(2deg); filter: drop-shadow(0 0 80px rgba(0, 240, 255, 0.9)); }
    }

    /* Lists */
    .task-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .task-item {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 12px;
        padding-bottom: 12px;
        border-bottom: 1px solid rgba(37, 77, 110, 0.15);
    }
    .task-item:last-child {
        margin: 0;
        padding: 0;
        border: none;
    }
    .status-dot {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        flex-shrink: 0;
    }
    .status-dot.pending { background: #ffaa00; }
    .status-dot.urgent { background: #ff0055; box-shadow: 0 0 10px #ff0055; }
    .status-dot.done { background: #00ff88; }
    
    .sidebar.busy-mode {
        background: rgba(255, 0, 85, 0.05);
    }
    .sidebar.busy-mode h3 {
        color: #ff0055;
    }
</style>
</head>
<body>
<!-- BEGIN: Header -->
<header class="flex justify-between items-center px-8 py-4 bg-brandBlue text-brandCream shadow-md">
    <div class="flex items-center gap-4">
        <div class="bg-red-600 text-white text-xs font-bold px-3 py-1 rounded-full animate-pulse uppercase tracking-widest">Live</div>
        <div>
            <h1 class="text-xl font-extrabold tracking-tight uppercase">Company Broadcast</h1>
        </div>
    </div>
    <div class="text-right">
        <p class="text-xs uppercase tracking-widest opacity-80">Event Session</p>
        <p class="font-bold">Q3 Global Kickoff</p>
    </div>
</header>
<!-- END: Header -->

<!-- BEGIN: Main Dashboard Content -->
<main class="main-grid">
    <!-- BEGIN: Left Visual Area -->
    <section class="flex flex-col gap-4">
        <div class="relative h-full w-full rounded-custom overflow-hidden shadow-xl bg-black flex items-end">
            
            <div id="video-layer" style="position: absolute; top:0; left:0; transition: opacity 1.5s ease; width: 100%; height: 100%;">
                <iframe id="main-video"
                    src="https://www.youtube.com/embed/jfKfPfyJRdk?autoplay=1&mute=1&controls=0&loop=1&playlist=jfKfPfyJRdk"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen style="width: 100%; height: 100%; border: none; object-fit: cover;"></iframe>
            </div>

            <!-- Abstract professional overlay content -->
            <div id="gallery-layer" class="abstract-bg flex items-end p-8" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 10; opacity: 0; background-size: cover; background-position: center; transition: opacity 1.5s ease;">
                <div class="z-10 w-full" style="padding: 20px; background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.3) 100%); border-radius: 8px;">
                    <span id="gallery-author" class="inline-block bg-brandTan text-brandCream px-4 py-1 rounded-full text-xs font-bold mb-4" style="display:none;"></span>
                    <h2 id="gallery-title" class="text-5xl font-extrabold text-brandCream leading-tight mb-4" style="text-shadow: 0 4px 15px rgba(0,0,0,0.6);"></h2>
                    <p id="gallery-desc" class="text-brandCream opacity-90 text-lg max-w-md" style="text-shadow: 0 2px 10px rgba(0,0,0,0.6);"></p>
                </div>
            </div>
        </div>
    </section>
    <!-- END: Left Visual Area -->

    <!-- BEGIN: Central World Clocks -->
    <section class="flex flex-col gap-4 sidebar">
        <div class="glass-panel rounded-custom p-6 flex flex-col h-full border border-brandGrey">
            <div class="flex items-center gap-2 mb-6">
                <span class="text-xl">🌎</span>
                <h3 class="text-xs font-bold uppercase tracking-widest text-brandTan">Relojes Mundiales</h3>
            </div>
            <div class="flex flex-col items-center justify-center py-8 mb-6 bg-brandBlue/5 rounded-custom">
                <span class="text-6xl font-bold text-brandBlue tracking-tighter" id="clock">11:22 AM</span>
                <span class="text-xs uppercase tracking-widest text-brandBlue opacity-60 mt-2">Hora Local (CDMX)</span>
            </div>
            
            <div class="clock-grid flex-grow">
                <div class="clock-item rounded-custom p-4 flex flex-col justify-between" id="cw-merida">
                    <span class="text-[10px] uppercase font-bold tracking-widest">Mérida</span>
                    <span class="text-2xl font-bold" id="wc-merida">--:--</span>
                </div>
                <div class="clock-item rounded-custom p-4 flex flex-col justify-between" id="cw-cabos">
                    <span class="text-[10px] uppercase font-bold tracking-widest">Los Cabos</span>
                    <span class="text-2xl font-bold" id="wc-cabos">--:--</span>
                </div>
                <div class="clock-item rounded-custom p-4 flex flex-col justify-between" id="cw-jamaica">
                    <span class="text-[10px] uppercase font-bold tracking-widest">Jamaica</span>
                    <span class="text-2xl font-bold" id="wc-jamaica">--:--</span>
                </div>
                <div class="clock-item rounded-custom p-4 flex flex-col justify-between" id="cw-punta">
                    <span class="text-[10px] uppercase font-bold tracking-widest">Punta Cana</span>
                    <span class="text-2xl font-bold" id="wc-punta">--:--</span>
                </div>
                <div class="clock-item rounded-custom p-4 flex flex-col justify-between" id="cw-milan">
                    <span class="text-[10px] uppercase font-bold tracking-widest opacity-80">Milán</span>
                    <span class="text-2xl font-bold" id="wc-milan">--:--</span>
                </div>
                <!-- Clima Milán / Custom -->
                <div class="clock-item rounded-custom p-4 flex flex-col justify-between bg-brandGrey border-none off-hours">
                    <span class="text-[10px] uppercase font-bold tracking-widest">Clima</span>
                    <div class="flex items-center gap-2">
                        <span class="text-2xl font-bold" id="weather-temp">--°C</span>
                        <span class="text-[10px] leading-tight font-bold" id="weather-cond">☁️</span>
                    </div>
                </div>
            </div>
            
        </div>
    </section>
    <!-- END: Central World Clocks -->

    <!-- BEGIN: Right Sidebar Metrics & Lists -->
    <aside class="flex flex-col gap-4 sidebar text-brandBlue">
        <!-- Metrics -->
        <div class="glass-panel rounded-custom p-6 border border-brandGrey">
            <h3 class="text-[10px] font-bold uppercase tracking-widest text-brandTan mb-4">Métricas de Evento</h3>
            <div class="grid grid-cols-2 gap-4">
                <div class="metric-card pl-4">
                    <span class="text-4xl font-extrabold text-brandBlue" id="stat-viewers">1,204</span>
                    <p class="text-[10px] uppercase font-bold text-brandBlue opacity-60">Viendo Ahora</p>
                </div>
                <div class="metric-card pl-4 border-l-[#22c55e]">
                    <span class="text-4xl font-extrabold text-[#22c55e]" id="stat-health">98%</span>
                    <p class="text-[10px] uppercase font-bold text-brandBlue opacity-60">Estabilidad</p>
                </div>
            </div>
        </div>
        <!-- Deadlines -->
        <div class="glass-panel rounded-custom p-6 border border-brandGrey flex-grow">
            <h3 class="text-[10px] font-bold uppercase tracking-widest text-brandTan mb-3">Próximos Deadlines</h3>
            <ul class="task-list" id="deadline-list"></ul>
        </div>
        <!-- In Meeting -->
        <div class="glass-panel rounded-custom p-6 border border-brandGrey flex-grow">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xs">🚫</span>
                <h3 class="text-[10px] font-bold uppercase tracking-widest text-brandTan">En Junta / Ocupados</h3>
            </div>
            <ul class="task-list" id="busy-list"></ul>
        </div>
        
        <!-- Vacations Widget (Restored so code doesn't break, keeping layout) -->
        <div class="glass-panel rounded-custom p-6 border border-brandGrey flex-grow" style="display:none;" id="vacation-widget">
            <ul class="task-list" id="vacation-list"></ul>
        </div>

        <!-- Birthdays -->
        <div class="glass-panel rounded-custom p-6 border border-brandGrey flex-grow">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xs">🎉</span>
                <h3 class="text-[10px] font-bold uppercase tracking-widest text-brandTan">Cumpleaños</h3>
            </div>
            <div class="mt-2" style="margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid rgba(37,77,110,0.15);">
                <p class="text-[10px] uppercase font-bold mb-1">Hoy celebramos a:</p>
                <div id="bday-main" class="text-2xl font-extrabold text-brandBlue">🎂 Cargando...</div>
                <div id="bday-dept" class="text-sm opacity-80 mt-1"></div>
            </div>
            <div class="mt-2 text-brandBlue">
                <p class="text-[10px] uppercase font-bold mb-1">Próximos:</p>
                <ul class="task-list" id="bday-next-list"></ul>
            </div>
        </div>
    </aside>
    <!-- END: Right Sidebar Metrics & Lists -->
</main>
<!-- END: Main Dashboard Content -->

<!-- BEGIN: News Ticker -->
<footer class="ticker-container flex items-center overflow-hidden" id="ticker-bar">
    <div id="ticker-label" class="ticker-label h-full flex items-center px-8 z-20 font-extrabold text-xl tracking-tight uppercase whitespace-nowrap">
        ÚLTIMA HORA
    </div>
    <div class="flex-grow bg-brandBlue relative flex items-center overflow-hidden h-full" id="ticker-content-box">
        <div class="ticker-text" id="ticker-text" style="display:inline-block; padding-left:100%; white-space:nowrap; align-items:center; height:100%; display:flex; color:white;">
            <span>Cargando anuncios...</span>
        </div>
    </div>
</footer>
<!-- END: News Ticker -->

<!-- Celebration Overlay -->
<div id="celebration-overlay">
    <div id="celebration-msg">¡FELICIDADES!</div>
</div>
"""

final_content = new_html + "\n" + script_content + "\n</body>\n</html>"

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)
