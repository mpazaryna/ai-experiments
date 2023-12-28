# Python Environments

## venv

```sh
python3 -m venv venv
source venv/bin/activate
deactivate
```

## Conda

```sh
# create and activate a new enviroment
conda create --name py3.12 python=3.12 
conda activate py3.12
```

```sh
# list all available environments
conda env list
```

```sh
# activate and install a package to condo
conda activate py35
conda install -c conda-forge python-pdfkit
```

```sh
conda env export > environment.yml
```

```sh
conda env create -f environment.yml
```

## Requirements File

In Python, a `requirements.txt` file is commonly used to specify and manage the dependencies of a project. Dependencies are external libraries or packages that your Python project relies on to function correctly. Here's a summary of how you use a `requirements.txt` file:

1. Creating a `requirements.txt` file:
   - You can create a `requirements.txt` file manually in the root directory of your project or use a command-line tool to generate it.

2. Listing dependencies:
   - In the `requirements.txt` file, you list the names and versions of the Python packages your project depends on. Each package should be on a separate line.
   - You can specify dependencies in different ways:
     - `package-name`: This will install the latest version of the package.
     - `package-name==1.2.3`: This specifies a specific version of the package.
     - `package-name>=1.2.3`: This specifies a minimum version requirement.
     - `package-name<=1.2.3`: This specifies a maximum version requirement.

3. Updating and installing dependencies:
   - To update or install the dependencies listed in your `requirements.txt` file, you can use the `pip` package manager. Run the following command in your terminal:

    ```sh
    pip install -r requirements.txt
    ```

   - This command reads the `requirements.txt` file and installs all the specified packages along with their required versions.

4. Managing versions:
   - It's important to specify versions for your dependencies to ensure that your project works consistently. You can use version constraints (e.g., `==`, `>=`, `<=`) to define acceptable versions.
   - You can use tools like `pip freeze` to generate a `requirements.txt` file from your current environment's installed packages. However, it's a good practice to review and manually curate the `requirements.txt` file to avoid issues caused by unwanted or unnecessary package versions.

5. Sharing and collaboration:
   - By including a `requirements.txt` file in your project, you make it easier for others to set up the same environment with the required dependencies. This is crucial for collaboration and ensuring that everyone is using the same versions of packages.
   - You can also use version control systems like Git to track changes in your `requirements.txt` file and collaborate with others effectively.

In summary, a `requirements.txt` file is a simple and effective way to manage and document the dependencies of your Python project. It helps ensure that your project is reproducible and can be easily shared with others.

## Monorepo and Requirements.txt

It seems as if in Github codespaces, I've had repeated problems with trying to run good code in the monorepo when I've got the requirements.txt file at the root level.  For an experiment, I removed it and built the .env from the file found in courses/deeplake.

