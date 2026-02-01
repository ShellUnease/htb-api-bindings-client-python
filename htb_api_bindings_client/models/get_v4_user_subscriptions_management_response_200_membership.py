from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_user_subscriptions_management_response_200_membership_annual_upgrade_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipAnnualUpgradeType0,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_created_at_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipCreatedAtType0,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_current_plan import (
        GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlan,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_ends_at_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipEndsAtType0,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_interval_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipIntervalType0,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_paused_at_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipPausedAtType0,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_renews_at_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipRenewsAtType0,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_resume_at_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipResumeAtType0,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_state_type_0 import (
        GetV4UserSubscriptionsManagementResponse200MembershipStateType0,
    )
    from ..models.get_v4_user_subscriptions_management_response_200_membership_upgrades_item import (
        GetV4UserSubscriptionsManagementResponse200MembershipUpgradesItem,
    )


T = TypeVar("T", bound="GetV4UserSubscriptionsManagementResponse200Membership")


@_attrs_define
class GetV4UserSubscriptionsManagementResponse200Membership:
    """
    Attributes:
        current_plan (GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlan | Unset):
        upgrades (list[GetV4UserSubscriptionsManagementResponse200MembershipUpgradesItem] | Unset):
        annual_upgrade (GetV4UserSubscriptionsManagementResponse200MembershipAnnualUpgradeType0 | None | Unset):
        state (GetV4UserSubscriptionsManagementResponse200MembershipStateType0 | None | Unset):
        allowed_actions (list[str] | Unset):
        interval (GetV4UserSubscriptionsManagementResponse200MembershipIntervalType0 | None | Unset):
        created_at (GetV4UserSubscriptionsManagementResponse200MembershipCreatedAtType0 | None | Unset):
        ends_at (GetV4UserSubscriptionsManagementResponse200MembershipEndsAtType0 | None | Unset):
        renews_at (GetV4UserSubscriptionsManagementResponse200MembershipRenewsAtType0 | None | Unset):
        paused_at (GetV4UserSubscriptionsManagementResponse200MembershipPausedAtType0 | None | Unset):
        resume_at (GetV4UserSubscriptionsManagementResponse200MembershipResumeAtType0 | None | Unset):
    """

    current_plan: GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlan | Unset = UNSET
    upgrades: list[GetV4UserSubscriptionsManagementResponse200MembershipUpgradesItem] | Unset = UNSET
    annual_upgrade: GetV4UserSubscriptionsManagementResponse200MembershipAnnualUpgradeType0 | None | Unset = UNSET
    state: GetV4UserSubscriptionsManagementResponse200MembershipStateType0 | None | Unset = UNSET
    allowed_actions: list[str] | Unset = UNSET
    interval: GetV4UserSubscriptionsManagementResponse200MembershipIntervalType0 | None | Unset = UNSET
    created_at: GetV4UserSubscriptionsManagementResponse200MembershipCreatedAtType0 | None | Unset = UNSET
    ends_at: GetV4UserSubscriptionsManagementResponse200MembershipEndsAtType0 | None | Unset = UNSET
    renews_at: GetV4UserSubscriptionsManagementResponse200MembershipRenewsAtType0 | None | Unset = UNSET
    paused_at: GetV4UserSubscriptionsManagementResponse200MembershipPausedAtType0 | None | Unset = UNSET
    resume_at: GetV4UserSubscriptionsManagementResponse200MembershipResumeAtType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_user_subscriptions_management_response_200_membership_annual_upgrade_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipAnnualUpgradeType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_created_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipCreatedAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_ends_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipEndsAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_interval_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipIntervalType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_paused_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipPausedAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_renews_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipRenewsAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_resume_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipResumeAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_state_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipStateType0,
        )

        current_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_plan, Unset):
            current_plan = self.current_plan.to_dict()

        upgrades: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.upgrades, Unset):
            upgrades = []
            for upgrades_item_data in self.upgrades:
                upgrades_item = upgrades_item_data.to_dict()
                upgrades.append(upgrades_item)

        annual_upgrade: dict[str, Any] | None | Unset
        if isinstance(self.annual_upgrade, Unset):
            annual_upgrade = UNSET
        elif isinstance(self.annual_upgrade, GetV4UserSubscriptionsManagementResponse200MembershipAnnualUpgradeType0):
            annual_upgrade = self.annual_upgrade.to_dict()
        else:
            annual_upgrade = self.annual_upgrade

        state: dict[str, Any] | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, GetV4UserSubscriptionsManagementResponse200MembershipStateType0):
            state = self.state.to_dict()
        else:
            state = self.state

        allowed_actions: list[str] | Unset = UNSET
        if not isinstance(self.allowed_actions, Unset):
            allowed_actions = self.allowed_actions

        interval: dict[str, Any] | None | Unset
        if isinstance(self.interval, Unset):
            interval = UNSET
        elif isinstance(self.interval, GetV4UserSubscriptionsManagementResponse200MembershipIntervalType0):
            interval = self.interval.to_dict()
        else:
            interval = self.interval

        created_at: dict[str, Any] | None | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, GetV4UserSubscriptionsManagementResponse200MembershipCreatedAtType0):
            created_at = self.created_at.to_dict()
        else:
            created_at = self.created_at

        ends_at: dict[str, Any] | None | Unset
        if isinstance(self.ends_at, Unset):
            ends_at = UNSET
        elif isinstance(self.ends_at, GetV4UserSubscriptionsManagementResponse200MembershipEndsAtType0):
            ends_at = self.ends_at.to_dict()
        else:
            ends_at = self.ends_at

        renews_at: dict[str, Any] | None | Unset
        if isinstance(self.renews_at, Unset):
            renews_at = UNSET
        elif isinstance(self.renews_at, GetV4UserSubscriptionsManagementResponse200MembershipRenewsAtType0):
            renews_at = self.renews_at.to_dict()
        else:
            renews_at = self.renews_at

        paused_at: dict[str, Any] | None | Unset
        if isinstance(self.paused_at, Unset):
            paused_at = UNSET
        elif isinstance(self.paused_at, GetV4UserSubscriptionsManagementResponse200MembershipPausedAtType0):
            paused_at = self.paused_at.to_dict()
        else:
            paused_at = self.paused_at

        resume_at: dict[str, Any] | None | Unset
        if isinstance(self.resume_at, Unset):
            resume_at = UNSET
        elif isinstance(self.resume_at, GetV4UserSubscriptionsManagementResponse200MembershipResumeAtType0):
            resume_at = self.resume_at.to_dict()
        else:
            resume_at = self.resume_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_plan is not UNSET:
            field_dict["currentPlan"] = current_plan
        if upgrades is not UNSET:
            field_dict["upgrades"] = upgrades
        if annual_upgrade is not UNSET:
            field_dict["annualUpgrade"] = annual_upgrade
        if state is not UNSET:
            field_dict["state"] = state
        if allowed_actions is not UNSET:
            field_dict["allowedActions"] = allowed_actions
        if interval is not UNSET:
            field_dict["interval"] = interval
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at
        if renews_at is not UNSET:
            field_dict["renewsAt"] = renews_at
        if paused_at is not UNSET:
            field_dict["pausedAt"] = paused_at
        if resume_at is not UNSET:
            field_dict["resumeAt"] = resume_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_user_subscriptions_management_response_200_membership_annual_upgrade_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipAnnualUpgradeType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_created_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipCreatedAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_current_plan import (
            GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlan,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_ends_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipEndsAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_interval_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipIntervalType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_paused_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipPausedAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_renews_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipRenewsAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_resume_at_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipResumeAtType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_state_type_0 import (
            GetV4UserSubscriptionsManagementResponse200MembershipStateType0,
        )
        from ..models.get_v4_user_subscriptions_management_response_200_membership_upgrades_item import (
            GetV4UserSubscriptionsManagementResponse200MembershipUpgradesItem,
        )

        d = dict(src_dict)
        _current_plan = d.pop("currentPlan", UNSET)
        current_plan: GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlan | Unset
        if isinstance(_current_plan, Unset):
            current_plan = UNSET
        else:
            current_plan = GetV4UserSubscriptionsManagementResponse200MembershipCurrentPlan.from_dict(_current_plan)

        _upgrades = d.pop("upgrades", UNSET)
        upgrades: list[GetV4UserSubscriptionsManagementResponse200MembershipUpgradesItem] | Unset = UNSET
        if _upgrades is not UNSET:
            upgrades = []
            for upgrades_item_data in _upgrades:
                upgrades_item = GetV4UserSubscriptionsManagementResponse200MembershipUpgradesItem.from_dict(
                    upgrades_item_data
                )

                upgrades.append(upgrades_item)

        def _parse_annual_upgrade(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipAnnualUpgradeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                annual_upgrade_type_0 = (
                    GetV4UserSubscriptionsManagementResponse200MembershipAnnualUpgradeType0.from_dict(data)
                )

                return annual_upgrade_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserSubscriptionsManagementResponse200MembershipAnnualUpgradeType0 | None | Unset, data)

        annual_upgrade = _parse_annual_upgrade(d.pop("annualUpgrade", UNSET))

        def _parse_state(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipStateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_0 = GetV4UserSubscriptionsManagementResponse200MembershipStateType0.from_dict(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserSubscriptionsManagementResponse200MembershipStateType0 | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        allowed_actions = cast(list[str], d.pop("allowedActions", UNSET))

        def _parse_interval(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipIntervalType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                interval_type_0 = GetV4UserSubscriptionsManagementResponse200MembershipIntervalType0.from_dict(data)

                return interval_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserSubscriptionsManagementResponse200MembershipIntervalType0 | None | Unset, data)

        interval = _parse_interval(d.pop("interval", UNSET))

        def _parse_created_at(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipCreatedAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_at_type_0 = GetV4UserSubscriptionsManagementResponse200MembershipCreatedAtType0.from_dict(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserSubscriptionsManagementResponse200MembershipCreatedAtType0 | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_ends_at(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipEndsAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ends_at_type_0 = GetV4UserSubscriptionsManagementResponse200MembershipEndsAtType0.from_dict(data)

                return ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserSubscriptionsManagementResponse200MembershipEndsAtType0 | None | Unset, data)

        ends_at = _parse_ends_at(d.pop("endsAt", UNSET))

        def _parse_renews_at(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipRenewsAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                renews_at_type_0 = GetV4UserSubscriptionsManagementResponse200MembershipRenewsAtType0.from_dict(data)

                return renews_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserSubscriptionsManagementResponse200MembershipRenewsAtType0 | None | Unset, data)

        renews_at = _parse_renews_at(d.pop("renewsAt", UNSET))

        def _parse_paused_at(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipPausedAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                paused_at_type_0 = GetV4UserSubscriptionsManagementResponse200MembershipPausedAtType0.from_dict(data)

                return paused_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserSubscriptionsManagementResponse200MembershipPausedAtType0 | None | Unset, data)

        paused_at = _parse_paused_at(d.pop("pausedAt", UNSET))

        def _parse_resume_at(
            data: object,
        ) -> GetV4UserSubscriptionsManagementResponse200MembershipResumeAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resume_at_type_0 = GetV4UserSubscriptionsManagementResponse200MembershipResumeAtType0.from_dict(data)

                return resume_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserSubscriptionsManagementResponse200MembershipResumeAtType0 | None | Unset, data)

        resume_at = _parse_resume_at(d.pop("resumeAt", UNSET))

        get_v4_user_subscriptions_management_response_200_membership = cls(
            current_plan=current_plan,
            upgrades=upgrades,
            annual_upgrade=annual_upgrade,
            state=state,
            allowed_actions=allowed_actions,
            interval=interval,
            created_at=created_at,
            ends_at=ends_at,
            renews_at=renews_at,
            paused_at=paused_at,
            resume_at=resume_at,
        )

        get_v4_user_subscriptions_management_response_200_membership.additional_properties = d
        return get_v4_user_subscriptions_management_response_200_membership

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
