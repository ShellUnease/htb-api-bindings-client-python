from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_season_list_response_200_data_item_current_week_type_0 import (
        GetV4SeasonListResponse200DataItemCurrentWeekType0,
    )
    from ..models.get_v4_season_list_response_200_data_item_trailer_type_0 import (
        GetV4SeasonListResponse200DataItemTrailerType0,
    )


T = TypeVar("T", bound="GetV4SeasonListResponse200DataItem")


@_attrs_define
class GetV4SeasonListResponse200DataItem:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        subtitle (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        state (str | Unset):
        is_visible (bool | Unset):
        active (bool | Unset):
        background_image (str | Unset):
        new_background_image (str | Unset):
        logo (str | Unset):
        weeks (float | Unset):
        current_week (GetV4SeasonListResponse200DataItemCurrentWeekType0 | None | Unset):
        players (float | Unset):
        trailer (GetV4SeasonListResponse200DataItemTrailerType0 | None | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    state: str | Unset = UNSET
    is_visible: bool | Unset = UNSET
    active: bool | Unset = UNSET
    background_image: str | Unset = UNSET
    new_background_image: str | Unset = UNSET
    logo: str | Unset = UNSET
    weeks: float | Unset = UNSET
    current_week: GetV4SeasonListResponse200DataItemCurrentWeekType0 | None | Unset = UNSET
    players: float | Unset = UNSET
    trailer: GetV4SeasonListResponse200DataItemTrailerType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_season_list_response_200_data_item_current_week_type_0 import (
            GetV4SeasonListResponse200DataItemCurrentWeekType0,
        )
        from ..models.get_v4_season_list_response_200_data_item_trailer_type_0 import (
            GetV4SeasonListResponse200DataItemTrailerType0,
        )

        id = self.id

        name = self.name

        subtitle = self.subtitle

        start_date = self.start_date

        end_date = self.end_date

        state = self.state

        is_visible = self.is_visible

        active = self.active

        background_image = self.background_image

        new_background_image = self.new_background_image

        logo = self.logo

        weeks = self.weeks

        current_week: dict[str, Any] | None | Unset
        if isinstance(self.current_week, Unset):
            current_week = UNSET
        elif isinstance(self.current_week, GetV4SeasonListResponse200DataItemCurrentWeekType0):
            current_week = self.current_week.to_dict()
        else:
            current_week = self.current_week

        players = self.players

        trailer: dict[str, Any] | None | Unset
        if isinstance(self.trailer, Unset):
            trailer = UNSET
        elif isinstance(self.trailer, GetV4SeasonListResponse200DataItemTrailerType0):
            trailer = self.trailer.to_dict()
        else:
            trailer = self.trailer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if state is not UNSET:
            field_dict["state"] = state
        if is_visible is not UNSET:
            field_dict["is_visible"] = is_visible
        if active is not UNSET:
            field_dict["active"] = active
        if background_image is not UNSET:
            field_dict["background_image"] = background_image
        if new_background_image is not UNSET:
            field_dict["new_background_image"] = new_background_image
        if logo is not UNSET:
            field_dict["logo"] = logo
        if weeks is not UNSET:
            field_dict["weeks"] = weeks
        if current_week is not UNSET:
            field_dict["current_week"] = current_week
        if players is not UNSET:
            field_dict["players"] = players
        if trailer is not UNSET:
            field_dict["trailer"] = trailer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_season_list_response_200_data_item_current_week_type_0 import (
            GetV4SeasonListResponse200DataItemCurrentWeekType0,
        )
        from ..models.get_v4_season_list_response_200_data_item_trailer_type_0 import (
            GetV4SeasonListResponse200DataItemTrailerType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        state = d.pop("state", UNSET)

        is_visible = d.pop("is_visible", UNSET)

        active = d.pop("active", UNSET)

        background_image = d.pop("background_image", UNSET)

        new_background_image = d.pop("new_background_image", UNSET)

        logo = d.pop("logo", UNSET)

        weeks = d.pop("weeks", UNSET)

        def _parse_current_week(data: object) -> GetV4SeasonListResponse200DataItemCurrentWeekType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_week_type_0 = GetV4SeasonListResponse200DataItemCurrentWeekType0.from_dict(data)

                return current_week_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SeasonListResponse200DataItemCurrentWeekType0 | None | Unset, data)

        current_week = _parse_current_week(d.pop("current_week", UNSET))

        players = d.pop("players", UNSET)

        def _parse_trailer(data: object) -> GetV4SeasonListResponse200DataItemTrailerType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trailer_type_0 = GetV4SeasonListResponse200DataItemTrailerType0.from_dict(data)

                return trailer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SeasonListResponse200DataItemTrailerType0 | None | Unset, data)

        trailer = _parse_trailer(d.pop("trailer", UNSET))

        get_v4_season_list_response_200_data_item = cls(
            id=id,
            name=name,
            subtitle=subtitle,
            start_date=start_date,
            end_date=end_date,
            state=state,
            is_visible=is_visible,
            active=active,
            background_image=background_image,
            new_background_image=new_background_image,
            logo=logo,
            weeks=weeks,
            current_week=current_week,
            players=players,
            trailer=trailer,
        )

        get_v4_season_list_response_200_data_item.additional_properties = d
        return get_v4_season_list_response_200_data_item

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
