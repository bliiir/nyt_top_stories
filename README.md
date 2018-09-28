# New York Times Top Stories Web server / API

Release: 0.1


*Simple [WISGI](https://wsgi.readthedocs.io/en/latest/index.html) based web-server that allows the user to read and write New York Times Top stories to a MySQL database using HTTP requests*


## Files

Deploy the inventory files below to your server:

| **Filename** | **Description** |
| :-- | :-- |
| **README.md** | This file |
| **environment.py** | The executable wisgi server |
| **ny_api.py** | The logic for the server |


## HTTP request and query method overview

| Method | Path | Description | Examlpes |
| :-- | :-- | :-- | :-- |
| `GET` | `~/load` | Read stories from the NYT api and store them in the MySQL database |  |
| `GET` | `~/stories` | Read stories from the database |  |



## load

| | |
| :-- | :-- |
| **Method** | `GET` |
| **Endpoint** | `/load` |
| **Query parameters** | None |
| **Description** | Read stories from the NYT api and store them in the MySQL database |
| **Example** | `localhost:8000/load` |


#### Sample response
```
{
{
"status": "OK",
"copyright": "Copyright (c) 2018 The New York Times Company. All Rights Reserved.",
"section": "home",
"last_updated": "2018-09-28T11:27:07-04:00",
"num_results": 46,
"results": [
    {
    "section": "U.S.",
    "subsection": "Politics",
    "title": "With a Key Vote Secured, Senators Will Advance Kavanaugh\u2019s Nomination",
    "abstract": "Shortly before the Senate Judiciary Committee was to decide to advance Judge Brett Kavanaugh to the Supreme Court, a key Republican senator announced his support.",
    "url": "https://www.nytimes.com/2018/09/28/us/politics/brett-kavanaugh-senate-judiciary.html",
    "byline": "By NICHOLAS FANDOS, SHERYL GAY STOLBERG and EILEEN SULLIVAN",
    "item_type": "Article",
    "updated_date": "2018-09-28T11:24:18-04:00",
    "created_date": "2018-09-28T09:09:22-04:00",
    "published_date": "2018-09-28T09:09:22-04:00",
    "material_type_facet": "",
    "kicker": "",
    "des_facet": [
        "United States Politics and Government",
        "Appointments and Executive Changes",
        "#MeToo Movement"
    ],
    "org_facet": [
        "Supreme Court (US)",
        "Senate Committee on the Judiciary"
    ],
    "per_facet": [
        "Kavanaugh, Brett M"
    ],
    "geo_facet": [],
    "multimedia": [],
    "short_url": "https://nyti.ms/2Ip07B4"
...
}
```

## stories

| | |
| :-- | :-- |
| **Method** | `GET` |
| **Endpoint** | `/stories` |
| **Query parameters** | None |
| **Description** | Read stories from the database |
| **Example** | `localhost:8000/stories` |


#### Sample response
```
[
    [
        1,
            "Brett Kavanaugh and Christine Blasey Ford Duel With Tears and Fury",
            "At an extraordinary hearing that gripped the country, Dr. Blasey emotionally detailed the night she said Judge Brett M. Kavanaugh sexually assaulted her.",
            "2018-09-27T14:08:17-04:00",
            "https://nyti.ms/2NOOYzD",
            "https://static01.nyt.com/images/2018/09/28/us/politics/28dc-assess/merlin_144419289_98f68a47-4d75-47eb-8fa0-2fea026530b5-superJumbo.jpg"
    ],
    [
        2,
            "4 Key Takeaways From the Blasey and Kavanaugh Hearing",
            "In a stunning hearing on Thursday, Christine Blasey Ford told her story in raw and gripping testimony as Judge Brett M. Kavanaugh fought to clear his name and salvage his confirmation.",
            "2018-09-27T22:02:35-04:00",
            "https://nyti.ms/2Iq06Nm",
            "https://static01.nyt.com/images/2018/09/28/us/28dc-takeaways-promo/28dc-takeaways-promo-superJumbo.jpg"
```



## Features

#### This release
- [x] Connect to NYT API
- [x] Retreive top stories
- [x] Store top stories in MySQL DB

#### Next release

- [ ] ...


### Contribute

- Issue Tracker: https://github.com/bliiir/nyt_top_stories/issues
- Source Code: https://github.com/bliiir/nyt_top_stories


### Support


If you are having issues, please let me know. My email address is: r@bit.io


### License

The project is licensed under the BSD license.
