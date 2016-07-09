# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Tasting Note Parser
# Parse a tasting note into a dict. 
# 
# ###Bugs/Tweaks:
# 
# ###Next Steps, ideas for improvement:

# <codecell>

#import re
#from __future__ import division
import sys, csv, datetime, re, pandas as pd, numpy as np, math
#from datetime import timedelta
from pandas import DataFrame, Series, date_range, concat
import random
#import graphlab as gl;
#import jellyfish as jf
#%matplotlib inline

# <codecell>

def getRS(tastingNote):
    tokens = tastingNote.strip().split(', ')
    enum = ['dry','slight rs','off-dry','sweet']
    for value in enum:
        try:
            tokens.index(value)
            print 'sweetness recognized as '+value
            return value
        except:
            continue
    return 'dry' #default

def getHue(tastingNote):
    tokens = tastingNote.strip().split(', ')
    enum = ['straw','yellow','gold']
    for value in enum:
        try:
            tokens.index(value)
            print 'hue recognized as '+value
            return value
        except:
            continue
    print 'no hue recognized - use [straw, yellow, gold]'
    return 'straw' #default

def getColorConcentration(tastingNote):
    wordPair = None
    tokens = tastingNote.strip().split(', ')
    for i in range(len(tokens)):
        words = tokens[i].split()
        try:
            words.index('color_concentration')
            wordPair = words
            break
        except:
            continue
    if wordPair != None:
        enum = ['light','moderate','elevated']
        for value in enum:
            try:
                wordPair.index(value)
                print 'color_concentration recognized as '+ value
                return value
            except:
                continue
        print 'error: color_concentration not recognized, use [light, moderate, elevated]'
    print 'error: no color_concentration specified'
    return 'moderate' #default

def getAlcohol(tastingNote):
    wordPair = None
    tokens = tastingNote.strip().split(', ')
    for i in range(len(tokens)):
        words = tokens[i].split()
        try:
            words.index('alcohol')
            wordPair = words
            break
        except:
            continue
    if wordPair != None:
        enum = ['diminished','moderate','elevated','high']
        for value in enum:
            try:
                wordPair.index(value)
                print 'alcohol recognized as '+ value
                return value
            except:
                continue
        print 'error: alcohol not recognized, use [diminished alcohol, moderate alcohol, elevated alcohol, high alcohol]'
    print 'error: no alcohol specified'
    return 'moderate' #default

def getAcid(tastingNote):
    wordPair = None
    tokens = tastingNote.strip().split(', ')
    for i in range(len(tokens)):
        words = tokens[i].split()
        try:
            words.index('acid')
            wordPair = words
            break
        except:
            continue
    if wordPair != None:
        enum = ['diminished','moderate','elevated','high']
        for value in enum:
            try:
                wordPair.index(value)
                print 'acid recognized as '+ value
                return value
            except:
                continue
        print 'error: acid not recognized, use [diminished acid, moderate acid, elevated acid, high acid]'
    print 'error: no acid specified'
    return 'moderate' #default


def getBooleanTraits(tastingNote):
    tokens = tastingNote.strip().split(', ')
    bool_enum = ['botrytis','floral','pyrazines','stone_fruit','thiols','low_terpenes','high_terpenes','oak','pommaceous_fruit','oxidation','phenolic_bitterness','white_pepper']
    traits = {}
    for value in bool_enum:
        try:
            tokens.index(value)
            traits[value]=1
            print "recognized " + value
        except:
            traits[value]=0
    return traits
    
def getAttributes(tastingNote):
    tn_dict = {}
    tn_dict['residual_sugar'] = getRS(tastingNote)
    tn_dict['hue']            = getHue(tastingNote)
    tn_dict['color_concentration']  = getColorConcentration(tastingNote)
    tn_dict['alcohol'] = getAlcohol(tastingNote)
    tn_dict['acid'] = getAcid(tastingNote)
    tn_dict.update(getBooleanTraits(tastingNote))
    return tn_dict


# <markdowncell>

# ### Test:

# <codecell>

#TEST:
string = 'slight rs, botrytis, light color_concentration, high acid, diminished alcohol, yellow, floral, stone fruit, thiols, oxidation, low_terpenes, high_terpenes, phenolic_bitterness, oak, pommaceous_fruit, pyrazines, white_pepper'

# <codecell>

#tn_dict=getAttributes(string)
#tn_dict

x = getBooleanTraits(string)
x

# <codecell>


# <codecell>


