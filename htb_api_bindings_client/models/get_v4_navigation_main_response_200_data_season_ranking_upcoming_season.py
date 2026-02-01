from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_background_image_type_0 import (
        GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonBackgroundImageType0,
    )
    from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_date_type_0 import (
        GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonDateType0,
    )
    from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_id_type_0 import (
        GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonIdType0,
    )
    from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_name_type_0 import (
        GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonNameType0,
    )


T = TypeVar("T", bound="GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeason")


@_attrs_define
class GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeason:
    """
    Attributes:
        id (GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonIdType0 | None | Unset):
        name (GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonNameType0 | None | Unset):
        date (GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonDateType0 | None | Unset):
        background_image (GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonBackgroundImageType0 | None |
            Unset):
    """

    id: GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonIdType0 | None | Unset = UNSET
    name: GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonNameType0 | None | Unset = UNSET
    date: GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonDateType0 | None | Unset = UNSET
    background_image: (
        GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonBackgroundImageType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_background_image_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonBackgroundImageType0,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_date_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonDateType0,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_id_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonIdType0,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_name_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonNameType0,
        )

        id: dict[str, Any] | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonIdType0):
            id = self.id.to_dict()
        else:
            id = self.id

        name: dict[str, Any] | None | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonNameType0):
            name = self.name.to_dict()
        else:
            name = self.name

        date: dict[str, Any] | None | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonDateType0):
            date = self.date.to_dict()
        else:
            date = self.date

        background_image: dict[str, Any] | None | Unset
        if isinstance(self.background_image, Unset):
            background_image = UNSET
        elif isinstance(
            self.background_image, GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonBackgroundImageType0
        ):
            background_image = self.background_image.to_dict()
        else:
            background_image = self.background_image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if date is not UNSET:
            field_dict["date"] = date
        if background_image is not UNSET:
            field_dict["background_image"] = background_image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_background_image_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonBackgroundImageType0,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_date_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonDateType0,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_id_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonIdType0,
        )
        from ..models.get_v4_navigation_main_response_200_data_season_ranking_upcoming_season_name_type_0 import (
            GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonNameType0,
        )

        d = dict(src_dict)

        def _parse_id(
            data: object,
        ) -> GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonIdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                id_type_0 = GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonIdType0.from_dict(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonIdType0 | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(
            data: object,
        ) -> GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_0 = GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonNameType0.from_dict(data)

                return name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonNameType0 | None | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_date(
            data: object,
        ) -> GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonDateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                date_type_0 = GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonDateType0.from_dict(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonDateType0 | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_background_image(
            data: object,
        ) -> GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonBackgroundImageType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                background_image_type_0 = (
                    GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonBackgroundImageType0.from_dict(data)
                )

                return background_image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetV4NavigationMainResponse200DataSeasonRankingUpcomingSeasonBackgroundImageType0 | None | Unset, data
            )

        background_image = _parse_background_image(d.pop("background_image", UNSET))

        get_v4_navigation_main_response_200_data_season_ranking_upcoming_season = cls(
            id=id,
            name=name,
            date=date,
            background_image=background_image,
        )

        get_v4_navigation_main_response_200_data_season_ranking_upcoming_season.additional_properties = d
        return get_v4_navigation_main_response_200_data_season_ranking_upcoming_season

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
