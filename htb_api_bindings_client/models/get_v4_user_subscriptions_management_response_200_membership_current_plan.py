from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_user_subscriptions_management_response_200_membership_current_plan_pricing_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanPricingType0,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_current_plan_recurly_plan_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanRecurlyPlanType0,
    )


T = TypeVar("T", bound="GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlan")


@_attrs_define
class GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlan:
    """
    Attributes:
        name (str | Unset):
        recurly_plan (GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanRecurlyPlanType0 | None | Unset):
        type_ (str | Unset):
        pricing (GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanPricingType0 | None | Unset):
    """

    name: str | Unset = UNSET
    recurly_plan: GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanRecurlyPlanType0 | None | Unset = (
        UNSET
    )
    type_: str | Unset = UNSET
    pricing: GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanPricingType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_user_subscriptions_management_response_200_membership_current_plan_pricing_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanPricingType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_current_plan_recurly_plan_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanRecurlyPlanType0,
        )

        name = self.name

        recurly_plan: dict[str, Any] | None | Unset
        if isinstance(self.recurly_plan, Unset):
            recurly_plan = UNSET
        elif isinstance(
            self.recurly_plan, GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanRecurlyPlanType0
        ):
            recurly_plan = self.recurly_plan.to_dict()
        else:
            recurly_plan = self.recurly_plan

        type_ = self.type_

        pricing: dict[str, Any] | None | Unset
        if isinstance(self.pricing, Unset):
            pricing = UNSET
        elif isinstance(self.pricing, GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanPricingType0):
            pricing = self.pricing.to_dict()
        else:
            pricing = self.pricing

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
        from ..models.get_v4_user_subscriptions_management_response_200_membership_current_plan_pricing_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanPricingType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_current_plan_recurly_plan_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanRecurlyPlanType0,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_recurly_plan(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanRecurlyPlanType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recurly_plan_type_0 = (
                    GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanRecurlyPlanType0.from_dict(data)
                )

                return recurly_plan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanRecurlyPlanType0 | None | Unset, data
            )

        recurly_plan = _parse_recurly_plan(d.pop("recurlyPlan", UNSET))

        type_ = d.pop("type", UNSET)

        def _parse_pricing(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanPricingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pricing_type_0 = GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanPricingType0.from_dict(
                    data
                )

                return pricing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlanPricingType0 | None | Unset, data
            )

        pricing = _parse_pricing(d.pop("pricing", UNSET))

        get_v4_user_subscriptions_management_response_200_membership_current_plan = cls(
            name=name,
            recurly_plan=recurly_plan,
            type_=type_,
            pricing=pricing,
        )

        get_v4_user_subscriptions_management_response_200_membership_current_plan.additional_properties = d
        return get_v4_user_subscriptions_management_response_200_membership_current_plan

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
