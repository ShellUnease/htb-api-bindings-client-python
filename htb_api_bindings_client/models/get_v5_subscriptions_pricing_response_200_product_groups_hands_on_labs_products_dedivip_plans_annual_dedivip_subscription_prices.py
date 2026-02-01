from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription_prices_eur import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesEUR,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription_prices_gbp import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesGBP,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription_prices_usd import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesUSD,
    )


T = TypeVar(
    "T",
    bound="GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPrices",
)


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPrices:
    """
    Attributes:
        eur (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPr
            icesEUR | Unset):
        gbp (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPr
            icesGBP | Unset):
        usd (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPr
            icesUSD | Unset):
    """

    eur: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesEUR
        | Unset
    ) = UNSET
    gbp: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesGBP
        | Unset
    ) = UNSET
    usd: (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesUSD
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eur: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eur, Unset):
            eur = self.eur.to_dict()

        gbp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gbp, Unset):
            gbp = self.gbp.to_dict()

        usd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usd, Unset):
            usd = self.usd.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eur is not UNSET:
            field_dict["EUR"] = eur
        if gbp is not UNSET:
            field_dict["GBP"] = gbp
        if usd is not UNSET:
            field_dict["USD"] = usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription_prices_eur import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesEUR,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription_prices_gbp import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesGBP,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription_prices_usd import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesUSD,
        )

        d = dict(src_dict)
        _eur = d.pop("EUR", UNSET)
        eur: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesEUR
            | Unset
        )
        if isinstance(_eur, Unset):
            eur = UNSET
        else:
            eur = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesEUR.from_dict(
                _eur
            )

        _gbp = d.pop("GBP", UNSET)
        gbp: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesGBP
            | Unset
        )
        if isinstance(_gbp, Unset):
            gbp = UNSET
        else:
            gbp = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesGBP.from_dict(
                _gbp
            )

        _usd = d.pop("USD", UNSET)
        usd: (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesUSD
            | Unset
        )
        if isinstance(_usd, Unset):
            usd = UNSET
        else:
            usd = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlansAnnualDedivipSubscriptionPricesUSD.from_dict(
                _usd
            )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription_prices = cls(
            eur=eur,
            gbp=gbp,
            usd=usd,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription_prices.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans_annual_dedivip_subscription_prices

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
