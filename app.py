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
    "Penalty Score": [
        16, 8, 5, 10, 6,
        9, 9, 9, 7, 9,
        12, 7, 9, 3, 5,
        9, 9, 5, 8, 4,
        2, 6, 9, 7, 6
    ],
    "Fluency": [3, 1, 2, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2, 0],
    "Terminology": [10, 5, 0, 5, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 2, 0, 2, 1],
    "Style": [2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 0, 1, 1, 1, 1, 2, 1, 0, 2, 3, 2, 1],
    "Coherence": [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    "Accuracy": [0, 0, 0, 1, 0, 2, 2, 1, 1, 0, 0, 0, 1, 0, 0, 2, 2, 1, 0, 1, 0, 0, 2, 0, 1],
    "Consistency": [0, 0, 0, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 0, 1, 0, 1, 2, 2, 0, 2, 0, 2]
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
    'Total Words': [10247, 10552, 10543, 10417, 10149],
    'WWC': [10050.85, 9444.05, 9181.45, 8944.25, 8756.1],
    'Context Match': [0, 156, 244, 299, 200],
    'Repetitions': [166, 142, 134, 154, 178],
    '101%': [0, 243, 289, 344, 258],
    '100%': [0, 289, 322, 367, 457],
    '95%-99%': [0, 289, 364, 254, 266],
    '85%-94%': [0, 213, 299, 322, 389],
    '75%-84%': [212, 441, 567, 589, 489],
    '50%-74%': [419, 659, 735, 877, 678],
    'No Match': [9450, 8120, 7589, 7211, 7234]
}
data_FR = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Total Words': [10247, 10049, 10126, 10025, 10339],
    'WWC': [9879.85, 9275.2, 8814.1, 8235.5, 7653.65],
    'Context Match': [0, 264, 564, 848, 1704],
    'Repetitions': [204, 207, 206, 204, 200],
    '101%': [0, 28, 47, 50, 80],
    '100%': [0, 10, 31, 120, 130],
    '95%-99%': [305, 525, 927, 1122, 1301],
    '85%-94%': [36, 29, 1, 80, 50],
    '75%-84%': [24, 35, 50, 47, 25],
    '50%-74%': [35, 20, 22, 50, 43],
    'No Match': [9643, 8931, 8278, 7504, 6806]
}
data_JA = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Total Words': [10210, 10267, 10834, 10399, 10494],
    'WWC': [9948, 9552.55, 9539.0, 8833.3, 8382.5],
    'Context Match': [0, 265, 571, 885, 1223],
    'Repetitions': [309, 207, 206, 207, 201],
    '101%': [0, 8, 21, 49, 46],
    '100%': [0, 34, 23, 35, 1],
    '95%-99%': [5, 325, 930, 839, 1311],
    '85%-94%': [17, 123, 31, 31, 35],
    '75%-84%': [15, 149, 25, 49, 5],
    '50%-74%': [40, 23, 30, 20, 32],
    'No Match': [9824, 9133, 8997, 8284, 7640]
}
data_ES = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Total Words': [10310, 10458, 10349, 10254, 10618],
    'WWC': [10026, 8574.15, 7681.95, 7123.25, 6581.2],
    'Context Match': [0, 1520, 2176, 2447, 3401],
    'Repetitions': [200, 202, 207, 203, 200],
    '101%': [0, 25, 18, 40, 0],
    '100%': [0, 16, 4, 43, 8],
    '95%-99%': [50, 506, 832, 1121, 1300],
    '85%-94%': [60, 5, 31, 30, 48],
    '75%-84%': [250, 43, 45, 24, 49],
    '50%-74%': [400, 45, 25, 45, 10],
    'No Match': [9350, 8096, 7011, 6301, 5602]
}
data_PT = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Total Words': [10092, 10249, 10272, 10213, 10039],
    'WWC': [9838.8, 8989.55, 8641.7, 8168.55, 7617.4],
    'Context Match': [0, 324, 899, 1215, 1525],
    'Repetitions': [208, 602, 209, 209, 209],
    '101%': [0, 46, 44, 49, 13],
    '100%': [0, 4, 30, 22, 41],
    '95%-99%': [0, 709, 942, 1153, 1360],
    '85%-94%': [12, 16, 44, 41, 33],
    '75%-84%': [25, 15, 12, 35, 31],
    '50%-74%': [34, 45, 16, 39, 14],
    'No Match': [9307, 8488, 8076, 7450, 6813]
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

    bar_traces = []
    error_types = ["Fluency", "Terminology", "Style", "Coherence", "Accuracy", "Consistency"]
    error_colors = ["#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62", "#8da0cb"]
    for error_type, color in zip(error_types, error_colors):
        bar_traces.append(go.Bar(
            name=error_type,
            x=filtered_df["Month"],
            y=filtered_df[error_type],
            marker=dict(color=color),
            hoverinfo="text",
            hovertext=[
                f"Language: {lang}<br>Month: {m}<br>{error_type}: {val}"
                for lang, m, val in zip(filtered_df["Language"], filtered_df["Month"], filtered_df[error_type])
            ],
            hovertemplate="%{hovertext}"
        ))

    line_traces = []
    for lang in filtered_df["Language"].unique():
        lang_df = filtered_df[filtered_df["Language"] == lang]
        line_traces.append(go.Scatter(
            name=f"Penalty Score ({lang})",
            x=lang_df["Month"],
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
    fig.update_layout(
        barmode="stack",
        title="Error Types & Penalty Score",
        xaxis=dict(title="Month"),
        yaxis=dict(title="Number of Errors"),
        legend_title="Error Types",
        template="plotly_white",
        autosize=True
    )

    # 动态设置柱子宽度
    unique_months = filtered_df["Month"].nunique()
    if unique_months == 1:
        bar_width = 0.3
    elif unique_months == 2:
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
        category_orders={"Month": ["Sep", "Oct", "Nov", "Dec", "Jan"]}
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
        category_orders={"Month": ["Sep", "Oct", "Nov", "Dec", "Jan"]}
    )
    fig_perc.update_layout(legend_title_text="Match Range", template="plotly_white")

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