from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_disliked_by_user_type_0 import (
        GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemDislikedByUserType0,
    )
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_language_code_type_0 import (
        GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageCodeType0,
    )
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_language_name_type_0 import (
        GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageNameType0,
    )
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_liked_by_user_type_0 import (
        GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLikedByUserType0,
    )


T = TypeVar("T", bound="GetV4MachineWalkthroughsIdResponse200MessageWriteupsItem")


@_attrs_define
class GetV4MachineWalkthroughsIdResponse200MessageWriteupsItem:
    """
    Attributes:
        id (float | Unset):
        user_id (float | Unset):
        user_name (str | Unset):
        user_avatar (str | Unset):
        url (str | Unset):
        created_at (str | Unset):
        total_ratings (float | Unset):
        rating (float | Unset):
        language_code (GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageCodeType0 | None | Unset):
        language_name (GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageNameType0 | None | Unset):
        liked_by_user (GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLikedByUserType0 | None | Unset):
        disliked_by_user (GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemDislikedByUserType0 | None | Unset):
    """

    id: float | Unset = UNSET
    user_id: float | Unset = UNSET
    user_name: str | Unset = UNSET
    user_avatar: str | Unset = UNSET
    url: str | Unset = UNSET
    created_at: str | Unset = UNSET
    total_ratings: float | Unset = UNSET
    rating: float | Unset = UNSET
    language_code: GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageCodeType0 | None | Unset = UNSET
    language_name: GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageNameType0 | None | Unset = UNSET
    liked_by_user: GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLikedByUserType0 | None | Unset = UNSET
    disliked_by_user: GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemDislikedByUserType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_disliked_by_user_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemDislikedByUserType0,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_language_code_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageCodeType0,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_language_name_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageNameType0,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_liked_by_user_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLikedByUserType0,
        )

        id = self.id

        user_id = self.user_id

        user_name = self.user_name

        user_avatar = self.user_avatar

        url = self.url

        created_at = self.created_at

        total_ratings = self.total_ratings

        rating = self.rating

        language_code: dict[str, Any] | None | Unset
        if isinstance(self.language_code, Unset):
            language_code = UNSET
        elif isinstance(self.language_code, GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageCodeType0):
            language_code = self.language_code.to_dict()
        else:
            language_code = self.language_code

        language_name: dict[str, Any] | None | Unset
        if isinstance(self.language_name, Unset):
            language_name = UNSET
        elif isinstance(self.language_name, GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageNameType0):
            language_name = self.language_name.to_dict()
        else:
            language_name = self.language_name

        liked_by_user: dict[str, Any] | None | Unset
        if isinstance(self.liked_by_user, Unset):
            liked_by_user = UNSET
        elif isinstance(self.liked_by_user, GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLikedByUserType0):
            liked_by_user = self.liked_by_user.to_dict()
        else:
            liked_by_user = self.liked_by_user

        disliked_by_user: dict[str, Any] | None | Unset
        if isinstance(self.disliked_by_user, Unset):
            disliked_by_user = UNSET
        elif isinstance(
            self.disliked_by_user, GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemDislikedByUserType0
        ):
            disliked_by_user = self.disliked_by_user.to_dict()
        else:
            disliked_by_user = self.disliked_by_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if user_avatar is not UNSET:
            field_dict["user_avatar"] = user_avatar
        if url is not UNSET:
            field_dict["url"] = url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if total_ratings is not UNSET:
            field_dict["total_ratings"] = total_ratings
        if rating is not UNSET:
            field_dict["rating"] = rating
        if language_code is not UNSET:
            field_dict["language_code"] = language_code
        if language_name is not UNSET:
            field_dict["language_name"] = language_name
        if liked_by_user is not UNSET:
            field_dict["liked_by_user"] = liked_by_user
        if disliked_by_user is not UNSET:
            field_dict["disliked_by_user"] = disliked_by_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_disliked_by_user_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemDislikedByUserType0,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_language_code_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageCodeType0,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_language_name_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageNameType0,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item_liked_by_user_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLikedByUserType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        user_avatar = d.pop("user_avatar", UNSET)

        url = d.pop("url", UNSET)

        created_at = d.pop("created_at", UNSET)

        total_ratings = d.pop("total_ratings", UNSET)

        rating = d.pop("rating", UNSET)

        def _parse_language_code(
            data: object,
        ) -> GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageCodeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                language_code_type_0 = (
                    GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageCodeType0.from_dict(data)
                )

                return language_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageCodeType0 | None | Unset, data)

        language_code = _parse_language_code(d.pop("language_code", UNSET))

        def _parse_language_name(
            data: object,
        ) -> GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                language_name_type_0 = (
                    GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageNameType0.from_dict(data)
                )

                return language_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLanguageNameType0 | None | Unset, data)

        language_name = _parse_language_name(d.pop("language_name", UNSET))

        def _parse_liked_by_user(
            data: object,
        ) -> GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLikedByUserType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                liked_by_user_type_0 = (
                    GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLikedByUserType0.from_dict(data)
                )

                return liked_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemLikedByUserType0 | None | Unset, data)

        liked_by_user = _parse_liked_by_user(d.pop("liked_by_user", UNSET))

        def _parse_disliked_by_user(
            data: object,
        ) -> GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemDislikedByUserType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                disliked_by_user_type_0 = (
                    GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemDislikedByUserType0.from_dict(data)
                )

                return disliked_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetV4MachineWalkthroughsIdResponse200MessageWriteupsItemDislikedByUserType0 | None | Unset, data
            )

        disliked_by_user = _parse_disliked_by_user(d.pop("disliked_by_user", UNSET))

        get_v4_machine_walkthroughs_id_response_200_message_writeups_item = cls(
            id=id,
            user_id=user_id,
            user_name=user_name,
            user_avatar=user_avatar,
            url=url,
            created_at=created_at,
            total_ratings=total_ratings,
            rating=rating,
            language_code=language_code,
            language_name=language_name,
            liked_by_user=liked_by_user,
            disliked_by_user=disliked_by_user,
        )

        get_v4_machine_walkthroughs_id_response_200_message_writeups_item.additional_properties = d
        return get_v4_machine_walkthroughs_id_response_200_message_writeups_item

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
