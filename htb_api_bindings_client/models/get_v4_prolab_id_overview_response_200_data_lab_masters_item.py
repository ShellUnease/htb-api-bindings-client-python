from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4ProlabIdOverviewResponse200DataLabMastersItem")


@_attrs_define
class GetV4ProlabIdOverviewResponse200DataLabMastersItem:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        avatar_thumb (str | Unset):
        account_id (str | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    avatar_thumb: str | Unset = UNSET
    account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        avatar_thumb = self.avatar_thumb

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if avatar_thumb is not UNSET:
            field_dict["avatar_thumb"] = avatar_thumb
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        avatar_thumb = d.pop("avatar_thumb", UNSET)

        account_id = d.pop("account_id", UNSET)

        get_v4_prolab_id_overview_response_200_data_lab_masters_item = cls(
            id=id,
            name=name,
            avatar_thumb=avatar_thumb,
            account_id=account_id,
        )

        get_v4_prolab_id_overview_response_200_data_lab_masters_item.additional_properties = d
        return get_v4_prolab_id_overview_response_200_data_lab_masters_item

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
