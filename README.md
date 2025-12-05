# Crime Description Prediction Based on Spatial-Temporal Data

**Python:** `3.11.14`   
**conda (Anaconda):** `24.11.3`

## Project Description


*This project applies classification models to Baltimore crime data to predict the description of a crime based on features like location, time, and premise type. The dataset includes major crimes against people reported under the NIBRS system.*

[Link of the dataset](https://data.baltimorecity.gov/datasets/baltimore::nibrs-group-a-crime-data/about)

---
The UI based on streamlit can be accessed publicly from the link which is hosted in streamlit's community cloud, **but do note if the number of website visitors is low** or even none, which is expected, **the working link can switch to sleeping/hibernation mode**. **This does not mean, the link will stop working**, but rather **it can take up couple of minutes till the website wakes up** and is functional to use.

**Streamlit App Link** (*give it some minutes to wake up*)

`https://mlda-cw1-15775-baltimore.streamlit.app`

---

## Prerequisities

* `conda 24.11.3` (*if not available then follow the instructions [here](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html#regular-installation) based on your OS. For this project Anaconda was used.*)
* `Python 3.11.14`
* `jupyter 1.1.1`

## Running the program locally

However if you want to `git clone` and make the program work locally, then do the following setups:
```shell
git clone https://github.com/00015775/MLDA-CW1-15775
```
```shell
cd MLDA-CW1-15775
```

`environments.yml` related to this project should be at the root directory, and if not found, then `cd` to where it is located. The below given command, recreates the conda environment with exact package versions. After than, simply activate the conda environment.

```shell
conda env create -f environments.yml
```
```shell
conda activate baltimore_crime_env
```

The model is already trained and saved in the corresponding folder, for more info scroll below of where it is. Basically, to run the Streamlit ui app locally, run the following command, and if `.py` is not found, then `cd` to where the `baltimore-crime-app.py` is located.

```shell
streamlit run ui/baltimore-crime-app.py
```


Streamlit will prompt to ask your gmail for its news feed, simply leave it empty(if you do not need that). After that, from the terminal you should see `Local URL:` or `Network URL:`, either of them if pasted to brower should open the website and you are ready to specify the inputs and get your predicted grade(G3).

---
You can see two environment files listed here `requirements.txt` and `environments.yml`. Basically, `environments.yml` is used for recreating the conda environment which you should use, but `requirements.txt` is created only for the Streamlit app, since it cannot download dependencies from `.yml`

---

Reading the `reproducibility.md` is *completely optional*, it is a self-note for making further conda environment reproducible and OS agnostic.

---

## Folder Tree Structure 

```
MLDA-CW1-15775/  
├── paper/
│   └── MLDA-CW1-15775-REPORT.pdf          # project description
│
├── src/            
│   ├── baltimore-crime-data.ipynb 
│   ├── models/                     # contains trained models
│   ├── plots/                      # any related diagrams
│   └── data/                       # dataset itself
│
├── ui/  
│   └── baltimore-crime-app.py       
├── .gitignore  
└── README.md  
```

## Machine Learning algorithms

* RandomForestClassifier
* HistGradientBoostingClassifier
* CatBoostClassifier

## Model evaluation metrics

* Accuracy
* Precision
* Recall
* F1-score

## Hyperparameter tunning 

`GridSearchCV` was used for finding the best values for `n_estimators` for Random Forest model individually. However, due to the time consuming nature of cross validation, for HistGradientBoostingClassifier and CatBoostClassifier the hyperparameters were chosen manually through heuristic experimentation of trying out different values for parameters such as `max_iter`, `learning_rate` and `depth`. Basically, the higher values for those parameters yielded better accuracy, however at the cost of computational power and time.

#### As for the reference, most of the libraries, coding examples and information were learned from [GeeksForGeeks](https://www.geeksforgeeks.org)
