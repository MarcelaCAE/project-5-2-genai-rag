# GEN AI Project: Financial bot development

## Objectives & Chatbot Goal's
- Developed a chatbot to offer financial advice inspired by the principles and lessons from the book Rich Dad Poor Dad by Robert T. Kiyosaki.
- Provided practical, actionable financial guidance to users.
- Simplifyed complex concepts from the book into clear, accessible chatbot interactions.
- Motivated users to adopt better financial habits and a wealth-building mindset.


## Book Overview
- Rich Dad Poor Dad by Robert T. Kiyosaki is a personal finance book contrasting the mindsets of the Rich Dad and Poor Dad.
- It teaches how to build wealth through investments, acquiring assets, and financial literacy.
- The book challenges traditional beliefs about job security and saving, encouraging readers to escape the rat race and achieve financial independence.

## Challenges & Solutions

**Challenge 1: Time Management**  
Time management due to the time spend to debugging the best environment (In total, were deleted 6x the wrong environment, before the right one be working)
**Solution 1:** Focus on the Driving Questions when building the chatbot: What do I want to achieve with this bot? Is it just financial advice based on the book, or do I want to apply this to real-life scenarios where people can connect and think from both perspectives in the book?

**Challenge 2: Understanding the Chatbot Workflow and NLP Approach**  
**Solution 2:** Debug with other teams, using available resources to increase the workflow of the project and connect the bot with a large audience.

## Conversation Flow Design

### **Driven Points**
- Presented both the Rich Dad and Poor Dad perspectives impartially, allowing users to reflect on which mindset aligns with theirs, without influencing their choice.
- Define the target audience for the chatbot and tailor the content to meet their specific needs and knowledge level, ensuring relevance and engagement.
- Structure the conversation flow to guide users clearly and effectively, explaining concepts in a simple and concise manner.

## Platform Selection
- Deploy the chatbot on Streamlit for interactive web-based functionality.
- Integrate the chatbot with Streamlit components (text inputs, buttons, responses).
- Optimize the user interface for a smooth, engaging experience.

## Chatbot Development
### Bot Type
- Build an AI-powered chatbot using OpenAI and NLP for dynamic, context-based responses.

### ETL
**Extract and Preprocess Data:**  
Extract the content of the *Rich Dad Poor Dad* PDF, then split the text into smaller chunks to facilitate efficient preprocessing and handling.

**Setup Chroma DB and OpenAI Embedding Model:**  
Access the OpenAI API key and initialize the Chroma DB client, which stores vectorized data in the chromadb directory for fast retrieval and comparisons.

**Define Embeddings for Text Representation:**  
Use the OpenAI embeddings model to convert text into numerical vector representations (embeddings).

### System Architecture
1. **User’s Question:** Save the user’s question in a variable.
2. **Find Relevant Information:** Use a search function to find the top 5 most relevant documents based on the user's question.
3. **Organize the Information:** Create a formatted string with the relevant content to give to the chatbot.
4. **Generate the Response:** Provide the formatted information to the chatbot to help it generate an answer based on the retrieved content.

### NLP & Prompt Engineering
- **Role of the Chatbot:** The bot is designed to give financial advice based on *Rich Dad Poor Dad*.
- **User Interaction:** The user asks a question, and the bot answers using the book's content.
- **Context Provided:** The bot is given key sections from the book to use as reference.
- **Response Guidelines:** The bot follows clear rules to ensure accurate, clear, and unbiased answers. It explains both perspectives (Rich Dad vs. Poor Dad), compares them, and gives an analogy to make it easier to understand.
- **Response Format:** The answer is structured in an organized way: title, user's question, the answer, a comparison of perspectives, an analogy, and the book reference.

### Deployment & System Integration
1. **Testing:** Send a user prompt to the model and get the bot’s response. Check if the response aligns with expectations.
2. **Integration with Other Systems:** Use Chroma DB for storing and retrieving relevant data for user queries. Perform document search (retrieved_docs) and prepare context for the response.
3. **Deployment:** Integrate the trained chatbot with the frontend platform (Streamlit). Make the bot accessible to users for real-time interaction.

### Maintenance & Improvements
- Continuously monitor user feedback and adjust the model's parameters.
- Update model parameters like temperature, tokens, etc., based on performance feedback.

## Improvements Done & Next Steps
- **Tested with the Question:** How Can I Save Money? 
- **Issue Found:** The source was not the book. After debugging, the issue was with the prompt. The prompt was improved, and now the book is correctly cited as the source.

## Streamlit Financial Bot
- Built the application using Streamlit, and the application is performing well, giving accurate responses.
- **Next Steps:** Fine-tune the model parameters for handling double questions and removing analogies from the book when the answer is not related to financial themes.

## Deliverables
1. **Python Code:** Includes all the steps needed for the model deployment on the Streamlit app.
2. **Presentation:** A detailed PowerPoint presentation summarizing all the steps taken, as well as the insights gained while building the model using NLP.
3. **Streamlit:** The Python code used to deploy the application on Streamlit.
