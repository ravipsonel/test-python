# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:35:04 2024

Main file for REST Application.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import baseRouter, apiRouter

# ----------------------------------------------------------------------------

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


# Router
app.include_router(baseRouter)
app.include_router(apiRouter)
# ----------------------------------------------------------------------------
