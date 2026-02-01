from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV5MachinesResponse200DataItemRetiring")


@_attrs_define
class GetV5MachinesResponse200DataItemRetiring:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        avatar (str | Unset):
        os (str | Unset):
        difficulty_text (str | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    avatar: str | Unset = UNSET
    os: str | Unset = UNSET
    difficulty_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        avatar = self.avatar

        os = self.os

        difficulty_text = self.difficulty_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if os is not UNSET:
            field_dict["os"] = os
        if difficulty_text is not UNSET:
            field_dict["difficultyText"] = difficulty_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        avatar = d.pop("avatar", UNSET)

        os = d.pop("os", UNSET)

        difficulty_text = d.pop("difficultyText", UNSET)

        get_v5_machines_response_200_data_item_retiring = cls(
            id=id,
            name=name,
            avatar=avatar,
            os=os,
            difficulty_text=difficulty_text,
        )

        get_v5_machines_response_200_data_item_retiring.additional_properties = d
        return get_v5_machines_response_200_data_item_retiring

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
