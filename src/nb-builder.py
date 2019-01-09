#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# This script demonstrates how to execute all fields in a Jupyter notebook file (*.ipynb)
# with the Jupyter nbformat + nbconvert libraries
#
# Dependencies for this script can be installed with:
#
#    $ pip3 install --upgrade jupyter
#
# ** note that there may be additional dependencies in the jupyter notebook that is executed **
#
# Run the script with:
#
#   $ python3 nb-builder.py
#

import os
import sys

import nbformat
from nbconvert.preprocessors import CellExecutionError, ExecutePreprocessor

PARDIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
NOTEBOOK_INPATH = os.path.join(PARDIR, "jupyter_notebooks", "gs-report.ipynb")
NOTEBOOK_OUTPATH = os.path.join(PARDIR, "jupyter_notebooks", "gs-report-built.ipynb")

with open(NOTEBOOK_INPATH) as f:
    nb = nbformat.read(f, as_version=4)

# setup the notebook preprocessor with defined timeout (in seconds)
ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

try:
    # execute the notebook file
    out = ep.preprocess(
        nb,
        {
            "metadata": {
                "path": os.path.join(
                    os.path.abspath(os.path.join(os.getcwd(), os.pardir)),
                    "jupyter_notebooks",
                )
            }
        },
    )
    # write the executed file out to disk
    with open(NOTEBOOK_OUTPATH, mode="wt") as f:
        nbformat.write(nb, f)
        print("Compiled notebook to path: '{}' ".format(NOTEBOOK_OUTPATH))
    sys.exit(0)
except CellExecutionError as cee:
    out = None
    msg = (
        'Error occurred during the execution of one or more of the notebook source fields in "%s".\n\n'
        % NOTEBOOK_INPATH
    )
    sys.stderr.write(msg + os.linesep)
    sys.stderr.write(str(cee) + os.linesep)
    sys.exit(1)
except Exception as e:
    out = None
    msg = 'Error during execution of the notebook "%s".\n\n' % NOTEBOOK_INPATH
    sys.stderr.write(msg + os.linesep)
    sys.stderr.write(str(e) + os.linesep)
    sys.exit(1)
