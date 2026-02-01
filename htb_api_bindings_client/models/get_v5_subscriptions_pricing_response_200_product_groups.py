from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabs,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs import (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabs,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200ProductGroups")


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroups:
    """
    Attributes:
        hands_on_labs (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabs | Unset):
        pro_labs (GetV5SubscriptionsPricingResponse200ProductGroupsProLabs | Unset):
    """

    hands_on_labs: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabs | Unset = UNSET
    pro_labs: GetV5SubscriptionsPricingResponse200ProductGroupsProLabs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hands_on_labs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hands_on_labs, Unset):
            hands_on_labs = self.hands_on_labs.to_dict()

        pro_labs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pro_labs, Unset):
            pro_labs = self.pro_labs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hands_on_labs is not UNSET:
            field_dict["hands-on-labs"] = hands_on_labs
        if pro_labs is not UNSET:
            field_dict["pro-labs"] = pro_labs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabs,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabs,
        )

        d = dict(src_dict)
        _hands_on_labs = d.pop("hands-on-labs", UNSET)
        hands_on_labs: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabs | Unset
        if isinstance(_hands_on_labs, Unset):
            hands_on_labs = UNSET
        else:
            hands_on_labs = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabs.from_dict(_hands_on_labs)

        _pro_labs = d.pop("pro-labs", UNSET)
        pro_labs: GetV5SubscriptionsPricingResponse200ProductGroupsProLabs | Unset
        if isinstance(_pro_labs, Unset):
            pro_labs = UNSET
        else:
            pro_labs = GetV5SubscriptionsPricingResponse200ProductGroupsProLabs.from_dict(_pro_labs)

        get_v5_subscriptions_pricing_response_200_product_groups = cls(
            hands_on_labs=hands_on_labs,
            pro_labs=pro_labs,
        )

        get_v5_subscriptions_pricing_response_200_product_groups.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups

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
