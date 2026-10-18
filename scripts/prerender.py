import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Shared Schema.org JSON-LD
STRUCTURED_DATA = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LocalBusiness",
      "@id": "https://qacover.com/#localbusiness",
      "name": "QAcover",
      "alternateName": ["QAcover Software QA", "QAcover Chandigarh QA", "QAcover Testing Services"],
      "url": "https://qacover.com",
      "logo": "https://qacover.com/images/logo-dark.webp",
      "image": "https://qacover.com/images/hero-character.webp",
      "email": "hello@qacover.com",
      "telephone": "+919872492649",
      "priceRange": "$$",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Chandigarh",
        "addressRegion": "Chandigarh",
        "postalCode": "160001",
        "addressCountry": "IN"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 30.7333,
        "longitude": 76.7794
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Chandigarh"
        },
        {
          "@type": "City",
          "name": "Mohali"
        },
        {
          "@type": "City",
          "name": "Panchkula"
        },
        {
          "@type": "City",
          "name": "Zirakpur"
        }
      ],
      "sameAs": [
        "https://www.linkedin.com/in/sahil-lohran-475791317/"
      ],
      "description": "QAcover is an independent software QA company based in Chandigarh tricity, serving Chandigarh, Mohali, Panchkula, and Zirakpur as well as global engineering teams with manual exploratory testing, Playwright/Cypress test automation, and white-label QA under NDA.",
      "founder": {
        "@type": "Person",
        "name": "Sahil Lohran",
        "jobTitle": "Founder & Lead QA",
        "sameAs": "https://www.linkedin.com/in/sahil-lohran-475791317/"
      }
    },
    {
      "@type": "ProfessionalService",
      "@id": "https://qacover.com/#service",
      "name": "QAcover — Software QA Testing & Test Automation Services",
      "url": "https://qacover.com",
      "provider": {
        "@id": "https://qacover.com/#localbusiness"
      },
      "serviceType": [
        "Manual QA Testing",
        "Exploratory Testing",
        "Test Automation Services",
        "Playwright Automation",
        "Cypress Automation",
        "White-Label QA for Agencies",
        "API & Backend Validation",
        "Mobile App Testing"
      ],
      "areaServed": ["Chandigarh", "Mohali", "Panchkula", "Zirakpur", "Worldwide"]
    }
  ]
}

JSON_LD_STR = json.dumps(STRUCTURED_DATA, indent=2)

NAVBAR_HTML = '''
<header class="v1-navbar">
  <div class="v1-navbar-container">
    <a href="/" class="v1-brand-link">
      <img src="/images/logo-dark.webp" alt="QAcover" style="height: 32px; width: auto; display: block;" />
    </a>
    <nav class="v1-nav-menu">
      <a href="/services" class="v1-nav-link">Services</a>
      <a href="/how-it-works" class="v1-nav-link">How it works</a>
      <a href="/white-label" class="v1-nav-link">White-label</a>
      <a href="/about" class="v1-nav-link">About</a>
      <a href="/free-audit" class="v1-nav-cta">Get a free flow audit &rarr;</a>
    </nav>
  </div>
</header>
'''

FOOTER_HTML = '''
<footer class="v1-footer-v2">
  <div class="v1-section-container">
    <div class="v1-footer-grid">
      <div class="v1-footer-brand">
        <a href="/" style="display:inline-block;text-decoration:none;margin-bottom:12px;">
          <img src="/images/logo-dark.webp" alt="QAcover" style="height:30px;width:auto;display:block;" />
        </a>
        <p>Manual + automation QA testing for product teams and agencies. Working inside your sprints under strict NDA.</p>
        <div class="v1-footer-contact-list">
          <a href="mailto:hello@qacover.com">hello@qacover.com</a>
          <a href="https://wa.me/919872492649?text=Hi%20QAcover" target="_blank" rel="noopener noreferrer">WhatsApp: +91 98724 92649</a>
          <span class="v1-footer-location">Based in the Chandigarh tricity, serving Chandigarh, Mohali, Panchkula and Zirakpur &bull; Working with teams worldwide</span>
        </div>
      </div>
      <div class="v1-footer-col">
        <h5>SERVICES</h5>
        <ul>
          <li><a href="/services/manual-qa">Manual QA</a></li>
          <li><a href="/services/automation-qa">Test Automation</a></li>
          <li><a href="/white-label">White-Label QA</a></li>
          <li><a href="/services">All QA Services &rarr;</a></li>
          <li><a href="/free-audit" style="color:#00b87c;font-weight:750;">Get a Free Flow Audit &rarr;</a></li>
        </ul>
      </div>
      <div class="v1-footer-col">
        <h5>COMPANY</h5>
        <ul>
          <li><a href="/how-it-works">How It Works</a></li>
          <li><a href="/qa-testing-chandigarh">Chandigarh Tricity QA</a></li>
          <li><a href="/about">About QAcover</a></li>
          <li><a href="/white-label">For Agencies &amp; Dev Shops</a></li>
          <li><a href="/free-audit">Free Audit Request</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
        </ul>
      </div>
      <div class="v1-footer-col">
        <h5>CONNECT</h5>
        <p style="color:#64748b;font-size:13.5px;line-height:1.5;margin:0 0 16px 0;">Direct access to our founder. No sales reps or gatekeepers.</p>
        <a href="https://www.linkedin.com/in/sahil-lohran-475791317/" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:8px;color:#064e3b;font-weight:700;font-size:14px;text-decoration:none;margin-bottom:12px;">
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"></path><circle cx="4" cy="4" r="2"></circle></svg>
          Sahil on LinkedIn &rarr;
        </a>
        <div>
          <a href="mailto:hello@qacover.com?subject=Book%20a%2020-min%20QA%20Strategy%20Call" style="color:#475569;font-size:13px;text-decoration:underline;">Email us to book a 20-min call</a>
        </div>
      </div>
    </div>
    <div class="v1-footer-bottom">
      <div>&copy; 2026 QAcover. All rights reserved.</div>
      <div>
        <a href="/privacy" style="color:#64748b;font-size:13px;text-decoration:none;">Privacy Policy</a>
      </div>
    </div>
  </div>
</footer>
'''

PAGES = [
    {
        "rel_path": "index.html",
        "title": "QAcover — Software QA Testing & Test Automation for Startups",
        "description": "QAcover provides manual exploratory testing, test automation (Playwright/Cypress), and white-label QA. Based in the Chandigarh tricity, serving Chandigarh, Mohali, Panchkula and Zirakpur — working with product teams worldwide. Start with a free flow audit under NDA.",
        "canonical": "https://qacover.com/",
        "noindex": False,
        "content_html": '''
<section class="v1-hero">
  <div class="v1-hero-container">
    <div class="v1-hero-badge">
      <span class="v1-badge-dot"></span>
      <span>INDEPENDENT SOFTWARE QA PARTNER</span>
    </div>
    <h1 class="v1-hero-title">
      Ship Releases Your Users Don't Have to <span class="highlight">Test For You</span>
    </h1>
    <p class="v1-hero-sub">
      Manual exploratory testing, Playwright &amp; Cypress test automation, and white-label QA for product teams and agencies. Based in the Chandigarh tricity, serving Chandigarh, Mohali, Panchkula, and Zirakpur &bull; working with engineering teams worldwide under strict mutual NDA.
    </p>
    <div class="v1-hero-cta-group">
      <a href="/free-audit?cta=home_hero" class="btn btn-primary btn-lg">Get a free flow audit &rarr;</a>
      <a href="/services" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Explore QA Services &rarr;</a>
    </div>
  </div>
</section>
<section class="v1-final-cta-section">
  <div class="v1-final-cta-container">
    <h2 class="v1-final-cta-title">Find out what's broken before your users do.</h2>
    <p class="v1-final-cta-desc">
      Request an exploratory audit of your key flow. Prioritized defect report delivered within 3 business days under strict mutual NDA.
    </p>
    <div class="v1-final-cta-actions">
      <a href="/free-audit?cta=home_closing" class="btn btn-primary btn-lg">Get my free flow audit &rarr;</a>
    </div>
  </div>
</section>
'''
    },
    {
        "rel_path": "services/index.html",
        "title": "Software QA Services | Manual, Automation & Sprint QA — QAcover",
        "description": "Explore QAcover's full software testing services: manual exploratory testing, Playwright & Cypress automation, API validation, and white-label QA for agencies. Fast turnaround under strict NDA.",
        "canonical": "https://qacover.com/services",
        "noindex": False,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">COMPREHENSIVE QA OFFERINGS</span>
      <h1 class="cp-hero-title">Full-Spectrum Software <span class="highlight">QA &amp; Testing Services</span></h1>
      <p class="cp-hero-desc">From human exploratory bug hunts to automated Playwright CI/CD release gates and white-label agency testing.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/services/manual-qa" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Manual QA Services &rarr;</a>
        <a href="/services/automation-qa" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Test Automation &rarr;</a>
        <a href="/free-audit?cta=services_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
      </div>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "services/manual-qa/index.html",
        "title": "Manual QA Testing Services | Exploratory & Functional QA — QAcover",
        "description": "Human-led manual exploratory testing across real iOS, Android, and web browsers. Edge-case discovery, detailed reproduction steps, and sprint release clearance.",
        "canonical": "https://qacover.com/services/manual-qa",
        "noindex": False,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">CORE QA DISCIPLINE</span>
      <h1 class="cp-hero-title">Manual Exploratory &amp; <span class="highlight">Functional QA Testing</span></h1>
      <p class="cp-hero-desc">Human intuition and systematic test exploration to discover edge cases, layout regressions, and broken user journeys before your paying users do.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?cta=manual_qa_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
        <a href="/services" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">All QA Services &rarr;</a>
      </div>
    </section>
  </div>
  <section style="padding:60px 0;background:#fff;">
    <div class="v1-section-container">
      <span class="cp-pill-badge">WHAT WE TEST</span>
      <h2 class="v1-section-h2">Comprehensive manual testing methodology</h2>
      <p class="v1-section-sub">We don't just follow checklists; we stress test user assumptions and simulate chaotic user interactions.</p>
      <div class="v1-workflow-grid">
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">01</span>
          <h3>Exploratory Bug Hunts</h3>
          <p>Unscripted, session-based testing designed to break edge cases, concurrent user actions, invalid data boundaries, and session timeouts.</p>
        </div>
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">02</span>
          <h3>Real Physical Devices</h3>
          <p>Testing across physical iOS and Android smartphones, tablets, macOS, Windows, and multiple browser engines (Chromium, WebKit, Gecko).</p>
        </div>
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">03</span>
          <h3>Engineered Bug Reports</h3>
          <p>Every defect logged in Jira, Linear, or GitHub includes annotated video proof, exact steps to reproduce, console error traces, and network logs.</p>
        </div>
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">04</span>
          <h3>Sprint Release Clearance</h3>
          <p>Direct coordination with your engineering team during sprint regression freezes to provide confident sign-off before production deployment.</p>
        </div>
      </div>
      <div style="text-align:center;margin-top:48px;">
        <a href="/free-audit?cta=manual_qa_bottom" class="btn btn-primary btn-lg">Start With a Free Flow Audit &rarr;</a>
      </div>
    </div>
  </section>
</div>
'''
    },
    {
        "rel_path": "services/automation-qa/index.html",
        "title": "Test Automation Services | Playwright, Cypress & CI/CD — QAcover",
        "description": "End-to-end automated test suites built in Playwright and Cypress. Integrated directly into GitHub Actions, GitLab, and CI/CD pipelines for zero regression leaks.",
        "canonical": "https://qacover.com/services/automation-qa",
        "noindex": False,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">TEST AUTOMATION</span>
      <h1 class="cp-hero-title">End-to-End Test Automation with <span class="highlight">Playwright &amp; Cypress</span></h1>
      <p class="cp-hero-desc">Fast, stable, maintainable test automation suites integrated into your CI/CD pipelines. Eliminate regression leaks and ship pull requests with complete confidence.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?cta=automation_qa_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
        <a href="/services" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">All QA Services &rarr;</a>
      </div>
    </section>
  </div>
  <section style="padding:60px 0;background:#fff;">
    <div class="v1-section-container">
      <span class="cp-pill-badge">AUTOMATION FRAMEWORK</span>
      <h2 class="v1-section-h2">Engineered for zero flakiness and rapid execution</h2>
      <p class="v1-section-sub">We build modular test suites following industry Page Object Model patterns that your dev team can easily extend.</p>
      <div class="v1-workflow-grid">
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">01</span>
          <h3>Playwright &amp; Cypress Suites</h3>
          <p>Modern TypeScript-based automated test architectures with auto-waiting, parallel worker execution, and isolated test contexts.</p>
        </div>
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">02</span>
          <h3>CI/CD Integration</h3>
          <p>Seamless pull request triggers in GitHub Actions, GitLab CI, or CircleCI. Fast feedback in under 5 minutes before code merges.</p>
        </div>
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">03</span>
          <h3>API &amp; Backend Validation</h3>
          <p>Validating REST and GraphQL endpoints, authentication tokens, payload schemas, and database side effects in conjunction with UI flows.</p>
        </div>
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">04</span>
          <h3>Zero Vendor Lock-In</h3>
          <p>All automation test code lives in your own Git repository with full documentation, easy local debugging, and clean scripts.</p>
        </div>
      </div>
      <div style="text-align:center;margin-top:48px;">
        <a href="/free-audit?cta=automation_qa_bottom" class="btn btn-primary btn-lg">Request a Test Automation Audit &rarr;</a>
      </div>
    </div>
  </section>
</div>
'''
    },
    {
        "rel_path": "qa-testing-chandigarh/index.html",
        "title": "QA Testing Services in Chandigarh, Mohali & Panchkula | QAcover",
        "description": "Software QA testing company in Chandigarh tricity. Serving IT Park Chandigarh, Mohali, Panchkula & Zirakpur with senior manual QA, Playwright automation, and sprint testing.",
        "canonical": "https://qacover.com/qa-testing-chandigarh",
        "noindex": False,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">CHANDIGARH TRICITY QA PARTNER</span>
      <h1 class="cp-hero-title">QA Testing Services in <span class="highlight">Chandigarh, Mohali &amp; Panchkula</span></h1>
      <p class="cp-hero-desc">Direct, senior-level software QA testing for product startups, IT companies, and software agencies across Chandigarh IT Park, Mohali (QuarkCity, Sector 67/82), Panchkula, and Zirakpur. Manual exploratory QA, Playwright test automation, and sprint release clearance under strict NDA.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?cta=chandigarh_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
        <a href="https://wa.me/919872492649?text=Hi%20Sahil%2C%20I%20am%20looking%20for%20QA%20testing%20in%20Chandigarh%20Tricity" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;text-decoration:none;display:inline-flex;align-items:center;">Chat with Sahil on WhatsApp &rarr;</a>
      </div>
    </section>
  </div>
  <section style="padding:60px 0;background:#fff;">
    <div class="v1-section-container">
      <span class="cp-pill-badge">LOCAL TRICITY COVERAGE</span>
      <h2 class="v1-section-h2">Serving the entire Chandigarh IT corridor</h2>
      <p class="v1-section-sub">Whether your engineering team is based in IT Park, Mohali industrial phases, or Panchkula, we offer fast in-person kickoffs and seamless daily sprint integration.</p>
      <div class="v1-workflow-grid">
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">01</span>
          <h3>Chandigarh</h3>
          <p>Rajiv Gandhi Chandigarh Technology Park (IT Park), Industrial Area Phase 1 &amp; 2. In-person or Slack sprint sync with zero communication lag.</p>
        </div>
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">02</span>
          <h3>Mohali</h3>
          <p>Sector 67, 82, QuarkCity &amp; Industrial Area Phase 8/8B. Deep QA integration for SaaS scale-ups and web/mobile development agencies.</p>
        </div>
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">03</span>
          <h3>Panchkula</h3>
          <p>MDC Sector 5 and Industrial Area Phase 1 &amp; 2. Comprehensive regression testing, responsive web verification, and security checklists.</p>
        </div>
        <div class="v1-wf-card">
          <span class="v1-wf-step-badge">04</span>
          <h3>Zirakpur</h3>
          <p>VIP Road, PR7 Aerocity corridor, and emerging tech startups. End-to-end testing for web applications, APIs, and mobile apps.</p>
        </div>
      </div>
    </div>
  </section>
  <section style="padding:60px 0;background:#f8fafc;">
    <div class="v1-section-container">
      <span class="cp-pill-badge">SERVICES</span>
      <h2 class="v1-section-h2">What we deliver to Tricity product teams</h2>
      <p class="v1-section-sub">From pre-launch blitz testing to automated CI/CD release verification.</p>
      <div class="v1-feature-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:32px;">
        <div class="v1-wf-card" style="background:#fff;">
          <h3 style="color:#064e3b;font-size:18px;margin-bottom:8px;">Manual Exploratory QA</h3>
          <p>Real device testing across iPhones, Androids, macOS, and Windows. We discover nuanced UI breaks, edge-case race conditions, and business logic flaws.</p>
        </div>
        <div class="v1-wf-card" style="background:#fff;">
          <h3 style="color:#064e3b;font-size:18px;margin-bottom:8px;">Playwright &amp; Cypress Automation</h3>
          <p>Robust end-to-end regression suites integrated directly into your GitHub Actions or GitLab pipelines. Fast, reliable test runs on every pull request.</p>
        </div>
        <div class="v1-wf-card" style="background:#fff;">
          <h3 style="color:#064e3b;font-size:18px;margin-bottom:8px;">White-Label Agency QA</h3>
          <p>Local software agencies in Chandigarh &amp; Mohali partner with us to guarantee flawless client deliverables under strict white-label NDA.</p>
        </div>
        <div class="v1-wf-card" style="background:#fff;">
          <h3 style="color:#064e3b;font-size:18px;margin-bottom:8px;">Founder-Led Accountability</h3>
          <p>Led by Sahil Lohran. No junior body-shopping or remote middleman agency layers. Direct, transparent Slack/Teams communication every sprint.</p>
        </div>
      </div>
      <div style="text-align:center;margin-top:48px;">
        <a href="/free-audit?cta=chandigarh_bottom" class="btn btn-primary btn-lg">Request a Free Flow Audit (3-Day Turnaround) &rarr;</a>
      </div>
    </div>
  </section>
</div>
'''
    },
    {
        "rel_path": "how-it-works/index.html",
        "title": "How It Works | Fast Sprint QA Integration & NDA — QAcover",
        "description": "How QAcover integrates into your development sprints: NDA-first, Slack/Jira integration, real bug reproduction videos, and guaranteed 1-business-day response.",
        "canonical": "https://qacover.com/how-it-works",
        "noindex": False,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">COLLABORATION WORKFLOW</span>
      <h1 class="cp-hero-title">How We Integrate With Your <span class="highlight">Engineering Sprints</span></h1>
      <p class="cp-hero-desc">We plug into your issue tracker, test on authentic devices, and sign off on staging before you deploy to production.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?cta=hiw_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
      </div>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "white-label/index.html",
        "title": "White-Label QA for Agencies & Dev Shops — QAcover",
        "description": "Invisible, high-grade QA testing for software development agencies and design studios. We test your client deliverables under strict white-label NDA.",
        "canonical": "https://qacover.com/white-label",
        "noindex": False,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">FOR DEV SHOPS &amp; AGENCIES</span>
      <h1 class="cp-hero-title">White-Label QA for Agencies &amp; <span class="highlight">Dev Shops</span></h1>
      <p class="cp-hero-desc">Scale your agency's delivery velocity and release quality without adding full-time QA headcount. We test your client software under your brand &mdash; completely invisible to your clients.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?type=agency&cta=wl_hero" class="btn btn-primary btn-lg">Get a Free White-Label Audit &rarr;</a>
        <a href="mailto:hello@qacover.com?subject=Agency%20Partnership%20Inquiry" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;text-decoration:none;display:inline-flex;align-items:center;">Schedule Agency Intro</a>
      </div>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "about/index.html",
        "title": "About QAcover | Built by Sahil Lohran, Founder & Lead QA",
        "description": "QAcover is an independent software QA company founded by Sahil Lohran. Based in the Chandigarh tricity, serving Chandigarh, Mohali, Panchkula, Zirakpur, and teams worldwide.",
        "canonical": "https://qacover.com/about",
        "noindex": False,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">ABOUT QACOVER</span>
      <h1 class="cp-hero-title">Dedicated QA Engineering for <span class="highlight">High-Velocity Teams</span></h1>
      <p class="cp-hero-desc">Built by QA professionals to give modern software teams and development agencies world-class quality coverage without hiring overhead or release bottlenecks.</p>
    </section>
  </div>
  <div class="info-page-container">
    <div class="about-content-card">
      <div class="info-lead-text">
        We founded QAcover with a simple realization: modern product teams move lightning-fast, but QA is often an afterthought. Developers end up testing their own code, critical regressions reach paying customers, and sprint releases get delayed. QAcover bridges that gap seamlessly.
      </div>
      <div class="founder-quote-banner">
        <div class="founder-avatar-circle">SL</div>
        <div class="founder-quote-text">
          <h3 style="margin:0 0 4px 0;font-size:19px;color:#064e3b;">Sahil Lohran</h3>
          <span style="display:block;margin-bottom:8px;font-weight:650;color:#087a55;">Built by Sahil Lohran, founder and lead QA</span>
          <p>"Software quality isn't just about finding bugs before launch. It's about giving your engineering team the confidence to ship ambitious features without dreading Monday morning regression reports."</p>
        </div>
      </div>
      <div class="info-block">
        <h3><span class="block-icon">📍</span>Based in the Chandigarh Tricity</h3>
        <p>Based in the Chandigarh tricity, serving Chandigarh, Mohali, Panchkula and Zirakpur — working with high-velocity software teams worldwide. Headquartered in India (IST), we operate with consistent daily overlap hours for teams in the US (morning EST), UK/Europe (GMT/CET), Australia (AEST), and the Middle East. We reply within 1 business day (IST). Report within 3 business days of access.</p>
      </div>
      <div style="display:flex;gap:16px;flex-wrap:wrap;margin-top:32px;padding-top:24px;border-top:1px solid #e2e8f0;">
        <a href="/free-audit?cta=about" class="btn btn-primary btn-lg">Get a free flow audit &rarr;</a>
        <a href="/services" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Explore QA Services &rarr;</a>
      </div>
    </div>
  </div>
</div>
'''
    },
    {
        "rel_path": "free-audit/index.html",
        "title": "Get a Free Flow Audit | 4-Field QA Assessment — QAcover",
        "description": "Get a free exploratory QA audit of one key user flow on your app or web platform. Prioritized bug report delivered within 3 business days under NDA.",
        "canonical": "https://qacover.com/free-audit",
        "noindex": False,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">FREE FLOW AUDIT</span>
      <h1 class="cp-hero-title">Get a Free Audit of Your <span class="highlight">Key User Flow</span></h1>
      <p class="cp-hero-desc">We test one core journey (checkout, onboarding, auth, or billing) on real devices and send back a prioritized defect report in 3 business days.</p>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "thank-you/index.html",
        "title": "Audit Request Received | QAcover",
        "description": "Thank you for requesting a free flow audit with QAcover. We reply within 1 business day (IST).",
        "canonical": "https://qacover.com/thank-you",
        "noindex": True,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">REQUEST RECEIVED</span>
      <h1 class="cp-hero-title">Audit Request <span class="highlight">Confirmed!</span></h1>
      <p class="cp-hero-desc">Thank you for trusting QAcover. Sahil has received your request and will personally review it.</p>
    </section>
  </div>
  <div class="info-page-container">
    <div class="privacy-content-card" style="text-align:center;max-width:680px;margin:0 auto;">
      <div style="font-size:48px;margin-bottom:16px;">🎉</div>
      <h2 style="font-size:24px;font-weight:650;color:#064e3b;margin-bottom:12px;">What Happens Next?</h2>
      <p style="font-size:15.5px;color:#334155;line-height:1.65;margin-bottom:24px;">We reply within 1 business day (IST). Report within 3 business days of access. We will review your application link and reach out via email to execute our Mutual NDA and receive test logins.</p>
      <div style="display:flex;justify-content:center;gap:16px;flex-wrap:wrap;">
        <a href="/" class="btn btn-primary">Return to Homepage &rarr;</a>
        <a href="https://wa.me/919872492649?text=Hi%20QAcover%2C%20I%20just%20submitted%20a%20flow%20audit" target="_blank" rel="noopener noreferrer" class="btn btn-secondary" style="background:#fff;border-color:#cbd5e1;text-decoration:none;display:inline-flex;align-items:center;">Chat with Sahil on WhatsApp &rarr;</a>
      </div>
    </div>
  </div>
</div>
'''
    },
    {
        "rel_path": "privacy/index.html",
        "title": "Privacy Policy & Data Security — QAcover",
        "description": "QAcover privacy policy: Mutual NDA protection, client intellectual property ownership, zero data retention, and third-party transparency.",
        "canonical": "https://qacover.com/privacy",
        "noindex": False,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">LEGAL &amp; PRIVACY</span>
      <h1 class="cp-hero-title">Privacy Policy &amp; <span class="highlight">Data Protection</span></h1>
      <p class="cp-hero-desc">How QAcover protects your intellectual property, staging environments, test accounts, and confidential data.</p>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "404.html",
        "title": "Page Not Found (404) | QAcover",
        "description": "The page you requested could not be found. Return to QAcover homepage or request a free flow audit.",
        "canonical": "https://qacover.com/404",
        "noindex": True,
        "content_html": '''
<div class="contact-page">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">404 ERROR</span>
      <h1 class="cp-hero-title">Page <span class="highlight">Not Found</span></h1>
      <p class="cp-hero-desc">The page you requested could not be found or has moved. Return to the homepage or explore our QA services below.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/" class="btn btn-primary btn-lg">Return to Homepage &rarr;</a>
        <a href="/free-audit" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Get a Free Flow Audit &rarr;</a>
      </div>
    </section>
  </div>
</div>
'''
    }
]

def render_page(page):
    robots_content = "noindex, nofollow" if page["noindex"] else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    
    html = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
    <!-- Primary SEO Meta Tags -->
    <title>{page["title"]}</title>
    <meta name="title" content="{page["title"]}" />
    <meta name="description" content="{page["description"]}" />
    <meta name="robots" content="{robots_content}" />
    <meta name="author" content="QAcover" />
    <link rel="canonical" href="{page["canonical"]}" />

    <!-- Open Graph / Facebook / LinkedIn Meta Tags -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{page["canonical"]}" />
    <meta property="og:site_name" content="QAcover" />
    <meta property="og:title" content="{page["title"]}" />
    <meta property="og:description" content="{page["description"]}" />
    <meta property="og:image" content="https://qacover.com/images/hero-character.webp" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:locale" content="en_IN" />

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:url" content="{page["canonical"]}" />
    <meta name="twitter:title" content="{page["title"]}" />
    <meta name="twitter:description" content="{page["description"]}" />
    <meta name="twitter:image" content="https://qacover.com/images/hero-character.webp" />

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="alternate icon" type="image/png" href="/images/logo-dark.png">

    <!-- Structured Data / JSON-LD for Google & Search Engines -->
    <script type="application/ld+json">
{JSON_LD_STR}
    </script>
    <script type="module" crossorigin src="/assets/index-FpVXcGDL.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-BTfoWXnZ.css">
  </head>
  <body>
    <div id="root">
      <div class="app-container">
        {NAVBAR_HTML}
        {page["content_html"]}
        {FOOTER_HTML}
      </div>
    </div>
  </body>
</html>
'''
    return html

def main():
    print(f"Starting prerender process for {len(PAGES)} pages...")
    for p in PAGES:
        target_path = os.path.join(BASE_DIR, p["rel_path"])
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        content = render_page(p)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Prerendered: {p['rel_path']} -> {target_path}")

    print("All pages prerendered successfully!")

if __name__ == "__main__":
    main()

