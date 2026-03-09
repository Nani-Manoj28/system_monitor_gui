# System Monitor Dashboard (Python)

## Overview

The System Monitor Dashboard is a desktop application built using Python that allows users to monitor system resource usage in real time. The application displays CPU usage, RAM usage, and Disk usage using graphical progress bars in a simple and user-friendly interface.

The project uses the Tkinter library for the graphical user interface and the psutil library to collect system performance statistics.

## Features

* Real-time CPU usage monitoring
* RAM usage tracking
* Disk usage monitoring
* Graphical progress bars for resource visualization
* Automatic refresh every second
* Warning message when system usage becomes high
* Manual refresh button

## Technologies Used

* Python
* Tkinter (GUI)
* psutil (System monitoring library)

## Installation

1. Install Python (version 3.7 or higher recommended).
2. Install the required library:

```
pip install psutil
```

3. Download or clone the repository.

## How to Run

1. Navigate to the project folder.
2. Run the Python file:

```
python system_monitor_gui.py
```

3. The System Monitor window will open and start displaying system usage automatically.

## Project Structure

```
system-monitor/
│
├── system_monitor_gui.py
└── README.md
```

## Future Improvements

* Add GPU monitoring
* Add graphical charts for usage history
* Add dark mode UI
* Add notifications for critical system usage

## Author

Manoj Nani
Electronics and Communication Engineering (ECE)

## License

This project is for educational and learning purposes.
