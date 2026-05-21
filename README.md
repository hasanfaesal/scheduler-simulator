# OS Scheduler Simulator - Deliverable 1

A comprehensive CPU scheduling simulation platform with multiple algorithms, real-time visualization, and performance metrics analysis.

## 🎯 Project Overview

This application implements five classic CPU scheduling algorithms and provides an interactive GUI to compare their performance on various workloads. It includes real-time Gantt chart visualization, detailed metrics calculation, and AI-based algorithm recommendations.

## ✨ Features

### 1. Scheduling Algorithms
- **FCFS** (First Come First Served) - Non-preemptive, fair scheduling
- **SJF** (Shortest Job First) - Non-preemptive, optimal average waiting time
- **Priority Scheduling** - Non-preemptive, supports process priorities
- **Round Robin** - Preemptive, configurable time quantum
- **MLFQ** (Multi-Level Feedback Queue) - Adaptive scheduling with 3-level queues

### 2. GUI Interface (Tkinter)
- **Process Management**: Dynamically add processes with arrival time, burst time, and priority
- **Algorithm Selection**: Choose any of the 5 scheduling algorithms
- **Simulation Controls**: Start, Pause, Resume, and Reset buttons
- **Real-time Results**: View metrics and process details immediately after simulation
- **Gantt Chart Visualization**: Color-coded process execution timeline
- **AI Recommendations**: Get intelligent algorithm suggestions based on workload characteristics

### 3. Performance Metrics
Automatically calculated for each simulation:
- **Waiting Time**: Average and per-process waiting time
- **Turnaround Time**: Average and per-process turnaround time
- **CPU Utilization**: Percentage of CPU busy time
- **Throughput**: Number of processes completed per unit time

### 4. Adaptive Features
- **Workload Analysis**: Analyzes process characteristics
- **Algorithm Recommendations**: Suggests best algorithm for current workload
- **Characteristic Identification**: Identifies workload properties:
  - Uniform vs varied burst times
  - Short, medium, or long jobs
  - Clustered vs spread arrivals
  - Prioritized vs non-prioritized workloads

### 5. Visualization
- **Interactive Gantt Chart**: 
  - Process ID labels
  - Time axis with grid
  - Color-coded process bars
  - Proper scaling and padding
  - Save as PNG image
- **Metrics Display**: Formatted tables with all performance metrics
- **Process Details**: Comprehensive process execution timeline

## 📋 Project Structure

```
os-scheduler/
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── algorithms/
│   ├── fcfs.py               # FCFS algorithm
│   ├── sjf.py                # SJF (preemptive & non-preemptive)
│   ├── priority.py           # Priority scheduling
│   ├── round_robin.py        # Round Robin scheduling
│   └── mlfq.py               # MLFQ algorithm
├── gui/
│   ├── app.py                # Main Tkinter GUI application
│   └── gantt.py              # Gantt chart visualization
├── metrics.py                # Performance metrics calculator
└── adaptive.py               # Adaptive scheduler recommendations
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### Installation

1. Clone or extract the project:
```bash
cd os-scheduler
```

2. Install dependencies:
```bash
uv pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

The GUI window will open with all the necessary controls.

## 📖 User Guide

### Adding Processes

1. Enter the process parameters:
   - **Arrival Time**: When the process arrives in the ready queue
   - **Burst Time**: CPU time required by the process
   - **Priority**: Priority level (1 = highest, higher numbers = lower priority)

2. Click **"Add Process"** to add it to the list

3. Repeat for additional processes

### Running a Simulation

1. Select a **scheduling algorithm** from the options
2. If using Round Robin or MLFQ, set the **Time Quantum**
3. Click **"▶ Start"** to run the simulation
4. View results in the tabs:
   - **📊 Metrics**: Performance calculations
   - **📈 Gantt Chart**: Visual timeline
   - **📋 Details**: Detailed process information

### Getting AI Recommendations

1. Add your processes
2. Click **"Get Recommendations"** in the AI Recommendations section
3. View the suggested algorithms based on workload analysis

### Saving Results

- **Show Gantt Chart**: Displays interactive matplotlib figure
- **Save Chart**: Exports Gantt chart as PNG image

## 📊 Metrics Explanation

### Average Waiting Time
The average time each process spends waiting in the ready queue before getting CPU time.
- **Formula**: Sum of all waiting times / Number of processes
- **Lower is better**: Indicates responsive scheduling

### Average Turnaround Time
The average time from when a process arrives until it completes.
- **Formula**: Sum of all turnaround times / Number of processes
- **Lower is better**: Indicates efficient scheduling

### CPU Utilization
The percentage of time the CPU is busy executing processes.
- **Formula**: (Total busy time / Total available time) × 100%
- **Higher is better**: Indicates minimal CPU idle time

### Throughput
The number of processes completed per unit of time.
- **Formula**: Number of processes / Total execution time
- **Higher is better**: Indicates more processes scheduled in less time

## 🧠 Adaptive Features

The system analyzes workload characteristics and recommends optimal algorithms:

### Workload Characteristics Identified
- **Burst Time Variance**: Uniform, mixed, or highly varied
- **Job Duration**: Short, medium, or long jobs
- **Arrival Pattern**: Clustered or spread arrivals
- **Priority Distribution**: Prioritized or non-prioritized

### Recommendation Logic
The adaptive scheduler uses rule-based recommendations:
- Short jobs → **SJF** (optimal waiting time)
- Prioritized workload → **Priority** or **MLFQ**
- Clustered arrivals → **FCFS** (fair scheduling)
- Long jobs with varied times → **MLFQ** (prevents starvation)
- Interactive/fair behavior → **Round Robin**
- Uniform workload → **FCFS** (minimal overhead)

## 🔬 Algorithm Comparison

| Feature | FCFS | SJF | Priority | Round Robin | MLFQ |
|---------|------|-----|----------|-------------|------|
| Simplicity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| Fairness | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Throughput | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Response Time | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Starvation Risk | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

## 📚 Example Scenarios

### Scenario 1: Batch Processing (Uniform Jobs)
```
Processes:
- P1: Arrival=0, Burst=10, Priority=1
- P2: Arrival=1, Burst=10, Priority=1
- P3: Arrival=2, Burst=10, Priority=1

Recommended: FCFS
Reason: Uniform burst times, fair scheduling needed
```

### Scenario 2: Time-sharing System (Short, Mixed Jobs)
```
Processes:
- P1: Arrival=0, Burst=3, Priority=1
- P2: Arrival=1, Burst=2, Priority=1
- P3: Arrival=2, Burst=5, Priority=2

Recommended: SJF
Reason: Short jobs with mixed times
```

### Scenario 3: Real-time System (Prioritized)
```
Processes:
- P1: Arrival=0, Burst=5, Priority=1 (critical)
- P2: Arrival=1, Burst=3, Priority=2 (important)
- P3: Arrival=2, Burst=8, Priority=3 (normal)

Recommended: Priority or MLFQ
Reason: Explicit priorities, need for priority handling
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError" when running
**Solution**: Install required packages
```bash
uv pip install -r requirements.txt
```

### Issue: Gantt chart doesn't display
**Solution**: Ensure matplotlib and numpy are installed
```bash
uv pip install --upgrade matplotlib numpy
```

### Issue: GUI appears frozen
**Solution**: Click "Reset" button to clear simulation state, then try again

## 📈 Performance Tips

- **Small workload (< 10 processes)**: All algorithms run instantly
- **Medium workload (10-50 processes)**: Slight delay for MLFQ due to complexity
- **Large workload (> 50 processes)**: Recommended to use simpler algorithms for faster results

## 🎓 Educational Value

This project demonstrates:
- Classic CPU scheduling algorithms in practice
- GUI development with Tkinter
- Data visualization with Matplotlib
- Performance metric calculation
- Workload analysis and optimization
- Comparative algorithm analysis

## 📝 Deliverable Components

This project fulfills all Deliverable 1 requirements:

✅ **1. GUI (gui/app.py)**
- Tkinter-based interface for dynamic process input
- Buttons for Start, Pause, Resume, and Reset
- Real-time metrics display

✅ **2. Visualization (gui/gantt.py)**
- Real-time color-coded Gantt chart
- Process state updates
- Time axis with labels
- Export functionality

✅ **3. Metrics (metrics.py)**
- Average Waiting Time calculation
- Turnaround Time calculation
- CPU Utilization percentage
- Throughput computation

✅ **4. Adaptive Features (adaptive.py)**
- Runtime algorithm switching capability
- Workload analysis and recommendations
- Algorithm comparison and suggestions

✅ **5. Integration (main.py)**
- Connects all components
- Launches the GUI
- Error handling and dependency checking

## 🤝 Contributing

This is an educational project. Suggestions for improvements are welcome!

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Developer Notes

### Key Design Decisions

1. **Tkinter for GUI**: Cross-platform, no external dependencies initially
2. **Matplotlib for Visualization**: Industry-standard, publication-quality charts
3. **Modular Architecture**: Each algorithm and component is separate and reusable
4. **Rule-based Adaptive System**: Interpretable recommendations based on workload
5. **Comprehensive Metrics**: Multiple dimensions for algorithm comparison

### Future Enhancements

- Web-based interface using Flask/Django
- Support for more complex scheduling scenarios
- Machine learning-based algorithm recommendations
- Real-time process simulation with animation
- Statistical analysis and comparison tools
- Export results to CSV/PDF

## 📞 Support

For issues or questions, please check:
1. This README file
2. Code comments and docstrings
3. Algorithm documentation in respective files

---

---

## 🐳 Deliverable 2: Containerization, Memory Management & Resource-Constrained Scheduling

### New Features

#### 6. Docker-Based Deployment
- **Dockerfile** with Python 3.11 slim, Tkinter/matplotlib dependencies
- **docker-compose.yml** with CPU/memory resource limits for multiple instances
- Headless mode for containerized execution (no GUI required)

```bash
# Build and run
docker build -t scheduler-sim .
docker run --cpus="1.0" --memory="512m" scheduler-sim

# Run multiple instances with different limits
docker-compose up
```

#### 7. Memory Management Module (`memory/`)
- **Fixed Partition Allocation** — pre-divided memory blocks
- **Variable Partition Allocation** — dynamic splitting with merge on free
- **Paging Simulation** — page tables, frame allocation, page fault tracking
- **Allocation Algorithms**:
  - First Fit
  - Best Fit
  - Worst Fit
- **Memory Visualization** — Matplotlib charts of allocation state

#### 8. Resource-Constrained Scheduling
- Processes include `memory_req` (abstract memory units)
- Scheduling respects both CPU and memory availability
- Memory wait time tracking (time spent waiting for allocation)
- Extended metrics: memory utilization, memory wait, allocation success rate

#### 9. Headless CLI Mode
Run simulations without GUI for containers or automation:

```bash
# Basic headless run
python main.py --headless -a fcfs -p simple

# With memory constraints
python main.py --headless -a mlfq -p memory_stress -m 400 --memory-algo best_fit

# All algorithms
python main.py --headless -a round_robin -p mixed -q 3
```

Outputs: `metrics_*.json`, `gantt_*.png`, `memory_*.png`, `details_*.txt`

#### 10. Linux Monitoring Integration (`monitor/`)
Wrappers for system tools:
- `top` / `ps aux` — process monitoring
- `docker stats` — container resource usage
- `/proc/meminfo`, `/proc/stat` — memory and CPU parsing
- Side-by-side logging of simulator vs real system metrics

```bash
python demo/monitor_demo.py -a round_robin -p mixed
```

#### 11. Process Isolation Demos
- **`demo/isolation.sh`** — PID namespace demonstration
- **`demo/resource_limits.sh`** — CPU/memory throttling effects
- **`docs/docker-flags.md`** — Complete Docker flags reference

### Updated Project Structure

```
os-scheduler/
├── main.py                       # Entry point (GUI + CLI)
├── headless.py                   # Headless simulation runner
├── Dockerfile                    # Container configuration
├── docker-compose.yml            # Multi-instance orchestration
├── requirements.txt              # Dependencies
│
├── algorithms/                   # Scheduling algorithms
│   ├── fcfs.py
│   ├── sjf.py
│   ├── priority.py
│   ├── round_robin.py
│   └── mlfq.py
│
├── memory/                       # NEW: Memory management
│   ├── partitions.py
│   ├── paging.py
│   ├── algorithms.py
│   └── visualizer.py
│
├── monitor/                      # NEW: System monitoring
│   └── system.py
│
├── gui/
│   ├── app.py                    # Updated with memory input
│   └── gantt.py
│
├── metrics.py                    # Updated with memory metrics
├── adaptive.py
│
├── demo/                         # NEW: Demonstration scripts
│   ├── isolation.sh
│   ├── resource_limits.sh
│   └── monitor_demo.py
│
├── docs/
│   ├── deliverable-2.md          # Full technical report
│   └── docker-flags.md
│
└── output/                       # Generated artifacts
```

### Quick Commands

```bash
# GUI mode
python main.py

# Headless simulation
python main.py --headless -a fcfs -p simple

# Docker with limits
docker run --cpus="0.5" --memory="256m" scheduler-sim

# Memory stress test
python main.py --headless -a best_fit -p memory_stress -m 512

# Monitoring demo
python demo/monitor_demo.py

# Isolation demo
./demo/isolation.sh

# Resource limits demo
./demo/resource_limits.sh
```

---

**Version**: 2.0
**Last Updated**: May 2026
**Status**: Complete - Deliverables 1 & 2
