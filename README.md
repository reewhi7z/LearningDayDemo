# LearningDayDemo

If you're running this on your local pc (not Simcenter Studio), please follow these steps to get setup

1. If you don't already have Python installed on your pc, install it from here https://www.python.org/downloads/

2. Clone this repo into a new project folder

3. Create a new virtual environment for Python. Run the following command in your project folder
    ```bash
    $ python -m venv venv
    ```

4. Activate your virtual environment
    ```bash
    $ .\venv\Scripts\activate
    ```

5. Install the required Python packages
    ```bash
    $ pip install fmpy[complete] plotly scipy ipython jupyter
    ```


# Running the example Notebooks

To run the notebooks, please change the FMU filename to match your OS (Win or Linux) and make sure you're connected to the Siemens network (either on the VPN or be on the office network). The Flomaster FMUs need to connect to a license server to run


# The fmpy GUI

If you're running this on your pc/laptop and want to show the fmpy GUI that was shown in the demo, run the following with your virtual environment activated:
```bash
$ python -m fmpy.gui
```