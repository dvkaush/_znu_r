#### 1 train & save model
location: "saved_model/my_model"

```shell
$ python v2/model.py
```

#### 2 api

```shell
$ cd v2
$ set FLASK_APP=api.py
$ python -m flask run
```

##### localhost:5000/predict
##### sample json

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