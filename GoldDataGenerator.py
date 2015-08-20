# Generate a synthetic dataset of wine tasting notes based on styles.

import sys, random, csv, datetime, re, pandas as pd, numpy as np, math, json
from pandas import DataFrame, Series, date_range, concat

# My Files
import GoldDataFunctions as gdf
import TastingNoteParser as tnp

all_style_profiles = {}

file = open("wine_profiles_from_google_sheet.json")
lines = file.readlines()
for line in lines:
  profile = json.loads(line)
  all_style_profiles.update(profile)

# Save synthetic tasting notes in a .csv : 

df_arr = []
for style_name in all_style_profiles:
  profile = all_style_profiles[style_name]
  boolean_traits = profile[gdf.STR_BOOLEAN_TRAITS]
  enum_traits    = profile[gdf.STR_ENUM_TRAITS]

  #notes   = gdf.get_note_list(boolean_traits,enum_traits,style_name)
  notes   = gdf.generateSyntheticTastingNotes(style_name, boolean_traits, enum_traits)
  notesDF = pd.DataFrame(notes)
  df_arr.append(notesDF)

all_synthetic_notes = concat(df_arr)
all_synthetic_notes.to_csv('synthetic_gold_data.csv');













