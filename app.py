import math
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots  # For creating subplots

# ------------------------------------------------------------------------
#  1) Original DataFrame: df_timeline
# ------------------------------------------------------------------------
df_timeline = pd.DataFrame([
    # ==== Sep Plan (All Languages) ====
    {"Task": "Project preparation", "Language": "Plan", "Start": "2024-09-02", "End": "2024-09-03", "Type": "Plan"},
    {"Task": "Translation",         "Language": "Plan", "Start": "2024-09-04", "End": "2024-09-09", "Type": "Plan"},
    {"Task": "Edit",                "Language": "Plan", "Start": "2024-09-10", "End": "2024-09-12", "Type": "Plan"},
    {"Task": "Proofreading",        "Language": "Plan", "Start": "2024-09-13", "End": "2024-09-16", "Type": "Plan"},
    {"Task": "DTP",                 "Language": "Plan", "Start": "2024-09-17", "End": "2024-09-18", "Type": "Plan"},
    {"Task": "LSO",                 "Language": "Plan", "Start": "2024-09-19", "End": "2024-09-19", "Type": "Plan"},
    {"Task": "Finalization",        "Language": "Plan", "Start": "2024-09-20", "End": "2024-09-20", "Type": "Plan"},
    # ==== Sep Actual - ZH ====
    {"Task": "Project preparation", "Language": "ZH",   "Start": "2024-09-02", "End": "2024-09-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ZH",   "Start": "2024-09-04", "End": "2024-09-09", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ZH",   "Start": "2024-09-10", "End": "2024-09-12", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ZH",   "Start": "2024-09-13", "End": "2024-09-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ZH",   "Start": "2024-09-17", "End": "2024-09-18", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ZH",   "Start": "2024-09-19", "End": "2024-09-20", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ZH",   "Start": "2024-09-21", "End": "2024-09-23", "Type": "Actual"},
    # ==== Sep Actual - FR ====
    {"Task": "Project preparation", "Language": "FR",   "Start": "2024-09-02", "End": "2024-09-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "FR",   "Start": "2024-09-04", "End": "2024-09-06", "Type": "Actual"},
    {"Task": "Edit",                "Language": "FR",   "Start": "2024-09-09", "End": "2024-09-11", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "FR",   "Start": "2024-09-12", "End": "2024-09-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "FR",   "Start": "2024-09-17", "End": "2024-09-18", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "FR",   "Start": "2024-09-19", "End": "2024-09-20", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "FR",   "Start": "2024-09-23", "End": "2024-09-24", "Type": "Actual"},
    # ==== Sep Actual - ES ====
    {"Task": "Project preparation", "Language": "ES",   "Start": "2024-09-02", "End": "2024-09-04", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ES",   "Start": "2024-09-05", "End": "2024-09-09", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ES",   "Start": "2024-09-10", "End": "2024-09-12", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ES",   "Start": "2024-09-13", "End": "2024-09-17", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ES",   "Start": "2024-09-18", "End": "2024-09-19", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ES",   "Start": "2024-09-20", "End": "2024-09-23", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ES",   "Start": "2024-09-24", "End": "2024-09-25", "Type": "Actual"},
    # ==== Sep Actual - PT ====
    {"Task": "Project preparation", "Language": "PT",   "Start": "2024-09-02", "End": "2024-09-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "PT",   "Start": "2024-09-04", "End": "2024-09-09", "Type": "Actual"},
    {"Task": "Edit",                "Language": "PT",   "Start": "2024-09-10", "End": "2024-09-12", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "PT",   "Start": "2024-09-13", "End": "2024-09-17", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "PT",   "Start": "2024-09-18", "End": "2024-09-19", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "PT",   "Start": "2024-09-20", "End": "2024-09-23", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "PT",   "Start": "2024-09-24", "End": "2024-09-24", "Type": "Actual"},
    # ==== Sep Actual - JA ====
    {"Task": "Project preparation", "Language": "JA",   "Start": "2024-09-02", "End": "2024-09-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "JA",   "Start": "2024-09-04", "End": "2024-09-09", "Type": "Actual"},
    {"Task": "Edit",                "Language": "JA",   "Start": "2024-09-10", "End": "2024-09-12", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "JA",   "Start": "2024-09-13", "End": "2024-09-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "JA",   "Start": "2024-09-17", "End": "2024-09-18", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "JA",   "Start": "2024-09-19", "End": "2024-09-20", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "JA",   "Start": "2024-09-21", "End": "2024-09-23", "Type": "Actual"},
    # ==== Oct Plan ====
    {"Task": "Project preparation", "Language": "Plan", "Start": "2024-10-01", "End": "2024-10-02", "Type": "Plan"},
    {"Task": "Translation",         "Language": "Plan", "Start": "2024-10-03", "End": "2024-10-08", "Type": "Plan"},
    {"Task": "Edit",                "Language": "Plan", "Start": "2024-10-09", "End": "2024-10-11", "Type": "Plan"},
    {"Task": "Proofreading",        "Language": "Plan", "Start": "2024-10-14", "End": "2024-10-15", "Type": "Plan"},
    {"Task": "DTP",                 "Language": "Plan", "Start": "2024-10-16", "End": "2024-10-17", "Type": "Plan"},
    {"Task": "LSO",                 "Language": "Plan", "Start": "2024-10-18", "End": "2024-10-21", "Type": "Plan"},
    {"Task": "Finalization",        "Language": "Plan", "Start": "2024-10-22", "End": "2024-10-24", "Type": "Plan"},
    # ==== Oct Actual - ZH ====
    {"Task": "Project preparation", "Language": "ZH",   "Start": "2024-10-08", "End": "2024-10-09", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ZH",   "Start": "2024-10-10", "End": "2024-10-13", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ZH",   "Start": "2024-10-14", "End": "2024-10-16", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ZH",   "Start": "2024-10-17", "End": "2024-10-19", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ZH",   "Start": "2024-10-20", "End": "2024-10-21", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ZH",   "Start": "2024-10-22", "End": "2024-10-23", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ZH",   "Start": "2024-10-24", "End": "2024-10-25", "Type": "Actual"},
    # ==== Oct Actual - FR ====
    {"Task": "Project preparation", "Language": "FR",   "Start": "2024-10-01", "End": "2024-10-02", "Type": "Actual"},
    {"Task": "Translation",         "Language": "FR",   "Start": "2024-10-03", "End": "2024-10-08", "Type": "Actual"},
    {"Task": "Edit",                "Language": "FR",   "Start": "2024-10-09", "End": "2024-10-11", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "FR",   "Start": "2024-10-14", "End": "2024-10-15", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "FR",   "Start": "2024-10-16", "End": "2024-10-17", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "FR",   "Start": "2024-10-18", "End": "2024-10-21", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "FR",   "Start": "2024-10-22", "End": "2024-10-24", "Type": "Actual"},
    # ==== Oct Actual - ES ====
    {"Task": "Project preparation", "Language": "ES",   "Start": "2024-10-01", "End": "2024-10-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ES",   "Start": "2024-10-04", "End": "2024-10-09", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ES",   "Start": "2024-10-10", "End": "2024-10-14", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ES",   "Start": "2024-10-15", "End": "2024-10-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ES",   "Start": "2024-10-17", "End": "2024-10-18", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ES",   "Start": "2024-10-21", "End": "2024-10-23", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ES",   "Start": "2024-10-24", "End": "2024-10-25", "Type": "Actual"},
    # ==== Oct Actual - PT ====
    {"Task": "Project preparation", "Language": "PT",   "Start": "2024-10-01", "End": "2024-10-02", "Type": "Actual"},
    {"Task": "Translation",         "Language": "PT",   "Start": "2024-10-03", "End": "2024-10-08", "Type": "Actual"},
    {"Task": "Edit",                "Language": "PT",   "Start": "2024-10-09", "End": "2024-10-11", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "PT",   "Start": "2024-10-14", "End": "2024-10-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "PT",   "Start": "2024-10-17", "End": "2024-10-18", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "PT",   "Start": "2024-10-21", "End": "2024-10-22", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "PT",   "Start": "2024-10-22", "End": "2024-10-22", "Type": "Actual"},
    # ==== Oct Actual - JA ====
    {"Task": "Project preparation", "Language": "JA",   "Start": "2024-10-01", "End": "2024-10-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "JA",   "Start": "2024-10-04", "End": "2024-10-08", "Type": "Actual"},
    {"Task": "Edit",                "Language": "JA",   "Start": "2024-10-09", "End": "2024-10-11", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "JA",   "Start": "2024-10-12", "End": "2024-10-15", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "JA",   "Start": "2024-10-16", "End": "2024-10-17", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "JA",   "Start": "2024-10-18", "End": "2024-10-19", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "JA",   "Start": "2024-10-22", "End": "2024-10-23", "Type": "Actual"},
    # ==== Nov Plan ====
    {"Task": "Project preparation", "Language": "Plan", "Start": "2024-11-01", "End": "2024-11-03", "Type": "Plan"},
    {"Task": "Translation",         "Language": "Plan", "Start": "2024-11-04", "End": "2024-11-06", "Type": "Plan"},
    {"Task": "Edit",                "Language": "Plan", "Start": "2024-11-07", "End": "2024-11-09", "Type": "Plan"},
    {"Task": "Proofreading",        "Language": "Plan", "Start": "2024-11-10", "End": "2024-11-14", "Type": "Plan"},
    {"Task": "DTP",                 "Language": "Plan", "Start": "2024-11-15", "End": "2024-11-16", "Type": "Plan"},
    {"Task": "LSO",                 "Language": "Plan", "Start": "2024-11-17", "End": "2024-11-20", "Type": "Plan"},
    {"Task": "Finalization",        "Language": "Plan", "Start": "2024-11-21", "End": "2024-11-22", "Type": "Plan"},
    # ==== Nov Actual - ZH ====
    {"Task": "Project preparation", "Language": "ZH",   "Start": "2024-11-01", "End": "2024-11-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ZH",   "Start": "2024-11-04", "End": "2024-11-06", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ZH",   "Start": "2024-11-07", "End": "2024-11-09", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ZH",   "Start": "2024-11-10", "End": "2024-11-14", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ZH",   "Start": "2024-11-15", "End": "2024-11-16", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ZH",   "Start": "2024-11-17", "End": "2024-11-20", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ZH",   "Start": "2024-11-21", "End": "2024-11-22", "Type": "Actual"},
    # ==== Nov Actual - FR ====
    {"Task": "Project preparation", "Language": "FR",   "Start": "2024-11-01", "End": "2024-11-04", "Type": "Actual"},
    {"Task": "Translation",         "Language": "FR",   "Start": "2024-11-05", "End": "2024-11-09", "Type": "Actual"},
    {"Task": "Edit",                "Language": "FR",   "Start": "2024-11-10", "End": "2024-11-12", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "FR",   "Start": "2024-11-13", "End": "2024-11-17", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "FR",   "Start": "2024-11-18", "End": "2024-11-19", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "FR",   "Start": "2024-11-20", "End": "2024-11-23", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "FR",   "Start": "2024-11-24", "End": "2024-11-25", "Type": "Actual"},
    # ==== Nov Actual - ES ====
    {"Task": "Project preparation", "Language": "ES",   "Start": "2024-11-01", "End": "2024-11-02", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ES",   "Start": "2024-11-03", "End": "2024-11-07", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ES",   "Start": "2024-11-08", "End": "2024-11-10", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ES",   "Start": "2024-11-11", "End": "2024-11-14", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ES",   "Start": "2024-11-15", "End": "2024-11-17", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ES",   "Start": "2024-11-18", "End": "2024-11-21", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ES",   "Start": "2024-11-22", "End": "2024-11-23", "Type": "Actual"},
    # ==== Nov Actual - PT ====
    {"Task": "Project preparation", "Language": "PT",   "Start": "2024-11-01", "End": "2024-11-04", "Type": "Actual"},
    {"Task": "Translation",         "Language": "PT",   "Start": "2024-11-05", "End": "2024-11-07", "Type": "Actual"},
    {"Task": "Edit",                "Language": "PT",   "Start": "2024-11-08", "End": "2024-11-10", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "PT",   "Start": "2024-11-11", "End": "2024-11-14", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "PT",   "Start": "2024-11-15", "End": "2024-11-17", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "PT",   "Start": "2024-11-18", "End": "2024-11-20", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "PT",   "Start": "2024-11-21", "End": "2024-11-22", "Type": "Actual"},
    # ==== Nov Actual - JA ====
    {"Task": "Project preparation", "Language": "JA",   "Start": "2024-11-01", "End": "2024-11-02", "Type": "Actual"},
    {"Task": "Translation",         "Language": "JA",   "Start": "2024-11-03", "End": "2024-11-05", "Type": "Actual"},
    {"Task": "Edit",                "Language": "JA",   "Start": "2024-11-06", "End": "2024-11-09", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "JA",   "Start": "2024-11-10", "End": "2024-11-13", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "JA",   "Start": "2024-11-14", "End": "2024-11-15", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "JA",   "Start": "2024-11-16", "End": "2024-11-18", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "JA",   "Start": "2024-11-19", "End": "2024-11-21", "Type": "Actual"},
    # ==== Dec Plan ====
    {"Task": "Project preparation", "Language": "Plan", "Start": "2024-12-02", "End": "2024-12-03", "Type": "Plan"},
    {"Task": "Translation",         "Language": "Plan", "Start": "2024-12-04", "End": "2024-12-06", "Type": "Plan"},
    {"Task": "Edit",                "Language": "Plan", "Start": "2024-12-09", "End": "2024-12-11", "Type": "Plan"},
    {"Task": "Proofreading",        "Language": "Plan", "Start": "2024-12-12", "End": "2024-12-16", "Type": "Plan"},
    {"Task": "DTP",                 "Language": "Plan", "Start": "2024-12-17", "End": "2024-12-18", "Type": "Plan"},
    {"Task": "LSO",                 "Language": "Plan", "Start": "2024-12-19", "End": "2024-12-23", "Type": "Plan"},
    {"Task": "Finalization",        "Language": "Plan", "Start": "2024-12-24", "End": "2024-12-24", "Type": "Plan"},
    # ==== Dec Actual - ZH ====
    {"Task": "Project preparation", "Language": "ZH",   "Start": "2024-12-02", "End": "2024-12-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ZH",   "Start": "2024-12-04", "End": "2024-12-09", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ZH",   "Start": "2024-12-10", "End": "2024-12-12", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ZH",   "Start": "2024-12-13", "End": "2024-12-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ZH",   "Start": "2024-12-17", "End": "2024-12-18", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ZH",   "Start": "2024-12-19", "End": "2024-12-20", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ZH",   "Start": "2024-12-23", "End": "2024-12-24", "Type": "Actual"},
    # ==== Dec Actual - FR ====
    {"Task": "Project preparation", "Language": "FR",   "Start": "2024-12-02", "End": "2024-12-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "FR",   "Start": "2024-12-04", "End": "2024-12-06", "Type": "Actual"},
    {"Task": "Edit",                "Language": "FR",   "Start": "2024-12-09", "End": "2024-12-11", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "FR",   "Start": "2024-12-12", "End": "2024-12-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "FR",   "Start": "2024-12-17", "End": "2024-12-18", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "FR",   "Start": "2024-12-19", "End": "2024-12-23", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "FR",   "Start": "2024-12-24", "End": "2024-12-24", "Type": "Actual"},
    # ==== Dec Actual - ES ====
    {"Task": "Project preparation", "Language": "ES",   "Start": "2024-12-02", "End": "2024-12-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ES",   "Start": "2024-12-04", "End": "2024-12-06", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ES",   "Start": "2024-12-09", "End": "2024-12-11", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ES",   "Start": "2024-12-12", "End": "2024-12-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ES",   "Start": "2024-12-17", "End": "2024-12-18", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ES",   "Start": "2024-12-19", "End": "2024-12-23", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ES",   "Start": "2024-12-24", "End": "2024-12-24", "Type": "Actual"},
    # ==== Dec Actual - PT ====
    {"Task": "Project preparation", "Language": "PT",   "Start": "2024-12-02", "End": "2024-12-04", "Type": "Actual"},
    {"Task": "Translation",         "Language": "PT",   "Start": "2024-12-05", "End": "2024-12-09", "Type": "Actual"},
    {"Task": "Edit",                "Language": "PT",   "Start": "2024-12-10", "End": "2024-12-13", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "PT",   "Start": "2024-12-16", "End": "2024-12-17", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "PT",   "Start": "2024-12-18", "End": "2024-12-19", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "PT",   "Start": "2024-12-20", "End": "2024-12-22", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "PT",   "Start": "2024-12-23", "End": "2024-12-23", "Type": "Actual"},
    # ==== Dec Actual - JA ====
    {"Task": "Project preparation", "Language": "JA",   "Start": "2024-12-02", "End": "2024-12-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "JA",   "Start": "2024-12-04", "End": "2024-12-09", "Type": "Actual"},
    {"Task": "Edit",                "Language": "JA",   "Start": "2024-12-10", "End": "2024-12-12", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "JA",   "Start": "2024-12-13", "End": "2024-12-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "JA",   "Start": "2024-12-17", "End": "2024-12-18", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "JA",   "Start": "2024-12-19", "End": "2024-12-20", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "JA",   "Start": "2024-12-23", "End": "2024-12-24", "Type": "Actual"},
    # ==== Jan Plan ====
    {"Task": "Project preparation", "Language": "Plan", "Start": "2025-01-02", "End": "2025-01-03", "Type": "Plan"},
    {"Task": "Translation",         "Language": "Plan", "Start": "2025-01-06", "End": "2025-01-08", "Type": "Plan"},
    {"Task": "Edit",                "Language": "Plan", "Start": "2025-01-09", "End": "2025-01-13", "Type": "Plan"},
    {"Task": "Proofreading",        "Language": "Plan", "Start": "2025-01-14", "End": "2025-01-16", "Type": "Plan"},
    {"Task": "DTP",                 "Language": "Plan", "Start": "2025-01-17", "End": "2025-01-20", "Type": "Plan"},
    {"Task": "LSO",                 "Language": "Plan", "Start": "2025-01-21", "End": "2025-01-23", "Type": "Plan"},
    {"Task": "Finalization",        "Language": "Plan", "Start": "2025-01-24", "End": "2025-01-24", "Type": "Plan"},
    # ==== Jan Actual - ZH ====
    {"Task": "Project preparation", "Language": "ZH",   "Start": "2025-01-02", "End": "2025-01-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ZH",   "Start": "2025-01-06", "End": "2025-01-08", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ZH",   "Start": "2025-01-09", "End": "2025-01-13", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ZH",   "Start": "2025-01-14", "End": "2025-01-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ZH",   "Start": "2025-01-17", "End": "2025-01-20", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ZH",   "Start": "2025-01-21", "End": "2025-01-23", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ZH",   "Start": "2025-01-24", "End": "2025-01-24", "Type": "Actual"},
    # ==== Jan Actual - FR ====
    {"Task": "Project preparation", "Language": "FR",   "Start": "2025-01-02", "End": "2025-01-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "FR",   "Start": "2025-01-06", "End": "2025-01-08", "Type": "Actual"},
    {"Task": "Edit",                "Language": "FR",   "Start": "2025-01-09", "End": "2025-01-13", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "FR",   "Start": "2025-01-14", "End": "2025-01-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "FR",   "Start": "2025-01-17", "End": "2025-01-20", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "FR",   "Start": "2025-01-21", "End": "2025-01-22", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "FR",   "Start": "2025-01-23", "End": "2025-01-23", "Type": "Actual"},
    # ==== Jan Actual - ES ====
    {"Task": "Project preparation", "Language": "ES",   "Start": "2025-01-02", "End": "2025-01-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "ES",   "Start": "2025-01-06", "End": "2025-01-08", "Type": "Actual"},
    {"Task": "Edit",                "Language": "ES",   "Start": "2025-01-09", "End": "2025-01-13", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "ES",   "Start": "2025-01-14", "End": "2025-01-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "ES",   "Start": "2025-01-17", "End": "2025-01-20", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "ES",   "Start": "2025-01-21", "End": "2025-01-22", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "ES",   "Start": "2025-01-23", "End": "2025-01-23", "Type": "Actual"},
    # ==== Jan Actual - PT ====
    {"Task": "Project preparation", "Language": "PT",   "Start": "2025-01-02", "End": "2025-01-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "PT",   "Start": "2025-01-06", "End": "2025-01-08", "Type": "Actual"},
    {"Task": "Edit",                "Language": "PT",   "Start": "2025-01-09", "End": "2025-01-13", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "PT",   "Start": "2025-01-14", "End": "2025-01-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "PT",   "Start": "2025-01-17", "End": "2025-01-20", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "PT",   "Start": "2025-01-21", "End": "2025-01-22", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "PT",   "Start": "2025-01-23", "End": "2025-01-23", "Type": "Actual"},
    # ==== Jan Actual - JA ====
    {"Task": "Project preparation", "Language": "JA",   "Start": "2025-01-02", "End": "2025-01-03", "Type": "Actual"},
    {"Task": "Translation",         "Language": "JA",   "Start": "2025-01-06", "End": "2025-01-08", "Type": "Actual"},
    {"Task": "Edit",                "Language": "JA",   "Start": "2025-01-09", "End": "2025-01-13", "Type": "Actual"},
    {"Task": "Proofreading",        "Language": "JA",   "Start": "2025-01-14", "End": "2025-01-16", "Type": "Actual"},
    {"Task": "DTP",                 "Language": "JA",   "Start": "2025-01-17", "End": "2025-01-20", "Type": "Actual"},
    {"Task": "LSO",                 "Language": "JA",   "Start": "2025-01-21", "End": "2025-01-23", "Type": "Actual"},
    {"Task": "Finalization",        "Language": "JA",   "Start": "2025-01-24", "End": "2025-01-24", "Type": "Actual"}
])

# Convert string to datetime
df_timeline["Start"] = pd.to_datetime(df_timeline["Start"])
df_timeline["End"] = pd.to_datetime(df_timeline["End"])

# Define a categorical order for "Task" so timeline is displayed in a fixed order
task_order = [
    "Project preparation", "Translation", "Edit",
    "Proofreading", "DTP", "LSO", "Finalization"
]
df_timeline["Task"] = pd.Categorical(df_timeline["Task"], categories=task_order, ordered=True)

# Custom color map (including Plan)
timeline_color_map = {
    "Plan": "#000000",  # Black for "Plan"
    "ZH": "#e41a1c",    # Red
    "FR": "#377eb8",    # Blue
    "JA": "#4daf4a",    # Green
    "PT": "#984ea3",    # Purple
    "ES": "#ff7f00"     # Orange
}

# Helper functions to filter by month range
def get_month_date_range(month_str):
    """
    Convert 'YYYY-MM' to a tuple of 
    (Timestamp('YYYY-MM-01'), Timestamp('YYYY-MM-(end_of_month)'))
    """
    y, m = month_str.split("-")
    y, m = int(y), int(m)
    start_date = pd.Timestamp(y, m, 1)
    if m == 12:
        end_date = pd.Timestamp(y + 1, 1, 1) - pd.Timedelta(days=1)
    else:
        end_date = pd.Timestamp(y, m + 1, 1) - pd.Timedelta(days=1)
    return start_date, end_date

def task_in_selected_months(row, selected_months):
    """
    Return True if a task overlaps with any selected month range,
    otherwise False.
    """
    row_start, row_end = row["Start"], row["End"]
    for mon in selected_months:
        ms, me = get_month_date_range(mon)
        if (row_end >= ms) and (row_start <= me):
            return True
    return False

# ------------------------------------------------------------------------
#  2) LQA Report Data
# ------------------------------------------------------------------------
data = {
    "Month": ["Sep", "Oct", "Nov", "Dec", "Jan"] * 5,
    "Language": ["ZH"] * 5 + ["FR"] * 5 + ["JA"] * 5 + ["PT"] * 5 + ["ES"] * 5,
    "Penalty Score": 
    [16, 8, 5, 10, 3, 9, 9, 6, 9, 5, 12, 7, 6, 10, 6, 9, 8, 5, 9, 4, 9, 7, 6, 9, 4],
    "Fluency": 
    [3, 1, 2, 1, 1, 0, 2, 1, 2, 1, 1, 1, 1, 0, 0, 0, 2, 0, 1, 1, 0, 1, 2, 1, 1],
    "Terminology": 
    [10, 5, 0, 5, 0, 5, 1, 0, 4, 0, 5, 1, 1, 8, 1, 3, 1, 1, 5, 0, 4, 1, 0, 6, 0],
    "Style": 
    [2, 1, 2, 1, 1, 1, 1, 2, 0, 1, 4, 4, 2, 0, 1, 3, 1, 1, 1, 1, 2, 2, 1, 0, 1],
    "Coherence": 
    [1, 1, 1, 0, 0, 0, 2, 0, 2, 1, 2, 0, 0, 1, 2, 0, 0, 2, 1, 0, 0, 1, 1, 0, 1],
    "Accuracy": 
    [0, 0, 0, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 2, 2, 1, 0, 1, 1, 1, 1, 0, 1],
    "Consistency": 
    [0, 0, 0, 2, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 2, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0]
}
df = pd.DataFrame(data)

language_colors = {
    "ZH": "#e41a1c",  # Red
    "FR": "#377eb8",  # Blue
    "JA": "#4daf4a",  # Green
    "PT": "#984ea3",  # Purple
    "ES": "#ff7f00"   # Orange
}

# ------------------------------------------------------------------------
#  3) CAT Tool Analysis Data
# ------------------------------------------------------------------------
data_ZH = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Total Words': [10200, 10050, 10150, 10100, 10200],
    'WWC': [10120, 9830, 8150, 7680, 7520],
    'Context Match': [0, 50, 200, 300, 400],
    'Repetitions': [50, 100, 150, 200, 220],
    '101%': [0, 0, 80, 100, 150],
    '100%': [0, 0, 100, 150, 200],
    '95%-99%': [20, 30, 300, 350, 400],
    '85%-94%': [30, 30, 200, 250, 300],
    '75%-84%': [30, 30, 150, 200, 250],
    '50%-74%': [3500, 3600, 150, 150, 150],
    'No Match': [6570, 6210, 8820, 8400, 8130]
}
data_FR = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Total Words': [10050, 10080, 10100, 10150, 10200],
    'WWC': [9900, 9700, 9500, 9330, 9150],
    'Context Match': [0, 200, 400, 600, 800],
    'Repetitions': [150, 180, 200, 220, 250],
    '101%': [0, 50, 80, 100, 150],
    '100%': [0, 50, 100, 150, 200],
    '95%-99%': [150, 200, 300, 400, 450],
    '85%-94%': [100, 150, 200, 250, 300],
    '75%-84%': [100, 120, 150, 200, 250],
    '50%-74%': [200, 150, 100, 80, 50],
    'No Match': [9350, 8980, 8570, 8150, 7750]
}
data_JA = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Total Words': [10040, 10100, 10150, 10200, 10280],
    'WWC': [9890, 9720, 9450, 9280, 9130],
    'Context Match': [0, 200, 500, 700, 900],
    'Repetitions': [150, 180, 200, 220, 250],
    '101%': [0, 40, 80, 120, 150],
    '100%': [0, 60, 100, 150, 200],
    '95%-99%': [100, 200, 300, 400, 500],
    '85%-94%': [50, 100, 200, 250, 300],
    '75%-84%': [50, 100, 150, 200, 250],
    '50%-74%': [200, 150, 80, 70, 50],
    'No Match': [9490, 9070, 8530, 8090, 7680]
}
data_ES = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Total Words': [10100, 10200, 10300, 10400, 10500],
    'WWC': [10000, 7500, 7050, 6600, 6150],  # 假设的加权字数，突出 10 月后降幅
    'Context Match': [0, 2500, 3000, 3500, 4000],
    'Repetitions': [100, 200, 250, 300, 350],
    '101%': [0, 100, 150, 200, 250],
    '100%': [0, 150, 300, 400, 500],
    '95%-99%': [50, 500, 600, 700, 800],
    '85%-94%': [50, 400, 500, 600, 700],
    '75%-84%': [100, 300, 400, 500, 500],
    '50%-74%': [200, 200, 150, 100, 50],
    'No Match': [9600, 5850, 4950, 4100, 3350]
}
data_PT = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Total Words': [10020, 10100, 10150, 10200, 10300],
    'WWC': [9900, 9800, 9670, 9500, 9380],
    'Context Match': [0, 150, 300, 500, 700],
    'Repetitions': [120, 150, 180, 200, 220],
    '101%': [0, 30, 60, 100, 150],
    '100%': [0, 40, 100, 150, 200],
    '95%-99%': [80, 200, 300, 400, 500],
    '85%-94%': [50, 100, 200, 250, 300],
    '75%-84%': [50, 100, 150, 200, 250],
    '50%-74%': [150, 150, 80, 70, 50],
    'No Match': [9570, 9180, 8780, 8330, 7930]
}

df_ZH = pd.DataFrame(data_ZH)
df_ZH["Language"] = "ZH"
df_FR = pd.DataFrame(data_FR)
df_FR["Language"] = "FR"
df_JA = pd.DataFrame(data_JA)
df_JA["Language"] = "JA"
df_ES = pd.DataFrame(data_ES)
df_ES["Language"] = "ES"
df_PT = pd.DataFrame(data_PT)
df_PT["Language"] = "PT"

df_cat = pd.concat([df_ZH, df_FR, df_JA, df_ES, df_PT], ignore_index=True)

# ------------------------------------------------------------------------
#  4) Initialize Dash App with external Bootstrap stylesheet
# ------------------------------------------------------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
server = app.server

# ------------------------------------------------------------------------
#  5) Define Layout for Each Dashboard
# ------------------------------------------------------------------------
def lqa_report_layout():
    return html.Div(className="box", children=[
        dbc.Row([
            dbc.Col([
                html.Label("Select Language:", className="fw-bold mb-2"),
                dcc.Dropdown(
                    id="language-filter",
                    options=[{"label": lang, "value": lang} for lang in df["Language"].unique()],
                    placeholder="Select language (default all)",
                    multi=True
                ),
            ], width=6),
            dbc.Col([
                html.Label("Select Month:", className="fw-bold mb-2"),
                dcc.Dropdown(
                    id="month-filter",
                    options=[{"label": month, "value": month} for month in df["Month"].unique()],
                    placeholder="Select months (default all)",
                    multi=True
                ),
            ], width=6)
        ], className="mb-3"),
        dcc.Graph(id="bar-line-chart", className="graph-margin")
    ])

def cat_tool_layout():
    return html.Div(className="box", children=[
        html.H2("CAT Tool Analysis Dashboard", className="section-title"),
        dbc.Row([
            dbc.Col([
                html.Label("Select Language:", className="fw-bold mb-2"),
                dcc.Dropdown(
                    id="cat-language-filter",
                    options=[{"label": lang, "value": lang} for lang in df_cat["Language"].unique()],
                    placeholder="Select language (default all)",
                    multi=True
                )
            ], width=6),
            dbc.Col([
                html.Label("Select Month:", className="fw-bold mb-2"),
                dcc.Dropdown(
                    id="cat-month-filter",
                    options=[{"label": month, "value": month} for month in df_cat["Month"].unique()],
                    placeholder="Select months (default all)",
                    multi=True
                )
            ], width=6),
        ], className="mb-3"),
        dcc.Graph(id="cat-tool-counts-chart", className="graph-margin"),
        dcc.Graph(id="cat-tool-percentages-chart", className="graph-margin"),
        dcc.Graph(id="cat-tool-donut-charts", className="graph-margin")
    ])

def timeline_layout():
    # Add a "MonthStr" column to help define the options
    df_timeline["MonthStr"] = df_timeline["Start"].dt.to_period("M").astype(str)
    all_languages = sorted(df_timeline["Language"].unique())
    all_months = sorted(df_timeline["MonthStr"].unique())

    return html.Div(className="box", children=[
        html.H2("Time Line Dashboard", className="section-title"),
        dbc.Row([
            dbc.Col([
                html.Label("Select Language:", className="fw-bold mb-2"),
                dcc.Dropdown(
                    id="timeline-language-filter",
                    options=[{"label": lang, "value": lang} for lang in all_languages],
                    multi=True,
                    placeholder="Select language (default all)"
                )
            ], width=6),
            dbc.Col([
                html.Label("Select Month:", className="fw-bold mb-2"),
                dcc.Dropdown(
                    id="timeline-month-filter",
                    options=[{"label": m, "value": m} for m in all_months],
                    multi=True,
                    placeholder="Select months (default all)"
                )
            ], width=6),
        ], className="mb-3"),
        # 这里统一让 Graph 占满一整行，且高度固定 900px
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="timeline-chart",
                    style={"width": "100%", "height": "900px"}
                ),
                width=12
            )
        ])
    ])

# Main layout with Tabs
app.layout = html.Div([
    html.H1(
        "Multilingual Translation Quality Dashboard",
        className="main-title"
    ),
    dcc.Tabs(
        id="tabs",
        value="tab-lqa",
        className="tabs-container",
        children=[
            dcc.Tab(label="LQA Report", value="tab-lqa", className="tab", selected_className="tab--selected"),
            dcc.Tab(label="CAT Tool Analysis", value="tab-cat", className="tab", selected_className="tab--selected"),
            dcc.Tab(label="Time Line Dashboard", value="tab-timeline", className="tab", selected_className="tab--selected")
        ]
    ),
    html.Div(id="tabs-content", className="content-area")
], className="app-container")

# ------------------------------------------------------------------------
#  7) Callback: Render tab content
# ------------------------------------------------------------------------
@callback(
    Output("tabs-content", "children"),
    Input("tabs", "value")
)
def render_content(tab):
    if tab == "tab-lqa":
        return lqa_report_layout()
    elif tab == "tab-cat":
        return cat_tool_layout()
    elif tab == "tab-timeline":
        return timeline_layout()
    else:
        return html.Div("No dashboard found for the selected tab.")

# ------------------------------------------------------------------------
#  8) LQA Report Callbacks
# ------------------------------------------------------------------------
@callback(
    Output("bar-line-chart", "figure"),
    Input("language-filter", "value"),
    Input("month-filter", "value")
)
def update_chart(selected_language, selected_month):
    filtered_df = df.copy()
    if selected_language:
        filtered_df = filtered_df[filtered_df["Language"].isin(selected_language)]
    if selected_month:
        filtered_df = filtered_df[filtered_df["Month"].isin(selected_month)]
    if filtered_df.empty:
        return go.Figure()

    # 准备柱状图 traces
    bar_traces = []
    error_types = ["Fluency", "Terminology", "Style", "Coherence", "Accuracy", "Consistency"]
    error_colors = ["#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62", "#8da0cb"]
    
    # 新增：用一个 set 记录已经在图例中出现过的 error type
    shown_legend_error_types = set()
    
    unique_months = filtered_df["Month"].unique()
    for month in unique_months:
        month_df = filtered_df[filtered_df["Month"] == month]
        for lang in month_df["Language"].unique():
            lang_df = month_df[month_df["Language"] == lang]
            for error_type, color in zip(error_types, error_colors):
                # 只在某个 error_type 首次出现时显示图例，后续相同类型的柱状图不再重复显示图例
                show_legend = error_type not in shown_legend_error_types

                bar_traces.append(go.Bar(
                    name=error_type,
                    legendgroup=error_type,
                    showlegend=show_legend,
                    x=[f"{lang}<br>{month}"],
                    y=lang_df[error_type],
                    marker=dict(color=color),
                    hoverinfo="y+name"
                ))
                
                if show_legend:
                    shown_legend_error_types.add(error_type)

    # 准备 Penalty Score 折线图 traces
    line_traces = []
    for lang in filtered_df["Language"].unique():
        lang_df = filtered_df[filtered_df["Language"] == lang]
        line_traces.append(go.Scatter(
            name=f"Penalty Score ({lang})",
            x=[f"{lang}<br>{m}" for m in lang_df["Month"]],
            y=lang_df["Penalty Score"],
            mode="lines+markers",
            line=dict(color=language_colors.get(lang, "black"), width=2),
            marker=dict(size=8, symbol="circle"),
            hoverinfo="text",
            text=[
                f"Language: {lang}<br>Month: {m}<br>Penalty Score: {ps}"
                for m, ps in zip(lang_df["Month"], lang_df["Penalty Score"])
            ],
            hovertemplate="%{text}"
        ))

    fig = go.Figure(data=bar_traces + line_traces)

    # 维持原有的竖线逻辑
    selected_lang_count = filtered_df["Language"].unique()
    selected_month_count = filtered_df["Month"].unique()
    vline_count = min(len(selected_lang_count), len(selected_month_count))
    for i in range(vline_count - 1):
        fig.add_vline(x=i * 5 + 4.5, line_width=1, line_dash="dash", line_color="black")

    fig.update_layout(
        barmode="stack",
        title="Error Types & Penalty Score",
        xaxis=dict(title="Month"),
        yaxis=dict(title="Penalty"),
        legend_title="Error Types",
        template="plotly_white",
        autosize=True,
        height=600,
    )

    # 维持原有的宽度控制逻辑
    if (selected_language and len(selected_language) == 1) or (selected_month and len(selected_month) == 1):
        bar_width = 0.3
    else:
        unique_months_count = filtered_df["Month"].nunique()
        if unique_months_count == 2:
            bar_width = 0.4
        else:
            bar_width = None

    if bar_width is not None:
        for trace in fig.data:
            if isinstance(trace, go.Bar):
                trace.width = bar_width

    return fig

# ------------------------------------------------------------------------
#  9) CAT Tool Analysis Callbacks
# ------------------------------------------------------------------------
@callback(
    Output("cat-tool-counts-chart", "figure"),
    Output("cat-tool-percentages-chart", "figure"),
    Output("cat-tool-donut-charts", "figure"),
    Input("cat-language-filter", "value"),
    Input("cat-month-filter", "value")
)
def update_cat_tool_charts(selected_language, selected_month):
    filtered_df = df_cat.copy()
    if selected_language:
        filtered_df = filtered_df[filtered_df["Language"].isin(selected_language)]
    if selected_month:
        filtered_df = filtered_df[filtered_df["Month"].isin(selected_month)]
    if filtered_df.empty:
        return go.Figure(), go.Figure(), go.Figure()

    # (1) Count Metrics
    counts_metrics = ["Total Words", "WWC", "Context Match", "Repetitions", "No Match"]
    df_counts = filtered_df.melt(
        id_vars=["Month", "Language"],
        value_vars=counts_metrics,
        var_name="Metric",
        value_name="Value"
    )
    fig_counts = px.line(
        df_counts,
        x="Month",
        y="Value",
        color="Metric",
        markers=True,
        facet_col="Language",
        title="Count Metrics Trend",
        # category_orders={"Month": ["Sep", "Oct", "Nov", "Dec", "Jan"]}
    )
    fig_counts.update_layout(legend_title_text="Metrics", template="plotly_white")

    # (2) Match Range Distribution (Stacked Bar)
    perc_metrics = ["101%", "100%", "95%-99%", "85%-94%", "75%-84%", "50%-74%"]
    df_perc = filtered_df.melt(
        id_vars=["Month", "Language"],
        value_vars=perc_metrics,
        var_name="Metric",
        value_name="Value"
    )
    fig_perc = px.bar(
        df_perc,
        x="Month",
        y="Value",
        color="Metric",
        barmode="stack",
        facet_col="Language",
        title="Distribution of Fuzzy Match Ranges",
        # category_orders={"Month": ["Sep", "Oct", "Nov", "Dec", "Jan"]}
    )
    fig_perc.update_layout(legend_title_text="Match Range", template="plotly_white")
     # 新增：控制柱状图宽度
    if (selected_language and len(selected_language) == 1) or (selected_month and len(selected_month) == 1):
        bar_width = 0.3
    else:
        unique_months_count = filtered_df["Month"].nunique()
        if unique_months_count == 2:
            bar_width = 0.4
        else:
            bar_width = None

    if bar_width is not None:
        for trace in fig_perc.data:
            if isinstance(trace, go.Bar):
                trace.width = bar_width   

    # (3) Donut Charts
    donut_categories = [
        "Context Match", "Repetitions", "101%", "100%",
        "95%-99%", "85%-94%", "75%-84%", "50%-74%", "No Match"
    ]
    fixed_month_order = ["Sep", "Oct", "Nov", "Dec", "Jan"]
    unique_langs = sorted(filtered_df["Language"].unique())
    unique_months = [m for m in fixed_month_order if m in filtered_df["Month"].unique()]

    n_rows = len(unique_langs)
    n_cols = len(unique_months)

    subplot_titles = []
    for lang in unique_langs:
        for month in unique_months:
            subplot_titles.append(f"{lang} - {month}")

    fig_donut = make_subplots(
        rows=n_rows,
        cols=n_cols,
        specs=[[{"type": "domain"} for _ in range(n_cols)] for _ in range(n_rows)],
        subplot_titles=subplot_titles
    )

    row_i, col_i = 1, 1
    for lang in unique_langs:
        for month in unique_months:
            sub_df = filtered_df[(filtered_df["Language"] == lang) & (filtered_df["Month"] == month)]
            if not sub_df.empty:
                values = [sub_df[cat].sum() for cat in donut_categories]
            else:
                values = [0] * len(donut_categories)

            fig_donut.add_trace(
                go.Pie(
                    labels=donut_categories,
                    values=values,
                    name=f"{lang}-{month}",
                    hole=0.4,
                    hovertemplate="%{label}: %{value} <extra></extra>"
                ),
                row=row_i,
                col=col_i
            )
            col_i += 1
        row_i += 1
        col_i = 1

    fig_donut.update_traces(textposition="inside", textinfo="percent+label")
    fig_donut.update_layout(
        title_text="Match Types Distribution by Language & Month (Donut Charts)",
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.1
        ),
        height=300 * n_rows,
        width=300 * n_cols,
        template="plotly_white"
    )

    return fig_counts, fig_perc, fig_donut

# ------------------------------------------------------------------------
# 10) Time Line Dashboard Callbacks
# ------------------------------------------------------------------------
@callback(
    Output("timeline-chart", "figure"),
    Input("timeline-language-filter", "value"),
    Input("timeline-month-filter", "value")
)
def update_timeline_chart(selected_langs, selected_months):
    filtered_df = df_timeline.copy()
    if selected_months and len(selected_months) > 0:
        mask = filtered_df.apply(task_in_selected_months, axis=1, args=(selected_months,))
        filtered_df = filtered_df[mask]
    if selected_langs and len(selected_langs) > 0:
        filtered_df = filtered_df[filtered_df["Language"].isin(selected_langs)]
    if filtered_df.empty:
        return go.Figure()

    fig = px.timeline(
        filtered_df,
        x_start="Start",
        x_end="End",
        y="Task",
        color="Language",
        color_discrete_map=timeline_color_map,
        hover_data=["Language", "Type", "Start", "End"]
    )
    fig.update_yaxes(autorange="reversed")

    fig.update_layout(barmode='group', template="plotly_white")
    fig.update_traces(width=0.2)

    # Make "Plan" visually distinct
    for trace in fig.data:
        if trace.name == "Plan":
            trace.marker.line.width = 2
            trace.marker.line.color = "black"
            trace.marker.pattern.shape = "/"
            trace.opacity = 1.0

    fig.update_layout(
        barmode='group',
        template='plotly_white',
        title="Timeline Comparison (Plan vs Actual)",
        xaxis_title="Date",
        yaxis_title="Tasks",
        autosize=True,                 # 重要：让图表自动填充容器宽度
        margin=dict(l=50, r=50, t=50, b=50)  # 适度留白
    )
    return fig

# ------------------------------------------------------------------------
# 11) Run the App
# ------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True)