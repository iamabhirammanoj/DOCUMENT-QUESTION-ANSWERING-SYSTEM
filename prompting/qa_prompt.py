from langchain_core.prompts import PromptTemplate

QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a document QA system.
Answer ONLY from the context.
If the answer is not found, say "I don't know".

Context:
{context}

Question:
{question}
"""
)
