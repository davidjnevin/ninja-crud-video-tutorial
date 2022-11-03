""" Services for api endpoints."""


def test(request) -> dict[str, str]:
    """test.

    :param request:
    :rtype: dict[str, str]
    """
    return {"message": "success!"}
