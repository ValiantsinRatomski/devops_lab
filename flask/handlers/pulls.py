import requests


def get_request(parameters):
    return requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls",
                        params=parameters)


def update_params(val):
    parameters = {"per_page": "100"}
    parameters.update(val)
    return parameters


def get_list(jsFile, state):
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
    if state == "open":
        up_params = update_params({"state": state})
        response = get_request(up_params)
        jsFile = response.json()
        result = get_list(jsFile, state)
        return result
    elif state == "closed":
        up_params = update_params({"state": state})
        response = get_request(up_params)
        jsFile = response.json()
        result = get_list(jsFile, state)
        return result
    elif state == "accepted":
        up_params = update_params({"state": "all"})
        response = get_request(up_params)
        jsFile = response.json()
        result = get_list(jsFile, state)
        return result
    elif state == "needs%20work":
        up_params = update_params({"state": "all"})
        response = get_request(up_params)
        jsFile = response.json()
        result = get_list(jsFile, state)
        return result
    else:
        up_params = update_params({"state": "all"})
        response = get_request(up_params)
        jsFile = response.json()
        result = get_list(jsFile, state)
        return result


if __name__ == '__main__':
    get_pulls(state)
