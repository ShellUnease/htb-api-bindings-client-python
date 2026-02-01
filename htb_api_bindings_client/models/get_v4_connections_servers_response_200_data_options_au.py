from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_connections_servers_response_200_data_options_auau_release_arena import (
        GetV4ConnectionsServersResponse200DataOptionsAUAUReleaseArena,
    )


T = TypeVar("T", bound="GetV4ConnectionsServersResponse200DataOptionsAU")


@_attrs_define
class GetV4ConnectionsServersResponse200DataOptionsAU:
    """
    Attributes:
        au_release_arena (GetV4ConnectionsServersResponse200DataOptionsAUAUReleaseArena | Unset):
    """

    au_release_arena: GetV4ConnectionsServersResponse200DataOptionsAUAUReleaseArena | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        au_release_arena: dict[str, Any] | Unset = UNSET
        if not isinstance(self.au_release_arena, Unset):
            au_release_arena = self.au_release_arena.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if au_release_arena is not UNSET:
            field_dict["AU - Release Arena"] = au_release_arena

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_connections_servers_response_200_data_options_auau_release_arena import (
            GetV4ConnectionsServersResponse200DataOptionsAUAUReleaseArena,
        )

        d = dict(src_dict)
        _au_release_arena = d.pop("AU - Release Arena", UNSET)
        au_release_arena: GetV4ConnectionsServersResponse200DataOptionsAUAUReleaseArena | Unset
        if isinstance(_au_release_arena, Unset):
            au_release_arena = UNSET
        else:
            au_release_arena = GetV4ConnectionsServersResponse200DataOptionsAUAUReleaseArena.from_dict(
                _au_release_arena
            )

        get_v4_connections_servers_response_200_data_options_au = cls(
            au_release_arena=au_release_arena,
        )

        get_v4_connections_servers_response_200_data_options_au.additional_properties = d
        return get_v4_connections_servers_response_200_data_options_au

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
