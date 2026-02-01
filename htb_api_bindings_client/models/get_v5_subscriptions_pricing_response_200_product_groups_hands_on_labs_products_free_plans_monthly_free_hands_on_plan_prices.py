from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan_prices_eur import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesEUR,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan_prices_gbp import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesGBP,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan_prices_usd import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesUSD,
    )


T = TypeVar(
    "T",
    bound="GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPrices",
)


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPrices:
    """
    Attributes:
        eur
            (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesEUR |
            Unset):
        usd
            (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesUSD |
            Unset):
        gbp
            (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesGBP |
            Unset):
    """

    eur: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesEUR
        | Unset
    ) = UNSET
    usd: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesUSD
        | Unset
    ) = UNSET
    gbp: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesGBP
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eur: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eur, Unset):
            eur = self.eur.to_dict()

        usd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usd, Unset):
            usd = self.usd.to_dict()

        gbp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gbp, Unset):
            gbp = self.gbp.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eur is not UNSET:
            field_dict["EUR"] = eur
        if usd is not UNSET:
            field_dict["USD"] = usd
        if gbp is not UNSET:
            field_dict["GBP"] = gbp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan_prices_eur import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesEUR,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan_prices_gbp import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesGBP,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan_prices_usd import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesUSD,
        )

        d = dict(src_dict)
        _eur = d.pop("EUR", UNSET)
        eur: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesEUR
            | Unset
        )
        if isinstance(_eur, Unset):
            eur = UNSET
        else:
            eur = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesEUR.from_dict(
                _eur
            )

        _usd = d.pop("USD", UNSET)
        usd: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesUSD
            | Unset
        )
        if isinstance(_usd, Unset):
            usd = UNSET
        else:
            usd = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesUSD.from_dict(
                _usd
            )

        _gbp = d.pop("GBP", UNSET)
        gbp: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesGBP
            | Unset
        )
        if isinstance(_gbp, Unset):
            gbp = UNSET
        else:
            gbp = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFreePlansMonthlyFreeHandsOnPlanPricesGBP.from_dict(
                _gbp
            )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan_prices = cls(
            eur=eur,
            usd=usd,
            gbp=gbp,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan_prices.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free_plans_monthly_free_hands_on_plan_prices

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
