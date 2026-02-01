from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlans,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivip")


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivip:
    """
    Attributes:
        perks (str | Unset):
        plans (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlans | Unset):
        type_ (str | Unset):
        upgrades_to (list[Any] | Unset):
    """

    perks: str | Unset = UNSET
    plans: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlans | Unset = UNSET
    type_: str | Unset = UNSET
    upgrades_to: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        perks = self.perks

        plans: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plans, Unset):
            plans = self.plans.to_dict()

        type_ = self.type_

        upgrades_to: list[Any] | Unset = UNSET
        if not isinstance(self.upgrades_to, Unset):
            upgrades_to = self.upgrades_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if perks is not UNSET:
            field_dict["perks"] = perks
        if plans is not UNSET:
            field_dict["plans"] = plans
        if type_ is not UNSET:
            field_dict["type"] = type_
        if upgrades_to is not UNSET:
            field_dict["upgrades_to"] = upgrades_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip_plans import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlans,
        )

        d = dict(src_dict)
        perks = d.pop("perks", UNSET)

        _plans = d.pop("plans", UNSET)
        plans: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlans | Unset
        if isinstance(_plans, Unset):
            plans = UNSET
        else:
            plans = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivipPlans.from_dict(_plans)

        type_ = d.pop("type", UNSET)

        upgrades_to = cast(list[Any], d.pop("upgrades_to", UNSET))

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip = cls(
            perks=perks,
            plans=plans,
            type_=type_,
            upgrades_to=upgrades_to,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip

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
