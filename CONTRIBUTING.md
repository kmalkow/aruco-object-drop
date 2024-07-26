# Contributing
Welcome to the `aruco-object-drop` repository! We appreciate your interest in contributing to our project. By following the guidelines below, you can ensure that your contributions are well-organized and aligned with our coding standards.

Please take a moment to review the guidelines for committing and pushing files, as well as the workflow for contributing to this repository. We have also provided information on the conventional commit format and coding conventions to help you maintain consistency throughout your contributions.

Thank you for your valuable contributions to `aruco-object-drop`!

## Committing and Pushing Files
When contributing to this repository, please follow the guidelines below for committing and pushing files.

### Workflow
To contribute to this repository, follow the steps below:

1. Clone the repository.
2. Create a new branch for your changes.
3. Make the necessary changes.
4. Run `make pre-commit` and commit changes using the guidelines mentioned below.
5. Run `make pre-push` and push your changes to the repository.
6. Open a pull request to the main branch of the repository, following the Pull Request process described below.

### Coding Conventions
When writing Python code, please adhere to the [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines.

### Conventional Commit Format
When writing commit messages, please follow the conventional commit format. The table below explains each topic and its meaning:

| Topic         | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| feat          | A new feature or enhancement                                                |
| fix           | A bug fix                                                                   |
| docs          | Documentation changes                                                       |
| style         | Changes that do not affect the code's functionality (e.g., formatting)      |
| refactor      | Code refactoring                                                            |
| test          | Adding or modifying tests                                                    |
| chore         | Other changes that do not modify the source code (e.g., build tasks)         |

Note: The parentheses () in the commit message are not optional and must be used to provide additional context.

#### Example
- Accepted commit message: `git commit -m "chore(build): Added new build chore."`
- Rejected commit message: `git commit -m "Added new build chore."`

### Hooks
We have implemented the following hooks to ensure code quality and maintain consistency:

- **pre-commit hook**: This hook checks for code format using `black`, linting using `flake8`, static types using `mypy`, and docstrings using `pydocstyle`. Here is an example of code that adheres to all of these guidelines and one that does not:
    - **Example**
        - Accepted code:
            ```python
            def add_numbers(a: int, b: int) -> int:
                """Add two numbers."""
                return a + b
            ```
        - Rejected code:
            ```python
            def addNumbers(a,b):
            return a+b
            ```

- **commit-msg hook**: This hook checks for conventional commit message format as mentioned above.

- **pre-push hook**: This hook runs unit tests using `pytest`. Here is an example that will be accepted and one that will not be:
    - **Example**
        - Accepted unit tests:
            ```python
            def test_add_numbers():
                assert add_numbers(2, 3) == 5
                assert add_numbers(-1, 1) == 0
            ```
        
        - Rejected unit tests:
            ```python
            def test_add_numbers():
                assert add_numbers(2, 3) == 6
                assert add_numbers(-1, 1) == 1 
            ```

You can manually run the pre-commit and pre-push hooks via the `Makefile` commands by executing the following commands in the terminal:

```bash
make pre-commit
make pre-push
```

## Pull Request Process
To submit your changes for review, please follow the steps below:

1. Create a draft pull request with the title formatted as `[PR-X]:`, where `X` is the next consecutive number.
2. Fill in the provided PR template with the necessary details.
3. Make the pull request a draft and wait for approval from the code owner.
4. Once approved, your code will be added to the repository.

## Code of Conduct

This project follows the [Contributor Covenant](http://contributor-covenant.org/version/1/4/) version 1.4. Please review the full version of the code of conduct at [http://contributor-covenant.org](http://contributor-covenant.org).

In summary, we expect all contributors to adhere to the following guidelines:

- Be respectful and inclusive towards others.
- Avoid any form of harassment or discrimination.
- Be open to constructive feedback and ideas.
- Maintain a positive and welcoming environment for everyone.

If you encounter any violations of the code of conduct, please report them to the code owners.

By participating in this project, you agree to abide by the code of conduct.

Thank you for your understanding and cooperation.

---

Thank you for your contributions, happy coding!
