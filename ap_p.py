# ============================
# Import Required Libraries
# ============================

# Load environment variables (optional)
from dotenv import load_dotenv

# Streamlit library
import streamlit as st
import pandas as pd

# SQLite library
import sqlite3

# Ollama library
import ollama

# ============================
# Load Environment Variables
# ============================

load_dotenv()

# ============================
# Function to Generate SQL Query
# ============================

def get_ollama_response(question, prompt):
    """
    Converts English question into SQLite SQL
    using Ollama Llama 3.2.
    """

    full_prompt = f"""
{prompt}

User Question:
{question}

Return ONLY the SQL query.
"""

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
        )

        sql_query = response["message"]["content"].strip()

        # Remove markdown if returned
        sql_query = sql_query.replace("```sql", "")
        sql_query = sql_query.replace("```", "")
        sql_query = sql_query.strip()

        return sql_query

    except Exception as e:
        return f"ERROR: {e}"


# ============================
# Function to Execute SQL Query
# ============================

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        # Extract column names from cursor description
        columns = [description[0] for description in cursor.description]
        
        conn.close()

        # Return a Pandas DataFrame with column headers
        return pd.DataFrame(rows, columns=columns)

    except Exception as e:
        conn.close()
        return str(e)

# ============================
# Prompt for Ollama
# ============================

prompt = """
You are an expert in converting English questions into SQLite SQL queries.

Database Tables

1. Actor
- Actor_ID
- Actor_name
- Gender
- debut_year

2. Director
- Director_ID
- Director_name
- no_of_movies

3. Movie
- Movie_name
- release_year
- genre
- lead_1
- lead_2
- director_id
- box_collection

4. DVD
- DVD_id
- Movie_name
- sale

Relationships

Movie.lead_1 = Actor.Actor_ID

Movie.lead_2 = Actor.Actor_ID

Movie.director_id = Director.Director_ID

DVD.Movie_name = Movie.Movie_name

Instructions

1. Convert English question into SQLite SQL query.

2. Return ONLY SQL query.

3. Don't explain anything.

4. Don't use markdown.

5. Use JOIN whenever needed.

6. Use valid SQLite syntax only.
"""

# ============================
# Streamlit Page Configuration
# ============================

st.set_page_config(
    page_title="SQL AI Assistant",
    layout="wide"
)

# ============================
# Page Title
# ============================

st.title(" AI SQL Query Generator using Ollama")

st.write(
    "Ask questions in English. "
    "The AI will generate a SQLite query and execute it."
)

# ============================
# User Input
# ============================

question = st.text_input(
    "Enter your question:",
    placeholder="Example: Show all actors"
)

submit = st.button("Ask Question")

# ============================
# Button Click Event
# ============================

if submit:

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating SQL Query..."):

            sql_query = get_ollama_response(question, prompt)

        if sql_query.startswith("ERROR"):

            st.error(sql_query)

        else:

            st.subheader("Generated SQL")

            st.code(sql_query, language="sql")

            with st.spinner("Executing Query..."):

                result = read_sql_query(sql_query, "grpby.db")

            st.subheader("Query Result")

            if isinstance(result, str):

                st.error(result)

            elif len(result) > 0:

                st.dataframe(result, use_container_width=True)

            else:

                st.info("No records found.")