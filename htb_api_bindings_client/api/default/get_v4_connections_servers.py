from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v4_connections_servers_response_200 import GetV4ConnectionsServersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    product: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["product"] = product

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/connections/servers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetV4ConnectionsServersResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV4ConnectionsServersResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetV4ConnectionsServersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: str | Unset = UNSET,
) -> Response[GetV4ConnectionsServersResponse200]:
    """GET servers

    Args:
        product (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV4ConnectionsServersResponse200]
    """

    kwargs = _get_kwargs(
        product=product,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product: str | Unset = UNSET,
) -> GetV4ConnectionsServersResponse200 | None:
    """GET servers

    Args:
        product (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV4ConnectionsServersResponse200
    """

    return sync_detailed(
        client=client,
        product=product,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: str | Unset = UNSET,
) -> Response[GetV4ConnectionsServersResponse200]:
    """GET servers

    Args:
        product (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV4ConnectionsServersResponse200]
    """

    kwargs = _get_kwargs(
        product=product,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product: str | Unset = UNSET,
) -> GetV4ConnectionsServersResponse200 | None:
    """GET servers

    Args:
        product (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV4ConnectionsServersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            product=product,
        )
    ).parsed
