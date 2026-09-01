from mmengine.config import read_base

with read_base():
    from .groups.general365 import general365_summary_groups

summarizer = dict(
    dataset_abbrs=[
        'General365',
        'General365-math',
        'General365-text',
    ],
    summary_groups=general365_summary_groups,
)
