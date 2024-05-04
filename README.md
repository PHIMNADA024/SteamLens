# SteamLens
SteamLens is a GUI data processing and visualization for steam games.

## Installation
1. Install [Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) by following the steps from this page first.
   - It is required for the data file that is currently stored in Git Large File Storage.
2. Clone the repository. (Make sure that `git lfs` is installed correctly before cloning)
```
git clone https://github.com/PHIMNADA024/SteamLens.git
```
3. Go to the project directory.
```
cd SteamLens
```
4. Download the data file.
```
git lfs pull
```

## How to run
1. Create a Python Virtual Environment. (If it doesn't work, please use `python3` instead of `python`)
```
python -m venv venv
```
2. Activate the virtual environment.
   - Linux and macOS
   ``` 
   source venv/bin/activate 
   ```
   - Windows
   ```  
   .\venv\Scripts\activate
   ```
3. Install dependencies.
```
pip install -r requirements.txt
```
4. Run the program. (If it doesn't work, please use `python3` instead of `python`)
```
python main.py
```