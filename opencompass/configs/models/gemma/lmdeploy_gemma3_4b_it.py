from opencompass.models import TurboMindModelwithChatTemplate

models = [
    dict(
        type=TurboMindModelwithChatTemplate,
        abbr='gemma-3-4b-it-turbomind',
        path='google/gemma-3-4b-it',
        engine_config=dict(session_len=32768, max_batch_size=16, tp=1),
        gen_config=dict(
            top_k=1, temperature=1e-6, top_p=0.9, max_new_tokens=8192
        ),
        stop_words=['<end_of_turn>'],
        max_seq_len=32768,
        max_out_len=8192,
        batch_size=16,
        run_cfg=dict(num_gpus=1),
    )
]