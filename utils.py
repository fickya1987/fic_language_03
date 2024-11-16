import openai

def get_image_description(client, image_file, prompt, model_choice):
    # Convert the image to base64 if needed, or handle it as required by your model
    image_data = image_file.read()  # Read the image file

    # Prepare the prompt and call the OpenAI API with the chosen model
    response = client.ChatCompletion.create(
        model=model_choice,
        messages=[
            {"role": "system", "content": "You are an AI model that describes images."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=1000
    )

    # Extract and return the description
    description = response['choices'][0]['message']['content']
    return description

