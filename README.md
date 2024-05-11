# SteamLens
SteamLens is a GUI data processing and visualization for steam games.

## Description
SteamLens utilizes a dataset comprising Steam game data for processing and visualization, <br>encompassing information such as game name, release date, price, supported operating systems (Windows, Mac, Linux), <br>user scores, positive and negative votes, developers, publishers, categories, genres, and tags.

## SteamLens UI
### Home menu
![SteamLens_home_menu.png](screenshots%2FSteamLens_home_menu.png)
### Search menu
![SteamLens_search_menu.png](screenshots%2FSteamLens_search_menu.png)
### Game price distribution menu
![SteamLens_price_dist_menu.png](screenshots%2FSteamLens_price_dist_menu.png)
### Game relationship menu
![SteamLens_relationship_menu.png](screenshots%2FSteamLens_relationship_menu.png)
### Game released each year menu
![SteamLens_released_year_menu.png](screenshots%2FSteamLens_released_year_menu.png)
### Game insights dashboard menu
![SteamLens_dashboard_menu.png](screenshots%2FSteamLens_dashboard_menu.png)

## Requirements
* python >= 3.9
* Git LFS

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
5. Create a Python Virtual Environment. (If it doesn't work, please use `python3` instead of `python`)
```
python -m venv venv
```
6. Activate the virtual environment.
   - Linux and macOS
   ``` 
   source venv/bin/activate 
   ```
   - Windows
   ```  
   .\venv\Scripts\activate
   ```
7. Install dependencies.
```
pip install -r requirements.txt
```

## How to run
1. Activate the virtual environment.
   - Linux and macOS
   ``` 
   source venv/bin/activate 
   ```
   - Windows
   ```  
   .\venv\Scripts\activate
   ```
2. Run the program. (If it doesn't work, please use `python3` instead of `python`)
```
python main.py
```

## SteamLens Wiki Page
* [SteamLens Wiki](https://github.com/PHIMNADA024/SteamLens/wiki)

## Project Documents
* [Project Proposal](https://docs.google.com/document/d/1GnFoABUNMin5Rpu-b2_vQP5a0CFT8EuwDSRImBIfSxE/edit?usp=sharing)
* [Development Plan](https://github.com/PHIMNADA024/SteamLens/wiki/Weekly-Plan)
* [UML Class Diagram](https://github.com/PHIMNADA024/SteamLens/wiki/UML-Class-Diagram)
* [UML Sequence Diagram](https://github.com/PHIMNADA024/SteamLens/wiki/UML-Sequence-Diagram)

## SteamLens Data
* [SteamLens Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset)

## SteamLens Videos
* [SteamLens Tutorial](https://drive.google.com/file/d/1WSx2U-twGqF8Z7QRK6l07Ttx32BeWlIn/view?usp=sharing)
* [SteamLens](https://drive.google.com/file/d/1fFkBN_aGm1_-kgyZNb0obAXeOBzmjO6z/view?usp=sharing)