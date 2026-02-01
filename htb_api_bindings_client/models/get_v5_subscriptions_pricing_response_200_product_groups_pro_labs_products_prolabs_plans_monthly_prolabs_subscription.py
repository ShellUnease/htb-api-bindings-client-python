from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription_prices import (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionPrices,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription_upgrades_to_type_0 import (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionUpgradesToType0,
    )


T = TypeVar(
    "T", bound="GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscription"
)


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscription:
    """
    Attributes:
        prices
            (GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionPrices |
            Unset):
        name (str | Unset):
        is_current_plan (bool | Unset):
        upgrades_to (GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscript
            ionUpgradesToType0 | None | Unset):
    """

    prices: (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionPrices
        | Unset
    ) = UNSET
    name: str | Unset = UNSET
    is_current_plan: bool | Unset = UNSET
    upgrades_to: (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionUpgradesToType0
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription_upgrades_to_type_0 import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionUpgradesToType0,
        )

        prices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prices, Unset):
            prices = self.prices.to_dict()

        name = self.name

        is_current_plan = self.is_current_plan

        upgrades_to: dict[str, Any] | None | Unset
        if isinstance(self.upgrades_to, Unset):
            upgrades_to = UNSET
        elif isinstance(
            self.upgrades_to,
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionUpgradesToType0,
        ):
            upgrades_to = self.upgrades_to.to_dict()
        else:
            upgrades_to = self.upgrades_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prices is not UNSET:
            field_dict["prices"] = prices
        if name is not UNSET:
            field_dict["name"] = name
        if is_current_plan is not UNSET:
            field_dict["is_current_plan"] = is_current_plan
        if upgrades_to is not UNSET:
            field_dict["upgrades_to"] = upgrades_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription_prices import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionPrices,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription_upgrades_to_type_0 import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionUpgradesToType0,
        )

        d = dict(src_dict)
        _prices = d.pop("prices", UNSET)
        prices: (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionPrices
            | Unset
        )
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionPrices.from_dict(
                _prices
            )

        name = d.pop("name", UNSET)

        is_current_plan = d.pop("is_current_plan", UNSET)

        def _parse_upgrades_to(
            data: object,
        ) -> (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionUpgradesToType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upgrades_to_type_0 = GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionUpgradesToType0.from_dict(
                    data
                )

                return upgrades_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabsPlansMonthlyProlabsSubscriptionUpgradesToType0
                | None
                | Unset,
                data,
            )

        upgrades_to = _parse_upgrades_to(d.pop("upgrades_to", UNSET))

        get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription = cls(
            prices=prices,
            name=name,
            is_current_plan=is_current_plan,
            upgrades_to=upgrades_to,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs_plans_monthly_prolabs_subscription

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
