from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_recommended_response_200_card_2_feedback_for_chart import (
        GetV4MachineRecommendedResponse200Card2FeedbackForChart,
    )


T = TypeVar("T", bound="GetV4MachineRecommendedResponse200Card2")


@_attrs_define
class GetV4MachineRecommendedResponse200Card2:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        os (str | Unset):
        release (str | Unset):
        retired (float | Unset):
        retired_date (str | Unset):
        difficulty_text (str | Unset):
        avatar (str | Unset):
        feedback_for_chart (GetV4MachineRecommendedResponse200Card2FeedbackForChart | Unset):
        points (float | Unset):
        user_owns_count (float | Unset):
        root_owns_count (float | Unset):
        stars (float | Unset):
        auth_user_in_user_owns (bool | Unset):
        auth_user_in_root_owns (bool | Unset):
        type_card (str | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    os: str | Unset = UNSET
    release: str | Unset = UNSET
    retired: float | Unset = UNSET
    retired_date: str | Unset = UNSET
    difficulty_text: str | Unset = UNSET
    avatar: str | Unset = UNSET
    feedback_for_chart: GetV4MachineRecommendedResponse200Card2FeedbackForChart | Unset = UNSET
    points: float | Unset = UNSET
    user_owns_count: float | Unset = UNSET
    root_owns_count: float | Unset = UNSET
    stars: float | Unset = UNSET
    auth_user_in_user_owns: bool | Unset = UNSET
    auth_user_in_root_owns: bool | Unset = UNSET
    type_card: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        os = self.os

        release = self.release

        retired = self.retired

        retired_date = self.retired_date

        difficulty_text = self.difficulty_text

        avatar = self.avatar

        feedback_for_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feedback_for_chart, Unset):
            feedback_for_chart = self.feedback_for_chart.to_dict()

        points = self.points

        user_owns_count = self.user_owns_count

        root_owns_count = self.root_owns_count

        stars = self.stars

        auth_user_in_user_owns = self.auth_user_in_user_owns

        auth_user_in_root_owns = self.auth_user_in_root_owns

        type_card = self.type_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if release is not UNSET:
            field_dict["release"] = release
        if retired is not UNSET:
            field_dict["retired"] = retired
        if retired_date is not UNSET:
            field_dict["retired_date"] = retired_date
        if difficulty_text is not UNSET:
            field_dict["difficultyText"] = difficulty_text
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if feedback_for_chart is not UNSET:
            field_dict["feedbackForChart"] = feedback_for_chart
        if points is not UNSET:
            field_dict["points"] = points
        if user_owns_count is not UNSET:
            field_dict["user_owns_count"] = user_owns_count
        if root_owns_count is not UNSET:
            field_dict["root_owns_count"] = root_owns_count
        if stars is not UNSET:
            field_dict["stars"] = stars
        if auth_user_in_user_owns is not UNSET:
            field_dict["authUserInUserOwns"] = auth_user_in_user_owns
        if auth_user_in_root_owns is not UNSET:
            field_dict["authUserInRootOwns"] = auth_user_in_root_owns
        if type_card is not UNSET:
            field_dict["typeCard"] = type_card

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_recommended_response_200_card_2_feedback_for_chart import (
            GetV4MachineRecommendedResponse200Card2FeedbackForChart,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        release = d.pop("release", UNSET)

        retired = d.pop("retired", UNSET)

        retired_date = d.pop("retired_date", UNSET)

        difficulty_text = d.pop("difficultyText", UNSET)

        avatar = d.pop("avatar", UNSET)

        _feedback_for_chart = d.pop("feedbackForChart", UNSET)
        feedback_for_chart: GetV4MachineRecommendedResponse200Card2FeedbackForChart | Unset
        if isinstance(_feedback_for_chart, Unset):
            feedback_for_chart = UNSET
        else:
            feedback_for_chart = GetV4MachineRecommendedResponse200Card2FeedbackForChart.from_dict(_feedback_for_chart)

        points = d.pop("points", UNSET)

        user_owns_count = d.pop("user_owns_count", UNSET)

        root_owns_count = d.pop("root_owns_count", UNSET)

        stars = d.pop("stars", UNSET)

        auth_user_in_user_owns = d.pop("authUserInUserOwns", UNSET)

        auth_user_in_root_owns = d.pop("authUserInRootOwns", UNSET)

        type_card = d.pop("typeCard", UNSET)

        get_v4_machine_recommended_response_200_card_2 = cls(
            id=id,
            name=name,
            os=os,
            release=release,
            retired=retired,
            retired_date=retired_date,
            difficulty_text=difficulty_text,
            avatar=avatar,
            feedback_for_chart=feedback_for_chart,
            points=points,
            user_owns_count=user_owns_count,
            root_owns_count=root_owns_count,
            stars=stars,
            auth_user_in_user_owns=auth_user_in_user_owns,
            auth_user_in_root_owns=auth_user_in_root_owns,
            type_card=type_card,
        )

        get_v4_machine_recommended_response_200_card_2.additional_properties = d
        return get_v4_machine_recommended_response_200_card_2

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
