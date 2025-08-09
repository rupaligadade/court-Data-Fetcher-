A small web app to fetch, parse and display Indian court case metadata and latest orders/judgments.

Features:

Simple UI to enter Case Type, Case Number, and Filing Year
Backend scraper that fetches case page(s), parses:
Parties’ names
Filing date & next-hearing dates
Order/judgment PDF links (shows latest)
Stores each query + raw response in SQLite.

Tech stack (suggested / reference implementation):

Backend: Python + Flask (or FastAPI)
Scraping / Navigation: Playwright (headless browser) or Requests + BeautifulSoup where possible
DB: SQLite (simple, file-based)
Frontend: Lightweight HTML + Bootstrap / Tailwind (simple form + results table)
Container: Optional Dockerfile for reproducible runs
You may adapt to Node/Express, Go, etc. — any stack is acceptable.
