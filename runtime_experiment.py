import random
import time
import matplotlib.pyplot as plt
import numpy as np

from sequence_alignment import sadp, read_costs


def generate_random_sequence(length: int) -> str:
    return ''.join(random.choices('AGTC', k=length))


def run_experiments(costs: dict) -> dict[int, float]:
    lengths = [500, 1000, 2000, 4000, 5000]
    results = {}

    print(f"{'Length':>8} | {'Avg Time (s)':>14} | {'Min (s)':>10} | {'Max (s)':>10}")
    print("-" * 50)

    for length in lengths:
        times = []
        for trial in range(10):
            s1 = generate_random_sequence(length)
            s2 = generate_random_sequence(length)

            start = time.time()
            sadp(costs, s1, s2)
            end = time.time()

            times.append(end - start)

        avg = sum(times) / len(times)
        results[length] = avg
        print(f"{length:>8} | {avg:>14.4f} | {min(times):>10.4f} | {max(times):>10.4f}")

    return results


def plot_results(results: dict[int, float]):
    lengths = list(results.keys())
    avg_times = list(results.values())
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.plot(lengths, avg_times, 'bo-', linewidth=2, markersize=8)
    ax1.set_xlabel('Sequence Length (n)', fontsize=12)
    ax1.set_ylabel('Average Time (seconds)', fontsize=12)
    ax1.set_title('Sequence Alignment Runtime', fontsize=14)
    ax1.grid(True, alpha=0.3)

    log_lengths = np.log(lengths)
    log_times = np.log(avg_times)

    slope, intercept = np.polyfit(log_lengths, log_times, 1)

    ax2.loglog(lengths, avg_times, 'bo-', linewidth=2, markersize=8, label='Measured')
    fit_times = [np.exp(intercept) * (l ** slope) for l in lengths]
    ax2.loglog(lengths, fit_times, 'r--', linewidth=2, label=f'Fitted slope = {slope:.2f}')
    ax2.set_xlabel('Sequence Length (n)', fontsize=12)
    ax2.set_ylabel('Average Time (seconds)', fontsize=12)
    ax2.set_title('Log-Log Plot of Runtime', fontsize=14)
    ax2.legend()
    ax2.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    plt.savefig('runtime_plot.png', dpi=150, bbox_inches='tight')

    print(f"Fitted slope on log-log plot: {slope:.4f}")
    print(f"This suggests experimental runtime of O(n^{slope:.2f})")


def main():
    costs = read_costs("imp2cost.txt")

    results = run_experiments(costs)
    plot_results(results)


if __name__ == "__main__":
    main()