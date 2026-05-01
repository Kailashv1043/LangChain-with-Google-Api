import google.generativeai as genai

genai.configure(api_key="AIzaSyBDsXfJp3BRFNderJ-XaQGnv1ahaACCZkk")

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)