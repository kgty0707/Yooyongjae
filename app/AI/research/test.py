import transformers

model = transformers.AutoModelForCausalLM.from_pretrained(
    'player1537/Dolphinette',
)

tokenizer = transformers.AutoTokenizer.from_pretrained(
    'player1537/Dolphinette',
)

pipeline = transformers.pipeline(
    'text-generation',
    model=model,
    tokenizer=tokenizer,
)

completion = pipeline(
    (
        r"""<s>INSTRUCTION: You are an AI assistant that helps people find"""
        r"""information. INPUT: Answer this question: what is the capital of"""
        r"""France? Be concise. OUTPUT:"""
    ),
    return_full_text=False,
    max_new_tokens=512,
)
completion = completion[0]['generated_text']

print(completion)