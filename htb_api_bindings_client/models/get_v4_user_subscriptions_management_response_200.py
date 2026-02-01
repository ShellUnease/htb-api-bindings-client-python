from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_user_subscriptions_management_response_200_membership import (
        GetV4UserSubscriptionsManagementResponse200Membership,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_prolabs import (
        GetV4UserSubscriptionsManagementResponse200Prolabs,
    )


T = TypeVar("T", bound="GetV4UserSubscriptionsManagementResponse200")


@_attrs_define
class GetV4UserSubscriptionsManagementResponse200:
    """
    Attributes:
        membership (GetV4UserSubscriptionsManagementResponse200Membership | Unset):
        prolabs (GetV4UserSubscriptionsManagementResponse200Prolabs | Unset):
    """

    membership: GetV4UserSubscriptionsManagementResponse200Membership | Unset = UNSET
    prolabs: GetV4UserSubscriptionsManagementResponse200Prolabs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        membership: dict[str, Any] | Unset = UNSET
        if not isinstance(self.membership, Unset):
            membership = self.membership.to_dict()

        prolabs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prolabs, Unset):
            prolabs = self.prolabs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if membership is not UNSET:
            field_dict["membership"] = membership
        if prolabs is not UNSET:
            field_dict["prolabs"] = prolabs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_user_subscriptions_management_response_200_membership import (
            GetV4UserSubscriptionsManagementResponse200Membership,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_prolabs import (
            GetV4UserSubscriptionsManagementResponse200Prolabs,
        )

        d = dict(src_dict)
        _membership = d.pop("membership", UNSET)
        membership: GetV4UserSubscriptionsManagementResponse200Membership | Unset
        if isinstance(_membership, Unset):
            membership = UNSET
        else:
            membership = GetV4UserSubscriptionsManagementResponse200Membership.from_dict(_membership)

        _prolabs = d.pop("prolabs", UNSET)
        prolabs: GetV4UserSubscriptionsManagementResponse200Prolabs | Unset
        if isinstance(_prolabs, Unset):
            prolabs = UNSET
        else:
            prolabs = GetV4UserSubscriptionsManagementResponse200Prolabs.from_dict(_prolabs)

        get_v4_user_subscriptions_management_response_200 = cls(
            membership=membership,
            prolabs=prolabs,
        )

        get_v4_user_subscriptions_management_response_200.additional_properties = d
        return get_v4_user_subscriptions_management_response_200

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
