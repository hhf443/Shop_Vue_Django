def get_auth_url():
    weibo_auth_url = 'https://api.weibo.com/oauth2/authorize'
    redirect_url = 'http://127.0.0.1:8000/complete/weibo'
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={re_url}".format(client_id=3393076475,
                                                                                      re_url=redirect_url)
    print(auth_url)


def get_access_token(code="xxx"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url, data={
        "client_id": 3393076475,
        "client_secret": "b5950a8c53624caa39348404c1d11f13",
        "grand_type": "authorization_code",
        "code": code,
        "redirect_uri": 'http://127.0.0.1:8000/complete/weibo'
    })
    pass


if __name__ == '__main__':
    get_auth_url()
    get_access_token("xxx")
