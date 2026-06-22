# Data Science Project Template

A data science project template to be used as a reference for future projects. 
Developed by me, [Francisco Bustamante](https://github.com/chicolucio), for beginner 
data science students in my courses and mentorship programs.

Inspiration: [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)

Click the **Use this template** button to create a new repository based on this model.

## Project Structure

```
├── .env                <- Environment variables file (do not commit/version)
├── .gitignore          <- Files and directories to be ignored by Git
├── environment.yml     <- Requirements file to reproduce the analysis environment
├── LICENSE             <- Open-source license (if one is chosen)
├── README.md           <- The main README for developers using this project.
|
├── data                <- Data files for the project.
|
├── models              <- Trained and serialized models, model predictions, or model summaries
|
├── notebooks           <- Jupyter notebooks. The naming convention is a number (for ordering),
│                          the creator's initials, and a short description separated by -, e.g.,
│                          01-fb-initial-data-exploration.
│
|   └──src              <- Source code for use in this project.
|      │
|      ├── init.py  <- Makes it a Python module
|      ├── config.py    <- Basic project configurations
|      └── plots.py     <- Scripts to create exploratory and results-oriented visualizations
|
├── references          <- Data dictionaries, manuals, and all other explanatory materials.
|
├── reports             <- Generated analyses in HTML, PDF, LaTeX, etc.
│   └── images          <- Generated graphics and figures to be used in reports
```

## Environment Setup

1. Clone the repository that will be created from this template.

    ```bash
    git clone REPOSITORY_URL
    ```

2. Create a virtual environment for your project using your preferred environment manager.

    a. If you are using `conda`, export the environment dependencies to the `environment.yml` file:

      ```bash
      conda env export > environment.yml
      ```

    b. If you are using another environment manager, export the dependencies to a `requirements.txt` file or any other format of your choice. Add the file to version control and remove the `environment.yml` file.

3. Check the `notebooks/01-fb-example.ipynb` file for code usage examples.
4. Rename `notebooks/01-fb-example.ipynb` to a name more appropriate for your project, and follow the naming convention for subsequent notebooks.
5. Remove example files and add your project's data files and notebooks.
6. Check the `notebooks/src/config.py` file for basic project configurations. Modify as needed, adding or removing file and directory paths.
7. Update the `references/01_data_dictionary.md` file with your project's data dictionary.
8. Update the `README.md` with information about your specific project.
9. Add a license to the project. Click [here](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) if you need help choosing a license.
10. Rename the `.env.example` file to `.env`.
11. Add sensitive environment variables to the `.env` file.

By default, the `.gitignore` file is already configured to ignore data files and Notebook files (for those using tools like [Jupytext](https://jupytext.readthedocs.io/en/latest/) and similar). Add or remove other files and directories from `.gitignore` as needed. If you want to force-add a Notebook to version control, perform a forced commit using the command `git add --force FILENAME.ipynb`.

For more information on how to use Git and GitHub, [click here](https://cienciaprogramada.com.br/2021/09/guia-definitivo-git-github/). For virtual environments, [click here](https://cienciaprogramada.com.br/2020/08/ambiente-virtual-projeto-python/).