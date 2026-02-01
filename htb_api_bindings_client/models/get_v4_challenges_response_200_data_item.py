from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_challenges_response_200_data_item_difficulty_chart import (
        GetV4ChallengesResponse200DataItemDifficultyChart,
    )
    from ..models.get_v4_challenges_response_200_data_item_labels_item import (
        GetV4ChallengesResponse200DataItemLabelsItem,
    )
    from ..models.get_v4_challenges_response_200_data_item_retires_type_0 import (
        GetV4ChallengesResponse200DataItemRetiresType0,
    )


T = TypeVar("T", bound="GetV4ChallengesResponse200DataItem")


@_attrs_define
class GetV4ChallengesResponse200DataItem:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        difficulty (str | Unset):
        user_difficulty (str | Unset):
        difficulty_chart (GetV4ChallengesResponse200DataItemDifficultyChart | Unset):
        state (str | Unset):
        category_id (float | Unset):
        category_name (str | Unset):
        solves (float | Unset):
        is_owned (bool | Unset):
        rating (float | Unset):
        rating_count (float | Unset):
        auth_user_has_reviewed (bool | Unset):
        avatar (str | Unset):
        release_date (str | Unset):
        pinned (bool | Unset):
        play_methods (list[str] | Unset):
        retires (GetV4ChallengesResponse200DataItemRetiresType0 | None | Unset):
        labels (list[GetV4ChallengesResponse200DataItemLabelsItem] | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    user_difficulty: str | Unset = UNSET
    difficulty_chart: GetV4ChallengesResponse200DataItemDifficultyChart | Unset = UNSET
    state: str | Unset = UNSET
    category_id: float | Unset = UNSET
    category_name: str | Unset = UNSET
    solves: float | Unset = UNSET
    is_owned: bool | Unset = UNSET
    rating: float | Unset = UNSET
    rating_count: float | Unset = UNSET
    auth_user_has_reviewed: bool | Unset = UNSET
    avatar: str | Unset = UNSET
    release_date: str | Unset = UNSET
    pinned: bool | Unset = UNSET
    play_methods: list[str] | Unset = UNSET
    retires: GetV4ChallengesResponse200DataItemRetiresType0 | None | Unset = UNSET
    labels: list[GetV4ChallengesResponse200DataItemLabelsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_challenges_response_200_data_item_retires_type_0 import (
            GetV4ChallengesResponse200DataItemRetiresType0,
        )

        id = self.id

        name = self.name

        difficulty = self.difficulty

        user_difficulty = self.user_difficulty

        difficulty_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.difficulty_chart, Unset):
            difficulty_chart = self.difficulty_chart.to_dict()

        state = self.state

        category_id = self.category_id

        category_name = self.category_name

        solves = self.solves

        is_owned = self.is_owned

        rating = self.rating

        rating_count = self.rating_count

        auth_user_has_reviewed = self.auth_user_has_reviewed

        avatar = self.avatar

        release_date = self.release_date

        pinned = self.pinned

        play_methods: list[str] | Unset = UNSET
        if not isinstance(self.play_methods, Unset):
            play_methods = self.play_methods

        retires: dict[str, Any] | None | Unset
        if isinstance(self.retires, Unset):
            retires = UNSET
        elif isinstance(self.retires, GetV4ChallengesResponse200DataItemRetiresType0):
            retires = self.retires.to_dict()
        else:
            retires = self.retires

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if user_difficulty is not UNSET:
            field_dict["user_difficulty"] = user_difficulty
        if difficulty_chart is not UNSET:
            field_dict["difficulty_chart"] = difficulty_chart
        if state is not UNSET:
            field_dict["state"] = state
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if solves is not UNSET:
            field_dict["solves"] = solves
        if is_owned is not UNSET:
            field_dict["is_owned"] = is_owned
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_count is not UNSET:
            field_dict["rating_count"] = rating_count
        if auth_user_has_reviewed is not UNSET:
            field_dict["auth_user_has_reviewed"] = auth_user_has_reviewed
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if play_methods is not UNSET:
            field_dict["play_methods"] = play_methods
        if retires is not UNSET:
            field_dict["retires"] = retires
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_challenges_response_200_data_item_difficulty_chart import (
            GetV4ChallengesResponse200DataItemDifficultyChart,
        )
        from ..models.get_v4_challenges_response_200_data_item_labels_item import (
            GetV4ChallengesResponse200DataItemLabelsItem,
        )
        from ..models.get_v4_challenges_response_200_data_item_retires_type_0 import (
            GetV4ChallengesResponse200DataItemRetiresType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        user_difficulty = d.pop("user_difficulty", UNSET)

        _difficulty_chart = d.pop("difficulty_chart", UNSET)
        difficulty_chart: GetV4ChallengesResponse200DataItemDifficultyChart | Unset
        if isinstance(_difficulty_chart, Unset):
            difficulty_chart = UNSET
        else:
            difficulty_chart = GetV4ChallengesResponse200DataItemDifficultyChart.from_dict(_difficulty_chart)

        state = d.pop("state", UNSET)

        category_id = d.pop("category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        solves = d.pop("solves", UNSET)

        is_owned = d.pop("is_owned", UNSET)

        rating = d.pop("rating", UNSET)

        rating_count = d.pop("rating_count", UNSET)

        auth_user_has_reviewed = d.pop("auth_user_has_reviewed", UNSET)

        avatar = d.pop("avatar", UNSET)

        release_date = d.pop("release_date", UNSET)

        pinned = d.pop("pinned", UNSET)

        play_methods = cast(list[str], d.pop("play_methods", UNSET))

        def _parse_retires(data: object) -> GetV4ChallengesResponse200DataItemRetiresType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retires_type_0 = GetV4ChallengesResponse200DataItemRetiresType0.from_dict(data)

                return retires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengesResponse200DataItemRetiresType0 | None | Unset, data)

        retires = _parse_retires(d.pop("retires", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: list[GetV4ChallengesResponse200DataItemLabelsItem] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = GetV4ChallengesResponse200DataItemLabelsItem.from_dict(labels_item_data)

                labels.append(labels_item)

        get_v4_challenges_response_200_data_item = cls(
            id=id,
            name=name,
            difficulty=difficulty,
            user_difficulty=user_difficulty,
            difficulty_chart=difficulty_chart,
            state=state,
            category_id=category_id,
            category_name=category_name,
            solves=solves,
            is_owned=is_owned,
            rating=rating,
            rating_count=rating_count,
            auth_user_has_reviewed=auth_user_has_reviewed,
            avatar=avatar,
            release_date=release_date,
            pinned=pinned,
            play_methods=play_methods,
            retires=retires,
            labels=labels,
        )

        get_v4_challenges_response_200_data_item.additional_properties = d
        return get_v4_challenges_response_200_data_item

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
