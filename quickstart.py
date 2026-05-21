#!/usr/bin/env python3
"""
Quick Start Guide for OS Scheduler Simulator

This script provides a simple way to get started with the OS Scheduler.
Run this file to check dependencies and launch the application.
"""

import sys
import subprocess
import os


def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required")
        print(f"   You have Python {sys.version_info.major}.{sys.version_info.minor}")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True


def check_and_install_dependencies():
    """Check and install required packages."""
    required_packages = {
        'matplotlib': 'matplotlib',
        'numpy': 'numpy'
    }
    
    missing_packages = []
    
    print("\nChecking dependencies...")
    for import_name, package_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"✓ {package_name} is installed")
        except ImportError:
            print(f"✗ {package_name} is NOT installed")
            missing_packages.append(package_name)
    
    if missing_packages:
        print(f"\n⚠️  Installing missing packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call(['uv', 'pip', 'install'] + missing_packages)
            print("✓ Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            print("   Please install manually: uv pip install -r requirements.txt")
            return False
    
    print("✓ All dependencies are installed")
    return True


def main():
    """Main entry point."""
    print("""
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║    🖥️  OS SCHEDULER SIMULATOR - QUICK START GUIDE     ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
    """)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check and install dependencies
    if not check_and_install_dependencies():
        sys.exit(1)
    
    print("\n" + "="*55)
    print("✓ System check passed - Ready to launch!")
    print("="*55)
    
    print("\nLaunching OS Scheduler Simulator...\n")
    
    # Launch the main application
    try:
        from gui.app import main as start_gui
        start_gui()
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
