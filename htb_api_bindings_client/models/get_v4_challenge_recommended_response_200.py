from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_challenge_recommended_response_200_card_1 import GetV4ChallengeRecommendedResponse200Card1
    from ..models.get_v4_challenge_recommended_response_200_card_2 import GetV4ChallengeRecommendedResponse200Card2


T = TypeVar("T", bound="GetV4ChallengeRecommendedResponse200")


@_attrs_define
class GetV4ChallengeRecommendedResponse200:
    """
    Attributes:
        state (list[str] | Unset):
        card1 (GetV4ChallengeRecommendedResponse200Card1 | Unset):
        card2 (GetV4ChallengeRecommendedResponse200Card2 | Unset):
    """

    state: list[str] | Unset = UNSET
    card1: GetV4ChallengeRecommendedResponse200Card1 | Unset = UNSET
    card2: GetV4ChallengeRecommendedResponse200Card2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: list[str] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        card1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card1, Unset):
            card1 = self.card1.to_dict()

        card2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card2, Unset):
            card2 = self.card2.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if card1 is not UNSET:
            field_dict["card1"] = card1
        if card2 is not UNSET:
            field_dict["card2"] = card2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_challenge_recommended_response_200_card_1 import GetV4ChallengeRecommendedResponse200Card1
        from ..models.get_v4_challenge_recommended_response_200_card_2 import GetV4ChallengeRecommendedResponse200Card2

        d = dict(src_dict)
        state = cast(list[str], d.pop("state", UNSET))

        _card1 = d.pop("card1", UNSET)
        card1: GetV4ChallengeRecommendedResponse200Card1 | Unset
        if isinstance(_card1, Unset):
            card1 = UNSET
        else:
            card1 = GetV4ChallengeRecommendedResponse200Card1.from_dict(_card1)

        _card2 = d.pop("card2", UNSET)
        card2: GetV4ChallengeRecommendedResponse200Card2 | Unset
        if isinstance(_card2, Unset):
            card2 = UNSET
        else:
            card2 = GetV4ChallengeRecommendedResponse200Card2.from_dict(_card2)

        get_v4_challenge_recommended_response_200 = cls(
            state=state,
            card1=card1,
            card2=card2,
        )

        get_v4_challenge_recommended_response_200.additional_properties = d
        return get_v4_challenge_recommended_response_200

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
