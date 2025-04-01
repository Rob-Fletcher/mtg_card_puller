# mtg_card_puller

Pull MTG card images in b

## Installation and Basic Usage
Setup a conda env so we dont mess up the system python
```bash
conda env create -n mtgp python=3.10 -y
conda activate mtgp
```

Now install the script from pypi:
```bash
pip install mtg-card-puller
```

Now create a folder in the desired location for the images.
```bash
mkdir my_folder_name
cd my_folder_name
```

Download the mox file to this directory. This should be the file that has the series and card
numbers on each line like this:
```txt
1 Mr. House, President and CEO (PIP) 7 *F*
1 Arcane Signet (M3C) 283
1 Arid Mesa (MH2) 244
1 Attempted Murder (UNF) 66 *F*
1 Automated Artificer (NEO) 239 *F*
```

Now you just need to run the script in this folder and pass the file name to the `-f` option:
```bash
mtg_card_puller -f mox_file_name.txt
```

You should see a status bar appear that tells you which card it is currently working on. Once this
is done, you should have all of the pngs for each card in the list in the current folder.


## Development

## Installation For Dev
To setup mtg_card_puller create a conda environment with the generated `environment.yaml`.
This sets up a development environment with all the required packages. This is what is used when building 
out the functionality of this project.
```bash
conda env create -f environment.yaml
conda activate mtg_puller
```

Then install the python module. This installs the module the same way as if someone just wanting 
to use this package would install it. This is what is used when using this package as a dependency.
**Note:** This installs the `dev` extra dependencies. When installing this to use as a standalone package,
you should leave off the `[dev]` part.
```bash
python -m pip install .[dev]
```

If functionality from this repo is needed in another project, you can install this package as a dependency
directly from the GitHub repo.
```bash
python -m pip install git+https://github.com/seerai/mtg_card_puller.git
```

You can then test that the docker image builds and runs correctly.
```bash
docker build -t mtg_card_puller:latest .
```
Once the build is complete, test the image:
```bash
docker run --rm mtg_card_puller:latest
```
You should see a message printed:
```
Replace this message by putting your code into mtg_card_puller.cli.main
See click documentation at https://click.palletsprojects.com/
```

### READMEs and Notes
Every folder in this project other than `mtg_card_puller`` should have a README.md
file (the template does this automatically for all folders). Each of these READMEs should be kept 
up to date and should describe the contents of the folder. This is especially important for the
the data folder and should include all data files, their sources and how to download them. This
is also a good place to put any notes about the contents of the folder. For example, if you are
working on a notebook and want to save some notes about what you are doing, you can put them in
the README for that folder. **You should always be asking yourself** "If someone else were to look at
this folder, would they know what is going on?". If the answer is no, then you should add more
information to the README.

### Dependency Management
When developing on this project, **make sure that you never directly `pip install` any packages**. This
leads to situations where peoples environemnts are different and the code will not run correctly
when another person tries to install the package. Instead, always add the dependency to the
`pyproject.toml` file and reinstall the package. This ensures that all dependencies are tracked and
others can use this package without issue. When possible, you should also pin a version or version range
of the dependency. i.e. `numpy==1.19.2` or `numpy>=1.19.2,<1.20.0`.

### Testing
Any functions implemened in this package should be covered by tests if possible. This doesnt mean that
every line of code needs to be tested, but that the functionality of the code is tested. Anything 
that is used only for development purposes can sometimes be excluded from testing. However, any 
function/class you expect someone to use after installing this as a package should be tested. 
**You should always be asking yourself** "If someone else were to use this code, would they know that it
works correctly?". If the answer is no, then you should add tests.

This project uses `pytest` for testing. To run the tests, cd to the root of the project and run:
```bash
coverage run -m pytest
```
This will run all the tests and generate a coverage report. To view the coverage report, run:
```bash
coverage report
```
