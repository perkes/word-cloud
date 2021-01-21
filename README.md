# Word Cloud

A tool to create simple word clouds.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- pip
- virtualenv
- A valid configuration file (see below).

To get **pip**: download [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
```
python get-pip.py
```
Pip is now installed!

To get **virutalenv**: 
```
pip install virtualenv
``` 

### Installing

Create a new virtual environment:
```
virtualenv -p python3 venv
```    

Start the virtual environment:
```
source venv/bin/activate
```    
Install requirements with pip:
```
pip install -r requirements.txt
```

### Configuring

#### Configuring the CSV to JSON configuration file

- **input**: Input data file (CSV).
- **output**: Name and path of the output file (PNG).
- **dimensions**: Columns to be used as data sources for text in the input file.
- **filters**: Criteria for row filtering. Each filter is an object with three keys:
    - **column**: The name of the column in the input CSV file.
    - **type**: Wether the value should (match) or should not be (no match) in the column.
    - **value**: The value the column must or must not have.
- **additional_stopwords**: Additional stopwords to be added to the default list. *Deafult*: \[\].
- **image_coloring**: if True, the mask will be used to color de words in the tag cloud. *Default*: False.
- **normalize_plurals**: Whether to remove trailing ‘s’ from words. If True and a word appears with and without a trailing ‘s’, the one with trailing ‘s’ is removed and its counts are added to the version without trailing ‘s’ – unless the word ends with ‘ss’. *Default*: True.
- **remove_stopwords**: Whether to eliminate stopwords or not. *Default*: True.
- **include_numbers**: Whether to include numbers as phrases or not. *Default*: False.
- **collocations**: Whether to include collocations (bigrams) of two words. *Default*: true.
- **background_color**: Background color for the word cloud image.
- **colormap**: Matplotlib colormap to randomly draw colors from for each word. For a full list of built-in colormaps refer to: https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html *Deafult*: viridis.
- **min_word_length**: Minimum number of letters a word must have to be included. *Deafult*: 3.
- **contour_width**: If mask is not None and contour_width > 0, draw the mask contour. *Default*: 0.
- **max_words**: The maximum number of words. *Deafult*: 200.
- **width**: Width of the canvas. *Default*: 1024.
- **height**: Height of the canvas. *Default*: 768.
 
### Running

To create a word cloud, you can run (substituting config.json by your own config file):
```
python word_cloud.py --config ./config.json
```

## Built With

* [Pandas](https://pandas.pydata.org/) - Data manipulation.
* [wordcloud](http://amueller.github.io/word_cloud/index.html) - Word Cloud creation.

## Authors

* **Jonathan Perkes** - [LinkedIn](https://www.linkedin.com/in/jonathan-perkes/)
