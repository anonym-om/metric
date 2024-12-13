# On Evaluation Metrics for Complex Matching based on Reference Alignments

This project is built using Python 3.12. Below are the instructions to install the necessary dependencies to run the project.

## Prerequisites

- Python 3.12

## Data

The data used in this project comes from OAEI 2020. Download the data from the following links and unzip the matchers outputs in each corresponding folder:
`edoal/hydrography` -> [Hydrography Results 2020](https://oaei.ontologymatching.org/2020/results/complex/hydrography/hydrography_results_2020.zip)
`edoal/populated_conference` -> [Populated Conference Results 2020](https://oaei.ontologymatching.org/2020/results/complex/popconf/results_conference.zip)
`edoal/populated_geolink` -> [Populated Geolink Results 2020](https://oaei.ontologymatching.org/2020/results/complex/popgeolink/popgeolink_results_2020.zip)

## Installation

1. **Create a virtual environment:**

    ```bash
    python3.12 -m venv venv
    ```

2. **Activate the virtual environment:**

    - On Linux or macOS:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
   
4. **Run:**

    ```bash
    python main.py
    ```


