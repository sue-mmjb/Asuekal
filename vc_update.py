with open('c:/Users/Sue/OneDrive/Desktop/Projects/Australian Deck/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# ── 1. REPLACE CSS ─────────────────────────────────────────────────────────────
old_css = """/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 VIDEO CARD \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */
#video-card {
  padding: 0 56px 80px;
  background: var(--black);
}
.vc-wrap {
  position: relative;
  width: 100%;
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.08);
  background: #000;
  box-shadow:
    0 0 0 1px rgba(3,161,253,0.07),
    0 40px 96px rgba(0,0,0,0.65);
  cursor: pointer;
}
/* Video element */
.vc-wrap video {
  width: 100%;
  display: block;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  filter: contrast(1.06) saturate(1.1) brightness(0.9);
  transition: filter 0.4s ease;
}
.vc-wrap:hover video { filter: contrast(1.08) saturate(1.15) brightness(0.95); }

/* Vignette */
.vc-vignette {
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.45) 100%);
  pointer-events: none;
  z-index: 1;
}

/* \u2500\u2500 Custom Controls Bar \u2500\u2500 */
.vc-controls {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  z-index: 10;
  padding: 48px 24px 20px;
  background: linear-gradient(to top, rgba(0,0,0,0.82) 0%, rgba(0,0,0,0.3) 60%, transparent 100%);
  display: flex;
  align-items: center;
  gap: 16px;
  opacity: 0;
  transform: translateY(6px);
  transition: opacity 0.35s ease, transform 0.35s ease;
}
.vc-wrap:hover .vc-controls { opacity: 1; transform: translateY(0); }

/* Play / Pause button */
.vc-btn-play {
  width: 40px; height: 40px;
  border-radius: 50%;
  border: 1.5px solid rgba(255,255,255,0.5);
  background: rgba(255,255,255,0.08);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; flex-shrink: 0;
  transition: background 0.25s ease, border-color 0.25s ease, transform 0.25s ease;
}
.vc-btn-play:hover {
  background: var(--accent);
  border-color: var(--accent);
  transform: scale(1.08);
}
.vc-btn-play svg { display: block; }

/* Progress bar */
.vc-progress {
  flex: 1;
  height: 3px;
  background: rgba(255,255,255,0.18);
  border-radius: 99px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.vc-progress-fill {
  height: 100%;
  width: 0%;
  background: var(--accent);
  border-radius: 99px;
  pointer-events: none;
  transition: width 0.1s linear;
}

/* Volume group */
.vc-vol-group {
  display: flex; align-items: center; gap: 8px; flex-shrink: 0;
}
.vc-btn-vol {
  width: 32px; height: 32px;
  border: none; background: none;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; opacity: 0.7;
  transition: opacity 0.2s ease;
  padding: 0;
}
.vc-btn-vol:hover { opacity: 1; }
.vc-btn-vol svg { display: block; }

/* Volume slider */
.vc-vol-slider {
  -webkit-appearance: none; appearance: none;
  width: 72px; height: 3px;
  background: rgba(255,255,255,0.2);
  border-radius: 99px;
  outline: none; cursor: pointer;
}
.vc-vol-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 12px; height: 12px;
  border-radius: 50%;
  background: var(--accent);
  cursor: pointer;
  transition: transform 0.2s ease;
}
.vc-vol-slider::-webkit-slider-thumb:hover { transform: scale(1.3); }
.vc-vol-slider::-moz-range-thumb {
  width: 12px; height: 12px;
  border-radius: 50%; border: none;
  background: var(--accent); cursor: pointer;
}

/* Time display */
.vc-time {
  font-family: 'Inter', sans-serif;
  font-size: 11px; font-weight: 500;
  letter-spacing: 0.04em;
  color: rgba(255,255,255,0.55);
  flex-shrink: 0;
  min-width: 72px; text-align: right;
}

/* Bottom accent line */
.vc-wrap::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, transparent 0%, var(--accent) 40%, rgba(3,161,253,0.35) 70%, transparent 100%);
  z-index: 11;
}

@media (max-width: 768px) {
  #video-card { padding: 0 20px 60px; }
  .vc-wrap { border-radius: 14px; }
  .vc-vol-slider { width: 52px; }
  .vc-controls { padding: 36px 16px 16px; gap: 12px; }
}"""

# Check if already updated
if '.vc-controls' in c and old_css in c:
    print("CSS already updated, skipping")
elif '.vc-controls' not in c:
    # First time — need to add from scratch
    print("First time update needed")
else:
    print("CSS state unclear")

# Find and replace old simple CSS
old_simple_css = """#video-card {
  padding: 0 56px 72px;
  background: var(--black);
}
.vc-wrap {
  position: relative;
  width: 100%;
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid var(--border);
  background: #000;
  box-shadow:
    0 0 0 1px rgba(3,161,253,0.06),
    0 32px 80px rgba(0,0,0,0.6);
}
.vc-wrap video {
  width: 100%;
  display: block;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  filter: contrast(1.08) saturate(1.12) brightness(0.88);
}
/* Gradient vignette inside card */
.vc-vignette {
  position: absolute; inset: 0;
  background: radial-gradient(
    ellipse at center,
    transparent 45%,
    rgba(0,0,0,0.5) 100%
  );
  pointer-events: none;
}
/* Bottom accent line */
.vc-wrap::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    var(--accent) 40%,
    rgba(3,161,253,0.4) 70%,
    transparent 100%
  );
}
@media (max-width: 768px) {
  #video-card { padding: 0 20px 56px; }
  .vc-wrap { border-radius: 14px; }
}"""

new_css = """/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 VIDEO CARD \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */
#video-card { padding: 0 56px 80px; background: var(--black); }
.vc-wrap {
  position: relative; width: 100%; border-radius: 20px;
  overflow: hidden; border: 1px solid rgba(255,255,255,0.08);
  background: #000; cursor: pointer;
  box-shadow: 0 0 0 1px rgba(3,161,253,0.07), 0 40px 96px rgba(0,0,0,0.65);
}
.vc-wrap video {
  width: 100%; display: block; aspect-ratio: 16/9;
  object-fit: cover;
  filter: contrast(1.06) saturate(1.1) brightness(0.9);
  transition: filter 0.4s ease;
}
.vc-wrap:hover video { filter: contrast(1.08) saturate(1.15) brightness(0.95); }
.vc-vignette {
  position: absolute; inset: 0; z-index: 1; pointer-events: none;
  background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.45) 100%);
}
/* Controls */
.vc-controls {
  position: absolute; bottom: 0; left: 0; right: 0; z-index: 10;
  padding: 48px 24px 20px; display: flex; align-items: center; gap: 16px;
  background: linear-gradient(to top, rgba(0,0,0,0.82) 0%, rgba(0,0,0,0.28) 60%, transparent 100%);
  opacity: 0; transform: translateY(6px);
  transition: opacity 0.35s ease, transform 0.35s ease;
}
.vc-wrap:hover .vc-controls { opacity: 1; transform: translateY(0); }
/* Play button */
.vc-btn-play {
  width: 40px; height: 40px; border-radius: 50%; flex-shrink: 0;
  border: 1.5px solid rgba(255,255,255,0.45);
  background: rgba(255,255,255,0.08);
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer;
  transition: background 0.25s ease, border-color 0.25s ease, transform 0.25s ease;
}
.vc-btn-play:hover { background: var(--accent); border-color: var(--accent); transform: scale(1.08); }
.vc-btn-play svg { display: block; }
/* Progress */
.vc-progress {
  flex: 1; height: 3px; border-radius: 99px; cursor: pointer;
  background: rgba(255,255,255,0.18); position: relative; overflow: hidden;
}
.vc-progress-fill {
  height: 100%; width: 0%; background: var(--accent);
  border-radius: 99px; pointer-events: none;
}
/* Volume */
.vc-vol-group { display: flex; align-items: center; gap: 8px; flex-shrink: 0; }
.vc-btn-vol {
  width: 32px; height: 32px; border: none; background: none; padding: 0;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; opacity: 0.65; transition: opacity 0.2s ease;
}
.vc-btn-vol:hover { opacity: 1; }
.vc-btn-vol svg { display: block; }
.vc-vol-slider {
  -webkit-appearance: none; appearance: none;
  width: 72px; height: 3px; border-radius: 99px; outline: none;
  background: rgba(255,255,255,0.2); cursor: pointer;
}
.vc-vol-slider::-webkit-slider-thumb {
  -webkit-appearance: none; width: 12px; height: 12px;
  border-radius: 50%; background: var(--accent); cursor: pointer;
  transition: transform 0.2s ease;
}
.vc-vol-slider::-webkit-slider-thumb:hover { transform: scale(1.3); }
.vc-vol-slider::-moz-range-thumb {
  width: 12px; height: 12px; border-radius: 50%;
  border: none; background: var(--accent); cursor: pointer;
}
/* Time */
.vc-time {
  font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 500;
  letter-spacing: 0.04em; color: rgba(255,255,255,0.5);
  flex-shrink: 0; min-width: 72px; text-align: right;
}
/* Accent bottom line */
.vc-wrap::after {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0;
  height: 2px; z-index: 11;
  background: linear-gradient(90deg, transparent 0%, var(--accent) 40%, rgba(3,161,253,0.35) 70%, transparent 100%);
}
@media (max-width: 768px) {
  #video-card { padding: 0 20px 60px; }
  .vc-wrap { border-radius: 14px; }
  .vc-vol-slider { width: 48px; }
  .vc-controls { padding: 32px 14px 14px; gap: 10px; }
}"""

c = c.replace(old_simple_css, new_css)
print("CSS done:", '.vc-controls' in c)

# ── 2. REPLACE HTML ────────────────────────────────────────────────────────────
old_html = """<section id="video-card">
  <div class="vc-wrap">
    <video autoplay muted loop playsinline preload="auto">
      <source src="Assets/IOZERA revamped.mp4" type="video/mp4">
    </video>
    <div class="vc-vignette"></div>
  </div>
</section>"""

new_html = """<section id="video-card">
  <div class="vc-wrap" id="vcWrap">
    <video id="vcVideo" playsinline preload="auto" loop>
      <source src="Assets/IOZERA revamped.mp4" type="video/mp4">
    </video>
    <div class="vc-vignette"></div>
    <div class="vc-controls">
      <!-- Play/Pause -->
      <button class="vc-btn-play" id="vcPlayBtn" aria-label="Play">
        <svg id="vcIconPlay" width="13" height="15" viewBox="0 0 13 15" fill="none">
          <path d="M1 1L12 7.5L1 14V1Z" fill="white" stroke="white" stroke-width="1.2" stroke-linejoin="round"/>
        </svg>
        <svg id="vcIconPause" width="11" height="14" viewBox="0 0 11 14" fill="none" style="display:none">
          <rect x="0.5" y="0.5" width="3.5" height="13" rx="1.5" fill="white"/>
          <rect x="7" y="0.5" width="3.5" height="13" rx="1.5" fill="white"/>
        </svg>
      </button>
      <!-- Progress -->
      <div class="vc-progress" id="vcProgress">
        <div class="vc-progress-fill" id="vcFill"></div>
      </div>
      <!-- Volume -->
      <div class="vc-vol-group">
        <button class="vc-btn-vol" id="vcMuteBtn" aria-label="Mute">
          <svg id="vcIconVol" width="17" height="15" viewBox="0 0 17 15" fill="none">
            <path d="M1 5H4L9 1V14L4 10H1V5Z" stroke="white" stroke-width="1.3" stroke-linejoin="round" fill="none"/>
            <path d="M11.5 3.5C13 4.8 14 6.3 14 7.5S13 10.2 11.5 11.5" stroke="white" stroke-width="1.3" stroke-linecap="round"/>
            <path d="M13.5 1C16 3 17 5 17 7.5S16 12 13.5 14" stroke="white" stroke-width="1.3" stroke-linecap="round"/>
          </svg>
          <svg id="vcIconMute" width="17" height="15" viewBox="0 0 17 15" fill="none" style="display:none">
            <path d="M1 5H4L9 1V14L4 10H1V5Z" stroke="white" stroke-width="1.3" stroke-linejoin="round" fill="none"/>
            <line x1="11" y1="4" x2="17" y2="11" stroke="white" stroke-width="1.3" stroke-linecap="round"/>
            <line x1="17" y1="4" x2="11" y2="11" stroke="white" stroke-width="1.3" stroke-linecap="round"/>
          </svg>
        </button>
        <input class="vc-vol-slider" id="vcVolSlider" type="range" min="0" max="1" step="0.02" value="0.8">
      </div>
      <!-- Time -->
      <span class="vc-time" id="vcTime">0:00 / 0:00</span>
    </div>
  </div>
</section>"""

c = c.replace(old_html, new_html)
print("HTML done:", 'vcVideo' in c)

# ── 3. INJECT JS ───────────────────────────────────────────────────────────────
js_block = """
/* ── VIDEO CARD CONTROLS ── */
(function () {
  var video     = document.getElementById('vcVideo');
  var wrap      = document.getElementById('vcWrap');
  var playBtn   = document.getElementById('vcPlayBtn');
  var iconPlay  = document.getElementById('vcIconPlay');
  var iconPause = document.getElementById('vcIconPause');
  var fill      = document.getElementById('vcFill');
  var progress  = document.getElementById('vcProgress');
  var muteBtn   = document.getElementById('vcMuteBtn');
  var iconVol   = document.getElementById('vcIconVol');
  var iconMute  = document.getElementById('vcIconMute');
  var volSlider = document.getElementById('vcVolSlider');
  var timeEl    = document.getElementById('vcTime');
  if (!video) return;

  video.volume = 0.8;
  video.muted  = false;

  function fmt(s) {
    var m = Math.floor(s / 60), sec = Math.floor(s % 60);
    return m + ':' + (sec < 10 ? '0' : '') + sec;
  }
  function syncIcons() {
    iconPlay.style.display  = video.paused ? 'block' : 'none';
    iconPause.style.display = video.paused ? 'none'  : 'block';
  }
  function togglePlay() { video.paused ? video.play() : video.pause(); syncIcons(); }

  playBtn.addEventListener('click', function(e){ e.stopPropagation(); togglePlay(); });
  wrap.addEventListener('click', function(e){
    if (!e.target.closest('.vc-controls')) togglePlay();
  });

  video.addEventListener('timeupdate', function () {
    if (!video.duration) return;
    fill.style.width = (video.currentTime / video.duration * 100) + '%';
    timeEl.textContent = fmt(video.currentTime) + ' / ' + fmt(video.duration);
  });
  progress.addEventListener('click', function (e) {
    var r = progress.getBoundingClientRect();
    video.currentTime = ((e.clientX - r.left) / r.width) * video.duration;
  });

  volSlider.addEventListener('input', function () {
    video.volume = parseFloat(volSlider.value);
    video.muted  = video.volume === 0;
    iconVol.style.display  = video.muted ? 'none'  : 'block';
    iconMute.style.display = video.muted ? 'block' : 'none';
  });
  muteBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    video.muted = !video.muted;
    volSlider.value = video.muted ? 0 : (video.volume || 0.8);
    iconVol.style.display  = video.muted ? 'none'  : 'block';
    iconMute.style.display = video.muted ? 'block' : 'none';
  });
})();
"""

old_end = "</script>\n</body>"
c = c.replace(old_end, js_block + "</script>\n</body>")
print("JS done:", 'VIDEO CARD CONTROLS' in c)

with open('c:/Users/Sue/OneDrive/Desktop/Projects/Australian Deck/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
