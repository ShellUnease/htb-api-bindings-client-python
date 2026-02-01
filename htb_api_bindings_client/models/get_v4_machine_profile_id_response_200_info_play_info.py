from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_profile_id_response_200_info_play_info_expires_at_type_0 import (
        GetV4MachineProfileIdResponse200InfoPlayInfoExpiresAtType0,
    )


T = TypeVar("T", bound="GetV4MachineProfileIdResponse200InfoPlayInfo")


@_attrs_define
class GetV4MachineProfileIdResponse200InfoPlayInfo:
    """
    Attributes:
        is_spawned (bool | Unset):
        is_spawning (bool | Unset):
        is_active (bool | Unset):
        active_player_count (float | Unset):
        expires_at (GetV4MachineProfileIdResponse200InfoPlayInfoExpiresAtType0 | None | Unset):
    """

    is_spawned: bool | Unset = UNSET
    is_spawning: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    active_player_count: float | Unset = UNSET
    expires_at: GetV4MachineProfileIdResponse200InfoPlayInfoExpiresAtType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machine_profile_id_response_200_info_play_info_expires_at_type_0 import (
            GetV4MachineProfileIdResponse200InfoPlayInfoExpiresAtType0,
        )

        is_spawned = self.is_spawned

        is_spawning = self.is_spawning

        is_active = self.is_active

        active_player_count = self.active_player_count

        expires_at: dict[str, Any] | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, GetV4MachineProfileIdResponse200InfoPlayInfoExpiresAtType0):
            expires_at = self.expires_at.to_dict()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_spawned is not UNSET:
            field_dict["isSpawned"] = is_spawned
        if is_spawning is not UNSET:
            field_dict["isSpawning"] = is_spawning
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if active_player_count is not UNSET:
            field_dict["active_player_count"] = active_player_count
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_profile_id_response_200_info_play_info_expires_at_type_0 import (
            GetV4MachineProfileIdResponse200InfoPlayInfoExpiresAtType0,
        )

        d = dict(src_dict)
        is_spawned = d.pop("isSpawned", UNSET)

        is_spawning = d.pop("isSpawning", UNSET)

        is_active = d.pop("isActive", UNSET)

        active_player_count = d.pop("active_player_count", UNSET)

        def _parse_expires_at(
            data: object,
        ) -> GetV4MachineProfileIdResponse200InfoPlayInfoExpiresAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                expires_at_type_0 = GetV4MachineProfileIdResponse200InfoPlayInfoExpiresAtType0.from_dict(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoPlayInfoExpiresAtType0 | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        get_v4_machine_profile_id_response_200_info_play_info = cls(
            is_spawned=is_spawned,
            is_spawning=is_spawning,
            is_active=is_active,
            active_player_count=active_player_count,
            expires_at=expires_at,
        )

        get_v4_machine_profile_id_response_200_info_play_info.additional_properties = d
        return get_v4_machine_profile_id_response_200_info_play_info

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
