from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_season_user_rank_id_response_200_data_flags_to_next_rank import (
        GetV4SeasonUserRankIdResponse200DataFlagsToNextRank,
    )
    from ..models.get_v4_season_user_rank_id_response_200_data_league_type_0 import (
        GetV4SeasonUserRankIdResponse200DataLeagueType0,
    )
    from ..models.get_v4_season_user_rank_id_response_200_data_next_rank import (
        GetV4SeasonUserRankIdResponse200DataNextRank,
    )
    from ..models.get_v4_season_user_rank_id_response_200_data_rank_suffix_type_0 import (
        GetV4SeasonUserRankIdResponse200DataRankSuffixType0,
    )
    from ..models.get_v4_season_user_rank_id_response_200_data_rank_type_0 import (
        GetV4SeasonUserRankIdResponse200DataRankType0,
    )
    from ..models.get_v4_season_user_rank_id_response_200_data_total_ranks_type_0 import (
        GetV4SeasonUserRankIdResponse200DataTotalRanksType0,
    )
    from ..models.get_v4_season_user_rank_id_response_200_data_total_season_flags import (
        GetV4SeasonUserRankIdResponse200DataTotalSeasonFlags,
    )


T = TypeVar("T", bound="GetV4SeasonUserRankIdResponse200Data")


@_attrs_define
class GetV4SeasonUserRankIdResponse200Data:
    """
    Attributes:
        league (GetV4SeasonUserRankIdResponse200DataLeagueType0 | None | Unset):
        rank (GetV4SeasonUserRankIdResponse200DataRankType0 | None | Unset):
        next_rank (GetV4SeasonUserRankIdResponse200DataNextRank | Unset):
        total_ranks (GetV4SeasonUserRankIdResponse200DataTotalRanksType0 | None | Unset):
        rank_suffix (GetV4SeasonUserRankIdResponse200DataRankSuffixType0 | None | Unset):
        total_season_points (float | Unset):
        flags_to_next_rank (GetV4SeasonUserRankIdResponse200DataFlagsToNextRank | Unset):
        total_season_flags (GetV4SeasonUserRankIdResponse200DataTotalSeasonFlags | Unset):
    """

    league: GetV4SeasonUserRankIdResponse200DataLeagueType0 | None | Unset = UNSET
    rank: GetV4SeasonUserRankIdResponse200DataRankType0 | None | Unset = UNSET
    next_rank: GetV4SeasonUserRankIdResponse200DataNextRank | Unset = UNSET
    total_ranks: GetV4SeasonUserRankIdResponse200DataTotalRanksType0 | None | Unset = UNSET
    rank_suffix: GetV4SeasonUserRankIdResponse200DataRankSuffixType0 | None | Unset = UNSET
    total_season_points: float | Unset = UNSET
    flags_to_next_rank: GetV4SeasonUserRankIdResponse200DataFlagsToNextRank | Unset = UNSET
    total_season_flags: GetV4SeasonUserRankIdResponse200DataTotalSeasonFlags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_season_user_rank_id_response_200_data_league_type_0 import (
            GetV4SeasonUserRankIdResponse200DataLeagueType0,
        )
        from ..models.get_v4_season_user_rank_id_response_200_data_rank_suffix_type_0 import (
            GetV4SeasonUserRankIdResponse200DataRankSuffixType0,
        )
        from ..models.get_v4_season_user_rank_id_response_200_data_rank_type_0 import (
            GetV4SeasonUserRankIdResponse200DataRankType0,
        )
        from ..models.get_v4_season_user_rank_id_response_200_data_total_ranks_type_0 import (
            GetV4SeasonUserRankIdResponse200DataTotalRanksType0,
        )

        league: dict[str, Any] | None | Unset
        if isinstance(self.league, Unset):
            league = UNSET
        elif isinstance(self.league, GetV4SeasonUserRankIdResponse200DataLeagueType0):
            league = self.league.to_dict()
        else:
            league = self.league

        rank: dict[str, Any] | None | Unset
        if isinstance(self.rank, Unset):
            rank = UNSET
        elif isinstance(self.rank, GetV4SeasonUserRankIdResponse200DataRankType0):
            rank = self.rank.to_dict()
        else:
            rank = self.rank

        next_rank: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_rank, Unset):
            next_rank = self.next_rank.to_dict()

        total_ranks: dict[str, Any] | None | Unset
        if isinstance(self.total_ranks, Unset):
            total_ranks = UNSET
        elif isinstance(self.total_ranks, GetV4SeasonUserRankIdResponse200DataTotalRanksType0):
            total_ranks = self.total_ranks.to_dict()
        else:
            total_ranks = self.total_ranks

        rank_suffix: dict[str, Any] | None | Unset
        if isinstance(self.rank_suffix, Unset):
            rank_suffix = UNSET
        elif isinstance(self.rank_suffix, GetV4SeasonUserRankIdResponse200DataRankSuffixType0):
            rank_suffix = self.rank_suffix.to_dict()
        else:
            rank_suffix = self.rank_suffix

        total_season_points = self.total_season_points

        flags_to_next_rank: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flags_to_next_rank, Unset):
            flags_to_next_rank = self.flags_to_next_rank.to_dict()

        total_season_flags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_season_flags, Unset):
            total_season_flags = self.total_season_flags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if league is not UNSET:
            field_dict["league"] = league
        if rank is not UNSET:
            field_dict["rank"] = rank
        if next_rank is not UNSET:
            field_dict["next_rank"] = next_rank
        if total_ranks is not UNSET:
            field_dict["total_ranks"] = total_ranks
        if rank_suffix is not UNSET:
            field_dict["rank_suffix"] = rank_suffix
        if total_season_points is not UNSET:
            field_dict["total_season_points"] = total_season_points
        if flags_to_next_rank is not UNSET:
            field_dict["flags_to_next_rank"] = flags_to_next_rank
        if total_season_flags is not UNSET:
            field_dict["total_season_flags"] = total_season_flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_season_user_rank_id_response_200_data_flags_to_next_rank import (
            GetV4SeasonUserRankIdResponse200DataFlagsToNextRank,
        )
        from ..models.get_v4_season_user_rank_id_response_200_data_league_type_0 import (
            GetV4SeasonUserRankIdResponse200DataLeagueType0,
        )
        from ..models.get_v4_season_user_rank_id_response_200_data_next_rank import (
            GetV4SeasonUserRankIdResponse200DataNextRank,
        )
        from ..models.get_v4_season_user_rank_id_response_200_data_rank_suffix_type_0 import (
            GetV4SeasonUserRankIdResponse200DataRankSuffixType0,
        )
        from ..models.get_v4_season_user_rank_id_response_200_data_rank_type_0 import (
            GetV4SeasonUserRankIdResponse200DataRankType0,
        )
        from ..models.get_v4_season_user_rank_id_response_200_data_total_ranks_type_0 import (
            GetV4SeasonUserRankIdResponse200DataTotalRanksType0,
        )
        from ..models.get_v4_season_user_rank_id_response_200_data_total_season_flags import (
            GetV4SeasonUserRankIdResponse200DataTotalSeasonFlags,
        )

        d = dict(src_dict)

        def _parse_league(data: object) -> GetV4SeasonUserRankIdResponse200DataLeagueType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                league_type_0 = GetV4SeasonUserRankIdResponse200DataLeagueType0.from_dict(data)

                return league_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SeasonUserRankIdResponse200DataLeagueType0 | None | Unset, data)

        league = _parse_league(d.pop("league", UNSET))

        def _parse_rank(data: object) -> GetV4SeasonUserRankIdResponse200DataRankType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rank_type_0 = GetV4SeasonUserRankIdResponse200DataRankType0.from_dict(data)

                return rank_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SeasonUserRankIdResponse200DataRankType0 | None | Unset, data)

        rank = _parse_rank(d.pop("rank", UNSET))

        _next_rank = d.pop("next_rank", UNSET)
        next_rank: GetV4SeasonUserRankIdResponse200DataNextRank | Unset
        if isinstance(_next_rank, Unset):
            next_rank = UNSET
        else:
            next_rank = GetV4SeasonUserRankIdResponse200DataNextRank.from_dict(_next_rank)

        def _parse_total_ranks(data: object) -> GetV4SeasonUserRankIdResponse200DataTotalRanksType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_ranks_type_0 = GetV4SeasonUserRankIdResponse200DataTotalRanksType0.from_dict(data)

                return total_ranks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SeasonUserRankIdResponse200DataTotalRanksType0 | None | Unset, data)

        total_ranks = _parse_total_ranks(d.pop("total_ranks", UNSET))

        def _parse_rank_suffix(data: object) -> GetV4SeasonUserRankIdResponse200DataRankSuffixType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rank_suffix_type_0 = GetV4SeasonUserRankIdResponse200DataRankSuffixType0.from_dict(data)

                return rank_suffix_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SeasonUserRankIdResponse200DataRankSuffixType0 | None | Unset, data)

        rank_suffix = _parse_rank_suffix(d.pop("rank_suffix", UNSET))

        total_season_points = d.pop("total_season_points", UNSET)

        _flags_to_next_rank = d.pop("flags_to_next_rank", UNSET)
        flags_to_next_rank: GetV4SeasonUserRankIdResponse200DataFlagsToNextRank | Unset
        if isinstance(_flags_to_next_rank, Unset):
            flags_to_next_rank = UNSET
        else:
            flags_to_next_rank = GetV4SeasonUserRankIdResponse200DataFlagsToNextRank.from_dict(_flags_to_next_rank)

        _total_season_flags = d.pop("total_season_flags", UNSET)
        total_season_flags: GetV4SeasonUserRankIdResponse200DataTotalSeasonFlags | Unset
        if isinstance(_total_season_flags, Unset):
            total_season_flags = UNSET
        else:
            total_season_flags = GetV4SeasonUserRankIdResponse200DataTotalSeasonFlags.from_dict(_total_season_flags)

        get_v4_season_user_rank_id_response_200_data = cls(
            league=league,
            rank=rank,
            next_rank=next_rank,
            total_ranks=total_ranks,
            rank_suffix=rank_suffix,
            total_season_points=total_season_points,
            flags_to_next_rank=flags_to_next_rank,
            total_season_flags=total_season_flags,
        )

        get_v4_season_user_rank_id_response_200_data.additional_properties = d
        return get_v4_season_user_rank_id_response_200_data

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
