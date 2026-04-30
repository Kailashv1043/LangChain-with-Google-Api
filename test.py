import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6JyP7A3Lv97W-qAcnn3NcjLU3gFT0yR5Gza2LZ_4BHvAw")

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)