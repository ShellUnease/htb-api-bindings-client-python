from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_challenge_info_id_response_200_challenge import GetV4ChallengeInfoIdResponse200Challenge


T = TypeVar("T", bound="GetV4ChallengeInfoIdResponse200")


@_attrs_define
class GetV4ChallengeInfoIdResponse200:
    """
    Attributes:
        challenge (GetV4ChallengeInfoIdResponse200Challenge | Unset):
    """

    challenge: GetV4ChallengeInfoIdResponse200Challenge | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.challenge, Unset):
            challenge = self.challenge.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge is not UNSET:
            field_dict["challenge"] = challenge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_challenge_info_id_response_200_challenge import GetV4ChallengeInfoIdResponse200Challenge

        d = dict(src_dict)
        _challenge = d.pop("challenge", UNSET)
        challenge: GetV4ChallengeInfoIdResponse200Challenge | Unset
        if isinstance(_challenge, Unset):
            challenge = UNSET
        else:
            challenge = GetV4ChallengeInfoIdResponse200Challenge.from_dict(_challenge)

        get_v4_challenge_info_id_response_200 = cls(
            challenge=challenge,
        )

        get_v4_challenge_info_id_response_200.additional_properties = d
        return get_v4_challenge_info_id_response_200

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
