# Building a REST API with FastAPI, PostgreSQL, and Swagger Documentation
Using FastAPI, we'll create a basic API for employee performance review. This API will be tied to a PostgreSQL database, ensuring the data storage and retrieval. Later on, we'll use Swagger documentation for interacting with the API. FastAPI automatically generates the Swagger documentation for our API, making it easy to test and visualize our endpoints.

The API will cover the following operations:

* **GET** requests to retrieve employee reviews
    
* **POST** requests to add new employee reviews
    
* **PUT** requests to update existing employee reviews
    
* **DELETE** requests to remove employee reviews
    
---

## Set Up the FastAPI Environment in Windows
Step 1: Install and activate the virtual environment using the Visual Studio Code (VS Code) terminal, then install FastAPI and Uvicorn.

For more information on this step, see the *Set Up the FastAPI Environment in Windows* section in [FastAPI Performance: Comparing Sync and Async Endpoints](../doc12/FastAPI_Performance.md){target="_blank"}.

Step 2: Install `asyncpg` using the command: `pip install asyncpg`

![pip install asyncpg](fadb1.png)

`asyncpg` lets you interact with the PostgreSQL database asynchronously, which can enhance your application's performance and responsiveness.

## Prepare Your PostgreSQL Database and Environment

Step 1: Connect to the PostgreSQL database and create a table for storing the employee reviews. To create the table, you can use this command in the SQL shell:

```pgsql
CREATE TABLE employee_reviews (
    employee_id INT,
    employee_name VARCHAR(255) NOT NULL,
    evaluation_period VARCHAR(255) NOT NULL,
    performance_rating INT,
    feedback_comments TEXT,	
    goals_objectives TEXT,
    reviewer_id INT,
    reviewer_name VARCHAR(255),
    PRIMARY KEY (employee_id, evaluation_period)
);
```

The combination of `employee_id` and `evaluation_period` must be unique, which is why they are set as the primary key. This setup allows employees to have multiple reviews for different periods.

When you create the table, you should see the response as *CREATE TABLE*:

![Response as CREATE TABLE](fadb2.png)

Step 2: There are several ways to store sensitive information. For now, we'll store the database username and password in an environment variable and access it from the application.

Type this command in the VS Code terminal (PowerShell):

```powershell
$env:DATABASE_URL="postgresql://myusername:mypassword@localhost/dbname
```

You'll need to replace `myusername` and `mypassword` with your actual database username and password. Also, replace `dbname` with the name of the database you want to connect to.

Note that the environment variable set using this command is temporary and will be lost when you close the terminal or deactivate the virtual environment.

## Create the FastAPI Application

Step 1: Create a file named `employee_reviews.py`.

Step 2: Import necessary components:

```python
import os
import asyncpg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
```

* `import os`: To read the environment variable for the database.
    
* `import asyncpg`: To interact with the PostgreSQL database.
    
* `from fastapi import FastAPI, HTTPException`: To import the main components of FastAPI. FastAPI is the web framework, and HTTPException is used to handle errors.
    
* `from pydantic import BaseModel`: To define the structure of the data we expect in requests and responses.
    

Step 3: Initialize the FastAPI application:

```python
app = FastAPI(
    title="Dinesh's Employee Review API",
    version="1.0",
    description="Create, update, or delete a performance review. You can also see all reviews.",
    contact={
        "name": "Dinesh Nair",
        "email": "dineshn@example.com"
    }
)
```

This initializes the FastAPI application with metadata such as title, version, description, and contact information.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">The auto-generated Swagger documentation will display this metadata to the users.</div>
</div>

Step 4: Define a data model for employee reviews using Pydantic. Each field has a type, ensuring data validation.

```python
class EmployeeReview(BaseModel):
    employee_id: int
    employee_name: str
    evaluation_period: str
    performance_rating: int
    feedback_comments: str
    goals_objectives: str
    reviewer_id: int
    reviewer_name: str
```

Pydantic uses Python types to validate and parse data. By defining the `EmployeeReview` class as a subclass of `BaseModel`, we create a data model where each field has a specific type. This means that `EmployeeReview` inherits all the features and capabilities of `BaseModel`, which ensures that the data is validated according to the types specified for each field.

For example:

* `employee_id` and `reviewer_id` must be integers.
    
* `employee_name`, `evaluation_period`, `feedback_comments`, `goals_objectives`, and `reviewer_name` must be strings.
    
* `performance_rating` must be an integer.
    

This ensures that only valid data is accepted, which helps maintain data integrity and prevents errors.

Step 5: Create the database connection:

```python
DATABASE_URL = os.getenv("DATABASE_URL")

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)
```

* `os.getenv`: Reads the `DATABASE_URL` environment variable to get the database connection string.
    
* `connect_to_db()`: Asynchronous function that connects to the PostgreSQL database using `asyncpg`.
    

Step 6: Define the endpoint for creating an employee review:

```python
@app.post("/employee_reviews/", response_model=EmployeeReview)
async def create_employee_review(employee_review: EmployeeReview):
    """
    Create a performance review for an employee.
    
    Fields:
    - **Employee ID**: Unique identifier of the employee whose performance is being reviewed.
    - **Employee Name**: Name of the employee.
    - **Evaluation Period**: Evaluation period for the review, such as "Q1 2023" or "January - June 2024".
    - **Performance Rating**: Performance rating of the employee. For example, on a scale of 1 to 5, you can enter 4.
    - **Feedback Comments**: Feedback comments for the employee.
    - **Goals Objectives**: Goals and objectives for the employee, such as increasing sales by 10%.
    - **Reviewer ID**: Unique identifier of the reviewer.
    - **Reviewer Name**: Name of the reviewer.
    """
    conn = await connect_to_db()
    try:
        await conn.execute('''
            INSERT INTO employee_reviews(employee_id, employee_name, evaluation_period, performance_rating, feedback_comments, goals_objectives, reviewer_id, reviewer_name)
            VALUES($1, $2, $3, $4, $5, $6, $7, $8)
        ''', employee_review.employee_id, employee_review.employee_name, employee_review.evaluation_period, employee_review.performance_rating, employee_review.feedback_comments, employee_review.goals_objectives, employee_review.reviewer_id, employee_review.reviewer_name)
    finally:
        await conn.close()
    return employee_review
```

The code connects to the database, runs an SQL `INSERT` command, and returns the created review.

* `app.post("/employee_reviews/")`: Defines a POST endpoint for creating a new employee review.
    
* `response_model=EmployeeReview`: Specifies the response model.
    
* **Docstring**: Provides a detailed description of the endpoint and the fields expected in the request body. FastAPI uses the docstring in the auto-generated Swagger documentation.
    

Step 7: Define the endpoint for retrieving employee reviews:

```python
@app.get("/employee_reviews/", response_model=list[EmployeeReview])
async def read_employee_reviews():
    # (Docstring describing what the endpoint does and its fields)
    conn = await connect_to_db()
    try:
        rows = await conn.fetch('SELECT * FROM employee_reviews')
    finally:
        await conn.close()
    
    if rows:
        return [EmployeeReview(**row) for row in rows]
    raise HTTPException(status_code=404, detail="No reviews found")
```

The code:

* Retrieves all records from the `employee_reviews` table.
    
* Converts these records into a list of `EmployeeReview` objects and returns it as a response.
    

Step 8: Define the endpoint for updating an employee review:

```python
@app.put("/employee_reviews/{employee_id}", response_model=EmployeeReview)
async def update_employee_review(employee_id: int, employee_review: EmployeeReview):
    # (Docstring describing what the endpoint does and its fields)
    conn = await connect_to_db()
    try:
        result = await conn.execute('''
            UPDATE employee_reviews
            SET employee_name=$1, evaluation_period=$2, performance_rating=$3, feedback_comments=$4, goals_objectives=$5, reviewer_id=$6, reviewer_name=$7
            WHERE employee_id=$8
        ''', employee_review.employee_name, employee_review.evaluation_period, employee_review.performance_rating, employee_review.feedback_comments, employee_review.goals_objectives, employee_review.reviewer_id, employee_review.reviewer_name, employee_id)
    finally:
        await conn.close()
    if result == 'UPDATE 0':
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_review
```

The code:

* Updates the review data in the `employee_reviews` table where the `employee_id` matches.
    
* Returns the updated `employee_review` object as a response.
    

Step 9: Define the endpoint for deleting an employee review:

```python
@app.delete("/employee_reviews/{employee_id}")
async def delete_employee_review(employee_id: int):
    # (Docstring describing what the endpoint does)
    conn = await connect_to_db()
    try:
        result = await conn.execute('DELETE FROM employee_reviews WHERE employee_id=$1', employee_id)
    finally:
        await conn.close()
    if result == 'DELETE 0':
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee review deleted"}
```

The code:

* Deletes the review data from the `employee_reviews` table where the `employee_id` matches.
    
* Returns a success message indicating that the review was deleted.
    

Step 10: Run the FastAPI application using the Uvicorn server:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

## Run the Application

Run `employee_reviews.py`. Once the server is running, you should see an output indicating that Uvicorn is running on `http://127.0.0.1:8000`.

![Uvicorn server is running](fadb3.png)

## Use the Swagger Documentation Interface

FastAPI provides an interactive API documentation interface using Swagger, which makes it easy to test your endpoints. Open your web browser and go to `http://127.0.0.1:8000/docs`. You should see the Swagger documentation.

![Swagger doc with API metadata and available endpoints](fadb4swg.png)

The doc shows all the available endpoints. You can interact with the API directly from this interface by clicking on the endpoints and providing the necessary input data.

### Creating an Employee Review

Step 1: Expand POST in the doc. You can see the docstring explaining the endpoint and its fields:

![Endpoint description and its fields](fadb5.png)

Step 2: Click **Try it out**.

Step 3: Enter the request body:

![Request body such as employee name and performance rating](fadb6_clickexcafterthis.png)

Step 4: Click **Execute** to send the request to the API.

Step 5: You will see a 200 response if all goes well:

![200 response from server](fadb7_postresponse.png)

We'll create a couple more records:

```json
  {
    "employee_id": 12933,
    "employee_name": "Michael Johnson",
    "evaluation_period": "Q4 2024",
    "performance_rating": 4,
    "feedback_comments": "Met expectations.",
    "goals_objectives": "Improve client communication",
    "reviewer_id": 18855,
    "reviewer_name": "Emily Anderson"
  },
  {
    "employee_id": 12934,
    "employee_name": "Jessica Taylor",
    "evaluation_period": "Q4 2024",
    "performance_rating": 5,
    "feedback_comments": "Outstanding performance.",
    "goals_objectives": "Lead a new project",
    "reviewer_id": 18856,
    "reviewer_name": "Priya Desai"
  }
```

### Retrieving Employee Reviews

Step 1: Expand GET in the doc. You can see the docstring explaining the endpoint and its fields:

![Get section in the doc with descriptions](fadb8_getstart.png)

Step 2: Click **Try it out**.

Step 3: Click **Execute**.

The API will process the request and retrieve all the employee reviews from the database. The response section displays the retrieved records:

![200 response with records of the 3 employees](fadb9.png)

### Updating an Employee Review

Step 1: Expand PUT in the doc. You can see the docstring explaining the endpoint and its fields.

Step 2: Click **Try it out**.

Step 3: Enter the employee ID, for example, `12932`, which we used earlier with the POST endpoint.

Step 4: Enter the request body. For example, change `“evaluation_period": "Q4 2024"` to `"evaluation_period": "Q3 2024"` while keeping the other text unchanged:

![JSON request body with the changed value for evaluation_period](fadb10put.png)

Step 5: Click **Execute** to send the updated data to the API.

If successful, the updated employee review will be displayed with a response code **200:**

![200 response with updated record of the employee](fadb11.png)

### Deleting an Employee Review

Step 1: Expand DELETE.

Step 2: Click **Try it out**.

Step 3: Enter employee ID for the record you want to delete. For example, enter `12932`:

![Employee ID entered in delete section of doc](fadb12.png)

Step 4: Click **Execute**.

You will see a response indicating that the employee review has been deleted:

![Response body showing employee review is deleted](fadb13.png)

Congratulations! You've learned how to build a basic REST API using FastAPI and PostgreSQL, covering GET, POST, PUT, and DELETE operations. You've seen how to describe the endpoints and their fields in the code to make the auto-generated API documentation clearer and more informative. Additionally, we've explored how to use the Swagger documentation interface to interact with the API effectively.