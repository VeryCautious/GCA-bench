#!/bin/bash
python run_evaluation.py \
    --predictions_path "./predictions.json" \
    --swe_bench_tasks "./swe-bench.json" \
    --log_dir "./logs" \
    --testbed "<path to folder>" \
    --skip_existing \
    --timeout 900 \
    --verbose
