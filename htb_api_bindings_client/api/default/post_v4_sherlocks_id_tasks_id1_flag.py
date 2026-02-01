from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_v4_sherlocks_id_tasks_id_1_flag_body import PostV4SherlocksIdTasksId1FlagBody
from ...models.post_v4_sherlocks_id_tasks_id_1_flag_response_400 import PostV4SherlocksIdTasksId1FlagResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    id1: str,
    *,
    body: PostV4SherlocksIdTasksId1FlagBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/sherlocks/{id}/tasks/{id1}/flag".format(
            id=quote(str(id), safe=""),
            id1=quote(str(id1), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostV4SherlocksIdTasksId1FlagResponse400 | None:
    if response.status_code == 400:
        response_400 = PostV4SherlocksIdTasksId1FlagResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostV4SherlocksIdTasksId1FlagResponse400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    id1: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostV4SherlocksIdTasksId1FlagBody | Unset = UNSET,
) -> Response[PostV4SherlocksIdTasksId1FlagResponse400]:
    """POST flag by id

    Args:
        id (str):
        id1 (str):
        body (PostV4SherlocksIdTasksId1FlagBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostV4SherlocksIdTasksId1FlagResponse400]
    """

    kwargs = _get_kwargs(
        id=id,
        id1=id1,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    id1: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostV4SherlocksIdTasksId1FlagBody | Unset = UNSET,
) -> PostV4SherlocksIdTasksId1FlagResponse400 | None:
    """POST flag by id

    Args:
        id (str):
        id1 (str):
        body (PostV4SherlocksIdTasksId1FlagBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostV4SherlocksIdTasksId1FlagResponse400
    """

    return sync_detailed(
        id=id,
        id1=id1,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    id1: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostV4SherlocksIdTasksId1FlagBody | Unset = UNSET,
) -> Response[PostV4SherlocksIdTasksId1FlagResponse400]:
    """POST flag by id

    Args:
        id (str):
        id1 (str):
        body (PostV4SherlocksIdTasksId1FlagBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostV4SherlocksIdTasksId1FlagResponse400]
    """

    kwargs = _get_kwargs(
        id=id,
        id1=id1,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    id1: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostV4SherlocksIdTasksId1FlagBody | Unset = UNSET,
) -> PostV4SherlocksIdTasksId1FlagResponse400 | None:
    """POST flag by id

    Args:
        id (str):
        id1 (str):
        body (PostV4SherlocksIdTasksId1FlagBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostV4SherlocksIdTasksId1FlagResponse400
    """

    return (
        await asyncio_detailed(
            id=id,
            id1=id1,
            client=client,
            body=body,
        )
    ).parsed
