from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscription,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_monthly_dedivip_subscription import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansMonthlyDedivipSubscription,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlans")


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlans:
    """
    Attributes:
        monthly_dedivip_subscription
            (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansMonthlyDedivipSubscription |
            Unset):
        annual_dedivip_subscription
            (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscription |
            Unset):
    """

    monthly_dedivip_subscription: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansMonthlyDedivipSubscription
        | Unset
    ) = UNSET
    annual_dedivip_subscription: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscription
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_dedivip_subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly_dedivip_subscription, Unset):
            monthly_dedivip_subscription = self.monthly_dedivip_subscription.to_dict()

        annual_dedivip_subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annual_dedivip_subscription, Unset):
            annual_dedivip_subscription = self.annual_dedivip_subscription.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monthly_dedivip_subscription is not UNSET:
            field_dict["monthly-dedivip-subscription"] = monthly_dedivip_subscription
        if annual_dedivip_subscription is not UNSET:
            field_dict["annual-dedivip-subscription"] = annual_dedivip_subscription

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscription,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_monthly_dedivip_subscription import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansMonthlyDedivipSubscription,
        )

        d = dict(src_dict)
        _monthly_dedivip_subscription = d.pop("monthly-dedivip-subscription", UNSET)
        monthly_dedivip_subscription: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansMonthlyDedivipSubscription
            | Unset
        )
        if isinstance(_monthly_dedivip_subscription, Unset):
            monthly_dedivip_subscription = UNSET
        else:
            monthly_dedivip_subscription = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansMonthlyDedivipSubscription.from_dict(
                _monthly_dedivip_subscription
            )

        _annual_dedivip_subscription = d.pop("annual-dedivip-subscription", UNSET)
        annual_dedivip_subscription: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscription
            | Unset
        )
        if isinstance(_annual_dedivip_subscription, Unset):
            annual_dedivip_subscription = UNSET
        else:
            annual_dedivip_subscription = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscription.from_dict(
                _annual_dedivip_subscription
            )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans = cls(
            monthly_dedivip_subscription=monthly_dedivip_subscription,
            annual_dedivip_subscription=annual_dedivip_subscription,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans

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
