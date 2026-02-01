from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_connections_servers_response_200_data_options_usus_release_arena import (
        GetV4ConnectionsServersResponse200DataOptionsUSUSReleaseArena,
    )


T = TypeVar("T", bound="GetV4ConnectionsServersResponse200DataOptionsUS")


@_attrs_define
class GetV4ConnectionsServersResponse200DataOptionsUS:
    """
    Attributes:
        us_release_arena (GetV4ConnectionsServersResponse200DataOptionsUSUSReleaseArena | Unset):
    """

    us_release_arena: GetV4ConnectionsServersResponse200DataOptionsUSUSReleaseArena | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        us_release_arena: dict[str, Any] | Unset = UNSET
        if not isinstance(self.us_release_arena, Unset):
            us_release_arena = self.us_release_arena.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if us_release_arena is not UNSET:
            field_dict["US - Release Arena"] = us_release_arena

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_connections_servers_response_200_data_options_usus_release_arena import (
            GetV4ConnectionsServersResponse200DataOptionsUSUSReleaseArena,
        )

        d = dict(src_dict)
        _us_release_arena = d.pop("US - Release Arena", UNSET)
        us_release_arena: GetV4ConnectionsServersResponse200DataOptionsUSUSReleaseArena | Unset
        if isinstance(_us_release_arena, Unset):
            us_release_arena = UNSET
        else:
            us_release_arena = GetV4ConnectionsServersResponse200DataOptionsUSUSReleaseArena.from_dict(
                _us_release_arena
            )

        get_v4_connections_servers_response_200_data_options_us = cls(
            us_release_arena=us_release_arena,
        )

        get_v4_connections_servers_response_200_data_options_us.additional_properties = d
        return get_v4_connections_servers_response_200_data_options_us

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
