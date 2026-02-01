from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups import (
        GetV5SubscriptionsPricingResponse200ProductGroups,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200")


@_attrs_define
class GetV5SubscriptionsPricingResponse200:
    """
    Attributes:
        default_currency (str | Unset):
        product_groups (GetV5SubscriptionsPricingResponse200ProductGroups | Unset):
    """

    default_currency: str | Unset = UNSET
    product_groups: GetV5SubscriptionsPricingResponse200ProductGroups | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_currency = self.default_currency

        product_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_groups, Unset):
            product_groups = self.product_groups.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_currency is not UNSET:
            field_dict["default_currency"] = default_currency
        if product_groups is not UNSET:
            field_dict["product_groups"] = product_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups import (
            GetV5SubscriptionsPricingResponse200ProductGroups,
        )

        d = dict(src_dict)
        default_currency = d.pop("default_currency", UNSET)

        _product_groups = d.pop("product_groups", UNSET)
        product_groups: GetV5SubscriptionsPricingResponse200ProductGroups | Unset
        if isinstance(_product_groups, Unset):
            product_groups = UNSET
        else:
            product_groups = GetV5SubscriptionsPricingResponse200ProductGroups.from_dict(_product_groups)

        get_v5_subscriptions_pricing_response_200 = cls(
            default_currency=default_currency,
            product_groups=product_groups,
        )

        get_v5_subscriptions_pricing_response_200.additional_properties = d
        return get_v5_subscriptions_pricing_response_200

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
