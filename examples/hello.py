"""Run from the repository root: python3 examples/hello.py."""


def greeting(name="iPad"):
    """Return a greeting; blank names use the default device name."""
    name = name.strip() or "iPad"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greeting())
