# Student Final Grade (G3) Prediction model

**Python:** `3.11.14`

## Project Description


*The user can specify 20 deterministic inputs features, and the model with 70% to 85% accuracy can provide the predicted final score (G3).*


---
The UI based on streamlit can be accessed publicly from the link which is hosted in streamlit's community cloud, **but do note if the number of website visitors is low** or even none, which is expected, <ins>the working link can switch to sleeping/hibernation mode<ins>. <ins>**This does not mean, the link will stop working**, but rather **it can take up from within 30 seconds to couple of minutes till the website wakes up** and is functional to use<ins>.

**Streamlit App Link** (*give it some minutes to wake up*)

`http://mlda-cw1-15775-student-performance-ui.streamlit.app `

---

## Running the program locally

However if you want to `git clone` and make the program work locally, then do the following setups:

1. `git clone https://github.com/00015775/MLDA-CW1-15775`

2. `cd MLDA-CW1-15775`

`environments.yml` related to this project should be at the root directory, and if not found, then `cd` to where it is located. The below given command, recreates the conda environment with exact package versions. After than, simply activate the conda environment.

3. `conda env create -f environments.yml`

4. `conda activate ml_student_performance_env`


The model is already trained and saved in the corresponding folder, for more info scroll below of where it is. Basically, to run the Streamlit ui app locally, run the following command, and if `.py` is not found, then `cd` to where the `student_performance_ui_app.py` is located.


5. `streamlit run ui/student_performance_ui_app.py` 


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
│   └── MLDA_CW1_15775.pdf          # project description
│
├── src/            
│   ├── Student_Performance.ipynb 
│   ├── models/                     # contains trained models
│   ├── plots/                      # any related diagrams
│   ├── selected_features/          # selected features based on embedded methods
│   └── student+performance/        # dataset itself
│
├── ui/  
│   └── student_performance_ui_app.py       
├── .gitignore  
└── README.md  
```
