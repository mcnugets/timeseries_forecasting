# timeseries_forecasting

## Get started

pull the repo first and install the deps
```bash
# Clone the repo (replace <owner> with the correct GitHub user/org)
git clone https://github.com/mcnugets/timeseries_forecasting.git
cd timeseries_forecasting

python3 -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
then do the following
```fastapi dev app.py```
once you ensured server is runnig run curl:
```bash
curl -X POST http://127.0.0.1:8000/predict
```
or go to `http://127.0.0.1:8000/docs` to test the api

---
`/predict` endpoint runs both OCR and LR. The visualisation gets saved in roor dir of the project.
