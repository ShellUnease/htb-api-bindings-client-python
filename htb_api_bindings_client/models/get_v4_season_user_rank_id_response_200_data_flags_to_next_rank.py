from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4SeasonUserRankIdResponse200DataFlagsToNextRank")


@_attrs_define
class GetV4SeasonUserRankIdResponse200DataFlagsToNextRank:
    """
    Attributes:
        obtained (float | Unset):
        total (float | Unset):
    """

    obtained: float | Unset = UNSET
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        obtained = self.obtained

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obtained is not UNSET:
            field_dict["obtained"] = obtained
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        obtained = d.pop("obtained", UNSET)

        total = d.pop("total", UNSET)

        get_v4_season_user_rank_id_response_200_data_flags_to_next_rank = cls(
            obtained=obtained,
            total=total,
        )

        get_v4_season_user_rank_id_response_200_data_flags_to_next_rank.additional_properties = d
        return get_v4_season_user_rank_id_response_200_data_flags_to_next_rank

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
