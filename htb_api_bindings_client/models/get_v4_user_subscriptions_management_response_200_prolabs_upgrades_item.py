from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_user_subscriptions_management_response_200_prolabs_upgrades_item_pricing import (
        GetV4UserSubscriptionsManagementResponse200ProlabsUpgradesItemPricing,
    )


T = TypeVar("T", bound="GetV4UserSubscriptionsManagementResponse200ProlabsUpgradesItem")


@_attrs_define
class GetV4UserSubscriptionsManagementResponse200ProlabsUpgradesItem:
    """
    Attributes:
        name (str | Unset):
        recurly_plan (str | Unset):
        type_ (str | Unset):
        pricing (GetV4UserSubscriptionsManagementResponse200ProlabsUpgradesItemPricing | Unset):
    """

    name: str | Unset = UNSET
    recurly_plan: str | Unset = UNSET
    type_: str | Unset = UNSET
    pricing: GetV4UserSubscriptionsManagementResponse200ProlabsUpgradesItemPricing | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        recurly_plan = self.recurly_plan

        type_ = self.type_

        pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if recurly_plan is not UNSET:
            field_dict["recurlyPlan"] = recurly_plan
        if type_ is not UNSET:
            field_dict["type"] = type_
        if pricing is not UNSET:
            field_dict["pricing"] = pricing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_user_subscriptions_management_response_200_prolabs_upgrades_item_pricing import (
            GetV4UserSubscriptionsManagementResponse200ProlabsUpgradesItemPricing,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        recurly_plan = d.pop("recurlyPlan", UNSET)

        type_ = d.pop("type", UNSET)

        _pricing = d.pop("pricing", UNSET)
        pricing: GetV4UserSubscriptionsManagementResponse200ProlabsUpgradesItemPricing | Unset
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = GetV4UserSubscriptionsManagementResponse200ProlabsUpgradesItemPricing.from_dict(_pricing)

        get_v4_user_subscriptions_management_response_200_prolabs_upgrades_item = cls(
            name=name,
            recurly_plan=recurly_plan,
            type_=type_,
            pricing=pricing,
        )

        get_v4_user_subscriptions_management_response_200_prolabs_upgrades_item.additional_properties = d
        return get_v4_user_subscriptions_management_response_200_prolabs_upgrades_item

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
