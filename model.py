import torch
import transformers

from transformers import LlamaForCausalLM, LlamaTokenizer

def create_pipeline():
    print("Loading model....")

    model_dir = "./Llama-2-7b-chat-hf"
    model = LlamaForCausalLM.from_pretrained(model_dir)
    print("Loaded model....")

    print("Loading tokenizer....")
    tokenizer = LlamaTokenizer.from_pretrained(model_dir)
    print("Loaded tokenizer....")

    print("Creating pipeline....")
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    print("Pipeline created....")

    return pipeline, tokenizer.eos_token_id