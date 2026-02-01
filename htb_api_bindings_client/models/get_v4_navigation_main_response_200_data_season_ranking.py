from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_navigation_main_response_200_data_season_ranking_latest_season import (
        GetV4NavigationMainResponse200DataSeasonRankingLatestSeason,
    )
    from ..models.get_v4_navigation_main_response_200_data_season_ranking_league_type_0 import (
        GetV4NavigationMainResponse200DataSeasonRankingLeagueType0,
    )
    from ..models.get_v4_navigation_main_response_200_data_season_ranking_rank_type_0 import (
        GetV4NavigationMainResponse200DataSeasonRankingRankType0,
    )
    from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season import (
        GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeason,
    )


T = TypeVar("T", bound="GetV4NavigationMainResponse200DataSeasonRanking")


@_attrs_define
class GetV4NavigationMainResponse200DataSeasonRanking:
    """
    Attributes:
        league (GetV4NavigationMainResponse200DataSeasonRankingLeagueType0 | None | Unset):
        rank (GetV4NavigationMainResponse200DataSeasonRankingRankType0 | None | Unset):
        rank_suffix (str | Unset):
        latest_season (GetV4NavigationMainResponse200DataSeasonRankingLatestSeason | Unset):
        upcoming_season (GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeason | Unset):
    """

    league: GetV4NavigationMainResponse200DataSeasonRankingLeagueType0 | None | Unset = UNSET
    rank: GetV4NavigationMainResponse200DataSeasonRankingRankType0 | None | Unset = UNSET
    rank_suffix: str | Unset = UNSET
    latest_season: GetV4NavigationMainResponse200DataSeasonRankingLatestSeason | Unset = UNSET
    upcoming_season: GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_league_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingLeagueType0,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_rank_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingRankType0,
        )

        league: dict[str, Any] | None | Unset
        if isinstance(self.league, Unset):
            league = UNSET
        elif isinstance(self.league, GetV4NavigationMainResponse200DataSeasonRankingLeagueType0):
            league = self.league.to_dict()
        else:
            league = self.league

        rank: dict[str, Any] | None | Unset
        if isinstance(self.rank, Unset):
            rank = UNSET
        elif isinstance(self.rank, GetV4NavigationMainResponse200DataSeasonRankingRankType0):
            rank = self.rank.to_dict()
        else:
            rank = self.rank

        rank_suffix = self.rank_suffix

        latest_season: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_season, Unset):
            latest_season = self.latest_season.to_dict()

        upcoming_season: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upcoming_season, Unset):
            upcoming_season = self.upcoming_season.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if league is not UNSET:
            field_dict["league"] = league
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_suffix is not UNSET:
            field_dict["rank_suffix"] = rank_suffix
        if latest_season is not UNSET:
            field_dict["latest_season"] = latest_season
        if upcoming_season is not UNSET:
            field_dict["upcoming_season"] = upcoming_season

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_latest_season import (
            GetV4NavigationMainResponse200DataSeasonRankingLatestSeason,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_league_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingLeagueType0,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_rank_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingRankType0,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season import (
            GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeason,
        )

        d = dict(src_dict)

        def _parse_league(data: object) -> GetV4NavigationMainResponse200DataSeasonRankingLeagueType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                league_type_0 = GetV4NavigationMainResponse200DataSeasonRankingLeagueType0.from_dict(data)

                return league_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4NavigationMainResponse200DataSeasonRankingLeagueType0 | None | Unset, data)

        league = _parse_league(d.pop("league", UNSET))

        def _parse_rank(data: object) -> GetV4NavigationMainResponse200DataSeasonRankingRankType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rank_type_0 = GetV4NavigationMainResponse200DataSeasonRankingRankType0.from_dict(data)

                return rank_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4NavigationMainResponse200DataSeasonRankingRankType0 | None | Unset, data)

        rank = _parse_rank(d.pop("rank", UNSET))

        rank_suffix = d.pop("rank_suffix", UNSET)

        _latest_season = d.pop("latest_season", UNSET)
        latest_season: GetV4NavigationMainResponse200DataSeasonRankingLatestSeason | Unset
        if isinstance(_latest_season, Unset):
            latest_season = UNSET
        else:
            latest_season = GetV4NavigationMainResponse200DataSeasonRankingLatestSeason.from_dict(_latest_season)

        _upcoming_season = d.pop("upcoming_season", UNSET)
        upcoming_season: GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeason | Unset
        if isinstance(_upcoming_season, Unset):
            upcoming_season = UNSET
        else:
            upcoming_season = GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeason.from_dict(_upcoming_season)

        get_v4_navigation_main_response_200_data_season_ranking = cls(
            league=league,
            rank=rank,
            rank_suffix=rank_suffix,
            latest_season=latest_season,
            upcoming_season=upcoming_season,
        )

        get_v4_navigation_main_response_200_data_season_ranking.additional_properties = d
        return get_v4_navigation_main_response_200_data_season_ranking

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
