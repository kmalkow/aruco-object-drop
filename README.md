
![Screenshot from 2023-09-17 22-35-36](https://github.com/user-attachments/assets/62dd7b2e-0fcf-4e8d-97e4-80312773b47d)

# aruco-object-drop
> Welcome aboard!🚀 This framework enables precise object dropping for UAVs through a real-time ArUco marker detection and tracking system, built on top of [OpenCV](https://opencv.org/) in Python.

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Structure](#structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About
The **aruco-object-drop** framework is designed for precise object dropping missions with UAVs. Its goal is to accurately drop an object from a UAV onto a 15x15 cm ArUco marker in outdoor settings. The framework features a real-time ArUco marker detection and tracking system that operates onboard, engineered to be robust and effective in challenging outdoor environments. Developed for the [IMAV 2024](https://2024.imavs.org/) competition, this project focuses on wildlife preservation and aims to enhance precision and reliability in demanding conditions.

## Installation
To begin using **aruco-object-drop**, you will need to set up your development environment, clone the repository, and ensure all dependencies are installed. Follow the instructions below to get everything up and running smoothly.

### 1. **Install `pyenv`**
`pyenv` helps manage multiple Python versions on your system. To install `pyenv`, follow these steps:

- **Install `pyenv` using pip**:
    ```bash
    pip install pyenv
    ```

- **Set the local Python version**:
    ```bash
    pyenv install 3.12.4
    cd aruco-object-drop
    pyenv local 3.12.4
    ```

For more information on `pyenv`, visit [this](https://github.com/pyenv/pyenv) page.

### 2. **Install `poetry`**
`poetry` is a dependency management tool for Python that simplifies package management and project setup. To install `poetry`, follow these steps:

- **Install `poetry` using pip**:
    ```bash
    pip install poetry
    ```

- **Configure `poetry` to use the installed Python version**:
    ```bash
    poetry env use python3.12
    ```

For more information on `poetry`, visit [this](https://python-poetry.org/docs/) page.

### 3. **Clone the Repository**
```bash
git clone https://github.com/kmalkow/aruco-object-drop.git
```

### 4. **Navigate to the Project Directory**    
```bash
cd aruco-object-drop
```

### 5. **Install Dependencies**
```bash
poetry install
```

### 6. **Activate Virtual Environment**
Activate the virtual environment using the following command:
    
```bash
poetry shell
```

And exit the virtual environment using the following command:

```bash
exit
```
    
These commands activate and exit the virtual environment, allowing you to work with the project's dependencies in isolation from your global Python environment.

### 7. **Verify the Installation**
To verify whether the project dependencies are installed correctly, run the following command:

```bash
poetry show
```

If it shows the same dependencies as in the `pyproject.toml` file, then everything has been installed correctly.

Well done! The **aruco-object-drop** framework has been installed correctly and is ready for use. If you encounter any issues, seek assistance through the [contact page](#contact).

## Structure
The **aruco-object-drop** project is organized as follows:

- `.github/`: GitHub workflows and pull request template.
- `aruco-object-drop/`: Main directory with:
  - `data/`: Data files.
  - `docs/`: Documentation.
  - `logs/`: Log files.
  - `src/modules/`: Marker detection and tracking.
  - `src/utils/`: Utility functions.
- `tests/`: Unit tests.
- `Makefile`: Task automation (formatting, linting, testing, etc.).
- `README.md`: Project overview and setup.

## Usage

Still a work in progress.

## Contributing

We welcome contributions to enhance **aruco-object-drop**. If you have suggestions, improvements, or bug fixes, please refer to our [Contributing Guidelines](CONTRIBUTING.md) for instructions on how to get involved.

## License

The **aruco-object-drop** framework is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or further information, please contact:

- Kevin Malkow
- 📧 Email: [k.malkow@student.tudelft.nl](mailto:k.malkow@student.tudelft.nl)
- 🌐 Code Owner Page: [https://github.com/kmalkow](https://github.com/kmalkow)

---

Thank you for your interest in **aruco-object-drop**. We look forward to your contributions and feedback. Happy coding!



