from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_prolab_id_reviews_overview_response_200_data_feedbacks_item import (
        GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItem,
    )


T = TypeVar("T", bound="GetV4ProlabIdReviewsOverviewResponse200Data")


@_attrs_define
class GetV4ProlabIdReviewsOverviewResponse200Data:
    """
    Attributes:
        total_number_of_ratings (float | Unset):
        users_average_rating (float | Unset):
        feedbacks (list[GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItem] | Unset):
    """

    total_number_of_ratings: float | Unset = UNSET
    users_average_rating: float | Unset = UNSET
    feedbacks: list[GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_number_of_ratings = self.total_number_of_ratings

        users_average_rating = self.users_average_rating

        feedbacks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feedbacks, Unset):
            feedbacks = []
            for feedbacks_item_data in self.feedbacks:
                feedbacks_item = feedbacks_item_data.to_dict()
                feedbacks.append(feedbacks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_number_of_ratings is not UNSET:
            field_dict["total_number_of_ratings"] = total_number_of_ratings
        if users_average_rating is not UNSET:
            field_dict["users_average_rating"] = users_average_rating
        if feedbacks is not UNSET:
            field_dict["feedbacks"] = feedbacks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_prolab_id_reviews_overview_response_200_data_feedbacks_item import (
            GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItem,
        )

        d = dict(src_dict)
        total_number_of_ratings = d.pop("total_number_of_ratings", UNSET)

        users_average_rating = d.pop("users_average_rating", UNSET)

        _feedbacks = d.pop("feedbacks", UNSET)
        feedbacks: list[GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItem] | Unset = UNSET
        if _feedbacks is not UNSET:
            feedbacks = []
            for feedbacks_item_data in _feedbacks:
                feedbacks_item = GetV4ProlabIdReviewsOverviewResponse200DataFeedbacksItem.from_dict(feedbacks_item_data)

                feedbacks.append(feedbacks_item)

        get_v4_prolab_id_reviews_overview_response_200_data = cls(
            total_number_of_ratings=total_number_of_ratings,
            users_average_rating=users_average_rating,
            feedbacks=feedbacks,
        )

        get_v4_prolab_id_reviews_overview_response_200_data.additional_properties = d
        return get_v4_prolab_id_reviews_overview_response_200_data

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
