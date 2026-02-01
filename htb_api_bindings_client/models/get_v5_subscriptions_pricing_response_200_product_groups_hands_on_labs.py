from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products import (
        GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProducts,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabs")


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabs:
    """
    Attributes:
        name (str | Unset):
        products (GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProducts | Unset):
    """

    name: str | Unset = UNSET
    products: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProducts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        products: dict[str, Any] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = self.products.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs_products import (
            GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProducts,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _products = d.pop("products", UNSET)
        products: GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProducts | Unset
        if isinstance(_products, Unset):
            products = UNSET
        else:
            products = GetV5SubscriptionsPricingResponse200ProductGroupsHandsOnLabsProducts.from_dict(_products)

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs = cls(
            name=name,
            products=products,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_hands_on_labs

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
