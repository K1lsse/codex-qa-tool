from pathlib import Path

base_dir = Path(__file__).parent
log_dir = base_dir / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "sample.log"

with open(log_file, "w", encoding="utf-8") as f:
    f.write("device boot success\n")
    f.write("camera error happened\n")
    f.write("test case fail\n")
    f.write("kernel panic detected\n")

print(f"Log file saved to: {log_file}")