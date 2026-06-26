# AIML - AI/ML Assistants and Agents Portfolio

Welcome to the **AIML** repository! This is a comprehensive collection of 25 AI-powered helper scripts, web interfaces, and intelligent agents built using LangChain, Google GenAI, Groq, Gradio, and RAG architectures.

## Portfolio Directory

The repository is organized into distinct subdirectories, each representing a complete, self-contained project:

### 1. Core AI Assistants (Google GenAI SDK)
*   [Language_Translator_Assistant](./Language_Translator_Assistant): Standard text translator.
*   [Question_Generator_Assistant](./Question_Generator_Assistant): Question generator helper.
*   [Study_Assistant](./Study_Assistant): Academic study guide companion.
*   [Tone_Modifier](./Tone_Modifier): Formal rewriter.

### 2. Configurable System Instruction Assistants
*   [Multi_Language_Translator_Assistant](./Multi_Language_Translator_Assistant): Multi-language translator (Hindi, Telugu, French) using custom system configs.
*   [Multi_Type_Question_Generator_Assistant](./Multi_Type_Question_Generator_Assistant): Question generator supporting MCQs, Short Answers, and Interview styles.
*   [Persona_Based_Study_Assistant](./Persona_Based_Study_Assistant): Conversational study helper with Friendly and Academic personas.
*   [Persona_Based_Tone_Modifier_Assistant](./Persona_Based_Tone_Modifier_Assistant): Conversational rewriter supporting Formal and Casual tones.

### 3. Interactive Web Apps (Gradio & Gemini)
*   [Interactive_Language_Translator](./Interactive_Language_Translator): Translator UI.
*   [Interactive_Question_Generator](./Interactive_Question_Generator): Question generator UI.
*   [Interactive_Study_Assistant](./Interactive_Study_Assistant): Persona-based study guide UI.
*   [Interactive_Tone_Translator](./Interactive_Tone_Translator): Multi-tone modifier UI.

### 4. Tool Calling (Function Calling)
*   [Weather_Assistant_With_Tool_Calling](./Weather_Assistant_With_Tool_Calling): Uses Groq and OpenWeatherMap API to answer weather queries dynamically.
*   [Currency_Converter_with_Tool_Calling](./Currency_Converter_with_Tool_Calling): Uses Gemini and ExchangeRate-API to convert currencies with live data.

### 5. LangChain Chat Models
*   [Travel_Guide_Assistant](./Travel_Guide_Assistant): Travel planner utilizing LangChain's dynamic chat model wrapper and Google GenAI.
*   [Python_Tutor_Assistant](./Python_Tutor_Assistant): Python programming tutor utilizing LangChain's dynamic chat model wrapper and Groq.

### 6. Document Ingestion & Splitting (LangChain Core)
*   [PDF_Content_Previewer](./PDF_Content_Previewer): Reads and parses metadata/text from local PDFs.
*   [PDF_Document_Splitter](./PDF_Document_Splitter): Segments PDF documents recursively into semantic chunks.
*   [Python_Code_Splitter](./Python_Code_Splitter): Segments Python files recursively based on code syntax rules.

### 7. Retrieval-Augmented Generation (RAG)
*   [Docuchat_with_PDF](./Docuchat_with_PDF): Local PDF document search Q&A using Chroma DB vector store and HuggingFace embeddings.
*   [Docuchat_with_Web_Docs](./Docuchat_with_Web_Docs): Web page scraper Q&A using `WebBaseLoader` and Chroma DB.

### 8. Multi-Tool Intelligent Agents (LangChain Agent Framework)
*   [SkillMap_Agent](./SkillMap_Agent): Career advisor agent utilizing Tavily Search and JSearch APIs.
*   [SkillMap_Agent_with_Memory](./SkillMap_Agent_with_Memory): Career advisor agent with memory checkpointing using Tavily Search and JSearch APIs.
*   [TravelBuddy_Agent](./TravelBuddy_Agent): Travel planner agent utilizing Tavily Search and SerpAPI Google Flights search.
*   [CourseFinder_Agent](./CourseFinder_Agent): Course recommendation agent utilizing Tavily Search and YouTube Data API v3.

---

## Global Setup Instructions

This repository provides a root-level `requirements.txt` containing all dependencies across all 25 projects for convenience.

1.  **Clone the repository and enter the directory:**
    ```bash
    git clone https://github.com/Guneshbari/AIML.git
    cd AIML
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install all dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys:**
    Most projects require configuration of environment variables. Create a `.env` file inside the specific project directory you want to run. Depending on the project, you will need:
    *   `GEMINI_API_KEY` / `GOOGLE_API_KEY`: For Gemini model invocations.
    *   `GROQ_API_KEY`: For Groq model invocations.
    *   `TAVILY_API_KEY`: For web searching capabilities.
    *   `WEATHER_API_KEY`: For OpenWeatherMap API weather fetching.
    *   `SERPAPI_KEY`: For Google Flights searching.
    *   `YOUTUBE_API_KEY`: For YouTube search queries.
    *   `RAPIDAPI_KEY`: For JSearch job listings.

## Running a Project

To run any project, navigate to its directory and execute its `app.py` script:

```bash
# Example: Running the SkillMap Agent with Memory
cd SkillMap_Agent_with_Memory
python app.py
```
Each subdirectory contains its own dedicated `README.md` file with detailed instructions specific to that project.
