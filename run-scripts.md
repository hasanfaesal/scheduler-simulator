## OS Scheduler Simulator — Codebase Analysis
What it is: A Python desktop/CLI educational tool simulating CPU scheduling algorithms, memory management, concurrency, and IPC. Built for an OS course (3 deliverables).
## How to Run
Task	Command
Install deps	uv pip install -r requirements.txt (only matplotlib + numpy)
Linux GUI prereq	sudo apt-get install python3-tk
Launch GUI	python main.py
Quick start	python quickstart.py (auto-checks + installs deps, launches GUI)
Headless run	python main.py --headless -a <algo> -p <preset>
Full evaluation	python main.py --full-eval
Tests	python test_scenarios.py
Docker	docker build -t scheduler-sim . && docker run --rm scheduler-sim
Docker Compose	docker-compose up (2 containers: 1CPU/512M + 0.5CPU/256M)
## Key Modes
- GUI — Tkinter app with process input, algorithm selection, Gantt charts, memory visualization, AI recommendations
- Headless — CLI mode for containers/scripts, outputs JSON metrics + PNG charts to output/
- Experiments — --experiment all runs 5 algos × 3 workloads
- Comparisons — --compare threads_vs_processes|host_vs_docker|memory_limits|cpu_limits
- IPC demo — --ipc-demo (pipes + shared memory)
Architecture
algorithms/    → FCFS, SJF, Priority, Round Robin, MLFQ
memory/        → Fixed/Variable partitions, Paging, Fit algorithms
gui/           → Tkinter GUI + Matplotlib Gantt charts
concurrency/   → Threads vs Processes comparison
ipc/           → Pipes + Shared Memory demos
experiments/   → Automated experiment runner
reporting/     → Charts + Markdown report generator
adaptive.py    → Workload analysis + algorithm recommendation engine
No database, no API server, no env vars required. Single Python process, self-contained.

## migration to uv:
Task	Command
Install deps	uv sync (uses pyproject.toml) or uv pip install -r requirements.txt
Launch GUI	python main.py
Quick start (auto-install + GUI)	python quickstart.py
Headless simulation	python main.py --headless -a fcfs -p simple
Full evaluation	python main.py --full-eval
Run tests	python test_scenarios.py
Docker build	docker build -t scheduler-sim .
Docker run	docker run --rm --cpus="1.0" --memory="512m" scheduler-sim
Docker compose	docker-compose up
No separate pip/venv step needed — uv sync handles everything, or you can use the --headless flag via docker-compose up directly.