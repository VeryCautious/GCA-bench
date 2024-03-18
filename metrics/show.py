from metrics.report import get_model_report

model = "GCA"
predictions_path = "/home/ian/Code/harness/predictions.json"
swe_bench_tasks = "/home/ian/Code/harness/swe-bench.json"
log_dir = "/home/ian/Code/harness/logs/" + model

report = get_model_report(model, predictions_path, swe_bench_tasks, log_dir)

none = sum([len(v['none']) for k, v in report.items() if isinstance(v, dict)])
generated = sum([len(v['generated']) for k, v in report.items() if isinstance(v, dict)])
with_logs = sum([len(v['with_logs']) for k, v in report.items() if isinstance(v, dict)])
applied = sum([len(v['applied']) for k, v in report.items() if isinstance(v, dict)])
resolved = sum([len(v['resolved']) for k, v in report.items() if isinstance(v, dict)])

print(f"{model} Evaluation Report:")
print(f"\tNone:      {none}")
print(f"\tGenerated: {generated}")
print(f"\tWith Logs: {with_logs}")
print(f"\tApplied:   {applied}")
print(f"\tResolved:  {resolved}")