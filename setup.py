from setuptools import setup, find_packages

setup(
    name="mlops_project_1",
    version="0.1",
    author="Sarthak",
    packages=find_packages(),
    install_requires=[
    "numpy",
    "pandas",
    "scikit-learn",
    "google-cloud-storage",
    "pyyaml",
    "imbalanced-learn",
    "lightgbm",
    "mlflow",
    "flask"
],
)