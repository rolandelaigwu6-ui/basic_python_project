# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/products")
# def get_products():
#     return [
#         {"id": 1, "name": "Laptop"},
#         {"id": 2, "name": "Phone"}
#     ]


from fastapi import FastAPI, HTTPException


app = FastAPI()

products = {
    1: "Laptop",
    2:"Phone",
    3:"Book"
}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )
    return {
        "id": product_id,
        "name": products[product_id]
    }