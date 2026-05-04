/* ============================================================
   Wiseble — ambient edge glyphs (NOT a rain)
   ------------------------------------------------------------
   Sparse, breathing glyphs in narrow vertical bands hugging
   the LEFT and RIGHT edges of any host element.
   Attaches to every <canvas class="glyph-canvas"> on the page.
   ============================================================ */
(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return;
  }

  const GLYPHS = (
    '0123456789ABCDEF' +
    '{}[]()<>/\\;:=+-*&|!?.' +
    '$%#@^~'
  ).split('');

  const TOKENS = [
    '0x', '402', 'USDC', 'MCP', 'GET', 'POST', '200',
    'x402', 'wallet', 'sig', 'tx', '/.well-known', '→',
    'idem', 'hook', 'verify', '{...}', '0xA1', '0xF4', '0xC0',
    '$99', '$49', 'agent', 'sdk',
  ];

  const FONT_SIZE = 13;
  const TARGET_PER_BAND = 18;
  const BAND_WIDTH_FRAC = 0.16;
  const EDGE_INSET_FRAC = 0.01;
  const HOT_RATIO = 0.18;

  function rand(min, max) { return Math.random() * (max - min) + min; }
  function pickGlyph() {
    if (Math.random() < 0.10) return TOKENS[(Math.random() * TOKENS.length) | 0];
    return GLYPHS[(Math.random() * GLYPHS.length) | 0];
  }

  function attach(canvas) {
    const ctx = canvas.getContext('2d', { alpha: true });
    let dpr = 1, width = 0, height = 0;
    let glyphs = [];
    let rafId = 0, lastT = performance.now();

    function makeGlyph(side) {
      const bandW = width * BAND_WIDTH_FRAC;
      const inset = width * EDGE_INSET_FRAC;
      let x;
      if (side < 0) x = rand(inset, inset + bandW);
      else x = rand(width - inset - bandW, width - inset);
      const y = rand(height * 0.05, height * 0.95);
      const lifetime = rand(2.4, 5.5);
      return {
        x, y, ch: pickGlyph(), lifetime,
        t: rand(0, lifetime),
        hot: Math.random() < HOT_RATIO,
        peak: rand(0.18, 0.55),
        swapAt: rand(0.35, 0.7) * lifetime,
      };
    }

    function rebuild() {
      glyphs = [];
      for (let i = 0; i < TARGET_PER_BAND; i++) glyphs.push(makeGlyph(-1));
      for (let i = 0; i < TARGET_PER_BAND; i++) glyphs.push(makeGlyph(+1));
    }

    function resize() {
      const rect = canvas.getBoundingClientRect();
      width = Math.max(1, rect.width);
      height = Math.max(1, rect.height);
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      rebuild();
    }

    function tick(now) {
      const dt = Math.min(0.05, (now - lastT) / 1000);
      lastT = now;
      ctx.clearRect(0, 0, width, height);
      ctx.font = `500 ${FONT_SIZE}px ui-monospace, SFMono-Regular, Menlo, monospace`;
      ctx.textBaseline = 'middle';
      ctx.textAlign = 'center';

      for (let i = 0; i < glyphs.length; i++) {
        const g = glyphs[i];
        g.t += dt;
        if (g.swapAt > 0 && g.t >= g.swapAt) { g.ch = pickGlyph(); g.swapAt = -1; }
        const u = Math.min(1, Math.max(0, g.t / g.lifetime));
        const env = Math.sin(u * Math.PI);
        const alpha = env * g.peak;
        if (alpha > 0.01) {
          ctx.fillStyle = g.hot
            ? `rgba(255, 140, 60, ${alpha.toFixed(3)})`
            : `rgba(220, 220, 225, ${alpha.toFixed(3)})`;
          ctx.fillText(g.ch, g.x, g.y);
        }
        if (g.t >= g.lifetime) {
          const side = g.x < width / 2 ? -1 : +1;
          Object.assign(g, makeGlyph(side));
        }
      }
      rafId = requestAnimationFrame(tick);
    }

    function start() {
      cancelAnimationFrame(rafId);
      lastT = performance.now();
      rafId = requestAnimationFrame(tick);
    }

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) cancelAnimationFrame(rafId);
      else start();
    });

    let resizeRaf = 0;
    window.addEventListener('resize', () => {
      cancelAnimationFrame(resizeRaf);
      resizeRaf = requestAnimationFrame(resize);
    }, { passive: true });

    resize();
    start();
  }

  // Attach to all glyph canvases on the page (incl. legacy #hero-rain id).
  const nodes = document.querySelectorAll('canvas.glyph-canvas, canvas#hero-rain');
  nodes.forEach(attach);
})();
