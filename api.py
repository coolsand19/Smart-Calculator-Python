from fastapi import FastAPI
from main import makeEquation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity, can be restricted in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Calculator API"}

@app.post("/calculate")
async def calculate(query: dict):
    equation = query.get("equation")
    if not equation:
        return {"error": "No equation provided"}
    
    # The makeEquation function expects a list of strings
    equation_parts = equation.split()
    
    result = makeEquation(equation_parts)
    
    if result is None:
        return {"error": "Could not parse the input!. Please enter a valid equation."}
        
    return {"result": result}
