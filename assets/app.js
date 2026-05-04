// Wiseble — minimal vanilla JS
// 1) Mobile menu toggle
// 2) Code-block copy buttons (with optional Plausible event)

(() => {
  const burger = document.getElementById('burger');
  const menu = document.getElementById('mobile-menu');
  if (burger && menu) {
    burger.addEventListener('click', () => {
      const open = !menu.hasAttribute('hidden');
      const icon = burger.querySelector('.material-symbols-outlined');
      if (open) {
        menu.setAttribute('hidden', '');
        burger.setAttribute('aria-expanded', 'false');
        if (icon) icon.textContent = 'menu';
      } else {
        menu.removeAttribute('hidden');
        burger.setAttribute('aria-expanded', 'true');
        if (icon) icon.textContent = 'close';
      }
    });
  }

  document.querySelectorAll('.copy-btn').forEach((btn) => {
    btn.addEventListener('click', async () => {
      const targetId = btn.getAttribute('data-target');
      const target = targetId && document.getElementById(targetId);
      if (!target) return;
      try {
        await navigator.clipboard.writeText(target.innerText.trim());
        const labelSpan = btn.querySelector('span:last-child');
        const original = labelSpan ? labelSpan.textContent : '';
        if (labelSpan) labelSpan.textContent = 'Copied';
        if (window.plausible) window.plausible('code_snippet_copied', { props: { snippet: targetId } });
        setTimeout(() => { if (labelSpan) labelSpan.textContent = original; }, 1500);
      } catch (e) {
        console.warn('Clipboard write failed', e);
      }
    });
  });
})();
