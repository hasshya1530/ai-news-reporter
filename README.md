# 📰 AI News Reporter

A multi-agent AI news reporting application built with **CrewAI, Google Gemma 4, Streamlit, and a free AI/technology news API**.

The application retrieves current AI and technology news, prepares a source-grounded research brief, and transforms the research into a structured article.

## 🚀 Live Demo

🌐 **Streamlit App:**  
https://ai-news-reporter.streamlit.app/

💻 **GitHub Repository:**  
https://github.com/hasshya1530/ai-news-reporter

---

## 📌 About This Project

This project is part of my practical implementation journey while learning from the Udemy course:

**Building Gen AI App 12+ Hands-on Projects with Gemini Pro**

by **Krish Naik**.

The course project and original repository provided the learning foundation for this application. I rebuilt the project as a working application, adapted it to the current Google GenAI SDK and **Gemma 4**, and extended it with additional functionality.

My goal with this project was not just to follow the tutorial, but to:

> **Learn → Build → Extend → Deploy**

The implementation includes a Streamlit interface, dynamic user inputs, source-grounded research, article customization, Markdown export, and a deployment on Streamlit Community Cloud.

### 🙏 Credits & Attribution

A special thanks to **Krish Naik** for the course and the original project implementation that served as the learning foundation for this project.

**Course:**  
[Building Gen AI App 12+ Hands-on Projects with Gemini Pro](https://tcsrecruits.udemy.com/course/building-gen-ai-app-end-to-end-projects-with-gemini-pro/)

**Instructor:**  
**Krish Naik**

**Original Repository:**  
https://github.com/krishnaik06/Build-Gen-AI-With-Google-Gemini

The original course and repository are credited as the source of the project concept and learning material. This repository contains my own implementation, adaptations, debugging, configuration changes, UI development, model integration changes, and additional features.

All original course materials and source code remain the property of their respective author.

---

# ✨ Features

### 🔎 Current News Retrieval

The application retrieves current AI and technology articles using a public news API.

Retrieved information includes:

- Article title
- Source
- Category
- Date
- Summary
- Original article URL

---

### 🤖 Multi-Agent Architecture

The application uses two CrewAI agents.

#### 1. Senior AI News Researcher

Responsible for:

- Reviewing retrieved articles
- Identifying relevant sources
- Extracting factual information
- Preparing a structured research brief
- Preserving source attribution

#### 2. AI Technology News Writer

Responsible for:

- Transforming the research brief into an article
- Maintaining source attribution
- Following the selected writing style
- Avoiding unsupported claims

---

## 📝 Article Styles

Users can choose between:

### News Report

A concise, factual, journalistic format focused on reported developments.

### Research Brief

A structured format focused on:

- Sources
- Findings
- Key facts
- Organizations
- Technologies
- Potential implications

### Explainer

An accessible format designed to explain reported developments clearly.

---

## 📏 Article Length

Users can select:

| Option | Target Length |
|---|---:|
| Short | ~400–600 words |
| Medium | ~700–900 words |
| Detailed | ~1000–1300 words |

---

# 🔬 Research Transparency

The application displays the retrieved research before generating the final article.

This creates the following workflow:

```text
Retrieved Sources
        ↓
Research Findings
        ↓
Researcher Agent
        ↓
Research Brief
        ↓
Writer Agent
        ↓
Final Article
