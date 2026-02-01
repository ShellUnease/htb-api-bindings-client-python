from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_connections_servers_response_200_data_options_eueu_release_arena import (
        GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArena,
    )


T = TypeVar("T", bound="GetV4ConnectionsServersResponse200DataOptionsEU")


@_attrs_define
class GetV4ConnectionsServersResponse200DataOptionsEU:
    """
    Attributes:
        eu_release_arena (GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArena | Unset):
    """

    eu_release_arena: GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArena | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eu_release_arena: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eu_release_arena, Unset):
            eu_release_arena = self.eu_release_arena.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eu_release_arena is not UNSET:
            field_dict["EU - Release Arena"] = eu_release_arena

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_connections_servers_response_200_data_options_eueu_release_arena import (
            GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArena,
        )

        d = dict(src_dict)
        _eu_release_arena = d.pop("EU - Release Arena", UNSET)
        eu_release_arena: GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArena | Unset
        if isinstance(_eu_release_arena, Unset):
            eu_release_arena = UNSET
        else:
            eu_release_arena = GetV4ConnectionsServersResponse200DataOptionsEUEUReleaseArena.from_dict(
                _eu_release_arena
            )

        get_v4_connections_servers_response_200_data_options_eu = cls(
            eu_release_arena=eu_release_arena,
        )

        get_v4_connections_servers_response_200_data_options_eu.additional_properties = d
        return get_v4_connections_servers_response_200_data_options_eu

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
