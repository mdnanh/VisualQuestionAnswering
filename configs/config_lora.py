tuning_config = dict(
    lora=True,
    lora_target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "to_q", "to_kv", "to_out", "ff.1", "ff.3", "query_key_value"],
    lora_r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    vis=False,
    unfrozen=[],
)
