import os
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage, AIMessage

os.environ["GROQ_API_KEY"] = "YOUR_API_KEY"

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

chat_history = []

print("AI Chat Started")
print("Type exit to stop\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Add user message
    chat_history.append(
        HumanMessage(content=user_input)
    )

    # Get AI response
    response = llm.invoke(chat_history)

    # Print AI response
    print("\nAI:")
    print(response.content)
    print()

    # Store AI response
    chat_history.append(
        AIMessage(content=response.content)
    )