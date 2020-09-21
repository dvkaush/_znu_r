#### 1 train & save model
location: "saved_model/my_model"

```shell
$ python v2/model.py
```

#### 2 api

```shell
$ set FLASK_APP=api.py
$ python -m flask run
```

sample json

```json
[
    {
        "age": 25,
        "gender": "Male",
        "emotion": "Happy",
        "color": "Blue",
        "animal": "Horse",
        "q3": "N1",
        "q4": "M1"
    }
]

```