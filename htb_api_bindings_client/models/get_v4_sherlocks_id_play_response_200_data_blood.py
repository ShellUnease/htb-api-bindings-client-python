from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_sherlocks_id_play_response_200_data_blood_blood_user_avatar_type_0 import (
        GetV4SherlocksIdPlayResponse200DataBloodBloodUserAvatarType0,
    )


T = TypeVar("T", bound="GetV4SherlocksIdPlayResponse200DataBlood")


@_attrs_define
class GetV4SherlocksIdPlayResponse200DataBlood:
    """
    Attributes:
        blood_user_id (float | Unset):
        blood_user (str | Unset):
        blood_user_avatar (GetV4SherlocksIdPlayResponse200DataBloodBloodUserAvatarType0 | None | Unset):
        blood_time (str | Unset):
    """

    blood_user_id: float | Unset = UNSET
    blood_user: str | Unset = UNSET
    blood_user_avatar: GetV4SherlocksIdPlayResponse200DataBloodBloodUserAvatarType0 | None | Unset = UNSET
    blood_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_sherlocks_id_play_response_200_data_blood_blood_user_avatar_type_0 import (
            GetV4SherlocksIdPlayResponse200DataBloodBloodUserAvatarType0,
        )

        blood_user_id = self.blood_user_id

        blood_user = self.blood_user

        blood_user_avatar: dict[str, Any] | None | Unset
        if isinstance(self.blood_user_avatar, Unset):
            blood_user_avatar = UNSET
        elif isinstance(self.blood_user_avatar, GetV4SherlocksIdPlayResponse200DataBloodBloodUserAvatarType0):
            blood_user_avatar = self.blood_user_avatar.to_dict()
        else:
            blood_user_avatar = self.blood_user_avatar

        blood_time = self.blood_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blood_user_id is not UNSET:
            field_dict["blood_user_id"] = blood_user_id
        if blood_user is not UNSET:
            field_dict["blood_user"] = blood_user
        if blood_user_avatar is not UNSET:
            field_dict["blood_user_avatar"] = blood_user_avatar
        if blood_time is not UNSET:
            field_dict["blood_time"] = blood_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_sherlocks_id_play_response_200_data_blood_blood_user_avatar_type_0 import (
            GetV4SherlocksIdPlayResponse200DataBloodBloodUserAvatarType0,
        )

        d = dict(src_dict)
        blood_user_id = d.pop("blood_user_id", UNSET)

        blood_user = d.pop("blood_user", UNSET)

        def _parse_blood_user_avatar(
            data: object,
        ) -> GetV4SherlocksIdPlayResponse200DataBloodBloodUserAvatarType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                blood_user_avatar_type_0 = GetV4SherlocksIdPlayResponse200DataBloodBloodUserAvatarType0.from_dict(data)

                return blood_user_avatar_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SherlocksIdPlayResponse200DataBloodBloodUserAvatarType0 | None | Unset, data)

        blood_user_avatar = _parse_blood_user_avatar(d.pop("blood_user_avatar", UNSET))

        blood_time = d.pop("blood_time", UNSET)

        get_v4_sherlocks_id_play_response_200_data_blood = cls(
            blood_user_id=blood_user_id,
            blood_user=blood_user,
            blood_user_avatar=blood_user_avatar,
            blood_time=blood_time,
        )

        get_v4_sherlocks_id_play_response_200_data_blood.additional_properties = d
        return get_v4_sherlocks_id_play_response_200_data_blood

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
