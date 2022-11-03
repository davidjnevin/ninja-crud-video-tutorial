""" Services for api endpoints."""


class Api_Services:
    """Api_Services."""

    def test(request) -> dict[str, str]:
        """test.

        :param request:
        :rtype: dict[str, str]
        """
        return {"message": "success!"}
