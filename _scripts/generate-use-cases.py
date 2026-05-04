#!/usr/bin/env python3
"""Generate the 10 /use-cases/<slug>.html detail pages from a single template.

Edit the CASES list, then run:  python3 _scripts/generate-use-cases.py

Outputs to wiseble-site/use-cases/<slug>.html.
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "use-cases"

CASES = [
    {
        "num": "01",
        "slug": "research-agents",
        "title": "Research agents",
        "headline": "Web data for research agents.",
        "subhead": "Real-time SERP, news, and academic sources for grounding LLM answers and powering Perplexity-style research products.",
        "problem": "Research agents need fresh, real-time web data to ground their answers. Static training data is months behind. Hardcoded API keys to scraping providers don't scale across thousands of agent instances or rotate cleanly when keys expire.",
        "solution": "A research agent calls <span class='font-mono text-accent-orange'>serp.search</span> or <span class='font-mono text-accent-orange'>news.fetch</span> from any agent-payable provider in the catalog. Each query costs $0.005–$0.05 in USDC, paid from the agent's budget. No human-managed account, no API key rotation, no quota negotiation.",
        "providers": ["SERP APIs", "News aggregators", "Academic paper databases", "Public records APIs"],
    },
    {
        "num": "02",
        "slug": "shopping-agents",
        "title": "Shopping agents",
        "headline": "Web data for shopping &amp; price-comparison agents.",
        "subhead": "Product, price, and availability across 50 retailers — through anti-bot defenses requiring residential proxies and JS rendering.",
        "problem": "A shopping agent comparing 50 retailers needs product, price, and availability data — often behind anti-bot defenses that require residential proxies and JS rendering. Coordinating accounts and credits across that many providers manually is impossible at agent speed.",
        "solution": "The agent buys a $99/250k-credits package from a scraping provider that handles e-commerce extraction. The agent gets a working API key in seconds, runs comparisons across thousands of products, and returns cited sources to the user. When credits run out, it tops up — within budget.",
        "providers": ["Bright Data Web Scraper", "Oxylabs E-commerce Scraper", "ScraperAPI", "ScrapingBee"],
    },
    {
        "num": "03",
        "slug": "lead-gen-agents",
        "title": "Lead-gen agents",
        "headline": "Web data for lead-gen &amp; SDR agents.",
        "subhead": "Company firmographics, contact data, technographics, intent signals — pulled from public sources at outbound scale.",
        "problem": "Outbound agents enriching prospects need company firmographics, contact data, technographics, and intent signals from public sources. Account creation across 5–10 enrichment vendors and managing per-vendor quotas is a permanent operational tax.",
        "solution": "The agent purchases lead-enrichment credits package-by-package as prospect lists grow. Cold-email and CRM-update workflows run autonomously without manual top-ups, audit trail per enriched contact, no shared API keys to leak.",
        "providers": ["B2B contact databases", "Technographic providers", "Intent-signal APIs", "Lead enrichment APIs"],
    },
    {
        "num": "04",
        "slug": "trading-agents",
        "title": "Trading agents",
        "headline": "Web data for trading &amp; market-intelligence agents.",
        "subhead": "Real-time news, social sentiment, on-chain analytics, and earnings — fragmented across 5–10 paid APIs, unified by your wallet.",
        "problem": "Trading agents need real-time news, social sentiment, on-chain analytics, and earnings data — usually fragmented across 5–10 paid APIs. Each API has its own pricing tier, key, and abuse policy. Reconciling spend at end of month is brutal.",
        "solution": "One agent wallet, one MCP namespace, dozens of data sources. Pay only for queries actually executed. Batch-purchase data packages during high-volume trading periods, scale down between events.",
        "providers": ["News APIs", "Twitter/X data APIs", "Financial data providers", "On-chain analytics"],
    },
    {
        "num": "05",
        "slug": "recruiting-agents",
        "title": "Recruiting agents",
        "headline": "Web data for recruiting &amp; talent-search agents.",
        "subhead": "Job postings, candidate profiles, and skills data — across LinkedIn, Indeed, niche boards. Bought package-by-package.",
        "problem": "Recruiting agents need job postings, candidate profiles, and skills data — pulled across LinkedIn, Indeed, and niche boards. ATS integrations are slow to negotiate; a human always has to maintain credentials.",
        "solution": "The agent purchases job-board scraping packages on-demand based on search volume. No ATS integration required, no human in the loop for credentials. Per-search cost goes from a fixed annual contract to a metered USDC stream.",
        "providers": ["LinkedIn scrapers", "Indeed scrapers", "Job-board aggregators", "Skill databases"],
    },
    {
        "num": "06",
        "slug": "real-estate-agents",
        "title": "Real estate agents",
        "headline": "Web data for real estate &amp; rental agents.",
        "subhead": "MLS data, public records, neighborhood comps, and listing photos — residential proxies bypass per-region MLS rate limits.",
        "problem": "Real estate agents (the AI kind) helping users find homes need MLS data, public records, neighborhood comps, and listing photos. Per-region MLS rate limits and licensing rules block many integrations outright.",
        "solution": "The agent buys a residential-proxy package to bypass per-region MLS rate limits, runs comparative market analysis, and returns curated listings with sources. Each search costs cents, not dollars; the agent escalates to a human only when the user is ready to act.",
        "providers": ["Real estate scrapers", "Public records APIs", "Geo-data providers", "Image hosting / CDN APIs"],
    },
    {
        "num": "07",
        "slug": "travel-agents",
        "title": "Travel agents",
        "headline": "Web data for travel &amp; pricing agents.",
        "subhead": "Real-time pricing across 20+ OTAs and direct airline sites — pages heavily protected by bot defenses, dynamic prices.",
        "problem": "Travel agents helping users book flights and hotels need real-time pricing across 20+ OTAs and direct airline sites — pages heavily protected by bot defenses and dynamic pricing tricks. CAPTCHA solving alone makes manual integrations untenable.",
        "solution": "The agent purchases JS-rendering scraper packages that handle CAPTCHA and dynamic pricing. The agent compares 50 itineraries in 30 seconds, presents the best three to the user, with every source cited. Top-ups happen mid-search if the budget allows.",
        "providers": ["Travel scrapers", "Flight aggregators", "Hotel APIs", "Currency conversion APIs"],
    },
    {
        "num": "08",
        "slug": "brand-monitoring-agents",
        "title": "Brand monitoring agents",
        "headline": "Web data for brand monitoring &amp; review-aggregation agents.",
        "subhead": "Mentions across social media, review sites, forums, news. Sentiment shifts surfaced in near-real-time.",
        "problem": "Brand-monitoring agents need to track mentions across social media, review sites, forums, and news outlets — aggregating sentiment in near-real-time. Annual contracts with monitoring vendors lock teams into capacity that doesn't match real spike-and-trough demand.",
        "solution": "The agent buys SERP and social-scraping packages on a daily cadence. When a mention spike happens, it tops up automatically. Alerts fire on sentiment shifts, priority responses are surfaced, the rest of the noise stays in the audit log.",
        "providers": ["Social listening APIs", "Review scrapers", "SERP monitoring", "News aggregators"],
    },
    {
        "num": "09",
        "slug": "osint-agents",
        "title": "OSINT agents",
        "headline": "Web data for OSINT &amp; threat-intelligence agents.",
        "subhead": "Dark-web, paste-site, public-source data — time-sensitive, high-volume, audit-trail per API call.",
        "problem": "Security agents monitoring threat actors need dark-web, paste-site, and public-source data — often time-sensitive and high-volume. Auditors want immutable logs of every query made on regulated investigations.",
        "solution": "The agent purchases specialized OSINT packages, escalates alerts to humans, and maintains a chain-anchored audit trail of every API call paid. Compliance and procurement get a clean per-investigation cost line; analysts get faster signal.",
        "providers": ["OSINT APIs", "Dark-web scrapers", "Threat-feed providers", "Public records APIs"],
    },
    {
        "num": "10",
        "slug": "knowledge-graph-agents",
        "title": "Knowledge-graph agents",
        "headline": "Web data for knowledge-graph &amp; LLM-grounding agents.",
        "subhead": "Wide, fresh, structured web data at scale. Batch-purchase high-volume packages monthly, ingest millions of pages.",
        "problem": "Agents building knowledge graphs or providing real-time grounding for LLM applications need wide, fresh, structured web data — at scale. Quotas at any single vendor cap throughput; spreading across vendors creates a per-vendor account zoo.",
        "solution": "The agent batch-purchases high-volume scraping packages monthly, ingests millions of pages, and builds and refreshes a knowledge index. Costs are predictable and scoped to the agent's budget. New providers join the network with zero integration work.",
        "providers": ["General web crawlers", "Structured-data extractors", "Document parsers", "Embedding-ready text APIs"],
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Wiseble use cases</title>
  <meta name="description" content="{subhead_meta}" />
  <link rel="canonical" href="https://wiseble.ai/use-cases/{slug}" />
  <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title} — Wiseble" />
  <meta property="og:description" content="{subhead_meta}" />
  <meta property="og:url" content="https://wiseble.ai/use-cases/{slug}" />
  <meta property="og:image" content="https://wiseble.ai/assets/og-default.png" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />

  <script src="https://cdn.tailwindcss.com"></script>
  <script src="../assets/tailwind-config.js"></script>
  <link rel="stylesheet" href="../assets/styles.css" />
</head>

<body data-page="use-cases">

  <nav class="fixed top-0 inset-x-0 z-50 bg-midnight-void border-b border-[#222]">
    <div class="max-w-wide mx-auto px-6 md:px-10 h-16 flex items-center justify-between">
      <a href="../index.html" class="flex items-center gap-3">
        <span class="display" style="font-size:22px;letter-spacing:-0.4px">Wiseble.ai</span>
      </a>
      <div class="hidden md:flex items-center gap-8">
        <a href="../index.html" class="label-sg text-muted-ash hover:text-ghost-white transition-colors">Home</a>
        <a href="../providers.html" class="label-sg text-muted-ash hover:text-ghost-white transition-colors">Providers</a>
        <a href="../developers.html" class="label-sg text-muted-ash hover:text-ghost-white transition-colors">Developers</a>
        <a href="index.html" class="label-sg text-ghost-white border-b-2 border-ghost-white pb-1">Use cases</a>
        <a href="../pricing.html" class="label-sg text-muted-ash hover:text-ghost-white transition-colors">Pricing</a>
        <a href="../about.html" class="label-sg text-muted-ash hover:text-ghost-white transition-colors">About</a>
      </div>
      <div class="flex items-center gap-3">
        <a href="../partner.html" class="hidden md:inline-flex btn-nav">Become a partner</a>
        <button id="burger" type="button" class="md:hidden p-2 text-ghost-white" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
          <span class="material-symbols-outlined">menu</span>
        </button>
      </div>
    </div>
    <div id="mobile-menu" class="mobile-menu md:hidden border-t border-[#222] bg-midnight-void" hidden>
      <div class="px-6 py-6 flex flex-col gap-4">
        <a href="../index.html" class="label-sg text-muted-ash">Home</a>
        <a href="../providers.html" class="label-sg text-muted-ash">Providers</a>
        <a href="../developers.html" class="label-sg text-muted-ash">Developers</a>
        <a href="index.html" class="label-sg text-ghost-white">Use cases</a>
        <a href="../pricing.html" class="label-sg text-muted-ash">Pricing</a>
        <a href="../about.html" class="label-sg text-muted-ash">About</a>
        <a href="../partner.html" class="btn-nav mt-2">Become a partner</a>
      </div>
    </div>
  </nav>

  <main class="pt-16">

    <section class="section">
      <div class="max-w-content mx-auto px-6 md:px-10">
        <div class="flex items-center gap-3 mb-6">
          <a href="index.html" class="caption text-muted-ash hover:text-accent-orange">Use cases</a>
          <span class="caption text-muted-ash">/</span>
          <span class="caption text-accent-orange">{num} · {title}</span>
        </div>
        <h1 class="display-xl text-ghost-white max-w-4xl">{headline}</h1>
        <p class="body-lg text-on-surface-variant max-w-3xl mt-8">{subhead}</p>
      </div>
    </section>

    <section class="section pt-0 md:pt-0 lg:pt-0 border-t border-[#222]">
      <div class="max-w-content mx-auto px-6 md:px-10 mt-16">
        <div class="grid md:grid-cols-2 gap-6">

          <article class="bracket-frame console-card-low"><span class="bl"></span><span class="br"></span>
            <span class="caption text-muted-ash">// The problem</span>
            <h2 class="heading text-ghost-white mt-3">What's broken today.</h2>
            <p class="body-lg text-on-surface-variant mt-6">{problem}</p>
          </article>

          <article class="bracket-frame border-2 border-accent-orange p-[30px] bg-surface-container-lowest"><span class="bl"></span><span class="br"></span>
            <span class="caption text-accent-orange">// With Wiseble</span>
            <h2 class="heading text-ghost-white mt-3">How it works through us.</h2>
            <p class="body-lg text-on-surface-variant mt-6">{solution}</p>
          </article>

        </div>
      </div>
    </section>

    <section class="section border-t border-[#222]">
      <div class="max-w-content mx-auto px-6 md:px-10">
        <p class="caption text-accent-orange mb-6">// Recommended provider categories</p>
        <h2 class="display text-ghost-white max-w-4xl">Providers in this category.</h2>
        <p class="body-lg text-on-surface-variant max-w-3xl mt-8">
          On launch, the Wiseble catalog will include partners across these categories. Are you a provider in this space? <a href="../providers.html" class="text-accent-orange underline">Apply to integrate →</a>
        </p>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-12">
{providers_html}
        </div>
      </div>
    </section>

    <section class="section border-t border-[#222]">
      <div class="max-w-content mx-auto px-6 md:px-10">
        <div class="border-2 border-accent-orange p-12 md:p-20 bg-surface-container-lowest text-center relative overflow-hidden">
          <div class="absolute -top-24 -right-24 w-64 h-64 bg-accent-orange/10 blur-3xl rounded-full"></div>
          <h2 class="display text-ghost-white max-w-3xl mx-auto">Selling to {title_lc}? List your API.</h2>
          <p class="body-lg text-on-surface-variant max-w-2xl mx-auto mt-6">
            One YAML, one middleware, one restart. Agents in this category find you the moment they need you.
          </p>
          <div class="flex flex-col sm:flex-row items-center justify-center gap-4 mt-10">
            <a href="../partner.html" class="btn-solid">Become a launch partner</a>
            <a href="../pricing.html" class="btn-outline">See pricing</a>
          </div>
        </div>
      </div>
    </section>

  </main>

  <footer class="border-t-2 border-ghost-white bg-midnight-void">
    <div class="max-w-wide mx-auto px-6 md:px-10 py-16 grid grid-cols-2 md:grid-cols-4 gap-12">
      <div class="col-span-2 flex flex-col gap-4">
        <span class="display" style="font-size:24px;letter-spacing:-0.4px">Wiseble.ai</span>
        <p class="helper max-w-md">Agent-payable interface for existing data APIs. Your tariffs, your wallet, your brand — invisible plumbing for the agentic web.</p>
        <p class="caption text-muted-ash mt-4">© 2026 Wiseble · Technical protocol established · Built in Spain</p>
      </div>
      <div class="flex flex-col gap-3">
        <span class="caption text-muted-ash">Product</span>
        <a href="../providers.html" class="caption text-ghost-white hover:text-accent-orange">For providers</a>
        <a href="../developers.html" class="caption text-ghost-white hover:text-accent-orange">For developers</a>
        <a href="index.html" class="caption text-ghost-white hover:text-accent-orange">Use cases</a>
        <a href="../pricing.html" class="caption text-ghost-white hover:text-accent-orange">Pricing</a>
      </div>
      <div class="flex flex-col gap-3">
        <span class="caption text-muted-ash">Company</span>
        <a href="../about.html" class="caption text-ghost-white hover:text-accent-orange">About</a>
        <a href="../partner.html" class="caption text-ghost-white hover:text-accent-orange">Become a partner</a>
        <a href="mailto:hello@wiseble.ai" class="caption text-ghost-white hover:text-accent-orange">hello@wiseble.ai</a>
        <a href="#" class="caption text-muted-ash hover:text-accent-orange">Privacy</a>
        <a href="#" class="caption text-muted-ash hover:text-accent-orange">Terms</a>
      </div>
    </div>
  </footer>

  <script src="../assets/app.js"></script>
</body>
</html>
"""


def render_providers(providers: list[str]) -> str:
    chunks = []
    for p in providers:
        chunks.append(
            f'          <div class="border border-[#353535] p-5">\n'
            f'            <h3 class="subheading text-ghost-white">{p}</h3>\n'
            f'          </div>'
        )
    return "\n".join(chunks)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for c in CASES:
        path = OUT / f"{c['slug']}.html"
        # Strip HTML tags from subhead for meta description
        import re
        subhead_meta = re.sub(r"<[^>]+>", "", c["subhead"]).replace('"', "'")
        title_lc = c["title"].lower()
        page = TEMPLATE.format(
            title=c["title"],
            title_lc=title_lc,
            slug=c["slug"],
            num=c["num"],
            headline=c["headline"],
            subhead=c["subhead"],
            subhead_meta=subhead_meta,
            problem=c["problem"],
            solution=c["solution"],
            providers_html=render_providers(c["providers"]),
        )
        path.write_text(page, encoding="utf-8")
        print(f"  wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
