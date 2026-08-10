# AI Agent Glossary

## LLM

My understanding:
An LLM (Large Language Model) is an AI model trained on a large amount of data to learn patterns in language and information. It generates responses by predicting appropriate tokens based on the input and context provided to it.

An LLM is the reasoning and language-generation component of our application. It doesn't automatically know how to interact with our codebase or execute Python functions, so we provide it with context, tools, memory, and instructions.

## Prompt

My understanding:
A prompt is the input or instruction given to an LLM that tells it what task to perform or what kind of response to generate. It doesn't necessarily have to be a question.

Prompts are important because they influence how the LLM behaves and responds. In our project, prompts will tell the AI Software Engineer how to analyze problems, use tools, and produce responses.

## System Prompt

My understanding:
A system prompt is an instruction provided by the application that defines how the LLM should behave, what role it should perform, and what rules it should follow.

For example, we could tell our AI Software Engineer that it is a software engineering assistant and that it should analyze code before suggesting a fix. The system prompt is controlled by our application rather than being the user's actual request.

## User Prompt

My understanding:
A user prompt is the actual request or information provided by the user to the LLM. For example, "Why is this Swift 6 test failing?" would be a user prompt.

The user prompt gives the agent the specific task it needs to work on, while the system prompt provides the general rules for how the agent should behave.

## Token

My understanding:
A token is a small unit of text that an LLM processes. A token is not necessarily one complete word because a word can be represented by one or multiple tokens, and tokens can also represent parts of words or punctuation.

Tokens are important because they affect how much information can fit into the context window, how much an API request costs, and in some cases API rate limits.

## Context Window

My understanding:
A context window is the maximum amount of tokenized information an LLM can consider during a particular interaction. This can include system instructions, user messages, previous conversation, documents, code, and tool results.

Context windows are important for agents because they can accumulate a lot of information while working. We need to decide what information is actually useful to give the LLM instead of sending everything.

## Structured Output

My understanding:
Structured output means asking an LLM to return information in a predefined machine-readable format instead of normal conversational text. For example, the LLM can return JSON containing `summary`, `search_queries`, and `priority`.

Structured output allows our Python application to reliably understand and use the LLM's response instead of trying to interpret a large block of natural language.

## Schema

My understanding:
A schema defines the expected structure of data, including what fields should exist and what type of value each field should contain. For example, `summary` can be a string and `search_queries` can be a list of strings.

A schema acts as a contract between the data producer and consumer. In our project, it helps define the structure that we expect the LLM to return.

## Pydantic

My understanding:
Pydantic is a Python library used to define, parse, and validate structured data using Python models. We use `BaseModel` to define what our data should look like.

In our project, Pydantic acts as a bridge between the LLM's structured response and Python code. It validates the response and gives us a Python object that we can work with using fields such as `plan.summary` and `plan.priority`.

## API

My understanding:
An API (Application Programming Interface) is a defined way for one piece of software to communicate with another. In our project, our Python application communicates with Google's Gemini service through its API.

The API defines how we send information such as our prompt and model configuration and how we receive the response from Gemini. It acts as the communication interface between our application and the external AI service.

## Tool

My understanding:
A tool is a function or capability that an AI agent can use to perform a specific operation outside the LLM itself. Examples could be searching code, reading a file, running tests, or executing a command.

The LLM decides or requests that a tool should be used, but our application actually executes the tool. The result is then given back to the LLM so it can decide what to do next.

## Agent

My understanding:
An agent is a system where an LLM can repeatedly decide what action to take, use tools, observe their results, and decide what to do next until it reaches a stopping condition or completes the task.

A simple agent works in a loop: **Goal → LLM decides → Tool/action → Result → LLM decides again → Final answer.** Our AI Software Engineer will eventually use this loop to search code, analyze files, run tests, and investigate problems.
