from openai import OpenAI
import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='components/.env')

api_key = os.environ.get("OPENAI_API_TOKEN")

client = OpenAI(api_key=os.environ.get("OPENAI_API_TOKEN"),)


user_prompt = input("Quelle image désire tu petit coquinou ? :")


def single_generated(x):
    response = client.images.generate(
        model="dall-e-3",
        prompt=x,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url


image_url = single_generated(user_prompt)


#print("Generated Image URL:", image_url)

# Download the image
image_response = requests.get(image_url)
if image_response.status_code == 200:
    # Save the image to a local file
    with open("data/generated/generated_image.jpg", "wb") as image_file:
        image_file.write(image_response.content)
    print("Image saved as 'data/generated/generated_image.jpg'")
else:
    print("Failed to download image")
