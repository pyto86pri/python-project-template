from subprocess import check_call


def test() -> None:
    check_call(["pytest", "-v", "tests"])


def cov() -> None:
    check_call(
        ["coverage", "run", "--source", "python_project", "-m", "pytest", "tests"]
    )
    check_call(["coveralls"])


def lint() -> None:
    check_call(["flake8", "--config=setup.cfg", "python_project", "tests"])


def format() -> None:
    check_call(["isort", "python_project", "tests"])
    check_call(["black", "python_project", "tests"])


def typecheck() -> None:
    check_call(["mypy", "--config-file=setup.cfg", "python_project", "tests"])
