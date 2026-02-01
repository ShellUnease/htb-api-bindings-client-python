from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV5MachinesResponse200DataItemFirstCreator")


@_attrs_define
class GetV5MachinesResponse200DataItemFirstCreator:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        avatar (str | Unset):
        is_respected (bool | Unset):
        profile_url (str | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    avatar: str | Unset = UNSET
    is_respected: bool | Unset = UNSET
    profile_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        avatar = self.avatar

        is_respected = self.is_respected

        profile_url = self.profile_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if is_respected is not UNSET:
            field_dict["isRespected"] = is_respected
        if profile_url is not UNSET:
            field_dict["profile_url"] = profile_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        avatar = d.pop("avatar", UNSET)

        is_respected = d.pop("isRespected", UNSET)

        profile_url = d.pop("profile_url", UNSET)

        get_v5_machines_response_200_data_item_first_creator = cls(
            id=id,
            name=name,
            avatar=avatar,
            is_respected=is_respected,
            profile_url=profile_url,
        )

        get_v5_machines_response_200_data_item_first_creator.additional_properties = d
        return get_v5_machines_response_200_data_item_first_creator

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
