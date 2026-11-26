# Runs every task script in the right order and saves the console output in the outputs folder
import os, subprocess, sys
BASE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(BASE, "outputs", "figures"), exist_ok=True)
order = ["task7_eda_inspection_cleaning", "task1_mean_median_mode", "task2_variance_std", "task3_correlation_probability",
         "task4_outlier_detection", "task5_matplotlib", "task6_seaborn", "task8_eda_correlation_insights", "task9_business_recommendations"]
for name in order:
    r = subprocess.run([sys.executable, os.path.join(BASE, name + ".py")], capture_output=True, text=True, cwd=BASE)
    open(os.path.join(BASE, "outputs", name + ".txt"), "w").write(r.stdout + r.stderr)
    print(name, "OK" if r.returncode == 0 else "FAILED")
