from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_annual_prolabs_subscription import (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansAnnualProlabsSubscription,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription import (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscription,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlans")


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlans:
    """
    Attributes:
        monthly_prolabs_subscription
            (GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscription |
            Unset):
        annual_prolabs_subscription
            (GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansAnnualProlabsSubscription | Unset):
    """

    monthly_prolabs_subscription: (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscription | Unset
    ) = UNSET
    annual_prolabs_subscription: (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansAnnualProlabsSubscription | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_prolabs_subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly_prolabs_subscription, Unset):
            monthly_prolabs_subscription = self.monthly_prolabs_subscription.to_dict()

        annual_prolabs_subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annual_prolabs_subscription, Unset):
            annual_prolabs_subscription = self.annual_prolabs_subscription.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monthly_prolabs_subscription is not UNSET:
            field_dict["monthly-prolabs-subscription"] = monthly_prolabs_subscription
        if annual_prolabs_subscription is not UNSET:
            field_dict["annual-prolabs-subscription"] = annual_prolabs_subscription

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_annual_prolabs_subscription import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansAnnualProlabsSubscription,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscription,
        )

        d = dict(src_dict)
        _monthly_prolabs_subscription = d.pop("monthly-prolabs-subscription", UNSET)
        monthly_prolabs_subscription: (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscription
            | Unset
        )
        if isinstance(_monthly_prolabs_subscription, Unset):
            monthly_prolabs_subscription = UNSET
        else:
            monthly_prolabs_subscription = GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscription.from_dict(
                _monthly_prolabs_subscription
            )

        _annual_prolabs_subscription = d.pop("annual-prolabs-subscription", UNSET)
        annual_prolabs_subscription: (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansAnnualProlabsSubscription
            | Unset
        )
        if isinstance(_annual_prolabs_subscription, Unset):
            annual_prolabs_subscription = UNSET
        else:
            annual_prolabs_subscription = GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansAnnualProlabsSubscription.from_dict(
                _annual_prolabs_subscription
            )

        get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans = cls(
            monthly_prolabs_subscription=monthly_prolabs_subscription,
            annual_prolabs_subscription=annual_prolabs_subscription,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans

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
