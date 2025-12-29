from fastapi import FastAPI
from fastapi import APIRouter
from time_series_forecasting import make_prediction
from iimg2text import img2text



router = APIRouter()



@router.post("/predict")
def predict():
    """POST function for performing OCR and LR"""
    make_prediction()
    ocr = img2text()
    result = ocr.run_ocr('images/')  
    return {
        "status": 200,
        "message": "LR graph saved and images analysed!",
        "data": result
    }


app = FastAPI()
app.include_router(router=router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
