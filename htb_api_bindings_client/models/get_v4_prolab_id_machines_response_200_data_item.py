from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4ProlabIdMachinesResponse200DataItem")


@_attrs_define
class GetV4ProlabIdMachinesResponse200DataItem:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        os (str | Unset):
        avatar_thumb_url (str | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    os: str | Unset = UNSET
    avatar_thumb_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        os = self.os

        avatar_thumb_url = self.avatar_thumb_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if avatar_thumb_url is not UNSET:
            field_dict["avatar_thumb_url"] = avatar_thumb_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        avatar_thumb_url = d.pop("avatar_thumb_url", UNSET)

        get_v4_prolab_id_machines_response_200_data_item = cls(
            id=id,
            name=name,
            os=os,
            avatar_thumb_url=avatar_thumb_url,
        )

        get_v4_prolab_id_machines_response_200_data_item.additional_properties = d
        return get_v4_prolab_id_machines_response_200_data_item

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
