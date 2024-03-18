#!/bin/bash
python run_evaluation.py \
    --predictions_path "/home/ian/Code/harness/predictions.json" \
    --swe_bench_tasks "/home/ian/Code/harness/swe-bench.json" \
    --log_dir "/home/ian/Code/harness/logs" \
    --testbed "/home/ian/Code/Sandbox" \
    --skip_existing \
    --timeout 900 \
    --verbose
