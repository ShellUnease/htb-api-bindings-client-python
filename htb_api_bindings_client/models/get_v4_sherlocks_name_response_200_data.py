from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_sherlocks_name_response_200_data_tags_item import GetV4SherlocksNameResponse200DataTagsItem


T = TypeVar("T", bound="GetV4SherlocksNameResponse200Data")


@_attrs_define
class GetV4SherlocksNameResponse200Data:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        difficulty (str | Unset):
        retired (bool | Unset):
        release_at (str | Unset):
        state (str | Unset):
        category_id (float | Unset):
        category_name (str | Unset):
        show_go_vip (bool | Unset):
        is_todo (bool | Unset):
        rating (float | Unset):
        rating_count (float | Unset):
        auth_user_has_reviewed (bool | Unset):
        user_can_review (bool | Unset):
        writeup_visible (bool | Unset):
        avatar (str | Unset):
        favorite (bool | Unset):
        tags (list[GetV4SherlocksNameResponse200DataTagsItem] | Unset):
        play_methods (list[str] | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    retired: bool | Unset = UNSET
    release_at: str | Unset = UNSET
    state: str | Unset = UNSET
    category_id: float | Unset = UNSET
    category_name: str | Unset = UNSET
    show_go_vip: bool | Unset = UNSET
    is_todo: bool | Unset = UNSET
    rating: float | Unset = UNSET
    rating_count: float | Unset = UNSET
    auth_user_has_reviewed: bool | Unset = UNSET
    user_can_review: bool | Unset = UNSET
    writeup_visible: bool | Unset = UNSET
    avatar: str | Unset = UNSET
    favorite: bool | Unset = UNSET
    tags: list[GetV4SherlocksNameResponse200DataTagsItem] | Unset = UNSET
    play_methods: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        difficulty = self.difficulty

        retired = self.retired

        release_at = self.release_at

        state = self.state

        category_id = self.category_id

        category_name = self.category_name

        show_go_vip = self.show_go_vip

        is_todo = self.is_todo

        rating = self.rating

        rating_count = self.rating_count

        auth_user_has_reviewed = self.auth_user_has_reviewed

        user_can_review = self.user_can_review

        writeup_visible = self.writeup_visible

        avatar = self.avatar

        favorite = self.favorite

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        play_methods: list[str] | Unset = UNSET
        if not isinstance(self.play_methods, Unset):
            play_methods = self.play_methods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if retired is not UNSET:
            field_dict["retired"] = retired
        if release_at is not UNSET:
            field_dict["release_at"] = release_at
        if state is not UNSET:
            field_dict["state"] = state
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if show_go_vip is not UNSET:
            field_dict["show_go_vip"] = show_go_vip
        if is_todo is not UNSET:
            field_dict["isTodo"] = is_todo
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_count is not UNSET:
            field_dict["rating_count"] = rating_count
        if auth_user_has_reviewed is not UNSET:
            field_dict["auth_user_has_reviewed"] = auth_user_has_reviewed
        if user_can_review is not UNSET:
            field_dict["user_can_review"] = user_can_review
        if writeup_visible is not UNSET:
            field_dict["writeup_visible"] = writeup_visible
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if tags is not UNSET:
            field_dict["tags"] = tags
        if play_methods is not UNSET:
            field_dict["play_methods"] = play_methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_sherlocks_name_response_200_data_tags_item import GetV4SherlocksNameResponse200DataTagsItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        retired = d.pop("retired", UNSET)

        release_at = d.pop("release_at", UNSET)

        state = d.pop("state", UNSET)

        category_id = d.pop("category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        show_go_vip = d.pop("show_go_vip", UNSET)

        is_todo = d.pop("isTodo", UNSET)

        rating = d.pop("rating", UNSET)

        rating_count = d.pop("rating_count", UNSET)

        auth_user_has_reviewed = d.pop("auth_user_has_reviewed", UNSET)

        user_can_review = d.pop("user_can_review", UNSET)

        writeup_visible = d.pop("writeup_visible", UNSET)

        avatar = d.pop("avatar", UNSET)

        favorite = d.pop("favorite", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[GetV4SherlocksNameResponse200DataTagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = GetV4SherlocksNameResponse200DataTagsItem.from_dict(tags_item_data)

                tags.append(tags_item)

        play_methods = cast(list[str], d.pop("play_methods", UNSET))

        get_v4_sherlocks_name_response_200_data = cls(
            id=id,
            name=name,
            difficulty=difficulty,
            retired=retired,
            release_at=release_at,
            state=state,
            category_id=category_id,
            category_name=category_name,
            show_go_vip=show_go_vip,
            is_todo=is_todo,
            rating=rating,
            rating_count=rating_count,
            auth_user_has_reviewed=auth_user_has_reviewed,
            user_can_review=user_can_review,
            writeup_visible=writeup_visible,
            avatar=avatar,
            favorite=favorite,
            tags=tags,
            play_methods=play_methods,
        )

        get_v4_sherlocks_name_response_200_data.additional_properties = d
        return get_v4_sherlocks_name_response_200_data

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
