from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import base64
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

system_prompt="""
### 1. Overview & Style
[Brief summary of the image type, mood, lighting, and overall visual style]

### 2. Main Subjects
- **[Subject 1]:** [Detailed description]
- **[Subject 2]:** [Detailed description]

### 3. Environment & Spatial Layout
[Describe the background and how the subjects are arranged physically in the frame]

### 4. Text & OCR
[Exact transcription of all visible text. Use bullet points or code blocks if necessary. If no text, write "None"]

### 5. Data & Diagrams (If applicable)
[Extraction of chart data, flowchart steps, or UI components. If not applicable, write "N/A"]
"""


def encode_image(image_path:str)->str:
    with open(image_path,"rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")
    
def describe_image(image_path:str)->str:
    image_base64=encode_image(image_path)

    llm=ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY
    )

    message=HumanMessage(
        content=[
            {"type":"text","text":system_prompt},
            {
                "type":"image_url",
                "image_url":f"data:image/jpeg;base64,{image_base64}"
            },
        ]
    )

    response=llm.invoke([message])

    return response.content