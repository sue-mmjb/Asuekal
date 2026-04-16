import re

with open('c:/Users/Sue/OneDrive/Desktop/Projects/Australian Deck/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# ── 1. REPLACE the entire vc CSS block (from #video-card through the 768px media query) ──
old_css = '''#video-card { padding: 0 56px 80px; background: var(--black); }
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
}'''

new_css = '''/* ── VIDEO CARD ── */
#video-card {
  padding: 0 56px 80px;
  background: var(--black);
}
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
/* Controls bar */
.vc-controls {
  position: absolute; bottom: 0; left: 0; right: 0; z-index: 10;
  padding: 48px 24px 20px; display: flex; align-items: center; gap: 16px;
  background: linear-gradient(to top, rgba(0,0,0,0.82) 0%, rgba(0,0,0,0.28) 60%, transparent 100%);
  opacity: 0; transform: translateY(6px);
  transition: opacity 0.35s ease, transform 0.35s ease;
  box-sizing: border-box;
}
/* Desktop hover shows controls */
.vc-wrap:hover .vc-controls { opacity: 1; transform: translateY(0); }
/* Touch devices: controls always visible */
@media (hover: none) {
  .vc-controls { opacity: 1; transform: translateY(0); }
}
/* Tap-to-reveal on touch: JS adds .vc-show-ctrl class */
.vc-wrap.vc-show-ctrl .vc-controls { opacity: 1; transform: translateY(0); }
/* Play button */
.vc-btn-play {
  width: 44px; height: 44px; border-radius: 50%; flex-shrink: 0;
  border: 1.5px solid rgba(255,255,255,0.45);
  background: rgba(255,255,255,0.08);
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer;
  transition: background 0.25s ease, border-color 0.25s ease, transform 0.25s ease;
}
.vc-btn-play:hover { background: var(--accent); border-color: var(--accent); transform: scale(1.08); }
.vc-btn-play svg { display: block; }
/* Progress bar — tall touch target via padding trick */
.vc-progress {
  flex: 1; height: 3px; border-radius: 99px; cursor: pointer;
  background: rgba(255,255,255,0.18); position: relative;
  padding: 10px 0; margin: -10px 0; box-sizing: content-box;
  overflow: visible;
}
.vc-progress-fill {
  height: 3px; width: 0%; background: var(--accent);
  border-radius: 99px; pointer-events: none; margin-top: 0;
}
/* Volume group */
.vc-vol-group { display: flex; align-items: center; gap: 8px; flex-shrink: 0; }
.vc-btn-vol {
  width: 44px; height: 44px; border: none; background: none; padding: 0;
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
  -webkit-appearance: none; width: 14px; height: 14px;
  border-radius: 50%; background: var(--accent); cursor: pointer;
  transition: transform 0.2s ease;
}
.vc-vol-slider::-webkit-slider-thumb:hover { transform: scale(1.3); }
.vc-vol-slider::-moz-range-thumb {
  width: 14px; height: 14px; border-radius: 50%;
  border: none; background: var(--accent); cursor: pointer;
}
/* Time */
.vc-time {
  font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 500;
  letter-spacing: 0.04em; color: rgba(255,255,255,0.5);
  flex-shrink: 0; min-width: 66px; text-align: right; white-space: nowrap;
}
/* Accent bottom line */
.vc-wrap::after {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0;
  height: 2px; z-index: 11;
  background: linear-gradient(90deg, transparent 0%, var(--accent) 40%, rgba(3,161,253,0.35) 70%, transparent 100%);
}
/* ── Responsive breakpoints ── */
@media (max-width: 1024px) {
  #video-card { padding: 0 36px 72px; }
}
@media (max-width: 768px) {
  #video-card { padding: 0 20px 56px; }
  .vc-wrap { border-radius: 16px; }
  .vc-controls { padding: 40px 16px 16px; gap: 12px; }
  .vc-vol-slider { width: 52px; }
  .vc-time { font-size: 10px; min-width: 58px; }
}
@media (max-width: 480px) {
  #video-card { padding: 0 14px 44px; }
  .vc-wrap { border-radius: 12px; }
  .vc-controls { padding: 36px 12px 14px; gap: 8px; }
  /* Hide volume slider on very small screens, keep mute icon */
  .vc-vol-slider { display: none; }
  .vc-time { min-width: 52px; font-size: 10px; }
  .vc-btn-play { width: 40px; height: 40px; }
}'''

if old_css in c:
    c = c.replace(old_css, new_css)
    print("CSS replaced: OK")
else:
    print("CSS block NOT found — check for drift")

# ── 2. REPLACE the JS IIFE for video card controls (add touch tap-to-toggle) ──
old_js = '''/* ── VIDEO CARD CONTROLS ── */
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
})();'''

new_js = '''/* ── VIDEO CARD CONTROLS ── */
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

  /* ── Desktop: click on video area (outside controls) toggles play ── */
  playBtn.addEventListener('click', function(e){ e.stopPropagation(); togglePlay(); });
  wrap.addEventListener('click', function(e){
    if (!e.target.closest('.vc-controls')) togglePlay();
  });

  /* ── Mobile: tap anywhere on wrap shows controls for 3 s, second tap plays/pauses ── */
  var hideTimer = null;
  function showCtrlsBriefly() {
    wrap.classList.add('vc-show-ctrl');
    clearTimeout(hideTimer);
    hideTimer = setTimeout(function(){ wrap.classList.remove('vc-show-ctrl'); }, 3000);
  }
  wrap.addEventListener('touchstart', function(e){
    if (e.target.closest('.vc-controls')) return; // let control touches pass through
    if (!wrap.classList.contains('vc-show-ctrl')) {
      e.preventDefault(); // prevent ghost click
      showCtrlsBriefly();
    } else {
      // controls already visible — toggle play on second tap
      showCtrlsBriefly();
      togglePlay();
    }
  }, { passive: false });

  /* ── Progress bar: click + touch seek ── */
  function seekTo(clientX) {
    var r = progress.getBoundingClientRect();
    video.currentTime = Math.max(0, Math.min(1, (clientX - r.left) / r.width)) * video.duration;
  }
  progress.addEventListener('click', function (e) { seekTo(e.clientX); });
  progress.addEventListener('touchstart', function (e) {
    e.stopPropagation();
    seekTo(e.touches[0].clientX);
    showCtrlsBriefly();
  }, { passive: true });
  progress.addEventListener('touchmove', function (e) {
    e.preventDefault();
    seekTo(e.touches[0].clientX);
  }, { passive: false });

  video.addEventListener('timeupdate', function () {
    if (!video.duration) return;
    fill.style.width = (video.currentTime / video.duration * 100) + '%';
    timeEl.textContent = fmt(video.currentTime) + ' / ' + fmt(video.duration);
  });

  /* ── Volume ── */
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
})();'''

if old_js in c:
    c = c.replace(old_js, new_js)
    print("JS replaced: OK")
else:
    print("JS block NOT found — check for drift")

with open('c:/Users/Sue/OneDrive/Desktop/Projects/Australian Deck/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done.")
