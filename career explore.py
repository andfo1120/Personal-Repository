import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

# Function for generating text completion
def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an assistant to help with career exploration."},
            {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message['content']

# Function for generating an image based on a prompt
def generate_image(prompt):
    response = openai.Image.create(
        model="dall-e-3",  # Use the appropriate model for image generation
        prompt=prompt,
        size="1024x1024",
        n=1
    )
    return response['data'][0]['url']

# Streamlit UI setup
st.title("AI-Powered Career Exploration Tool")

# Input fields
job_title = st.text_input("Enter a job title to explore:", "")

if st.button('Get Skills Information'):
    if job_title:
        skills_info = get_completion(f"Describe the technical and soft skills required for the role of {job_title}.")
        st.write(f"Skills required for the role of {job_title}:")
        st.write(skills_info)
    else:
        st.write("Please enter a job title.")

if st.button('Generate Workspace Image'):
    if job_title:
        image_url = generate_image(f"Generate an image of a typical workspace for a {job_title}.")
        st.image(image_url, caption=f"Workspace of a {job_title}")
    else:
        st.write("Please enter a job title.")
