
#llm params
MODEL = "qwen2-0_5b-instruct-q5_k_m.gguf"
GPU_LAYERS = -1
N_BATCH = 1024
N_CTX=4096
N_THREADS=10
N_THREADS_BATCH=10

#prompts
SYS_PROMPT = "You are excpected to answer user's questions about some file that will be send to you with his question. " \
             "DO NOT add any extra info that is not presented in file. Use only given info to answer question." \
             "If you are asked a question that is not related to file, then DO NOT ANSWER TO IT"
