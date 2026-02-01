from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_navigation_main_response_200_data_ranking import GetV4NavigationMainResponse200DataRanking
    from ..models.get_v4_navigation_main_response_200_data_season_ranking import (
        GetV4NavigationMainResponse200DataSeasonRanking,
    )


T = TypeVar("T", bound="GetV4NavigationMainResponse200Data")


@_attrs_define
class GetV4NavigationMainResponse200Data:
    """
    Attributes:
        sso_linked (bool | Unset):
        ranking (GetV4NavigationMainResponse200DataRanking | Unset):
        season_ranking (GetV4NavigationMainResponse200DataSeasonRanking | Unset):
    """

    sso_linked: bool | Unset = UNSET
    ranking: GetV4NavigationMainResponse200DataRanking | Unset = UNSET
    season_ranking: GetV4NavigationMainResponse200DataSeasonRanking | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sso_linked = self.sso_linked

        ranking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ranking, Unset):
            ranking = self.ranking.to_dict()

        season_ranking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.season_ranking, Unset):
            season_ranking = self.season_ranking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sso_linked is not UNSET:
            field_dict["sso_linked"] = sso_linked
        if ranking is not UNSET:
            field_dict["ranking"] = ranking
        if season_ranking is not UNSET:
            field_dict["season_ranking"] = season_ranking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_navigation_main_response_200_data_ranking import GetV4NavigationMainResponse200DataRanking
        from ..models.get_v4_navigation_main_response_200_data_season_ranking import (
            GetV4NavigationMainResponse200DataSeasonRanking,
        )

        d = dict(src_dict)
        sso_linked = d.pop("sso_linked", UNSET)

        _ranking = d.pop("ranking", UNSET)
        ranking: GetV4NavigationMainResponse200DataRanking | Unset
        if isinstance(_ranking, Unset):
            ranking = UNSET
        else:
            ranking = GetV4NavigationMainResponse200DataRanking.from_dict(_ranking)

        _season_ranking = d.pop("season_ranking", UNSET)
        season_ranking: GetV4NavigationMainResponse200DataSeasonRanking | Unset
        if isinstance(_season_ranking, Unset):
            season_ranking = UNSET
        else:
            season_ranking = GetV4NavigationMainResponse200DataSeasonRanking.from_dict(_season_ranking)

        get_v4_navigation_main_response_200_data = cls(
            sso_linked=sso_linked,
            ranking=ranking,
            season_ranking=season_ranking,
        )

        get_v4_navigation_main_response_200_data.additional_properties = d
        return get_v4_navigation_main_response_200_data

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
