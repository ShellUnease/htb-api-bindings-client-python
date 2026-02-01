from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivip,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFree,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProducts")


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProducts:
    """
    Attributes:
        dedivip (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivip | Unset):
        free (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFree | Unset):
    """

    dedivip: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivip | Unset = UNSET
    free: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFree | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dedivip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dedivip, Unset):
            dedivip = self.dedivip.to_dict()

        free: dict[str, Any] | Unset = UNSET
        if not isinstance(self.free, Unset):
            free = self.free.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dedivip is not UNSET:
            field_dict["dedivip"] = dedivip
        if free is not UNSET:
            field_dict["free"] = free

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_dedivip import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivip,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products_free import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFree,
        )

        d = dict(src_dict)
        _dedivip = d.pop("dedivip", UNSET)
        dedivip: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivip | Unset
        if isinstance(_dedivip, Unset):
            dedivip = UNSET
        else:
            dedivip = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsDedivip.from_dict(_dedivip)

        _free = d.pop("free", UNSET)
        free: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFree | Unset
        if isinstance(_free, Unset):
            free = UNSET
        else:
            free = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProductsFree.from_dict(_free)

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products = cls(
            dedivip=dedivip,
            free=free,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products

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
