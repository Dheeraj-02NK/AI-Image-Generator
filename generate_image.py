import os
import openai

# Set your OpenAI API key here
openai.api_key = "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"

user_prompt = "cat wearing red cape"

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)
