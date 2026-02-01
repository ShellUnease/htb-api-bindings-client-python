from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_user_dashboard_recommended_response_200_sherlocks_item_status_type_0 import (
        GetV5UserDashboardRecommendedResponse200SherlocksItemStatusType0,
    )


T = TypeVar("T", bound="GetV5UserDashboardRecommendedResponse200SherlocksItem")


@_attrs_define
class GetV5UserDashboardRecommendedResponse200SherlocksItem:
    """
    Attributes:
        url_name (str | Unset):
        difficulty (str | Unset):
        url (str | Unset):
        category_id (float | Unset):
        category_name (str | Unset):
        avatar (str | Unset):
        avatar_url (str | Unset):
        rating (float | Unset):
        rating_count (float | Unset):
        tasks_completed (float | Unset):
        tasks_total (float | Unset):
        progress (float | Unset):
        status (GetV5UserDashboardRecommendedResponse200SherlocksItemStatusType0 | None | Unset):
        id (float | Unset):
        name (str | Unset):
        type_ (str | Unset):
    """

    url_name: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    url: str | Unset = UNSET
    category_id: float | Unset = UNSET
    category_name: str | Unset = UNSET
    avatar: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    rating: float | Unset = UNSET
    rating_count: float | Unset = UNSET
    tasks_completed: float | Unset = UNSET
    tasks_total: float | Unset = UNSET
    progress: float | Unset = UNSET
    status: GetV5UserDashboardRecommendedResponse200SherlocksItemStatusType0 | None | Unset = UNSET
    id: float | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v5_user_dashboard_recommended_response_200_sherlocks_item_status_type_0 import (
            GetV5UserDashboardRecommendedResponse200SherlocksItemStatusType0,
        )

        url_name = self.url_name

        difficulty = self.difficulty

        url = self.url

        category_id = self.category_id

        category_name = self.category_name

        avatar = self.avatar

        avatar_url = self.avatar_url

        rating = self.rating

        rating_count = self.rating_count

        tasks_completed = self.tasks_completed

        tasks_total = self.tasks_total

        progress = self.progress

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, GetV5UserDashboardRecommendedResponse200SherlocksItemStatusType0):
            status = self.status.to_dict()
        else:
            status = self.status

        id = self.id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url_name is not UNSET:
            field_dict["urlName"] = url_name
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if url is not UNSET:
            field_dict["url"] = url
        if category_id is not UNSET:
            field_dict["categoryID"] = category_id
        if category_name is not UNSET:
            field_dict["categoryName"] = category_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
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
        from ..models.get_v5_user_dashboard_recommended_response_200_sherlocks_item_status_type_0 import (
            GetV5UserDashboardRecommendedResponse200SherlocksItemStatusType0,
        )

        d = dict(src_dict)
        url_name = d.pop("urlName", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        url = d.pop("url", UNSET)

        category_id = d.pop("categoryID", UNSET)

        category_name = d.pop("categoryName", UNSET)

        avatar = d.pop("avatar", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        rating = d.pop("rating", UNSET)

        rating_count = d.pop("ratingCount", UNSET)

        tasks_completed = d.pop("tasksCompleted", UNSET)

        tasks_total = d.pop("tasksTotal", UNSET)

        progress = d.pop("progress", UNSET)

        def _parse_status(
            data: object,
        ) -> GetV5UserDashboardRecommendedResponse200SherlocksItemStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_0 = GetV5UserDashboardRecommendedResponse200SherlocksItemStatusType0.from_dict(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV5UserDashboardRecommendedResponse200SherlocksItemStatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        get_v5_user_dashboard_recommended_response_200_sherlocks_item = cls(
            url_name=url_name,
            difficulty=difficulty,
            url=url,
            category_id=category_id,
            category_name=category_name,
            avatar=avatar,
            avatar_url=avatar_url,
            rating=rating,
            rating_count=rating_count,
            tasks_completed=tasks_completed,
            tasks_total=tasks_total,
            progress=progress,
            status=status,
            id=id,
            name=name,
            type_=type_,
        )

        get_v5_user_dashboard_recommended_response_200_sherlocks_item.additional_properties = d
        return get_v5_user_dashboard_recommended_response_200_sherlocks_item

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
