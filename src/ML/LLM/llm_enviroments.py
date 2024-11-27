
#llm params
MODEL = "qwen2-0_5b-instruct-q5_k_m.gguf"
GPU_LAYERS = -1
N_BATCH = 1024
N_CTX=4096
N_THREADS=10
N_THREADS_BATCH=10

#prompts
SYS_PROMPT = "You are excpected to answer user's questions about some file that will be send to you with his question."
