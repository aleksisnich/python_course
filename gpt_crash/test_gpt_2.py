from g4f.client import Client

client = Client()
response = client.images.generate(
    model="flux",
    prompt="cartoon dino with volleyball ball in red and white colors in minimalism style",
    response_format="url"
)

print(f"Generated image URL: {response.data[0].url}")