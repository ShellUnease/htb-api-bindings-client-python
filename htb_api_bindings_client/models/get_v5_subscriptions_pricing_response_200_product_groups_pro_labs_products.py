from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_free import (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFree,
    )
    from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs import (
        GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabs,
    )


T = TypeVar("T", bound="GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProducts")


@_attrs_define
class GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProducts:
    """
    Attributes:
        prolabs (GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabs | Unset):
        free (GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFree | Unset):
    """

    prolabs: GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabs | Unset = UNSET
    free: GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFree | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prolabs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prolabs, Unset):
            prolabs = self.prolabs.to_dict()

        free: dict[str, Any] | Unset = UNSET
        if not isinstance(self.free, Unset):
            free = self.free.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prolabs is not UNSET:
            field_dict["prolabs"] = prolabs
        if free is not UNSET:
            field_dict["free"] = free

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_free import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFree,
        )
        from ..models.get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products_prolabs import (
            GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabs,
        )

        d = dict(src_dict)
        _prolabs = d.pop("prolabs", UNSET)
        prolabs: GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabs | Unset
        if isinstance(_prolabs, Unset):
            prolabs = UNSET
        else:
            prolabs = GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsProlabs.from_dict(_prolabs)

        _free = d.pop("free", UNSET)
        free: GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFree | Unset
        if isinstance(_free, Unset):
            free = UNSET
        else:
            free = GetV5SubscriptionsPricingResponse200ProductGroupsProLabsProductsFree.from_dict(_free)

        get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products = cls(
            prolabs=prolabs,
            free=free,
        )

        get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products.additional_properties = d
        return get_v5_subscriptions_pricing_response_200_product_groups_pro_labs_products

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
