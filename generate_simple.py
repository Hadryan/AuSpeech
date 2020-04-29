import pandas as pd
import json
from run_generation_continuous import initiate_model, get_response

all_outputs = []
model, tokenizer, args = initiate_model()
j = 0

def generate(row):
    global j

    responses = []
    for i in range(5):
        responses.append(get_response(model, tokenizer, row["Utterance"], args).replace(row["Utterance"].lower(), ""))
    all_outputs.append({
        "id": row["uttid"],
        "utt": row["Utterance"],
        "generations": responses
    })
    print("Generation complete for item {}".format(j))
    j += 1

if __name__ == "__main__":

    df = pd.read_csv("filtered_test.csv")
    print(df.shape)
    _ = df.apply(generate, axis=1)
    with open("generations.json", "w") as fp:
        json.dump(all_outputs, fp)
