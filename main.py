"""
OS Scheduler Simulator - Main Entry Point

This is the main application launcher for the OS Scheduler Simulator.
It orchestrates all components including:
- Scheduling Algorithms (FCFS, SJF, Priority, Round Robin, MLFQ)
- GUI Interface (Tkinter)
- Gantt Chart Visualization (Matplotlib)
- Performance Metrics Calculation
- Adaptive Algorithm Recommendations
- Headless Mode (Docker/container-friendly CLI)
- Memory Management Integration

Usage:
    python main.py                    # Launch GUI
    python main.py --headless         # Run headless simulation
    python main.py --headless --algorithm fcfs --preset simple
    python main.py --headless --algorithm mlfq --preset memory_stress --memory-total 512 --memory-algo best_fit
"""

import sys
import os
import json
import glob
import argparse

# Add parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def print_banner():
    """Print application banner."""
    banner = """
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║   OS SCHEDULER SIMULATOR - DELIVERABLE 3              ║
    ║   Concurrency, IPC & Final Performance Evaluation     ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
    
    Scheduling: FCFS | SJF | Priority | Round Robin | MLFQ
    Memory: Fixed/Variable Partitions | Paging | Fit Algorithms
    Concurrency: Multi-threading | Multi-processing (fork)
    IPC: Pipes | Shared Memory
    """
    print(banner)


def run_headless(args):
    """Run headless simulation and output results."""
    from headless import run_headless_simulation, PRESET_WORKLOADS

    print("\n📊 Running Headless Simulation...")
    print(f"   Algorithm: {args.algorithm}")
    print(f"   Preset: {args.preset}")
    print(f"   Memory Total: {args.memory_total}")
    print(f"   Memory Algorithm: {args.memory_algo}")
    print(f"   Quantum: {args.quantum}")
    print(f"   Output Directory: {args.output_dir}")
    print("-" * 50)

    processes = PRESET_WORKLOADS.get(args.preset, PRESET_WORKLOADS["simple"])

    result = run_headless_simulation(
        algorithm=args.algorithm,
        processes=processes,
        memory_total=args.memory_total,
        memory_algo=args.memory_algo,
        output_dir=args.output_dir,
        quantum=args.quantum,
    )

    print("\n✅ Simulation Complete!")
    print("\n📁 Output Files:")
    for name, path in result["files"].items():
        if path:
            print(f"   {name}: {path}")

    print("\n📈 Metrics Summary:")
    metrics = result["metrics"]
    print(f"   Avg Waiting Time: {metrics['waiting_time']['average']}")
    print(f"   Avg Turnaround Time: {metrics['turnaround_time']['average']}")
    print(f"   CPU Utilization: {metrics['cpu_utilization']}%")
    print(f"   Throughput: {metrics['throughput']}")
    print(f"   Memory Utilization: {metrics['memory']['utilization']}%")
    print(f"   Avg Memory Wait: {metrics['memory']['avg_memory_wait']}")

    print("\n📋 Process Details:")
    print(
        f"   {'PID':<6} {'Arr':<5} {'Burst':<6} {'MemReq':<7} {'Allocated':<10} {'MemWait':<8}"
    )
    print("   " + "-" * 50)
    for p in result["result"]:
        alloc = "Yes" if p.get("memory_allocated") else "No"
        print(
            f"   {p['pid']:<6} {p['arrival']:<5} {p['burst']:<6} "
            f"{p.get('memory_req', 0):<7} {alloc:<10} {p.get('memory_wait', 0):<8}"
        )

    return result


def run_gui():
    """Launch the GUI application."""
    from gui.app import main as start_gui

    print("\n📱 Launching GUI Interface...")
    print("   (Use --headless flag for containerized/CLI mode)\n")

    try:
        start_gui()
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("\nPlease ensure all required packages are installed:")
        print("  uv pip install matplotlib")
        print("  uv pip install numpy")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def run_experiments(output_dir):
    """Run all algorithms on all workload types."""
    from experiments.runner import run_all_experiments

    print("\n📊 Running All Experiments...")
    print("   Algorithms: FCFS, SJF, Priority, Round Robin, MLFQ")
    print("   Workloads: CPU-bound, I/O-bound, Mixed")
    print("-" * 50)

    all_results, filepath = run_all_experiments(output_dir)
    print(f"\n✅ Experiments saved to: {filepath}")

    # Print summary
    for workload_name, results in all_results.items():
        print(f"\n  {workload_name.upper()} WORKLOAD:")
        for r in results:
            m = r["metrics"]
            print(
                f"    {r['algorithm_name']:<14} | "
                f"Wait: {m['waiting_time']['average']:<6} | "
                f"TAT: {m['turnaround_time']['average']:<6} | "
                f"CPU: {m['cpu_utilization']}%"
            )

    # Generate comparison chart
    from experiments.comparisons import compare_algorithms
    from reporting.charts import plot_algorithm_comparison

    comparison = compare_algorithms(all_results)
    chart_path = os.path.join(output_dir, "compare_algorithms.png")
    plot_algorithm_comparison(comparison, chart_path)
    print(f"\n📈 Comparison chart saved to: {chart_path}")

    return all_results


def run_comparison(compare_type, output_dir):
    """Run a specific comparison analysis."""
    os.makedirs(output_dir, exist_ok=True)

    if compare_type == "threads_vs_processes":
        print("\n🧵 Comparing Threads vs Processes...")
        from concurrency import compare_threads_vs_processes, plot_threads_vs_processes
        from experiments.workloads import MIXED

        workload = [
            {"pid": p["pid"], "burst": p["burst"], "io_burst": p.get("io_burst", 0)}
            for p in MIXED
        ]
        comparison = compare_threads_vs_processes(workload)
        chart_path = os.path.join(output_dir, "compare_concurrency.png")
        plot_threads_vs_processes(comparison, chart_path)

        print(f"  Threads elapsed: {comparison['threads']['elapsed']}s")
        print(f"  Processes elapsed: {comparison['processes']['elapsed']}s")
        print(f"  Overhead ratio: {comparison['ratio']}x")
        print(f"  Chart saved to: {chart_path}")
        return comparison

    elif compare_type == "host_vs_docker":
        print("\n🐳 Comparing Host vs Docker...")
        from experiments.comparisons import compare_host_vs_docker

        result = compare_host_vs_docker(output_dir)
        if result.get("error"):
            print(f"  ⚠️ {result['error']}")
        print("  Comparison data saved to output directory")
        return result

    elif compare_type == "memory_limits":
        print("\n🧠 Comparing Low vs High Memory Limits...")
        from experiments.comparisons import compare_memory_limits
        from reporting.charts import plot_memory_comparison

        result = compare_memory_limits(low=256, high=1024, output_dir=output_dir)
        chart_path = os.path.join(output_dir, "compare_memory.png")
        plot_memory_comparison(result, chart_path)

        print(f"  Chart saved to: {chart_path}")
        return result

    elif compare_type == "cpu_limits":
        print("\n💻 Comparing CPU Limits in Docker...")
        from experiments.comparisons import compare_cpu_limits
        from reporting.charts import plot_cpu_limits_comparison

        result = compare_cpu_limits(output_dir)
        chart_path = os.path.join(output_dir, "compare_cpu_limits.png")
        plot_cpu_limits_comparison(result, chart_path)

        print(f"  Chart saved to: {chart_path}")
        for limit, data in result.items():
            print(f"  CPU {limit}: {data.get('status', 'N/A')}")
        return result


def run_ipc_demo(output_dir):
    """Run IPC mechanism demos."""
    print("\n🔗 Running IPC Demos...")
    print("   Mechanisms: Pipes, Shared Memory")
    print("-" * 50)

    from ipc import run_ipc_demo as run_ipc
    from experiments.workloads import MIXED

    workload = [
        {
            "pid": p["pid"],
            "burst": p["burst"] // 4 + 1,
            "io_burst": p.get("io_burst", 0) // 4,
        }
        for p in MIXED
    ]

    results = run_ipc(workload)

    for method, data in results.items():
        print(f"\n  📬 {method.upper()}:")
        print(f"     Execution time: {data['elapsed']}s")
        print(f"     Processes: {data.get('process_count', 'N/A')}")

    return results


def generate_report(output_dir):
    """Generate final markdown report."""
    print("\n📝 Generating Final Report...")
    print("-" * 50)

    from reporting.generator import generate_final_report

    # Try to load existing experiment data
    experiment_results = None
    exp_files = sorted(glob.glob(os.path.join(output_dir, "experiments_*.json")))
    if exp_files:
        with open(exp_files[-1]) as f:
            experiment_results = json.load(f)
        print(f"  Using experiment data from: {exp_files[-1]}")

    filepath = generate_final_report(
        experiment_results=experiment_results,
        output_dir=output_dir,
    )
    print(f"  Report saved to: {filepath}")
    return filepath


def run_full_evaluation(output_dir):
    """Run all experiments, comparisons, and generate final report."""
    print("\n" + "=" * 60)
    print("  FULL EVALUATION - Deliverable 3")
    print("=" * 60)

    # Step 1: Run experiments
    print("\n[1/4] Running scheduling experiments...")
    all_results = run_experiments(output_dir)

    # Step 2: Threads vs Processes comparison
    print("\n[2/4] Running concurrency comparison...")
    from concurrency import compare_threads_vs_processes, plot_threads_vs_processes
    from experiments.workloads import MIXED

    concurrency_workload = [
        {"pid": p["pid"], "burst": p["burst"], "io_burst": p.get("io_burst", 0)}
        for p in MIXED
    ]
    concurrency_data = compare_threads_vs_processes(concurrency_workload)
    concurrency_chart = os.path.join(output_dir, "compare_concurrency.png")
    plot_threads_vs_processes(concurrency_data, concurrency_chart)
    print(f"  Threads: {concurrency_data['threads']['elapsed']}s")
    print(f"  Processes: {concurrency_data['processes']['elapsed']}s")

    # Step 3: IPC demo
    print("\n[3/4] Running IPC demos...")
    from ipc import run_ipc_demo as run_ipc

    ipc_workload = [
        {
            "pid": p["pid"],
            "burst": max(1, p["burst"] // 4),
            "io_burst": p.get("io_burst", 0) // 4,
        }
        for p in MIXED
    ]
    ipc_data = run_ipc(ipc_workload)

    # Step 4: Memory comparison
    print("\n[3.5/4] Running memory limits comparison...")
    from experiments.comparisons import compare_memory_limits
    from reporting.charts import plot_memory_comparison

    memory_data = compare_memory_limits(low=256, high=1024, output_dir=output_dir)
    memory_chart = os.path.join(output_dir, "compare_memory.png")
    plot_memory_comparison(memory_data, memory_chart)

    # Step 5: Generate report
    print("\n[4/4] Generating final report...")
    from reporting.generator import generate_final_report
    from experiments.comparisons import compare_algorithms
    from reporting.charts import plot_algorithm_comparison

    from experiments.comparisons import compare_cpu_limits
    from reporting.charts import plot_cpu_limits_comparison

    cpu_data = None
    try:
        cpu_data = compare_cpu_limits(output_dir)
        cpu_chart = os.path.join(output_dir, "compare_cpu_limits.png")
        plot_cpu_limits_comparison(cpu_data, cpu_chart)
    except Exception as e:
        print(f"  CPU limits comparison skipped: {e}")

    comparison = compare_algorithms(all_results)
    chart_path = os.path.join(output_dir, "compare_algorithms.png")
    plot_algorithm_comparison(comparison, chart_path)

    report_path = generate_final_report(
        experiment_results=all_results,
        concurrency_data=concurrency_data,
        ipc_data=ipc_data,
        memory_data=memory_data,
        cpu_data=cpu_data,
        output_dir=output_dir,
    )

    print(f"\n{'=' * 60}")
    print("  ✅ Full evaluation complete!")
    print(f"  📁 Report: {report_path}")
    print(f"  📁 Outputs: {output_dir}/")
    print(f"{'=' * 60}")


def main():
    """
    Main entry point for the OS Scheduler application.
    Parses arguments and runs either GUI or headless mode.
    """
    parser = argparse.ArgumentParser(
        description="OS Scheduler Simulator - Deliverable 3",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                                     # Launch GUI
  python main.py --headless                          # Default headless sim
  python main.py --experiment all                    # Full experiment suite
  python main.py --compare threads_vs_processes      # Concurrency comparison
  python main.py --ipc-demo                          # IPC demos
  python main.py --generate-report                   # Generate final report
  python main.py --full-eval                         # Run everything
        """,
    )

    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run in headless mode (no GUI, output to files)",
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        choices=["fcfs", "sjf", "priority", "round_robin", "mlfq"],
        default="fcfs",
        help="Scheduling algorithm to use (default: fcfs)",
    )
    parser.add_argument(
        "-p",
        "--preset",
        choices=[
            "simple",
            "memory_stress",
            "mixed",
            "cpu_bound",
            "io_bound",
            "mixed_workload",
        ],
        default="simple",
        help="Process workload preset (default: simple)",
    )
    parser.add_argument(
        "-m",
        "--memory-total",
        type=int,
        default=512,
        help="Total memory size in abstract units (default: 512)",
    )
    parser.add_argument(
        "--memory-algo",
        choices=["first_fit", "best_fit", "worst_fit"],
        default="first_fit",
        help="Memory allocation algorithm (default: first_fit)",
    )
    parser.add_argument(
        "-q",
        "--quantum",
        type=int,
        default=2,
        help="Time quantum for Round Robin / MLFQ (default: 2)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="output",
        help="Output directory for headless mode files (default: output)",
    )

    # Deliverable 3 new arguments
    parser.add_argument(
        "--experiment",
        choices=["all"],
        help="Run full experiment suite (all algorithms x all workloads)",
    )
    parser.add_argument(
        "--compare",
        choices=[
            "threads_vs_processes",
            "host_vs_docker",
            "memory_limits",
            "cpu_limits",
        ],
        help="Run a specific comparison analysis",
    )
    parser.add_argument(
        "--ipc-demo", action="store_true", help="Run IPC mechanism demos"
    )
    parser.add_argument(
        "--generate-report",
        action="store_true",
        help="Generate final markdown report from latest experiment data",
    )
    parser.add_argument(
        "--full-eval",
        action="store_true",
        help="Run all experiments, comparisons, and generate report",
    )

    args = parser.parse_args()

    print_banner()

    if args.full_eval:
        run_full_evaluation(args.output_dir)
    elif args.experiment == "all":
        run_experiments(args.output_dir)
    elif args.compare:
        run_comparison(args.compare, args.output_dir)
    elif args.ipc_demo:
        run_ipc_demo(args.output_dir)
    elif args.generate_report:
        generate_report(args.output_dir)
    elif args.headless:
        run_headless(args)
    else:
        run_gui()


if __name__ == "__main__":
    main()
