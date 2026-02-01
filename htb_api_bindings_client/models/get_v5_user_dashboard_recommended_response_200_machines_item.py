from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_user_dashboard_recommended_response_200_machines_item_points_type_0 import (
        GetV5UserDashboardRecommendedResponse200MachinesItemPointsType0,
    )
    from ..models.get_v5_user_dashboard_recommended_response_200_machines_item_status_type_0 import (
        GetV5UserDashboardRecommendedResponse200MachinesItemStatusType0,
    )


T = TypeVar("T", bound="GetV5UserDashboardRecommendedResponse200MachinesItem")


@_attrs_define
class GetV5UserDashboardRecommendedResponse200MachinesItem:
    """
    Attributes:
        os (str | Unset):
        difficulty (str | Unset):
        avatar (str | Unset):
        url (str | Unset):
        user_flag (bool | Unset):
        root_flag (bool | Unset):
        avatar_url (str | Unset):
        points (GetV5UserDashboardRecommendedResponse200MachinesItemPointsType0 | None | Unset):
        rating (float | Unset):
        rating_count (float | Unset):
        tasks_completed (float | Unset):
        tasks_total (float | Unset):
        progress (float | Unset):
        guided (bool | Unset):
        status (GetV5UserDashboardRecommendedResponse200MachinesItemStatusType0 | None | Unset):
        id (float | Unset):
        name (str | Unset):
        type_ (str | Unset):
    """

    os: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    avatar: str | Unset = UNSET
    url: str | Unset = UNSET
    user_flag: bool | Unset = UNSET
    root_flag: bool | Unset = UNSET
    avatar_url: str | Unset = UNSET
    points: GetV5UserDashboardRecommendedResponse200MachinesItemPointsType0 | None | Unset = UNSET
    rating: float | Unset = UNSET
    rating_count: float | Unset = UNSET
    tasks_completed: float | Unset = UNSET
    tasks_total: float | Unset = UNSET
    progress: float | Unset = UNSET
    guided: bool | Unset = UNSET
    status: GetV5UserDashboardRecommendedResponse200MachinesItemStatusType0 | None | Unset = UNSET
    id: float | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v5_user_dashboard_recommended_response_200_machines_item_points_type_0 import (
            GetV5UserDashboardRecommendedResponse200MachinesItemPointsType0,
        )
        from ..models.get_v5_user_dashboard_recommended_response_200_machines_item_status_type_0 import (
            GetV5UserDashboardRecommendedResponse200MachinesItemStatusType0,
        )

        os = self.os

        difficulty = self.difficulty

        avatar = self.avatar

        url = self.url

        user_flag = self.user_flag

        root_flag = self.root_flag

        avatar_url = self.avatar_url

        points: dict[str, Any] | None | Unset
        if isinstance(self.points, Unset):
            points = UNSET
        elif isinstance(self.points, GetV5UserDashboardRecommendedResponse200MachinesItemPointsType0):
            points = self.points.to_dict()
        else:
            points = self.points

        rating = self.rating

        rating_count = self.rating_count

        tasks_completed = self.tasks_completed

        tasks_total = self.tasks_total

        progress = self.progress

        guided = self.guided

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, GetV5UserDashboardRecommendedResponse200MachinesItemStatusType0):
            status = self.status.to_dict()
        else:
            status = self.status

        id = self.id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if os is not UNSET:
            field_dict["os"] = os
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if url is not UNSET:
            field_dict["url"] = url
        if user_flag is not UNSET:
            field_dict["user_flag"] = user_flag
        if root_flag is not UNSET:
            field_dict["root_flag"] = root_flag
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if points is not UNSET:
            field_dict["points"] = points
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_count is not UNSET:
            field_dict["ratingCount"] = rating_count
        if tasks_completed is not UNSET:
            field_dict["tasksCompleted"] = tasks_completed
        if tasks_total is not UNSET:
            field_dict["tasksTotal"] = tasks_total
        if progress is not UNSET:
            field_dict["progress"] = progress
        if guided is not UNSET:
            field_dict["guided"] = guided
        if status is not UNSET:
            field_dict["status"] = status
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_user_dashboard_recommended_response_200_machines_item_points_type_0 import (
            GetV5UserDashboardRecommendedResponse200MachinesItemPointsType0,
        )
        from ..models.get_v5_user_dashboard_recommended_response_200_machines_item_status_type_0 import (
            GetV5UserDashboardRecommendedResponse200MachinesItemStatusType0,
        )

        d = dict(src_dict)
        os = d.pop("os", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        avatar = d.pop("avatar", UNSET)

        url = d.pop("url", UNSET)

        user_flag = d.pop("user_flag", UNSET)

        root_flag = d.pop("root_flag", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        def _parse_points(
            data: object,
        ) -> GetV5UserDashboardRecommendedResponse200MachinesItemPointsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                points_type_0 = GetV5UserDashboardRecommendedResponse200MachinesItemPointsType0.from_dict(data)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV5UserDashboardRecommendedResponse200MachinesItemPointsType0 | None | Unset, data)

        points = _parse_points(d.pop("points", UNSET))

        rating = d.pop("rating", UNSET)

        rating_count = d.pop("ratingCount", UNSET)

        tasks_completed = d.pop("tasksCompleted", UNSET)

        tasks_total = d.pop("tasksTotal", UNSET)

        progress = d.pop("progress", UNSET)

        guided = d.pop("guided", UNSET)

        def _parse_status(
            data: object,
        ) -> GetV5UserDashboardRecommendedResponse200MachinesItemStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_0 = GetV5UserDashboardRecommendedResponse200MachinesItemStatusType0.from_dict(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV5UserDashboardRecommendedResponse200MachinesItemStatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        get_v5_user_dashboard_recommended_response_200_machines_item = cls(
            os=os,
            difficulty=difficulty,
            avatar=avatar,
            url=url,
            user_flag=user_flag,
            root_flag=root_flag,
            avatar_url=avatar_url,
            points=points,
            rating=rating,
            rating_count=rating_count,
            tasks_completed=tasks_completed,
            tasks_total=tasks_total,
            progress=progress,
            guided=guided,
            status=status,
            id=id,
            name=name,
            type_=type_,
        )

        get_v5_user_dashboard_recommended_response_200_machines_item.additional_properties = d
        return get_v5_user_dashboard_recommended_response_200_machines_item

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
