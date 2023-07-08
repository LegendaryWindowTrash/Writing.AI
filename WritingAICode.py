import os
import google.generativeai as palm

modelName = "null"

palm.configure(api_key=os.environ["API_KEY"]) #this is obviously not a API key so this won't run

print("Hello. I am Writing.AI, a writing assistant. Here's what I can and can't do:")
print("I can:\n  Give you tips for writing. \n  Re-write things so they make more sense. \n  Give you ideas on how to continue a story you paste in.")
print("What I can't do: \n  Write stuff for you. If I detect that you are asking me to write a story, I will respond with something along the lines of \"I'm sorry. I can't write stuff for you.\" \nRemember that I'm a Language Model, so what I say may not be true. If something is off, head to this repository: \nhttps://github.com/LegendaryWindowTrash/Writing.AI\n and make a new issue.")
print("(This isn't an AI response. This will always appear when you boot up the app.)")

while True:
    prompt = input("Now, what do you need help with?")
    if (str.lower(prompt) == "exit"):
        break
    response = palm.generate_text(model=modelName, prompt=prompt)

    print(response)
print("Exiting application...")