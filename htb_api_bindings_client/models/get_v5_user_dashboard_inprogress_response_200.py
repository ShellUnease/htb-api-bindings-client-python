from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV5UserDashboardInprogressResponse200")


@_attrs_define
class GetV5UserDashboardInprogressResponse200:
    """
    Attributes:
        starting_points (list[Any] | Unset):
        machines (list[Any] | Unset):
        challenges (list[Any] | Unset):
        sherlocks (list[Any] | Unset):
        pro_labs (list[Any] | Unset):
        tracks (list[Any] | Unset):
        fortresses (list[Any] | Unset):
    """

    starting_points: list[Any] | Unset = UNSET
    machines: list[Any] | Unset = UNSET
    challenges: list[Any] | Unset = UNSET
    sherlocks: list[Any] | Unset = UNSET
    pro_labs: list[Any] | Unset = UNSET
    tracks: list[Any] | Unset = UNSET
    fortresses: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        starting_points: list[Any] | Unset = UNSET
        if not isinstance(self.starting_points, Unset):
            starting_points = self.starting_points

        machines: list[Any] | Unset = UNSET
        if not isinstance(self.machines, Unset):
            machines = self.machines

        challenges: list[Any] | Unset = UNSET
        if not isinstance(self.challenges, Unset):
            challenges = self.challenges

        sherlocks: list[Any] | Unset = UNSET
        if not isinstance(self.sherlocks, Unset):
            sherlocks = self.sherlocks

        pro_labs: list[Any] | Unset = UNSET
        if not isinstance(self.pro_labs, Unset):
            pro_labs = self.pro_labs

        tracks: list[Any] | Unset = UNSET
        if not isinstance(self.tracks, Unset):
            tracks = self.tracks

        fortresses: list[Any] | Unset = UNSET
        if not isinstance(self.fortresses, Unset):
            fortresses = self.fortresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if starting_points is not UNSET:
            field_dict["startingPoints"] = starting_points
        if machines is not UNSET:
            field_dict["machines"] = machines
        if challenges is not UNSET:
            field_dict["challenges"] = challenges
        if sherlocks is not UNSET:
            field_dict["sherlocks"] = sherlocks
        if pro_labs is not UNSET:
            field_dict["proLabs"] = pro_labs
        if tracks is not UNSET:
            field_dict["tracks"] = tracks
        if fortresses is not UNSET:
            field_dict["fortresses"] = fortresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        starting_points = cast(list[Any], d.pop("startingPoints", UNSET))

        machines = cast(list[Any], d.pop("machines", UNSET))

        challenges = cast(list[Any], d.pop("challenges", UNSET))

        sherlocks = cast(list[Any], d.pop("sherlocks", UNSET))

        pro_labs = cast(list[Any], d.pop("proLabs", UNSET))

        tracks = cast(list[Any], d.pop("tracks", UNSET))

        fortresses = cast(list[Any], d.pop("fortresses", UNSET))

        get_v5_user_dashboard_inprogress_response_200 = cls(
            starting_points=starting_points,
            machines=machines,
            challenges=challenges,
            sherlocks=sherlocks,
            pro_labs=pro_labs,
            tracks=tracks,
            fortresses=fortresses,
        )

        get_v5_user_dashboard_inprogress_response_200.additional_properties = d
        return get_v5_user_dashboard_inprogress_response_200

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
