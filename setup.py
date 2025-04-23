from setuptools import setup, find_packages

setup(
    name="nlp2sql",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "sqlalchemy",
        "pandas",
        "fastapi",
        "uvicorn"
    ],
    author="Seu Nome",
    description="Biblioteca para converter linguagem natural em SQL com OpenAI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
