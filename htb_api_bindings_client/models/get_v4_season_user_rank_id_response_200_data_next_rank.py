from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4SeasonUserRankIdResponse200DataNextRank")


@_attrs_define
class GetV4SeasonUserRankIdResponse200DataNextRank:
    """
    Attributes:
        id (float | Unset):
        title (str | Unset):
        requirement (float | Unset):
    """

    id: float | Unset = UNSET
    title: str | Unset = UNSET
    requirement: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        requirement = self.requirement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if requirement is not UNSET:
            field_dict["requirement"] = requirement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        requirement = d.pop("requirement", UNSET)

        get_v4_season_user_rank_id_response_200_data_next_rank = cls(
            id=id,
            title=title,
            requirement=requirement,
        )

        get_v4_season_user_rank_id_response_200_data_next_rank.additional_properties = d
        return get_v4_season_user_rank_id_response_200_data_next_rank

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
