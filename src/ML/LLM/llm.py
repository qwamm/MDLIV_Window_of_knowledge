from llama_cpp import Llama
from .llm_enviroments import *
import os

class LLM:
    def __init__(self, model: str=MODEL, gpu_layers=GPU_LAYERS, n_batch=N_BATCH, n_ctx=N_CTX, n_threads=N_THREADS, n_threads_batch=N_THREADS_BATCH) -> None:
        self.llm = Llama(
                model_path=os.path.join(os.path.dirname(__file__), model),
                n_gpu_layers=gpu_layers,
                n_batch=n_batch,
                use_mlock=True,
                n_ctx=n_ctx,
                n_threads=n_threads,
                n_threads_batch=n_threads_batch
            )

    def _create_user_prompt(self, request: str, content: str):
        return "question: " + request + "\n" + "file contents:\n" + content

    def answer(self, request: str, content: str):
        response = self.llm.create_chat_completion(
            messages=[
                {"role":"system", "content": SYS_PROMPT},
                {"role": "user", "content": self._create_user_prompt(request, content)}
            ]
        )['choices'][0]['message']['content']
        self.llm.reset()
        return response
