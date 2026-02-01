from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_user_dashboard_recommended_response_200_challenges_item import (
        GetV5UserDashboardRecommendedResponse200ChallengesItem,
    )
    from ..models.get_v5_user_dashboard_recommended_response_200_machines_item import (
        GetV5UserDashboardRecommendedResponse200MachinesItem,
    )
    from ..models.get_v5_user_dashboard_recommended_response_200_sherlocks_item import (
        GetV5UserDashboardRecommendedResponse200SherlocksItem,
    )
    from ..models.get_v5_user_dashboard_recommended_response_200_starting_points_item import (
        GetV5UserDashboardRecommendedResponse200StartingPointsItem,
    )


T = TypeVar("T", bound="GetV5UserDashboardRecommendedResponse200")


@_attrs_define
class GetV5UserDashboardRecommendedResponse200:
    """
    Attributes:
        starting_points (list[GetV5UserDashboardRecommendedResponse200StartingPointsItem] | Unset):
        machines (list[GetV5UserDashboardRecommendedResponse200MachinesItem] | Unset):
        challenges (list[GetV5UserDashboardRecommendedResponse200ChallengesItem] | Unset):
        sherlocks (list[GetV5UserDashboardRecommendedResponse200SherlocksItem] | Unset):
        pro_labs (list[Any] | Unset):
        tracks (list[Any] | Unset):
        fortresses (list[Any] | Unset):
    """

    starting_points: list[GetV5UserDashboardRecommendedResponse200StartingPointsItem] | Unset = UNSET
    machines: list[GetV5UserDashboardRecommendedResponse200MachinesItem] | Unset = UNSET
    challenges: list[GetV5UserDashboardRecommendedResponse200ChallengesItem] | Unset = UNSET
    sherlocks: list[GetV5UserDashboardRecommendedResponse200SherlocksItem] | Unset = UNSET
    pro_labs: list[Any] | Unset = UNSET
    tracks: list[Any] | Unset = UNSET
    fortresses: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        starting_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.starting_points, Unset):
            starting_points = []
            for starting_points_item_data in self.starting_points:
                starting_points_item = starting_points_item_data.to_dict()
                starting_points.append(starting_points_item)

        machines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.machines, Unset):
            machines = []
            for machines_item_data in self.machines:
                machines_item = machines_item_data.to_dict()
                machines.append(machines_item)

        challenges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.challenges, Unset):
            challenges = []
            for challenges_item_data in self.challenges:
                challenges_item = challenges_item_data.to_dict()
                challenges.append(challenges_item)

        sherlocks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sherlocks, Unset):
            sherlocks = []
            for sherlocks_item_data in self.sherlocks:
                sherlocks_item = sherlocks_item_data.to_dict()
                sherlocks.append(sherlocks_item)

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
        from ..models.get_v5_user_dashboard_recommended_response_200_challenges_item import (
            GetV5UserDashboardRecommendedResponse200ChallengesItem,
        )
        from ..models.get_v5_user_dashboard_recommended_response_200_machines_item import (
            GetV5UserDashboardRecommendedResponse200MachinesItem,
        )
        from ..models.get_v5_user_dashboard_recommended_response_200_sherlocks_item import (
            GetV5UserDashboardRecommendedResponse200SherlocksItem,
        )
        from ..models.get_v5_user_dashboard_recommended_response_200_starting_points_item import (
            GetV5UserDashboardRecommendedResponse200StartingPointsItem,
        )

        d = dict(src_dict)
        _starting_points = d.pop("startingPoints", UNSET)
        starting_points: list[GetV5UserDashboardRecommendedResponse200StartingPointsItem] | Unset = UNSET
        if _starting_points is not UNSET:
            starting_points = []
            for starting_points_item_data in _starting_points:
                starting_points_item = GetV5UserDashboardRecommendedResponse200StartingPointsItem.from_dict(
                    starting_points_item_data
                )

                starting_points.append(starting_points_item)

        _machines = d.pop("machines", UNSET)
        machines: list[GetV5UserDashboardRecommendedResponse200MachinesItem] | Unset = UNSET
        if _machines is not UNSET:
            machines = []
            for machines_item_data in _machines:
                machines_item = GetV5UserDashboardRecommendedResponse200MachinesItem.from_dict(machines_item_data)

                machines.append(machines_item)

        _challenges = d.pop("challenges", UNSET)
        challenges: list[GetV5UserDashboardRecommendedResponse200ChallengesItem] | Unset = UNSET
        if _challenges is not UNSET:
            challenges = []
            for challenges_item_data in _challenges:
                challenges_item = GetV5UserDashboardRecommendedResponse200ChallengesItem.from_dict(challenges_item_data)

                challenges.append(challenges_item)

        _sherlocks = d.pop("sherlocks", UNSET)
        sherlocks: list[GetV5UserDashboardRecommendedResponse200SherlocksItem] | Unset = UNSET
        if _sherlocks is not UNSET:
            sherlocks = []
            for sherlocks_item_data in _sherlocks:
                sherlocks_item = GetV5UserDashboardRecommendedResponse200SherlocksItem.from_dict(sherlocks_item_data)

                sherlocks.append(sherlocks_item)

        pro_labs = cast(list[Any], d.pop("proLabs", UNSET))

        tracks = cast(list[Any], d.pop("tracks", UNSET))

        fortresses = cast(list[Any], d.pop("fortresses", UNSET))

        get_v5_user_dashboard_recommended_response_200 = cls(
            starting_points=starting_points,
            machines=machines,
            challenges=challenges,
            sherlocks=sherlocks,
            pro_labs=pro_labs,
            tracks=tracks,
            fortresses=fortresses,
        )

        get_v5_user_dashboard_recommended_response_200.additional_properties = d
        return get_v5_user_dashboard_recommended_response_200

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
