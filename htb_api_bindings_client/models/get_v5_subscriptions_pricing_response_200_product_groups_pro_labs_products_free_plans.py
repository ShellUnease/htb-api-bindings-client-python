from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_free_plans_annual_free_pro_lab_plan import (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansAnnualFreeProLabPlan,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_free_plans_monthly_free_pro_lab_plan import (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansMonthlyFreeProLabPlan,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlans")


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlans:
    """
    Attributes:
        annual_free_pro_lab_plan
            (GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansAnnualFreeProLabPlan | Unset):
        monthly_free_pro_lab_plan
            (GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansMonthlyFreeProLabPlan | Unset):
    """

    annual_free_pro_lab_plan: (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansAnnualFreeProLabPlan | Unset
    ) = UNSET
    monthly_free_pro_lab_plan: (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansMonthlyFreeProLabPlan | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annual_free_pro_lab_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annual_free_pro_lab_plan, Unset):
            annual_free_pro_lab_plan = self.annual_free_pro_lab_plan.to_dict()

        monthly_free_pro_lab_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly_free_pro_lab_plan, Unset):
            monthly_free_pro_lab_plan = self.monthly_free_pro_lab_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annual_free_pro_lab_plan is not UNSET:
            field_dict["annual-free-pro-lab-plan"] = annual_free_pro_lab_plan
        if monthly_free_pro_lab_plan is not UNSET:
            field_dict["monthly-free-pro-lab-plan"] = monthly_free_pro_lab_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_free_plans_annual_free_pro_lab_plan import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansAnnualFreeProLabPlan,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_free_plans_monthly_free_pro_lab_plan import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansMonthlyFreeProLabPlan,
        )

        d = dict(src_dict)
        _annual_free_pro_lab_plan = d.pop("annual-free-pro-lab-plan", UNSET)
        annual_free_pro_lab_plan: (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansAnnualFreeProLabPlan | Unset
        )
        if isinstance(_annual_free_pro_lab_plan, Unset):
            annual_free_pro_lab_plan = UNSET
        else:
            annual_free_pro_lab_plan = (
                GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansAnnualFreeProLabPlan.from_dict(
                    _annual_free_pro_lab_plan
                )
            )

        _monthly_free_pro_lab_plan = d.pop("monthly-free-pro-lab-plan", UNSET)
        monthly_free_pro_lab_plan: (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansMonthlyFreeProLabPlan | Unset
        )
        if isinstance(_monthly_free_pro_lab_plan, Unset):
            monthly_free_pro_lab_plan = UNSET
        else:
            monthly_free_pro_lab_plan = GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFreePlansMonthlyFreeProLabPlan.from_dict(
                _monthly_free_pro_lab_plan
            )

        get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_free_plans = cls(
            annual_free_pro_lab_plan=annual_free_pro_lab_plan,
            monthly_free_pro_lab_plan=monthly_free_pro_lab_plan,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_free_plans.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_free_plans

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
