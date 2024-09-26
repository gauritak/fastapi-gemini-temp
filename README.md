# task

Owner: Shreyaan Seth

Task 1: Create a FastAPI Endpoint to Interact with Gemini API

---

### Objective:

- Build an endpoint in FastAPI that communicates with the Gemini API to fetch LLM-powered responses for a **specific use case**.

### Steps:

1. **Pick a Use Case**:
Choose **one** of the following use cases to implement:
    - **Text Summarization**: Take a large text input from the user and use Gemini to generate a concise summary.
    - **Text Sentiment Analysis**: Send text to Gemini to get a sentiment analysis (positive, negative, or neutral) of the content.
    - **Content Generation**: Generate a paragraph or short content based on user-provided input (e.g., write a product description or marketing blurb).
2. **Understand the Gemini API**:
    - Refer to the [Gemini API documentation](https://ai.google.dev/gemini-api/docs) and figure out how to authenticate and interact with the API.
    - You will be given the API key, but **you** are responsible for integrating the authentication. The API likely uses API keys or OAuth—figure out the method by exploring the docs.
3. **Design and Implement the FastAPI Route**:
    - Create a route (e.g., `/gemini/insights`) that accepts user input in the request body and sends it to the Gemini API based on the selected use case (Summarization, Sentiment Analysis, or Content Generation).
    - **Postman**: Use Postman to test the endpoint by sending POST requests. Set up appropriate headers (e.g., API key) and payloads in Postman to ensure it works as expected.
4. **Test and Debug**:
    - Use Postman to test the FastAPI route with different inputs and check if the Gemini API responses are returned correctly.
    - Make sure the response is structured and meaningful for your use case.

### Expected Outcome:

- A FastAPI route that fetches and returns results from Gemini API based on one of the predefined use cases.

---

### Task 2: Save Gemini API Response in PostgreSQL and Retrieve Data

### Objective:

- Store the input and response from the Gemini API into a PostgreSQL database using SQLAlchemy and create another endpoint to retrieve and display the stored data.

### Steps:

1. **Create a Database Model**:
    - Use SQLAlchemy to design a model that fits the data you are handling.
    - The model should include fields such as:
        - `id`: Primary key
        - `input_text`: The text that was sent to the Gemini API
        - `response`: The result returned by the Gemini API (summary, sentiment, or generated content)
        - `created_at`: A timestamp for when the request was made
    - **You are responsible for figuring out how to structure the model properly** based on your use case.
2. **Create the Table**:
    - Use the provided PostgreSQL URL to connect to the database.
    - Write SQLAlchemy code to create the necessary table.
    - **Postman Testing**: You can use Postman to trigger the FastAPI route and insert the data into PostgreSQL, ensuring that your endpoint integrates with the database.
3. **Save Data to the Database**:
    - Modify the route from Task 1 to store the API input and response in the database.
    - Ensure the data is saved **after each request** to Gemini, and handle any possible errors or failed requests.
4. **Retrieve and Display Stored Data**:
    - Add another route (e.g., `/gemini/insights/stored`) to fetch and return all saved records from the database.
    - **Postman Testing**: Use Postman to test this retrieval route and verify the data from PostgreSQL is being returned correctly.

### Expected Outcome:

- A fully functioning FastAPI project with the following:
    1. A route to interact with Gemini API and store the data in PostgreSQL.
    2. Another route to retrieve and display the stored data.

---

### Tools & Suggestions:

1. **Postman**:
    - Use Postman for testing both the Gemini API and your FastAPI endpoints. You should:
        - Set up API requests with the proper authentication headers.
        - Test the endpoints with various inputs for your chosen use case (summarization, sentiment analysis, content generation).
    - **Hint**: Research how to set headers and request bodies in Postman, as this will be critical when testing the FastAPI and Gemini API integration.
2. **Database Viewer**:
    - Use **pgAdmin** or **DBeaver** to visually inspect the PostgreSQL database. This will help you verify that the data is being stored correctly and allow you to see how your database schema aligns with the API responses.
3. **Learning FastAPI**: Refer to the following video if needed:
    - [FastAPI Tutorial Video](https://youtu.be/SORiTsvnU28).
    - https://www.youtube.com/watch?v=aAy-B6KPld8&pp=ygUWZmFzdGFwaSBzcWxhbGNoZW15IDIuMA==

---

### Deliverables:

1. A working FastAPI project with the following:
    - One route interacting with the Gemini API for one of the predefined use cases.
    - A SQLAlchemy model to store the API input and response.
    - A route to save and retrieve the Gemini API results from PostgreSQL.
2. Postman collection (optional): If you want, you can export your Postman requests and share them to demonstrate how you tested the API and endpoints.

---
