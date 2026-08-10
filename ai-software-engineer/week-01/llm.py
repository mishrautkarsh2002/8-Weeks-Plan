import os

from dotenv import load_dotenv
from google import genai

from models import InitialPlan


load_dotenv()

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)


def create_plan(question: str) -> InitialPlan:

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            """
            You are a research planning assistant.

            Given a software engineering question:

            1. Summarize the problem.

            2. Generate useful search queries that would
               help investigate the problem.

            3. Assign a priority:
               - High
               - Medium
               - Low

            4. Determine whether the problem is likely to
               require changes to source code.
               Return true if source code changes are likely
               required.
               Return false if the question is primarily
               informational or conceptual.

            Return the information using the requested structure.
            """,
            question,
        ],
        config={
            "response_mime_type": "application/json",
            "response_json_schema": InitialPlan.model_json_schema(),
        },
    )

    return InitialPlan.model_validate_json(response.text)