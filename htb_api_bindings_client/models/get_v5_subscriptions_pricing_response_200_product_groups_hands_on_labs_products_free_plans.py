from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_annual_free_hands_on_plan import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansAnnualFreeHandsOnPlan,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlan,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlans")


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlans:
    """
    Attributes:
        annual_free_hands_on_plan
            (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansAnnualFreeHandsOnPlan | Unset):
        monthly_free_hands_on_plan
            (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlan | Unset):
    """

    annual_free_hands_on_plan: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansAnnualFreeHandsOnPlan | Unset
    ) = UNSET
    monthly_free_hands_on_plan: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlan | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annual_free_hands_on_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annual_free_hands_on_plan, Unset):
            annual_free_hands_on_plan = self.annual_free_hands_on_plan.to_dict()

        monthly_free_hands_on_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly_free_hands_on_plan, Unset):
            monthly_free_hands_on_plan = self.monthly_free_hands_on_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annual_free_hands_on_plan is not UNSET:
            field_dict["annual-free-hands-on-plan"] = annual_free_hands_on_plan
        if monthly_free_hands_on_plan is not UNSET:
            field_dict["monthly-free-hands-on-plan"] = monthly_free_hands_on_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_annual_free_hands_on_plan import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansAnnualFreeHandsOnPlan,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlan,
        )

        d = dict(src_dict)
        _annual_free_hands_on_plan = d.pop("annual-free-hands-on-plan", UNSET)
        annual_free_hands_on_plan: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansAnnualFreeHandsOnPlan | Unset
        )
        if isinstance(_annual_free_hands_on_plan, Unset):
            annual_free_hands_on_plan = UNSET
        else:
            annual_free_hands_on_plan = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansAnnualFreeHandsOnPlan.from_dict(
                _annual_free_hands_on_plan
            )

        _monthly_free_hands_on_plan = d.pop("monthly-free-hands-on-plan", UNSET)
        monthly_free_hands_on_plan: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlan | Unset
        )
        if isinstance(_monthly_free_hands_on_plan, Unset):
            monthly_free_hands_on_plan = UNSET
        else:
            monthly_free_hands_on_plan = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlan.from_dict(
                _monthly_free_hands_on_plan
            )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans = cls(
            annual_free_hands_on_plan=annual_free_hands_on_plan,
            monthly_free_hands_on_plan=monthly_free_hands_on_plan,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans

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
