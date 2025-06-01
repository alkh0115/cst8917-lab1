# cst8917-lab1
## Part1: Azure Function with Output Binding (Queue)
### Lab Overview

This lab demonstrates the creation of a Python-based Azure Function App using an HTTP trigger with an output binding to **Azure Storage Queue**. The function accepts a user's name as input and pushes the data as a JSON message to a queue.

### Setup Instructions
#### Prerequisites

- Azure Subscription
- Python 3.10 or 3.12
- Azure Functions Core Tools
- Visual Studio Code with:
  - Azure Functions extension
  - Azure Account extension
  - Python extension
- Azure Storage Explorer (for verification)

#### Resources Created

- **Resource Group**: `rg-cst8917-lab1`
- **Storage Account**: `storagelab1rahaf`
- **Storage Queue**: `myqueue-items`
- **Function App Plan**: Flex Consumption (Linux)
- **Function App**: `lab1storagequeue-rahaf`

### Running the Function Locally

1. Clone this repository and open the project in VS Code.
2. Activate your Python virtual environment:
   ```bash
   .venv\Scripts\Activate
   ```
3. Start the function:
  ```bash
  func start
  ```
4. Test it:
  ```bash
  Invoke-WebRequest -Uri "http://localhost:7071/api/QueueOutputFunction?name=Rahaf" -Method POST
  ```
### Deployment to Azure
1. Right-click the project folder → Deploy to Function App

2. Choose: lab1storagequeue-rahaf

3. VS Code will upload and configure the function automatically.

### Live Function URL
  ```bash
  https://lab1storagequeue-rahaf.azurewebsites.net/api/QueueOutputFunction
  ```
Test:
  ```bash
  https://lab1storagequeue-rahaf.azurewebsites.net/api/QueueOutputFunction?name=Rahaf
  ```
-----
## Part2: Azure Function with SQL Output Binding

This part contains an Azure Function that demonstrates writing data to an Azure SQL Database using an output binding.

### Function Overview

- **Trigger:** HTTP POST request
- **Output Binding:** Azure SQL Database
- **Target Table:** `dbo.ToDoItems`

### How It Works

The function expects a JSON body like:

```json
{
  "title": "Submit lab",
  "isComplete": false
}
```

When called, it inserts a new row into the Azure SQL `ToDoItems` table.

### Local Testing

#### 1. Start the function

```bash
func start
```

#### 2. Use curl to invoke the function:

```bash
curl -X POST http://localhost:7071/api/SqlOutputFunction -H "Content-Type: application/json" -d "{"title":"Submit lab","isComplete":false}"
```

#### 3. Verify data in Azure SQL

Use the Query Editor in the Azure Portal:

```sql
SELECT * FROM dbo.ToDoItems;
```

### Required Configuration

In `local.settings.json` (excluded from repo), add:

```json
"Values": {
  "SqlConnectionString": "<your-connection-string>"
}
```

### Notes

- The extension bundle version in `host.json` is set to:
  ```json
  "version": "[4.*, 5.0.0)"
  ```
- The SQL binding extension is included in this version.

-----
## Video Demo:
Please visit the link:
**[https://youtu.be/MLQCwxjfmk4](https://youtu.be/MLQCwxjfmk4)**



