# AI-Powered Travel Planner & Itinerary Builder

A Flask-based travel planning API that generates complete itineraries using AI, Wikipedia-based retrieval (RAG), and a zero-shot decision agent.

This project takes a destination, number of days, user interests, and optional budget — and returns a structured, realistic, day-wise trip plan with real attractions, unique activities, budget estimation, and editing options through multiple API endpoints.

---

## Features

- Retrieval-Augmented Generation (RAG) using Wikipedia Search + Page Summary API  
- AI-generated summaries of attractions using BART (facebook/bart-large-cnn)  
- Zero-shot trip-style classification using BART MNLI  
- Automatic generation of day-wise itineraries with varied activities  
- Shareable text summary of the complete trip  
- INR-based budget estimation  
- Endpoints to add, update, remove, and view itinerary items  
- Lightweight and framework-independent backend (Flask + Python)

---

## Tech Stack

**Backend:** Flask  
**AI Models:** HuggingFace Transformers (BART CNN for summarization, BART MNLI for mode classification)  
**Retrieval:** Wikipedia REST & Search API  
**Storage:** In-memory dictionary  
**Language:** Python  

---

## How It Works

### 1. Retrieval-Augmented Generation (RAG)
The system performs multiple Wikipedia searches such as:  
- “Top attractions in <destination>”  
- “Places to visit in <destination>”  
- “<interest> in <destination>”  

It collects page titles, filters out non-POI pages, fetches summaries, and generates a short refined summary for each attraction using BART.

These attractions become anchor points inside the daily itinerary.

### 2. Zero-Shot Decision Agent
The agent classifies the trip mode into:
- budget-friendly  
- adventure  
- luxury  

The model uses trip details (days, interests, budget input) to infer the best travel style.

### 3. Itinerary Generation
Each day includes:
- 1 real attraction from RAG  
- 3 unique activities selected from curated activity pools  
- Mode-responsive and interest-aligned choices  
- No repetition across days  

### 4. Budget Estimation (INR)
Includes:
- Lodging cost  
- Meals  
- Activities  
- Optional flights  

Prices scale with the mode selected by the agent.

---
