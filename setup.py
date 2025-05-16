from setuptools import setup, find_packages

setup(
    name="gerador_plano_aula",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'crewai',
        'python-docx',
        'python-dotenv'
    ],
)