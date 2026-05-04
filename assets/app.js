// Wiseble — minimal vanilla JS for the marketing site.
// 1) Mobile menu toggle
// 2) Code-block copy buttons
// 3) Plausible custom events (no-op if Plausible not loaded)

(() => {
  const burger = document.getElementById('burger');
  const menu = document.getElementById('mobile-menu');

  if (burger && menu) {
    burger.addEventListener('click', () => {
      const open = !menu.hasAttribute('hidden');
      if (open) {
        menu.setAttribute('hidden', '');
        burger.setAttribute('aria-expanded', 'false');
        burger.querySelector('.material-symbols-outlined').textContent = 'menu';
      } else {
        menu.removeAttribute('hidden');
        burger.setAttribute('aria-expanded', 'true');
        burger.querySelector('.material-symbols-outlined').textContent = 'close';
      }
    });
  }

  // Copy buttons — each button has data-target pointing to a <pre> id
  document.querySelectorAll('.copy-btn').forEach((btn) => {
    btn.addEventListener('click', async () => {
      const targetId = btn.getAttribute('data-target');
      const target = targetId && document.getElementById(targetId);
      if (!target) return;

      try {
        await navigator.clipboard.writeText(target.innerText.trim());
        const label = btn.querySelector('span.code') || btn.querySelector('span:last-child');
        const original = label ? label.textContent : '';
        if (label) label.textContent = 'Copied';
        if (window.plausible) window.plausible('code_snippet_copied', { props: { snippet: targetId } });
        setTimeout(() => { if (label) label.textContent = original; }, 1500);
      } catch (e) {
        console.warn('Clipboard write failed', e);
      }
    });
  });
})();
