# Final-Project-Template
<!-- Edit the title above with your project title -->

## Project Overview

## Self Assessment and Reflection

<!-- Edit the following section with your self assessment and reflection -->

### Self Assessment
<!-- Replace the (...) with your score -->

| Category          | Score    |
| ----------------- | -------- |
| **Setup**         | 10 / 10 |
| **Execution**     | 17 / 20 | - This is because I couldn't figure out: How to set the y-axis to start from 0; the negative correlation with one of my linear regression models 
| **Documentation** | 10 / 10 |
| **Presentation**  | 27 / 30 | - I think I did good at presenting overall (just not the best presenter in general!)
| **Total**         | 64 / 70 |

### Reflection
<!-- Edit the following section with your reflection -->

#### What went well?
- The visualizations part went really well for me. Also, the linear regression models as I was able to predict values for one of them. Overall, I'm happy with my project!
#### What did not go well?
- I had a hard time importing data on my system especially from the online PDF (ended up manually copying the data into Excel).
#### What did you learn?
- EDA, visualizations, linear regression models. Also, even though I was unable to import data directly from the online PDF (due to the type of the PDF I believe), I learned how to do so for both text and table imports.
#### What would you do differently next time?
- Find easy-to-import datasets (it can be difficult however, on topics such as mine- because in this case, the most reliable source was NHTSA or The National Highway Traffic Safety Administration).
---

## Getting Started
### Installing Dependencies

To ensure that you have all the dependencies installed, and that we can have a reproducible environment, we will be using `pipenv` to manage our dependencies. `pipenv` is a tool that allows us to create a virtual environment for our project, and install all the dependencies we need for our project. This ensures that we can have a reproducible environment, and that we can all run the same code.

```bash
pipenv install
```

This sets up a virtual environment for our project, and installs the following dependencies:

- `ipykernel`
- `jupyter`
- `notebook`
- `black`
  Throughout your analysis and development, you will need to install additional packages. You can can install any package you need using `pipenv install <package-name>`. For example, if you need to install `numpy`, you can do so by running:

```bash
pipenv install numpy
```

This will update update the `Pipfile` and `Pipfile.lock` files, and install the package in your virtual environment.

## Helpful Resources:
* [Markdown Syntax Cheatsheet](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Dataset options](https://it4063c.github.io/guides/datasets)