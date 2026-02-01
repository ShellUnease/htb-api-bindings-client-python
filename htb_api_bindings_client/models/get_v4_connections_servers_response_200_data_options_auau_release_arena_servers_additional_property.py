from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4ConnectionsServersResponse200DataOptionsAUAUReleaseArenaServersAdditionalProperty")


@_attrs_define
class GetV4ConnectionsServersResponse200DataOptionsAUAUReleaseArenaServersAdditionalProperty:
    """
    Attributes:
        id (float | Unset):
        friendly_name (str | Unset):
        full (bool | Unset):
        current_clients (float | Unset):
        location (str | Unset):
    """

    id: float | Unset = UNSET
    friendly_name: str | Unset = UNSET
    full: bool | Unset = UNSET
    current_clients: float | Unset = UNSET
    location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        friendly_name = self.friendly_name

        full = self.full

        current_clients = self.current_clients

        location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if full is not UNSET:
            field_dict["full"] = full
        if current_clients is not UNSET:
            field_dict["current_clients"] = current_clients
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        friendly_name = d.pop("friendly_name", UNSET)

        full = d.pop("full", UNSET)

        current_clients = d.pop("current_clients", UNSET)

        location = d.pop("location", UNSET)

        get_v4_connections_servers_response_200_data_options_auau_release_arena_servers_additional_property = cls(
            id=id,
            friendly_name=friendly_name,
            full=full,
            current_clients=current_clients,
            location=location,
        )

        get_v4_connections_servers_response_200_data_options_auau_release_arena_servers_additional_property.additional_properties = d
        return get_v4_connections_servers_response_200_data_options_auau_release_arena_servers_additional_property

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
