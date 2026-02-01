from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_official_disliked_by_user_type_0 import (
        GetV4MachineWalkthroughsIdResponse200MessageOfficialDislikedByUserType0,
    )
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_official_liked_by_user_type_0 import (
        GetV4MachineWalkthroughsIdResponse200MessageOfficialLikedByUserType0,
    )


T = TypeVar("T", bound="GetV4MachineWalkthroughsIdResponse200MessageOfficial")


@_attrs_define
class GetV4MachineWalkthroughsIdResponse200MessageOfficial:
    """
    Attributes:
        rating (float | Unset):
        liked_by_user (GetV4MachineWalkthroughsIdResponse200MessageOfficialLikedByUserType0 | None | Unset):
        disliked_by_user (GetV4MachineWalkthroughsIdResponse200MessageOfficialDislikedByUserType0 | None | Unset):
        total_ratings (float | Unset):
        threshold_for_display_reached (float | Unset):
        filename (str | Unset):
        sha256 (str | Unset):
    """

    rating: float | Unset = UNSET
    liked_by_user: GetV4MachineWalkthroughsIdResponse200MessageOfficialLikedByUserType0 | None | Unset = UNSET
    disliked_by_user: GetV4MachineWalkthroughsIdResponse200MessageOfficialDislikedByUserType0 | None | Unset = UNSET
    total_ratings: float | Unset = UNSET
    threshold_for_display_reached: float | Unset = UNSET
    filename: str | Unset = UNSET
    sha256: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_official_disliked_by_user_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageOfficialDislikedByUserType0,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_official_liked_by_user_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageOfficialLikedByUserType0,
        )

        rating = self.rating

        liked_by_user: dict[str, Any] | None | Unset
        if isinstance(self.liked_by_user, Unset):
            liked_by_user = UNSET
        elif isinstance(self.liked_by_user, GetV4MachineWalkthroughsIdResponse200MessageOfficialLikedByUserType0):
            liked_by_user = self.liked_by_user.to_dict()
        else:
            liked_by_user = self.liked_by_user

        disliked_by_user: dict[str, Any] | None | Unset
        if isinstance(self.disliked_by_user, Unset):
            disliked_by_user = UNSET
        elif isinstance(self.disliked_by_user, GetV4MachineWalkthroughsIdResponse200MessageOfficialDislikedByUserType0):
            disliked_by_user = self.disliked_by_user.to_dict()
        else:
            disliked_by_user = self.disliked_by_user

        total_ratings = self.total_ratings

        threshold_for_display_reached = self.threshold_for_display_reached

        filename = self.filename

        sha256 = self.sha256

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rating is not UNSET:
            field_dict["rating"] = rating
        if liked_by_user is not UNSET:
            field_dict["likedByUser"] = liked_by_user
        if disliked_by_user is not UNSET:
            field_dict["dislikedByUser"] = disliked_by_user
        if total_ratings is not UNSET:
            field_dict["total_ratings"] = total_ratings
        if threshold_for_display_reached is not UNSET:
            field_dict["threshold_for_display_reached"] = threshold_for_display_reached
        if filename is not UNSET:
            field_dict["filename"] = filename
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_official_disliked_by_user_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageOfficialDislikedByUserType0,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_official_liked_by_user_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageOfficialLikedByUserType0,
        )

        d = dict(src_dict)
        rating = d.pop("rating", UNSET)

        def _parse_liked_by_user(
            data: object,
        ) -> GetV4MachineWalkthroughsIdResponse200MessageOfficialLikedByUserType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                liked_by_user_type_0 = GetV4MachineWalkthroughsIdResponse200MessageOfficialLikedByUserType0.from_dict(
                    data
                )

                return liked_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineWalkthroughsIdResponse200MessageOfficialLikedByUserType0 | None | Unset, data)

        liked_by_user = _parse_liked_by_user(d.pop("likedByUser", UNSET))

        def _parse_disliked_by_user(
            data: object,
        ) -> GetV4MachineWalkthroughsIdResponse200MessageOfficialDislikedByUserType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                disliked_by_user_type_0 = (
                    GetV4MachineWalkthroughsIdResponse200MessageOfficialDislikedByUserType0.from_dict(data)
                )

                return disliked_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineWalkthroughsIdResponse200MessageOfficialDislikedByUserType0 | None | Unset, data)

        disliked_by_user = _parse_disliked_by_user(d.pop("dislikedByUser", UNSET))

        total_ratings = d.pop("total_ratings", UNSET)

        threshold_for_display_reached = d.pop("threshold_for_display_reached", UNSET)

        filename = d.pop("filename", UNSET)

        sha256 = d.pop("sha256", UNSET)

        get_v4_machine_walkthroughs_id_response_200_message_official = cls(
            rating=rating,
            liked_by_user=liked_by_user,
            disliked_by_user=disliked_by_user,
            total_ratings=total_ratings,
            threshold_for_display_reached=threshold_for_display_reached,
            filename=filename,
            sha256=sha256,
        )

        get_v4_machine_walkthroughs_id_response_200_message_official.additional_properties = d
        return get_v4_machine_walkthroughs_id_response_200_message_official

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
