from fastapi import FastAPI, Query

#Annotated can be used to add metadata to your parameters (metadata means giving mre details about the data like constraints , default values ...)

from typing import Annotated

app = FastAPI()


@app.get("/items/")
# THE q IS A QUERY PARAM OF TYPE Union[str, None]  or str | None that means that it's of type str but could also be None,
# and indeed, the default value is None, so FastAPI will know it's not required.
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#q: str | None = None
#q: Annotated[str | None] = None

#those 2 lines of codes means the same thing : q is a parameter that can be a str or None, and by default, it is None .
