# ticket-prediction-flight-server

Type `uvicorn main:app` to run the uvicorn server on port `8000`

This prediction feature was developed using python and applied to the [back-end-server-flights](https://github.com/MaysaM-M-Mousa/back-end-server-flights).

`Linear Regression` was used as an algorithm to predict the price of the ticket in [this](https://www.kaggle.com/datasets/zernach/2018-airplane-flights) dataset.

We got R<sup>2</sup> of `0.333` using LR.

Check the `.ipynb` file in the `notebooks` folder to see more details about the model training.

The feature was deployed on `Heroku`. Follow the [link](https://ticket-prediction-app.herokuapp.com) to access the deployed feature.

There are 2 endpoints for this deployed feature:
  * GET [URL](https://ticket-prediction-app.herokuapp.com)/
  * POST [URL](https://ticket-prediction-app.herokuapp.com)/ticket/predict


### Note: It's important to mention that it's very hard to get high R<sup>2</sup> values with this dataset because of the very low correlation between the independent variables and dependent variable (there is barely a noticable pattern in this dataset). Anyway we got R<sup>2</sup> value equals to `0.333` using only linear regression without trying to optimize with advanced techniques which may yield enhancing R<sup>2</sup> a little bit. 
