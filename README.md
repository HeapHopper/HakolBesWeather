# HakolBesWeather!
![HakolBesWeather.png](assets/HakolBesWeather.png)
## Project Description

### Background

As part of BIU-DS18 course the participants needs to submit a python project for **demonstrating the skills** they have gained during the course so far:

- Understanding the Python programming language.
- Working with Data Science oriented Python packages such as `pandas` and `seaborn`.
- Retrieving data form external sources using their API and the `requests` package.
- Creating UI Widgets using the `streamlit` package.
- Working with version-control-systems (Git) to manage and deploy the codebase.

Those skills are all combined to create a basic weather-forecast application.

### Project structure

The project follows MVP guidelines, with location and forecast data being declared as Models,
using Streamlit as View and implementing middle layers as presenters/controllers.

Following Uncle Bob Clean Architecture philosophy, the MVP is implemented such that:
* A forecast widget depends on a forecast date presenter
* The presenter depends on a factory method to create a forecast model
* The factory methods depends on the Model strict definition
* the model is the heart of the program, and has zero knowledge about outer layers

And as Steve Bishop said, ["Clean Architecture is NOT a project structure"](https://medium.com/@stevebishop_89684/clean-architecture-is-not-a-project-structure-b158c9c4163f),
meaning that the widgets, presenters, factories and models should not be stored horizontally, but vertically
using Feature Folders.

## Usage

Using the app is available by Streamlit UI engine ([link](https://hakolbesweather.streamlit.app/))

For local installation:
1. Clone the app repo
2. Use the `pyproject.toml` and `poetry.lock` files for setting up the enviroment
3. run `streamlit run main.py`