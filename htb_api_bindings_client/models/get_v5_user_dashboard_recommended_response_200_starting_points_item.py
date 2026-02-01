from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV5UserDashboardRecommendedResponse200StartingPointsItem")


@_attrs_define
class GetV5UserDashboardRecommendedResponse200StartingPointsItem:
    """
    Attributes:
        description (str | Unset):
        difficulty (str | Unset):
        completion_percentage (float | Unset):
        free_machine_completion_percentage (float | Unset):
        avatar (str | Unset):
        avatar_url (str | Unset):
        progress (float | Unset):
        tasks_completed (float | Unset):
        tasks_total (float | Unset):
        id (float | Unset):
        name (str | Unset):
        type_ (str | Unset):
    """

    description: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    completion_percentage: float | Unset = UNSET
    free_machine_completion_percentage: float | Unset = UNSET
    avatar: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    progress: float | Unset = UNSET
    tasks_completed: float | Unset = UNSET
    tasks_total: float | Unset = UNSET
    id: float | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        difficulty = self.difficulty

        completion_percentage = self.completion_percentage

        free_machine_completion_percentage = self.free_machine_completion_percentage

        avatar = self.avatar

        avatar_url = self.avatar_url

        progress = self.progress

        tasks_completed = self.tasks_completed

        tasks_total = self.tasks_total

        id = self.id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if completion_percentage is not UNSET:
            field_dict["completionPercentage"] = completion_percentage
        if free_machine_completion_percentage is not UNSET:
            field_dict["freeMachineCompletionPercentage"] = free_machine_completion_percentage
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if progress is not UNSET:
            field_dict["progress"] = progress
        if tasks_completed is not UNSET:
            field_dict["tasksCompleted"] = tasks_completed
        if tasks_total is not UNSET:
            field_dict["tasksTotal"] = tasks_total
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        completion_percentage = d.pop("completionPercentage", UNSET)

        free_machine_completion_percentage = d.pop("freeMachineCompletionPercentage", UNSET)

        avatar = d.pop("avatar", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        progress = d.pop("progress", UNSET)

        tasks_completed = d.pop("tasksCompleted", UNSET)

        tasks_total = d.pop("tasksTotal", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        get_v5_user_dashboard_recommended_response_200_starting_points_item = cls(
            description=description,
            difficulty=difficulty,
            completion_percentage=completion_percentage,
            free_machine_completion_percentage=free_machine_completion_percentage,
            avatar=avatar,
            avatar_url=avatar_url,
            progress=progress,
            tasks_completed=tasks_completed,
            tasks_total=tasks_total,
            id=id,
            name=name,
            type_=type_,
        )

        get_v5_user_dashboard_recommended_response_200_starting_points_item.additional_properties = d
        return get_v5_user_dashboard_recommended_response_200_starting_points_item

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
