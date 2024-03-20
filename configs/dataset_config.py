visual_datasets = [
    dict(
        type="aokvqa",
        vis_root="/content/train2017",
        ann_paths=[
            "/content/aokvqa_v1p0_train_test.json",
        ],
        sample=5000,
    ),
    dict(
        type="vlsp",
        vis_root="./training-data/training-images",
        ann_paths= 
          "./Fim1/data/vlsp2023_train_data.json",
        sample=10,
    ),
]

# language_datasets = [
#     dict(
#         type="dolly",
#         ann_path="data/dolly/databricks-dolly-15k.jsonl",
#     ),
#     dict(
#         type="alpaca_gpt4",
#         ann_path="data/alpaca_gpt4/alpaca_gpt4_data.json",
#     ),
#     dict(
#         type="baize",
#         ann_path="data/baize/quora_chat_data.json",
#     ),
# ]
