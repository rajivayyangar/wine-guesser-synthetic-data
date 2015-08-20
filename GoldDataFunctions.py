import sys, random, csv, datetime, re, pandas as pd, numpy as np, math
from pandas import DataFrame, Series, date_range, concat

# global constants:
SAMPLES_PER_STYLE = 20

# global strings:
STR_STYLE_NAME = 'style_name'
STR_BOOLEAN_TRAITS = 'boolean_traits'
STR_ENUM_TRAITS = 'enum_traits'
# string names for specific enum traits:
STR_HUE = 'hue'                 
STR_COLOR_CONCENTRATION = 'color_concentration'
STR_RESIDUAL_SUGAR = 'residual_sugar'


# Functions for assembling the profiles from JSON:
def assembleStyleProfile(style_name, hue, color_concentration, residual_sugar, boolean_traits):
    profile = {}
    all_enum_traits =  assembleEnumTraits(hue,color_concentration,residual_sugar)
    profile[STR_ENUM_TRAITS] = all_enum_traits
    profile[STR_BOOLEAN_TRAITS] = boolean_traits
    profile[STR_STYLE_NAME] = style_name
    return profile

def assembleEnumTraits(hue,color_concentration,residual_sugar):
    enum_traits =  {STR_HUE:hue, 
                    STR_COLOR_CONCENTRATION:color_concentration, 
                    STR_RESIDUAL_SUGAR:residual_sugar}
    return enum_traits


# Functions for generating synthetic data: 
def generateSyntheticEnumTraitValues(enum_trait):
    synthetic_values = []
    for possible_value in enum_trait:
        prevalence = enum_trait[possible_value] #how often does this trait, e.g. hue = 'gold' occur? (between 0 and 1.0)
        value_name = possible_value
        synthetic_values += proportionalNumberOfSyntheticEnumValues(value_name,prevalence)
    random.shuffle(synthetic_values)
    return synthetic_values

def proportionalNumberOfSyntheticEnumValues(value_name, prevalence):
    proportional_number_of_values = int(prevalence * SAMPLES_PER_STYLE)
    synthetic_values_for_this_possible_value = []
    for i in range(proportional_number_of_values):
        synthetic_values_for_this_possible_value.append(value_name)
    return synthetic_values_for_this_possible_value

def generateSyntheticBooleanTraitValues(boolean_traits):
    boolean_trait_synthetic_values = {}
    for trait_name in boolean_traits:
        prevalence = boolean_traits[trait_name] # How often does this trait (e.g. pyrazines) equal True? (between 0 and 1.0)
        synthetic_values = proportionalNumberOfSyntheticBooleanValues(trait_name,prevalence)
        boolean_trait_synthetic_values[trait_name] = synthetic_values
    return boolean_trait_synthetic_values

def proportionalNumberOfSyntheticBooleanValues(trait_name,prevalence):
    proportional_number_of_trues = int(prevalence * SAMPLES_PER_STYLE)
    synthetic_values_for_this_trait = initializeArrayOfFalseValues()
    for i in range(proportional_number_of_trues):
        synthetic_values_for_this_trait[i] = True
    random.shuffle(synthetic_values_for_this_trait)
    return synthetic_values_for_this_trait

def initializeArrayOfFalseValues():
    false_array = np.zeros(SAMPLES_PER_STYLE, dtype=bool)
    return false_array

def get_note_list(bool_traits, enum_traits_dicts_dict, style):
    enum_traits_dict = {}
    for trait in enum_traits_dicts_dict:
        enum_traits_dict[trait]=generateSyntheticEnumTraitValues(enum_traits_dicts_dict[trait])
    bool_traits_dict= generateSyntheticBooleanTraitValues(bool_traits) 
    note_array = []
    for i in range(SAMPLES_PER_STYLE):
        tasting_note = {}
        tasting_note['style'] = style
        for enum_trait in enum_traits_dict:
            tasting_note[enum_trait]= enum_traits_dict[enum_trait][i]
        for trait in bool_traits_dict:
            if(bool_traits_dict[trait][i]):
                tasting_note[trait]=1
            else:
                tasting_note[trait]=0
        note_array.append(tasting_note)
    return note_array


def generateSyntheticTastingNotes(style_name, bool_traits, enum_traits):
    enum_trait_note_values = {}
    for trait in enum_traits:
        enum_trait_note_values[trait]=generateSyntheticEnumTraitValues(enum_traits[trait])
    bool_traits_dict= generateSyntheticBooleanTraitValues(bool_traits) 
    note_array = []
    for i in range(SAMPLES_PER_STYLE):# This is a liability - it relies on there being n=SAMPLES_PER_STYLE elements in the various arrays.
        tasting_note = {}
        tasting_note[STR_STYLE_NAME] = style_name
        for enum_trait in enum_trait_note_values:
            tasting_note[enum_trait]= enum_trait_note_values[enum_trait][i]
        for trait in bool_traits_dict:
            if(bool_traits_dict[trait][i]):
                tasting_note[trait]=1
            else:
                tasting_note[trait]=0
        note_array.append(tasting_note)
    return note_array

def print_friendly_notes(bool_traits, enum_traits_dicts_array,style):
    enum_traits_array = []
    for trait in enum_traits_dicts_array:
        enum_traits_array.append(generateSyntheticEnumTraitValues(trait)) 
    bool_traits_dict = generateSyntheticBooleanTraitValues(bool_traits) 
    print 'all notes are for: ' + style
    for i in range(SAMPLES_PER_STYLE):
        tasting_note = []
        for enum_trait in enum_traits_array:
            #print enum_trait
            tasting_note.append(enum_trait[i])
        for trait in bool_traits_dict:
            if(bool_traits_dict[trait][i]):
                tasting_note.append(trait)
        print tasting_note
# e.g. print_friendly_notes(style_dict[style]['boolean_traits'],style_dict[style]['enum_traits'].values(),style)
        


