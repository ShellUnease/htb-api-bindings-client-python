from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4NavigationMainResponse200DataRanking")


@_attrs_define
class GetV4NavigationMainResponse200DataRanking:
    """
    Attributes:
        name (str | Unset):
        id (float | Unset):
        current_xp (float | Unset):
        next_rank_xp (float | Unset):
    """

    name: str | Unset = UNSET
    id: float | Unset = UNSET
    current_xp: float | Unset = UNSET
    next_rank_xp: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        current_xp = self.current_xp

        next_rank_xp = self.next_rank_xp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if current_xp is not UNSET:
            field_dict["current_xp"] = current_xp
        if next_rank_xp is not UNSET:
            field_dict["next_rank_xp"] = next_rank_xp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        current_xp = d.pop("current_xp", UNSET)

        next_rank_xp = d.pop("next_rank_xp", UNSET)

        get_v4_navigation_main_response_200_data_ranking = cls(
            name=name,
            id=id,
            current_xp=current_xp,
            next_rank_xp=next_rank_xp,
        )

        get_v4_navigation_main_response_200_data_ranking.additional_properties = d
        return get_v4_navigation_main_response_200_data_ranking

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
