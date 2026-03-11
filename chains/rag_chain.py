def run_rag(query, retriever, llm, prompt):
    # 1. Retrieve
    docs = retriever.invoke(query)

    # 2. Build context
    context = "\n\n".join(
        f"[{d.metadata['section']} | page {d.metadata['page']}]\n{d.page_content}"
        for d in docs
    )

    # 3. Build prompt
    final_prompt = prompt.format(
        context=context,
        question=query
    )

    # 4. LLM call (NEW API)
    response = llm.invoke(final_prompt)

    # 5. Extract text
    answer = response.content

    return answer, docs
