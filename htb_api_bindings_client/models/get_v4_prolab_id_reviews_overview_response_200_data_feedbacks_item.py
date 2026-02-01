from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_prolab_id_reviews_overview_response_200_data_feedbacks_item_user import (
        GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItemUser,
    )


T = TypeVar("T", bound="GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItem")


@_attrs_define
class GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItem:
    """
    Attributes:
        rating (float | Unset):
        text (str | Unset):
        user (GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItemUser | Unset):
    """

    rating: float | Unset = UNSET
    text: str | Unset = UNSET
    user: GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItemUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rating = self.rating

        text = self.text

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rating is not UNSET:
            field_dict["rating"] = rating
        if text is not UNSET:
            field_dict["text"] = text
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_prolab_id_reviews_overview_response_200_data_feedbacks_item_user import (
            GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItemUser,
        )

        d = dict(src_dict)
        rating = d.pop("rating", UNSET)

        text = d.pop("text", UNSET)

        _user = d.pop("user", UNSET)
        user: GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItemUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItemUser.from_dict(_user)

        get_v4_prolab_id_reviews_overview_response_200_data_feedbacks_item = cls(
            rating=rating,
            text=text,
            user=user,
        )

        get_v4_prolab_id_reviews_overview_response_200_data_feedbacks_item.additional_properties = d
        return get_v4_prolab_id_reviews_overview_response_200_data_feedbacks_item

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
