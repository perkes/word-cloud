from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

import numpy as np
import pandas as pd
import argparse
import random
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Create a simple wordcloud.')
    parser.add_argument('--config', required = True, help = 'Path to the config file')
    args = parser.parse_args()
    config = json.load(open(args.config, 'r'))

    stop_words = {}
    if config['remove_stopwords']: 
        stop_words = set(STOPWORDS)
        stop_words.update(set(config['additional_stopwords']))
        
    mask = None    
    if config['mask']:
        mask = np.array(Image.open(config['mask']))

    df = pd.read_csv(config['input'])

    for filter_ in config['filters']:
        if filter_['type'] == 'match':
            df = df[df[filter_['column']] == filter_['value']]
        else:
            df = df[df[filter_['column']] != filter_['value']]
    
    terms = []
    for dimension in config['dimensions']:
        terms += list(df[dimension])
    
    random.shuffle(terms)
    long_string = ' '.join(terms)

    wordcloud = WordCloud(mask = mask,
                          stopwords = stop_words, 
                          background_color = config['background_color'], 
                          min_word_length = config['min_word_length'],
                          max_words = config['max_words'], 
                          contour_width = config['contour_width'], 
                          colormap = config['colormap'], 
                          collocations = config['collocations'],
                          include_numbers = config['include_numbers'],
                          normalize_plurals = config['normalize_plurals'],
                          width = config['width'], 
                          height = config['height'])

    wordcloud.generate(long_string)
    
    if config['image_coloring']:
        image_colors = ImageColorGenerator(mask)
        wordcloud.recolor(color_func=image_colors)
    
    wordcloud.to_file(config['output'])