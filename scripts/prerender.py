import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Shared Schema.org JSON-LD
LOCAL_BUSINESS_DATA = {
  "@type": "LocalBusiness",
  "@id": "https://qacover.com/#localbusiness",
  "name": "QAcover",
  "alternateName": ["QAcover Software QA", "QAcover Chandigarh QA", "QAcover Testing Services"],
  "url": "https://qacover.com",
  "logo": "https://qacover.com/images/logo-dark.webp",
  "image": "https://qacover.com/images/og-image.png",
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
    { "@type": "City", "name": "Chandigarh" },
    { "@type": "City", "name": "Mohali" },
    { "@type": "City", "name": "Panchkula" },
    { "@type": "City", "name": "Zirakpur" }
  ],
  "description": "QAcover is an independent software QA company based in Chandigarh tricity, serving Chandigarh, Mohali, Panchkula, and Zirakpur as well as global engineering teams with manual exploratory testing, Playwright/Cypress test automation, and white-label QA under NDA."
}

PROFESSIONAL_SERVICE_DATA = {
  "@type": "ProfessionalService",
  "@id": "https://qacover.com/#service",
  "name": "QAcover — Software QA Testing & Test Automation Services",
  "url": "https://qacover.com",
  "provider": { "@id": "https://qacover.com/#localbusiness" },
  "serviceType": [
    "Manual QA Testing",
    "Exploratory Testing",
    "Test Automation Services",
    "Playwright Automation",
    "Cypress Automation",
    "Mobile App Testing",
    "API & Backend Validation",
    "White-Label QA for Agencies"
  ],
  "areaServed": ["Chandigarh", "Mohali", "Panchkula", "Zirakpur", "Worldwide"]
}

FAQ_DATA = {
  "@type": "FAQPage",
  "@id": "https://qacover.com/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does the free flow audit work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You submit one key user flow on your app or web platform (e.g. auth, checkout, or onboarding). We execute exploratory testing across physical devices and send you a prioritized defect report with video proof and reproduction steps within 3 business days under mutual NDA."
      }
    },
    {
      "@type": "Question",
      "name": "Do you sign a Mutual NDA before accessing our app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, always. We execute a bilateral Mutual Non-Disclosure Agreement (NDA) before receiving test credentials, repo access, or staging URLs. Your code, client data, and IP remain 100% yours."
      }
    },
    {
      "@type": "Question",
      "name": "What test automation frameworks do you specialize in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We build fast, stable, and maintainable end-to-end automation in Playwright and Cypress with TypeScript or Python, integrated directly into your GitHub Actions, GitLab CI, or CircleCI pipelines."
      }
    },
    {
      "@type": "Question",
      "name": "How do you collaborate with our sprint team?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We integrate directly into your daily workflow on Slack, Linear, or Jira. We operate with daily IST overlap hours covering US morning EST, UK/Europe GMT/CET, and APAC timezones with 1 business day response SLAs."
      }
    },
    {
      "@type": "Question",
      "name": "Do you offer white-label QA for development agencies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Dev shops, SaaS studios, and product agencies partner with QAcover to deliver spotless releases to their clients under strict white-label confidentiality."
      }
    }
  ]
}

def get_breadcrumbs(canonical_url, title):
    path = canonical_url.replace("https://qacover.com", "").strip("/")
    items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://qacover.com/"
        }
    ]
    if path:
        parts = path.split("/")
        curr = "https://qacover.com"
        for idx, part in enumerate(parts):
            curr += f"/{part}"
            readable = part.replace("-", " ").title()
            items.append({
                "@type": "ListItem",
                "position": idx + 2,
                "name": readable if idx < len(parts) - 1 else title.split("|")[0].split("—")[0].strip(),
                "item": curr
            })
    return {
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

NAVBAR_HTML = '''
<nav class="navbar" id="navbar">
  <div class="container">
    <div class="navbar-inner">
      <a href="/" class="navbar-logo">
        <img src="/images/logo-dark.webp" alt="QAcover" class="navbar-logo-img" style="height: 38px; width: auto; display: block;" />
      </a>
      <div class="navbar-menu">
        <a href="/" class="active">Home</a>
        <a href="/services">Services</a>
        <a href="/how-it-works">How it works</a>
        <a href="/white-label">White-label</a>
        <a href="/about">About</a>
        <a href="mailto:hello@qacover.com?subject=Book%20a%2020-min%20QA%20Strategy%20Call" class="mobile-email-link">Email us to book a 20-min call</a>
        <a href="/free-audit?cta=nav_mobile" class="btn btn-primary btn-sm mobile-menu-cta">Get a free flow audit &rarr;</a>
      </div>
      <div class="navbar-cta">
        <a href="mailto:hello@qacover.com?subject=Book%20a%2020-min%20QA%20Strategy%20Call" class="navbar-cta-email">Email us to book a 20-min call</a>
        <a href="/free-audit?cta=nav" class="btn btn-primary btn-sm" style="padding: 8px 18px; font-size: 13.5px; text-decoration: none;">Get a free flow audit &rarr;</a>
      </div>
      <button class="mobile-toggle" aria-label="Toggle menu">
        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="4" y1="6" x2="20" y2="6"></line><line x1="4" y1="12" x2="20" y2="12"></line><line x1="4" y1="18" x2="20" y2="18"></line></svg>
      </button>
    </div>
  </div>
</nav>
'''

FOOTER_HTML = '''
<footer class="v1-footer-v2">
  <div class="v1-section-container">
    <div class="v1-footer-grid">
      <div class="v1-footer-brand">
        <a href="/" style="display:inline-block;text-decoration:none;margin-bottom:12px;">
          <img src="/images/logo-dark.webp" alt="QAcover" style="height:34px;width:auto;display:block;" />
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
          <li><a href="/services/playwright-testing">Playwright Automation</a></li>
          <li><a href="/services/mobile-app-testing">Mobile App QA</a></li>
          <li><a href="/services/api-testing">API &amp; Backend Testing</a></li>
          <li><a href="/white-label">White-Label QA</a></li>
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
        <div class="footer-social-row">
          <a href="https://wa.me/919872492649?text=Hi%20QAcover%2C%20I%20have%20a%20QA%20question" target="_blank" rel="noopener noreferrer" class="footer-social-icon" aria-label="WhatsApp" title="WhatsApp: +91 98724 92649">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.23 8.23 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.19 8.19 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.25-.13-1.47-.72-1.7-.81-.23-.08-.39-.13-.56.13-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.13-1.06-.39-2.02-1.25-.75-.67-1.26-1.5-1.4-1.75-.15-.25-.02-.39.11-.51.11-.11.25-.29.38-.44.13-.15.17-.25.25-.42.08-.17.04-.32-.02-.44-.06-.13-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43h-.48c-.17 0-.44.06-.67.32-.23.25-.88.86-.88 2.1 0 1.24.9 2.44 1.03 2.61.13.17 1.78 2.72 4.31 3.81.6.26 1.07.42 1.44.54.61.19 1.16.17 1.6.1.49-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.15-1.18-.06-.1-.23-.17-.48-.29z"/></svg>
          </a>
          <a href="https://www.linkedin.com/company/qacoverr/?viewAsMember=true" target="_blank" rel="noopener noreferrer" class="footer-social-icon" aria-label="LinkedIn" title="QAcover on LinkedIn">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 8.76a1.64 1.64 0 1 0 0-3.28 1.64 1.64 0 0 0 0 3.28m1.39 9.74v-8.37H5.07v8.37h2.78z"/></svg>
          </a>
          <a href="mailto:hello@qacover.com" class="footer-social-icon" aria-label="Email" title="Email: hello@qacover.com">
            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
          </a>
        </div>
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

CRITICAL_CSS = '''
<style>
/* Instant First-Paint Layout - Prevents unstyled flash */
body {
  margin: 0;
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: #f8fafc;
  color: #0f172a;
  -webkit-font-smoothing: antialiased;
}
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 72px;
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid #e2e8f0;
  z-index: 1000;
  display: flex;
  align-items: center;
}
.navbar .container {
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 24px;
}
.navbar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}
.navbar-logo {
  display: flex;
  align-items: center;
  text-decoration: none;
}
.navbar-logo-img {
  height: 38px;
  width: auto;
  display: block;
}
.navbar-menu {
  display: flex;
  align-items: center;
  gap: 28px;
}
.navbar-menu a {
  font-size: 14.5px;
  font-weight: 600;
  color: #334155;
  text-decoration: none;
}
.navbar-cta {
  display: flex;
  align-items: center;
  gap: 14px;
}
.mobile-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px;
  color: #0f172a;
}
.mobile-email-link {
  display: none;
}
@media (max-width: 768px) {
  .navbar-menu, .navbar-cta {
    display: none !important;
  }
  .mobile-toggle {
    display: flex !important;
  }
  .navbar-logo-img {
    height: 36px !important;
  }
}
</style>
'''

PAGES = [
    {
        "rel_path": "index.html",
        "title": "QAcover — Software QA Testing & Test Automation for Startups",
        "description": "QAcover provides manual exploratory testing, test automation (Playwright/Cypress), and white-label QA. Based in the Chandigarh tricity, serving Chandigarh, Mohali, Panchkula and Zirakpur — working with product teams worldwide. Start with a free flow audit under NDA.",
        "canonical": "https://qacover.com/",
        "noindex": False,
        "is_home": True,
        "content_html": '''
<div class="hero-wrapper" style="padding-top: 100px;">
  <section class="hero" id="hero">
    <div class="hero-container hero-container-centered">
      <div class="hero-content">
        <span class="cp-pill-badge" style="margin-bottom: 22px;">MANUAL + AUTOMATION QA FOR PRODUCT TEAMS AND AGENCIES</span>
        <h1 class="cp-hero-title" style="font-size: clamp(38px, 5.8vw, 68px); font-weight: 650; letter-spacing: -0.03em; color: #0f172a; margin: 0 auto 24px auto; max-width: 920px; line-height: 1.12;">
          Ship <span class="highlight" style="color: #087a55;">releases</span> your users<br />don't have to test for you.
        </h1>
        <p class="cp-hero-desc" style="max-width: 840px; margin: 0 auto 30px auto; font-size: 19px; line-height: 1.68; color: #475569;">
          Manual exploratory testing, Playwright &amp; Cypress test automation, and white-label QA for product teams and agencies. Based in the Chandigarh tricity, serving Chandigarh, Mohali, Panchkula, and Zirakpur &bull; working with engineering teams worldwide under strict mutual NDA.
        </p>
        <div class="hero-buttons hero-buttons-centered" style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
          <a href="/free-audit?cta=home_hero" class="btn btn-primary btn-lg">Get a free flow audit &rarr;</a>
          <a href="/services" class="btn btn-secondary btn-lg" style="background: #fff; border-color: #cbd5e1;">Explore QA Services &rarr;</a>
        </div>
      </div>
    </div>
  </section>
</div>
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
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">COMPREHENSIVE QA OFFERINGS</span>
      <h1 class="cp-hero-title">Full-Spectrum Software <span class="highlight">QA &amp; Testing Services</span></h1>
      <p class="cp-hero-desc">From human exploratory bug hunts to automated Playwright CI/CD release gates and white-label agency testing.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/services/manual-qa" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Manual QA &rarr;</a>
        <a href="/services/automation-qa" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Automation QA &rarr;</a>
        <a href="/services/playwright-testing" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Playwright &rarr;</a>
        <a href="/services/mobile-app-testing" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Mobile App QA &rarr;</a>
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
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
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
</div>
'''
    },
    {
        "rel_path": "services/automation-qa/index.html",
        "title": "Test Automation Services | Playwright, Cypress & CI/CD — QAcover",
        "description": "End-to-end automated test suites built in Playwright and Cypress. Integrated directly into GitHub Actions, GitLab, and CI/CD pipelines for zero regression leaks.",
        "canonical": "https://qacover.com/services/automation-qa",
        "noindex": False,
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">TEST AUTOMATION</span>
      <h1 class="cp-hero-title">End-to-End Test Automation with <span class="highlight">Playwright &amp; Cypress</span></h1>
      <p class="cp-hero-desc">Fast, stable, maintainable test automation suites integrated into your CI/CD pipelines. Eliminate regression leaks and ship pull requests with complete confidence.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?cta=automation_qa_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
        <a href="/services/playwright-testing" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Playwright Focus &rarr;</a>
      </div>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "services/playwright-testing/index.html",
        "title": "Playwright Test Automation Services | CI/CD E2E QA — QAcover",
        "description": "Specialized Playwright test automation services for modern web applications. TypeScript test suites, auto-waiting, parallel CI/CD runs, and zero flakiness.",
        "canonical": "https://qacover.com/services/playwright-testing",
        "noindex": False,
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">PLAYWRIGHT AUTOMATION SPECIALISTS</span>
      <h1 class="cp-hero-title">Playwright Test Automation for <span class="highlight">Modern Web Apps</span></h1>
      <p class="cp-hero-desc">Fast, stable, and auto-waiting end-to-end regression suites built in TypeScript. We engineer maintainable Playwright frameworks directly in your repo with parallel CI/CD execution.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?cta=playwright_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
        <a href="/services/automation-qa" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">Test Automation &rarr;</a>
      </div>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "services/mobile-app-testing/index.html",
        "title": "Mobile App QA Testing Services | iOS & Android Real Devices — QAcover",
        "description": "Professional mobile application testing for iOS and Android on real physical devices. Exploratory bug hunts, push notifications, offline states, and OS matrix.",
        "canonical": "https://qacover.com/services/mobile-app-testing",
        "noindex": False,
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">REAL DEVICE TESTING</span>
      <h1 class="cp-hero-title">Mobile App QA Testing for <span class="highlight">iOS &amp; Android</span></h1>
      <p class="cp-hero-desc">Exhaustive manual and automated testing on authentic smartphones and tablets. We catch battery drain, background state losses, notification breaks, and device fragmentation flaws before your app hits the App Store or Google Play.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?cta=mobile_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
        <a href="/services" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">All QA Services &rarr;</a>
      </div>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "services/api-testing/index.html",
        "title": "API & Backend QA Testing Services | REST, GraphQL & Microservices — QAcover",
        "description": "Validate REST and GraphQL endpoints, authentication security, schema integrity, payload validation, and database state persistence under high concurrency.",
        "canonical": "https://qacover.com/services/api-testing",
        "noindex": False,
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">BACKEND &amp; API TESTING</span>
      <h1 class="cp-hero-title">API &amp; Backend QA Testing for <span class="highlight">REST &amp; GraphQL</span></h1>
      <p class="cp-hero-desc">Validate your core business logic at the data layer. We stress test endpoints, inspect authentication tokens, verify schema contracts, and guarantee zero regressions across microservices.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?cta=api_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
        <a href="/services" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;">All QA Services &rarr;</a>
      </div>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "qa-testing-chandigarh/index.html",
        "title": "QA Testing Services in Chandigarh, Mohali & Panchkula | QAcover",
        "description": "Software QA testing company in Chandigarh tricity. Serving IT Park Chandigarh, Mohali, Panchkula & Zirakpur with senior manual QA, Playwright automation, and sprint testing.",
        "canonical": "https://qacover.com/qa-testing-chandigarh",
        "noindex": False,
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">CHANDIGARH TRICITY QA PARTNER</span>
      <h1 class="cp-hero-title">QA Testing Services in <span class="highlight">Chandigarh, Mohali &amp; Panchkula</span></h1>
      <p class="cp-hero-desc">Direct, senior-level software QA testing for product startups, IT companies, and software agencies across Chandigarh IT Park, Mohali (QuarkCity, Sector 67/82), Panchkula, and Zirakpur. Manual exploratory QA, Playwright test automation, and sprint release clearance under strict NDA.</p>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:24px;flex-wrap:wrap;">
        <a href="/free-audit?cta=chandigarh_hero" class="btn btn-primary btn-lg">Get a Free Flow Audit &rarr;</a>
        <a href="https://wa.me/919872492649?text=Hi%20QAcover%2C%20I%20am%20looking%20for%20QA%20testing%20in%20Chandigarh%20Tricity" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-lg" style="background:#fff;border-color:#cbd5e1;text-decoration:none;display:inline-flex;align-items:center;">Chat on WhatsApp &rarr;</a>
      </div>
    </section>
  </div>
</div>
'''
    },
    {
        "rel_path": "how-it-works/index.html",
        "title": "How It Works | Fast Sprint QA Integration & NDA — QAcover",
        "description": "How QAcover integrates into your development sprints: NDA-first, Slack/Jira integration, real bug reproduction videos, and guaranteed 1-business-day response.",
        "canonical": "https://qacover.com/how-it-works",
        "noindex": False,
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
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
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
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
        "title": "About QAcover | Independent Software QA & Quality Engineering",
        "description": "QAcover is an independent software QA company based in the Chandigarh tricity, serving product teams and agencies worldwide with dedicated manual and automated testing.",
        "canonical": "https://qacover.com/about",
        "noindex": False,
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
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
        <div class="founder-avatar-circle">QA</div>
        <div class="founder-quote-text">
          <h3 style="margin:0 0 4px 0;font-size:19px;color:#064e3b;">Engineering-Grade Quality</h3>
          <span style="display:block;margin-bottom:8px;font-weight:650;color:#087a55;">Dedicated QA specialists embedded directly in your sprints</span>
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
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
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
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
  <div class="container-lg">
    <section class="contact-hero">
      <span class="cp-pill-badge">REQUEST RECEIVED</span>
      <h1 class="cp-hero-title">Audit Request <span class="highlight">Confirmed!</span></h1>
      <p class="cp-hero-desc">Thank you for trusting QAcover. Our QA team has received your request and will review your flow.</p>
    </section>
  </div>
  <div class="info-page-container">
    <div class="privacy-content-card" style="text-align:center;max-width:680px;margin:0 auto;">
      <div style="font-size:48px;margin-bottom:16px;">🎉</div>
      <h2 style="font-size:24px;font-weight:650;color:#064e3b;margin-bottom:12px;">What Happens Next?</h2>
      <p style="font-size:15.5px;color:#334155;line-height:1.65;margin-bottom:24px;">We reply within 1 business day (IST). Report within 3 business days of access. We will review your application link and reach out via email to execute our Mutual NDA and receive test logins.</p>
      <div style="display:flex;justify-content:center;gap:16px;flex-wrap:wrap;">
        <a href="/" class="btn btn-primary">Return to Homepage &rarr;</a>
        <a href="https://wa.me/919872492649?text=Hi%20QAcover%2C%20I%20just%20submitted%20a%20flow%20audit" target="_blank" rel="noopener noreferrer" class="btn btn-secondary" style="background:#fff;border-color:#cbd5e1;text-decoration:none;display:inline-flex;align-items:center;">Chat with us on WhatsApp &rarr;</a>
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
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
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
        "is_home": False,
        "content_html": '''
<div class="contact-page" style="padding-top: 100px;">
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
    
    # Build schema graph
    schema_graph = [LOCAL_BUSINESS_DATA, PROFESSIONAL_SERVICE_DATA]
    
    # Add FAQPage schema for home page
    if page.get("is_home"):
        schema_graph.append(FAQ_DATA)
        
    # Add BreadcrumbList schema
    schema_graph.append(get_breadcrumbs(page["canonical"], page["title"]))
    
    schema_full = {
        "@context": "https://schema.org",
        "@graph": schema_graph
    }
    schema_str = json.dumps(schema_full, indent=2)

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
    <meta property="og:image" content="https://qacover.com/images/og-image.png" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:locale" content="en_IN" />

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:url" content="{page["canonical"]}" />
    <meta name="twitter:title" content="{page["title"]}" />
    <meta name="twitter:description" content="{page["description"]}" />
    <meta name="twitter:image" content="https://qacover.com/images/og-image.png" />

    <!-- Preload & Load Main Stylesheet Immediately at Head Top -->
    <link rel="preload" href="/assets/index-D1a0e91f.css" as="style" />
    <link rel="stylesheet" crossorigin href="/assets/index-D1a0e91f.css" />

    {CRITICAL_CSS}

    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />

    <!-- Structured Data / JSON-LD for Google & Search Engines (LocalBusiness, Breadcrumbs, FAQs) -->
    <script type="application/ld+json">
{schema_str}
    </script>
    <script type="module" crossorigin src="/assets/index-E2b1f02a.js"></script>
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

    print("All pages prerendered successfully with FAQPage & BreadcrumbList Schemas!")

if __name__ == "__main__":
    main()
