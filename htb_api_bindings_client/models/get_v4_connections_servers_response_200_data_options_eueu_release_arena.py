from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_connections_servers_response_200_data_options_eueu_release_arena_servers import (
        GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArenaServers,
    )


T = TypeVar("T", bound="GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArena")


@_attrs_define
class GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArena:
    """
    Attributes:
        location (str | Unset):
        name (str | Unset):
        servers (GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArenaServers | Unset):
    """

    location: str | Unset = UNSET
    name: str | Unset = UNSET
    servers: GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArenaServers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        name = self.name

        servers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_connections_servers_response_200_data_options_eueu_release_arena_servers import (
            GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArenaServers,
        )

        d = dict(src_dict)
        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        _servers = d.pop("servers", UNSET)
        servers: GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArenaServers | Unset
        if isinstance(_servers, Unset):
            servers = UNSET
        else:
            servers = GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArenaServers.from_dict(_servers)

        get_v4_connections_servers_response_200_data_options_eueu_release_arena = cls(
            location=location,
            name=name,
            servers=servers,
        )

        get_v4_connections_servers_response_200_data_options_eueu_release_arena.additional_properties = d
        return get_v4_connections_servers_response_200_data_options_eueu_release_arena

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
