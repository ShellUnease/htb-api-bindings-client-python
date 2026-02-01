from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_profile_id_response_200_info_user_blood_user import (
        GetV4MachineProfileIdResponse200InfoUserBloodUser,
    )


T = TypeVar("T", bound="GetV4MachineProfileIdResponse200InfoUserBlood")


@_attrs_define
class GetV4MachineProfileIdResponse200InfoUserBlood:
    """
    Attributes:
        user (GetV4MachineProfileIdResponse200InfoUserBloodUser | Unset):
        blood_difference (str | Unset):
        created_at (str | Unset):
    """

    user: GetV4MachineProfileIdResponse200InfoUserBloodUser | Unset = UNSET
    blood_difference: str | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        blood_difference = self.blood_difference

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if blood_difference is not UNSET:
            field_dict["blood_difference"] = blood_difference
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_profile_id_response_200_info_user_blood_user import (
            GetV4MachineProfileIdResponse200InfoUserBloodUser,
        )

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: GetV4MachineProfileIdResponse200InfoUserBloodUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = GetV4MachineProfileIdResponse200InfoUserBloodUser.from_dict(_user)

        blood_difference = d.pop("blood_difference", UNSET)

        created_at = d.pop("created_at", UNSET)

        get_v4_machine_profile_id_response_200_info_user_blood = cls(
            user=user,
            blood_difference=blood_difference,
            created_at=created_at,
        )

        get_v4_machine_profile_id_response_200_info_user_blood.additional_properties = d
        return get_v4_machine_profile_id_response_200_info_user_blood

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
