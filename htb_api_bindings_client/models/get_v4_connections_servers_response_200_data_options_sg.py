from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_connections_servers_response_200_data_options_sgsg_release_arena import (
        GetV4ConnectionsServersResponse200DataOptionsSGSGReleaseArena,
    )


T = TypeVar("T", bound="GetV4ConnectionsServersResponse200DataOptionsSG")


@_attrs_define
class GetV4ConnectionsServersResponse200DataOptionsSG:
    """
    Attributes:
        sg_release_arena (GetV4ConnectionsServersResponse200DataOptionsSGSGReleaseArena | Unset):
    """

    sg_release_arena: GetV4ConnectionsServersResponse200DataOptionsSGSGReleaseArena | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sg_release_arena: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sg_release_arena, Unset):
            sg_release_arena = self.sg_release_arena.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sg_release_arena is not UNSET:
            field_dict["SG - Release Arena"] = sg_release_arena

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_connections_servers_response_200_data_options_sgsg_release_arena import (
            GetV4ConnectionsServersResponse200DataOptionsSGSGReleaseArena,
        )

        d = dict(src_dict)
        _sg_release_arena = d.pop("SG - Release Arena", UNSET)
        sg_release_arena: GetV4ConnectionsServersResponse200DataOptionsSGSGReleaseArena | Unset
        if isinstance(_sg_release_arena, Unset):
            sg_release_arena = UNSET
        else:
            sg_release_arena = GetV4ConnectionsServersResponse200DataOptionsSGSGReleaseArena.from_dict(
                _sg_release_arena
            )

        get_v4_connections_servers_response_200_data_options_sg = cls(
            sg_release_arena=sg_release_arena,
        )

        get_v4_connections_servers_response_200_data_options_sg.additional_properties = d
        return get_v4_connections_servers_response_200_data_options_sg

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
