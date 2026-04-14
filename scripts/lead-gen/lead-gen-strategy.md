# AI Lead Generation Setup: Capital Cabinetry & Assembly

## Goal: Automate lead monitoring on Kijiji, Marketplace, and Craigslist with human-in-the-loop responses.

### 1. The Strategy: "The Bilingual Listener"
We want the AI to "listen" for high-intent keywords and draft a response that sounds professional but personal. We focus on **Urgency** and **Bilingual Expertise**.

---

### 2. Key Phrases to Monitor (English & French)
- **High Intent:** "IKEA assembly", "TV wall mount", "kitchen cabinets", "need handyman", "broken cabinet", "flat pack assembly", "Wayfair desk".
- **French Equivalents:** "Assemblage IKEA", "Fixation murale TV", "Armoires de cuisine", "Besoin d'un bricoleur", "Meubles en kit".
- **Urgent Keywords:** "Today", "Moving", "Help", "Emergency", "ASAP", "Urgent", "Aujourd'hui", "Déménagement".

---

### 3. OpenClaw / Claude API Prompt for Drafting
When a lead is found, use this prompt to generate a draft response for your review:

**Prompt:**
> You are the business manager for **Capital Cabinetry & Assembly / Ébénisterie et Assemblage de la Capitale**. 
>
> **Task:** Draft a short, professional, and friendly response to the following job posting.
>
> **Job Posting:** [INSERT LEAD TEXT HERE]
>
> **Guidelines:**
> 1. Start with a friendly greeting in the language of the post (English or French).
> 2. Mention that we are a bilingual local service in the Ottawa/Gatineau area.
> 3. Highlight that we have professional tools and specialize in [MATCH SERVICE: e.g., IKEA assembly, TV mounting, Cabinetry].
> 4. Mention that we offer **free quotes** and are available for **cash jobs** if the customer prefers.
> 5. End with a Call to Action: "I can help you today or tomorrow. Text me at 819-592-3372 for a quick quote!"
> 6. Keep the tone human-to-human. No corporate-speak.

---

### 4. Implementation Steps (For User)
1. **Launch OpenClaw:** Open your local instance.
2. **Set Scraping URL:** Aim at `https://www.kijiji.ca/b-skilled-trades/ottawa-gatineau-area/` or similar Marketplace/Craigslist search results.
3. **Filter Keywords:** Use the list provided in Section 2.
4. **Output to Claude:** Send the scraped description to Claude using the prompt in Section 3.
5. **Review & Send:** Once Claude gives you the draft, copy-paste it into the platform's messaging system.

---

### 5. Priority Lead Filtering (Logic)
- **Level A (High Priority):** "Moving today", "TV mounting", "IKEA Kitchen". These are high-cash, quick-turnaround jobs.
- **Level B:** "General furniture assembly", "Floating shelves".
- **Level C:** "Custom cabinet build from scratch". (High value, but long lead time).
