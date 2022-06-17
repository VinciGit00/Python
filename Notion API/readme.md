# Notion Api

## General info

This is a python script for making POST and GET to Notion database.

The reference for the script is here: [https://www.youtube.com/watch?v=sdn1HgxLwEg](https://www.youtube.com/watch?v=sdn1HgxLwEg)

## Requirements

The library required is requests. To install the library on your venv use the following command:

```
//With pip
pip install requests

//Alternatively you can install using conda
conda install requests
```

To import the library on python use the following command:

```python
import requests
```

## Credentials of the database

- The ID of the Notion database is: 58e434b9417e4416b138f11eae5071cb
- The secret code for the API instead is: is:secret_5w19b4cVlMo4Djag6wslfgWVjgy0HQulpyx9qiMjaJZ

The header for the GET JSON file is the following:

```json
"Authorization": "Bearer secret_5w19b4cVlMo4Djag6wslfgWVjgy0HQulpyx9qiMjaJZ",
"Notion-Version": "2022-02-22"
```

The header for the POST JSON file is the following:

```json
"Authorization": "Bearer secret_5w19b4cVlMo4Djag6wslfgWVjgy0HQulpyx9qiMjaJZ",
"Content-Type": "application/json",
"Notion-Version": "2022-02-22"
```

The body of the JSON file for the post is the following:

```json
"parent": {"database_id": databaseId},
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": "Marco"
                        }
                    }
                ]
            },
            "Value": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Franco"
                        }
                    }
                ]
            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Giuseppe"
                        }
                    }
                ]
            }
        },
```

## Final considerations

It’s very difficult to change the single line because each line has an unique ID
