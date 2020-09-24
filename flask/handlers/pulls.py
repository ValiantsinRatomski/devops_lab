import requests


def getList(jsFile, state):
    res = list()
    if state == "open" or state == "closed" or state is None:
        for ob in jsFile:
            num = ob["number"]
            title = ob["title"]
            link = ob["url"]
            res.append({"num": num, "title": title, "link": link})
        return res
    elif state == "accepted" or state == "needs work":
        for ob in jsFile:
            if ob["labels"] and ob["labels"][0]["name"] == state:
                num = ob["number"]
                title = ob["title"]
                link = ob["url"]
                res.append({"num": num, "title": title, "link": link})
        return res


def get_pulls(state):
    parameters = {"per_page": "100"}
    if state == "open":
        parameters.update({"state": state})
        response = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls",
                                params=parameters)
        jsFile = response.json()
        return getList(jsFile, state)
    elif state == "closed":
        parameters.update({"state": state})
        response = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls",
                                params=parameters)
        jsFile = response.json()
        return getList(jsFile, state)
    elif state == "accepted":
        parameters.update({"state": "all"})
        response = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls",
                                params=parameters)
        jsFile = response.json()
        return getList(jsFile, state)
    elif state == "needs%20work":
        parameters.update({"state": "all"})
        response = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls",
                                params=parameters)
        jsFile = response.json()
        return getList(jsFile, state)
    else:
        parameters.update({"state": "all"})
        response = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls",
                                params=parameters)
        jsFile = response.json()
        return getList(jsFile, state)
