# **aruco-object-drop**: Precision Object Dropping for UAVs

> Welcome aboard!🚀 This framework provides real-time ArUco marker detection and tracking on UAVs for precision object dropping missions, built on top of [OpenCV](https://opencv.org/).

## Table of Contents

- [About](#about)
- [Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Structure](#structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

**aruco-object-drop** is a robust framework designed for real-time ArUco marker detection and tracking on UAVs in outdoor environments, making it ideal for object dropping missions. Developed for [IMAV 2024](https://2024.imavs.org/), this project is centered around the theme of wildlife preservation and aims to enhance precision and robustness in challenging environments.

## Getting Started

To begin using **aruco-object-drop**, you'll need to set up your development environment. Follow the instructions below to get everything up and running smoothly.

### Prerequisites

Before you can use **aruco-object-drop**, ensure you have the following tools installed:

#### 1. **Install `pyenv`**

`pyenv` helps manage multiple Python versions on your system. To install `pyenv`, follow these steps:

1. **Install `pyenv` using pip**:
    ```bash
    pip install pyenv
    ```

2. **Set the global Python version**:
    ```bash
    pyenv install 3.12.4
    pyenv global 3.12.4
    ```

For more information on `pyenv`, visit the [pyenv GitHub page](https://github.com/pyenv/pyenv).

#### 2. **Install `Poetry`**

`Poetry` is a dependency management tool for Python that simplifies package management and project setup.

1. **Install `Poetry` using pip**:
    ```bash
    pip install poetry
    ```

2. **Configure `Poetry` to use the installed Python version** (if necessary):
    ```bash
    poetry env use $(pyenv which python)
    ```

For detailed instructions and more options, refer to the [Poetry documentation](https://python-poetry.org/docs/).

After installing both `pyenv` and `poetry`, you will be ready to install the project dependencies and start using **aruco-object-drop**!


### Installation

Now that your development environment is set up, you are ready to install **aruco-object-drop**. Follow these steps to set up the project and get it running on your local machine:

#### 1. **Clone the Repository**

    Begin by cloning the **aruco-object-drop** repository from GitHub to your local machine.

    ```bash
    git clone https://github.com/kmalkow/aruco-object-drop.git
    ```

#### 2. **Navigate to the Project Directory**

    Once the cloning process is complete, change your working directory to the newly cloned project folder. 
    
    ```bash
    cd aruco-object-drop
    ```

#### 3. **Install Dependencies**

    Once you are in the working directory, install the project’s dependencies using Poetry.

    ```bash
    poetry install
    ```

#### 4. **Activate Virtual Environment**

    After installing the dependencies, activate the virtual environment using the following command:
    
    ```bash
    poetry shell
    ```

    And exit the virtual environment using the following command:

    ```bash
    exit
    ```
    
    These commands activate and exit the virtual environment, allowing you to work with the project's dependencies in isolation from your global Python environment.

#### 5. **Verify the Installation**

   To verify whether the project dependencies are installed correctly, run the following command:

    ```bash
    poetry show
    ```

    If it shows the same __main__ dependencies as in the `pyproject.toml` file, then everything has been installed correctly.

Well done! The **aruco-object-drop** project is now installed correctly and ready for use. If you encounter any issues, seek assistance through the [contact page](#contact).

## Structure

The **aruco-object-drop** project is organized to facilitate ease of navigation and development. Here’s a quick overview:

- **`.github/`**: GitHub workflows and pull request template.
- **`aruco-object-drop/`**: Main directory with:
  - **`data/`**: Project-specific data files.
  - **`docs/`**: Documentation files.
  - **`logs/`**: Log files for tracking variables of interest.
  - **`src/modules/`**: Core functionality for marker detection and tracking.
  - **`src/utils/`**: Utility functions and helpers.
- **`tests/`**: Unit tests for verifying project functionality.
- **`Makefile`**: Automates tasks such as formatting, linting, static type checking, docstring validation, and unit testing.
- **`README.md`**: Project overview and setup instructions.

## Usage

Still a work in progress.

## Contributing

We welcome contributions to enhance **aruco-object-drop**. If you have suggestions, improvements, or bug fixes, please refer to our [Contributing Guidelines](CONTRIBUTING.md) for instructions on how to get involved.

## License

**aruco-object-drop** is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or further information, please contact:

- **Kevin Malkow**
- 📧 Email: [k.malkow@student.tudelft.nl](mailto:k.malkow@student.tudelft.nl)
- 🌐 Project Page: [https://github.com/kmalkow/aruco-object-drop](https://github.com/kmalkow/aruco-object-drop)

---

Thank you for your interest in **aruco-object-drop**. We look forward to your contributions and feedback. Happy coding!



