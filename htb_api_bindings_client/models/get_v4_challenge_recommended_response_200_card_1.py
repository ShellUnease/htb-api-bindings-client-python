from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4ChallengeRecommendedResponse200Card1")


@_attrs_define
class GetV4ChallengeRecommendedResponse200Card1:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        url_name (str | Unset):
        difficulty (str | Unset):
        category_name (str | Unset):
        retired (bool | Unset):
        release_date (str | Unset):
        retire_challenge_id (float | Unset):
        rating (float | Unset):
        state (str | Unset):
        avatar_url (str | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    url_name: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    category_name: str | Unset = UNSET
    retired: bool | Unset = UNSET
    release_date: str | Unset = UNSET
    retire_challenge_id: float | Unset = UNSET
    rating: float | Unset = UNSET
    state: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url_name = self.url_name

        difficulty = self.difficulty

        category_name = self.category_name

        retired = self.retired

        release_date = self.release_date

        retire_challenge_id = self.retire_challenge_id

        rating = self.rating

        state = self.state

        avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url_name is not UNSET:
            field_dict["url_name"] = url_name
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if retired is not UNSET:
            field_dict["retired"] = retired
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if retire_challenge_id is not UNSET:
            field_dict["retire_challenge_id"] = retire_challenge_id
        if rating is not UNSET:
            field_dict["rating"] = rating
        if state is not UNSET:
            field_dict["state"] = state
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url_name = d.pop("url_name", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        category_name = d.pop("category_name", UNSET)

        retired = d.pop("retired", UNSET)

        release_date = d.pop("release_date", UNSET)

        retire_challenge_id = d.pop("retire_challenge_id", UNSET)

        rating = d.pop("rating", UNSET)

        state = d.pop("state", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        get_v4_challenge_recommended_response_200_card_1 = cls(
            id=id,
            name=name,
            url_name=url_name,
            difficulty=difficulty,
            category_name=category_name,
            retired=retired,
            release_date=release_date,
            retire_challenge_id=retire_challenge_id,
            rating=rating,
            state=state,
            avatar_url=avatar_url,
        )

        get_v4_challenge_recommended_response_200_card_1.additional_properties = d
        return get_v4_challenge_recommended_response_200_card_1

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
