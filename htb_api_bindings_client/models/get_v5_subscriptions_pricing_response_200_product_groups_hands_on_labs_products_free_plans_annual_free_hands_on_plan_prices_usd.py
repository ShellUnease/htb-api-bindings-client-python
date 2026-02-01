from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansAnnualFreeHandsOnPlanPricesUSD",
)


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansAnnualFreeHandsOnPlanPricesUSD:
    """
    Attributes:
        setup (float | Unset):
        per_period (float | Unset):
    """

    setup: float | Unset = UNSET
    per_period: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        setup = self.setup

        per_period = self.per_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if setup is not UNSET:
            field_dict["setup"] = setup
        if per_period is not UNSET:
            field_dict["per_period"] = per_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        setup = d.pop("setup", UNSET)

        per_period = d.pop("per_period", UNSET)

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_annual_free_hands_on_plan_prices_usd = cls(
            setup=setup,
            per_period=per_period,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_annual_free_hands_on_plan_prices_usd.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_annual_free_hands_on_plan_prices_usd

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
