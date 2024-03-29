# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route('/calculate')
def calculate():
    return_str = ''
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])

    return_str += 'x dot y : {}'.format(str(np.dot(x, y)))
    # data=pd.read_csv("day.csv")
    # import statsmodels.formula.api as smf
    #
    # #lm.params
    #
    # #lm.pvalues
    # print(lm.rsquared)
    # print(lm.rsquared_adj)
    #
    # print(lm.summary())
    #
    #
    # print ( data.head() )
    # #return_str += 'x: {} , y: {}<br />'.format(str(x), str(y))
    # return_str += str(lm.rsquared) + ' , ' + str(lm.rsquared_adj)
    # # Multiply matrices
    # #return_str += 'x dot y : {}'.format(str(np.dot(x, y)))
    return return_str


@app.route('/lineal')
def lineal():
    return_str = ''
    data = pd.read_csv("day.csv")

    import statsmodels.formula.api as smf

    lm = smf.ols(formula="cnt~weathersit", data=data).fit()
    lm.params
    print(lm.summary())

    return_str += str(lm.rsquared) + ' , ' + str(lm.rsquared_adj)

    return return_str


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
