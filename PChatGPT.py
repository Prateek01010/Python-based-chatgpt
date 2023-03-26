import openai
openai.api_key = "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"

while True:
    model = "text-davinci-003"
    user = input("Enter Your Question Here:\n")
    if "exit" in user:
        break

    completion = openai.Completion.create(model = "text-davinci-003",
    prompt = user,
    max_tokens = 2048,
    temperature = 0.2,
    n = 1,
    stop = None
    )

    response = completion.choices[0].text
    print(response)
