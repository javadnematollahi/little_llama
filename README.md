## LLAMA

This is an openai model that able you to give your own text to it and ask question of that text from model.

To use this model first you need to buy a token from openai.

link of model documentation:

https://docs.llamaindex.ai/


## How to use Model:

```
lama = llama_model("Your data text file directory, "Your open ai token)
result = lama.getquery("Your query)
print(result)
```