from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/reviews/{company_name}")
def get_company_reviews(company_name: str):
    # Placeholder logic to fetch reviews for a company
    reviews = {"company_name": company_name, "reviews": ["Review 1", "Review 2", "Review 3"]}
    return reviews
