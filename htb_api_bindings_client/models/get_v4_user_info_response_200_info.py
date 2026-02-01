from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_user_info_response_200_info_avatar_type_0 import GetV4UserInfoResponse200InfoAvatarType0
    from ..models.get_v4_user_info_response_200_info_subscription_plan_type_0 import (
        GetV4UserInfoResponse200InfoSubscriptionPlanType0,
    )
    from ..models.get_v4_user_info_response_200_info_team_type_0 import GetV4UserInfoResponse200InfoTeamType0
    from ..models.get_v4_user_info_response_200_info_university_type_0 import (
        GetV4UserInfoResponse200InfoUniversityType0,
    )


T = TypeVar("T", bound="GetV4UserInfoResponse200Info")


@_attrs_define
class GetV4UserInfoResponse200Info:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        email (str | Unset):
        timezone (str | Unset):
        is_vip (bool | Unset):
        is_moderator (bool | Unset):
        is_bg_moderator (bool | Unset):
        is_chat_banned (bool | Unset):
        is_dedicated_vip (bool | Unset):
        subscription_type (str | Unset):
        can_access_vip (bool | Unset):
        can_access_dedilab (bool | Unset):
        is_server_vip (bool | Unset):
        server_id (float | Unset):
        avatar (GetV4UserInfoResponse200InfoAvatarType0 | None | Unset):
        beta_tester (float | Unset):
        rank_id (float | Unset):
        onboarding_tutorial_complete (float | Unset):
        verified (bool | Unset):
        can_delete_avatar (bool | Unset):
        team (GetV4UserInfoResponse200InfoTeamType0 | None | Unset):
        university (GetV4UserInfoResponse200InfoUniversityType0 | None | Unset):
        identifier (str | Unset):
        has_team_invitation (bool | Unset):
        has_app_tokens (bool | Unset):
        opt_in (float | Unset):
        is_sso_connected (bool | Unset):
        has_reviewed_platform (bool | Unset):
        account_id (str | Unset):
        subscription_plan (GetV4UserInfoResponse200InfoSubscriptionPlanType0 | None | Unset):
        dunning_exists (bool | Unset):
        currency (str | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    timezone: str | Unset = UNSET
    is_vip: bool | Unset = UNSET
    is_moderator: bool | Unset = UNSET
    is_bg_moderator: bool | Unset = UNSET
    is_chat_banned: bool | Unset = UNSET
    is_dedicated_vip: bool | Unset = UNSET
    subscription_type: str | Unset = UNSET
    can_access_vip: bool | Unset = UNSET
    can_access_dedilab: bool | Unset = UNSET
    is_server_vip: bool | Unset = UNSET
    server_id: float | Unset = UNSET
    avatar: GetV4UserInfoResponse200InfoAvatarType0 | None | Unset = UNSET
    beta_tester: float | Unset = UNSET
    rank_id: float | Unset = UNSET
    onboarding_tutorial_complete: float | Unset = UNSET
    verified: bool | Unset = UNSET
    can_delete_avatar: bool | Unset = UNSET
    team: GetV4UserInfoResponse200InfoTeamType0 | None | Unset = UNSET
    university: GetV4UserInfoResponse200InfoUniversityType0 | None | Unset = UNSET
    identifier: str | Unset = UNSET
    has_team_invitation: bool | Unset = UNSET
    has_app_tokens: bool | Unset = UNSET
    opt_in: float | Unset = UNSET
    is_sso_connected: bool | Unset = UNSET
    has_reviewed_platform: bool | Unset = UNSET
    account_id: str | Unset = UNSET
    subscription_plan: GetV4UserInfoResponse200InfoSubscriptionPlanType0 | None | Unset = UNSET
    dunning_exists: bool | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_user_info_response_200_info_avatar_type_0 import GetV4UserInfoResponse200InfoAvatarType0
        from ..models.get_v4_user_info_response_200_info_subscription_plan_type_0 import (
            GetV4UserInfoResponse200InfoSubscriptionPlanType0,
        )
        from ..models.get_v4_user_info_response_200_info_team_type_0 import GetV4UserInfoResponse200InfoTeamType0
        from ..models.get_v4_user_info_response_200_info_university_type_0 import (
            GetV4UserInfoResponse200InfoUniversityType0,
        )

        id = self.id

        name = self.name

        email = self.email

        timezone = self.timezone

        is_vip = self.is_vip

        is_moderator = self.is_moderator

        is_bg_moderator = self.is_bg_moderator

        is_chat_banned = self.is_chat_banned

        is_dedicated_vip = self.is_dedicated_vip

        subscription_type = self.subscription_type

        can_access_vip = self.can_access_vip

        can_access_dedilab = self.can_access_dedilab

        is_server_vip = self.is_server_vip

        server_id = self.server_id

        avatar: dict[str, Any] | None | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        elif isinstance(self.avatar, GetV4UserInfoResponse200InfoAvatarType0):
            avatar = self.avatar.to_dict()
        else:
            avatar = self.avatar

        beta_tester = self.beta_tester

        rank_id = self.rank_id

        onboarding_tutorial_complete = self.onboarding_tutorial_complete

        verified = self.verified

        can_delete_avatar = self.can_delete_avatar

        team: dict[str, Any] | None | Unset
        if isinstance(self.team, Unset):
            team = UNSET
        elif isinstance(self.team, GetV4UserInfoResponse200InfoTeamType0):
            team = self.team.to_dict()
        else:
            team = self.team

        university: dict[str, Any] | None | Unset
        if isinstance(self.university, Unset):
            university = UNSET
        elif isinstance(self.university, GetV4UserInfoResponse200InfoUniversityType0):
            university = self.university.to_dict()
        else:
            university = self.university

        identifier = self.identifier

        has_team_invitation = self.has_team_invitation

        has_app_tokens = self.has_app_tokens

        opt_in = self.opt_in

        is_sso_connected = self.is_sso_connected

        has_reviewed_platform = self.has_reviewed_platform

        account_id = self.account_id

        subscription_plan: dict[str, Any] | None | Unset
        if isinstance(self.subscription_plan, Unset):
            subscription_plan = UNSET
        elif isinstance(self.subscription_plan, GetV4UserInfoResponse200InfoSubscriptionPlanType0):
            subscription_plan = self.subscription_plan.to_dict()
        else:
            subscription_plan = self.subscription_plan

        dunning_exists = self.dunning_exists

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if is_vip is not UNSET:
            field_dict["isVip"] = is_vip
        if is_moderator is not UNSET:
            field_dict["isModerator"] = is_moderator
        if is_bg_moderator is not UNSET:
            field_dict["isBGModerator"] = is_bg_moderator
        if is_chat_banned is not UNSET:
            field_dict["isChatBanned"] = is_chat_banned
        if is_dedicated_vip is not UNSET:
            field_dict["isDedicatedVip"] = is_dedicated_vip
        if subscription_type is not UNSET:
            field_dict["subscriptionType"] = subscription_type
        if can_access_vip is not UNSET:
            field_dict["canAccessVIP"] = can_access_vip
        if can_access_dedilab is not UNSET:
            field_dict["canAccessDedilab"] = can_access_dedilab
        if is_server_vip is not UNSET:
            field_dict["isServerVIP"] = is_server_vip
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if beta_tester is not UNSET:
            field_dict["beta_tester"] = beta_tester
        if rank_id is not UNSET:
            field_dict["rank_id"] = rank_id
        if onboarding_tutorial_complete is not UNSET:
            field_dict["onboarding_tutorial_complete"] = onboarding_tutorial_complete
        if verified is not UNSET:
            field_dict["verified"] = verified
        if can_delete_avatar is not UNSET:
            field_dict["can_delete_avatar"] = can_delete_avatar
        if team is not UNSET:
            field_dict["team"] = team
        if university is not UNSET:
            field_dict["university"] = university
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if has_team_invitation is not UNSET:
            field_dict["hasTeamInvitation"] = has_team_invitation
        if has_app_tokens is not UNSET:
            field_dict["hasAppTokens"] = has_app_tokens
        if opt_in is not UNSET:
            field_dict["opt_in"] = opt_in
        if is_sso_connected is not UNSET:
            field_dict["is_sso_connected"] = is_sso_connected
        if has_reviewed_platform is not UNSET:
            field_dict["hasReviewedPlatform"] = has_reviewed_platform
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if subscription_plan is not UNSET:
            field_dict["subscription_plan"] = subscription_plan
        if dunning_exists is not UNSET:
            field_dict["dunning_exists"] = dunning_exists
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_user_info_response_200_info_avatar_type_0 import GetV4UserInfoResponse200InfoAvatarType0
        from ..models.get_v4_user_info_response_200_info_subscription_plan_type_0 import (
            GetV4UserInfoResponse200InfoSubscriptionPlanType0,
        )
        from ..models.get_v4_user_info_response_200_info_team_type_0 import GetV4UserInfoResponse200InfoTeamType0
        from ..models.get_v4_user_info_response_200_info_university_type_0 import (
            GetV4UserInfoResponse200InfoUniversityType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        timezone = d.pop("timezone", UNSET)

        is_vip = d.pop("isVip", UNSET)

        is_moderator = d.pop("isModerator", UNSET)

        is_bg_moderator = d.pop("isBGModerator", UNSET)

        is_chat_banned = d.pop("isChatBanned", UNSET)

        is_dedicated_vip = d.pop("isDedicatedVip", UNSET)

        subscription_type = d.pop("subscriptionType", UNSET)

        can_access_vip = d.pop("canAccessVIP", UNSET)

        can_access_dedilab = d.pop("canAccessDedilab", UNSET)

        is_server_vip = d.pop("isServerVIP", UNSET)

        server_id = d.pop("server_id", UNSET)

        def _parse_avatar(data: object) -> GetV4UserInfoResponse200InfoAvatarType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                avatar_type_0 = GetV4UserInfoResponse200InfoAvatarType0.from_dict(data)

                return avatar_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserInfoResponse200InfoAvatarType0 | None | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        beta_tester = d.pop("beta_tester", UNSET)

        rank_id = d.pop("rank_id", UNSET)

        onboarding_tutorial_complete = d.pop("onboarding_tutorial_complete", UNSET)

        verified = d.pop("verified", UNSET)

        can_delete_avatar = d.pop("can_delete_avatar", UNSET)

        def _parse_team(data: object) -> GetV4UserInfoResponse200InfoTeamType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_0 = GetV4UserInfoResponse200InfoTeamType0.from_dict(data)

                return team_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserInfoResponse200InfoTeamType0 | None | Unset, data)

        team = _parse_team(d.pop("team", UNSET))

        def _parse_university(data: object) -> GetV4UserInfoResponse200InfoUniversityType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                university_type_0 = GetV4UserInfoResponse200InfoUniversityType0.from_dict(data)

                return university_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserInfoResponse200InfoUniversityType0 | None | Unset, data)

        university = _parse_university(d.pop("university", UNSET))

        identifier = d.pop("identifier", UNSET)

        has_team_invitation = d.pop("hasTeamInvitation", UNSET)

        has_app_tokens = d.pop("hasAppTokens", UNSET)

        opt_in = d.pop("opt_in", UNSET)

        is_sso_connected = d.pop("is_sso_connected", UNSET)

        has_reviewed_platform = d.pop("hasReviewedPlatform", UNSET)

        account_id = d.pop("account_id", UNSET)

        def _parse_subscription_plan(data: object) -> GetV4UserInfoResponse200InfoSubscriptionPlanType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscription_plan_type_0 = GetV4UserInfoResponse200InfoSubscriptionPlanType0.from_dict(data)

                return subscription_plan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserInfoResponse200InfoSubscriptionPlanType0 | None | Unset, data)

        subscription_plan = _parse_subscription_plan(d.pop("subscription_plan", UNSET))

        dunning_exists = d.pop("dunning_exists", UNSET)

        currency = d.pop("currency", UNSET)

        get_v4_user_info_response_200_info = cls(
            id=id,
            name=name,
            email=email,
            timezone=timezone,
            is_vip=is_vip,
            is_moderator=is_moderator,
            is_bg_moderator=is_bg_moderator,
            is_chat_banned=is_chat_banned,
            is_dedicated_vip=is_dedicated_vip,
            subscription_type=subscription_type,
            can_access_vip=can_access_vip,
            can_access_dedilab=can_access_dedilab,
            is_server_vip=is_server_vip,
            server_id=server_id,
            avatar=avatar,
            beta_tester=beta_tester,
            rank_id=rank_id,
            onboarding_tutorial_complete=onboarding_tutorial_complete,
            verified=verified,
            can_delete_avatar=can_delete_avatar,
            team=team,
            university=university,
            identifier=identifier,
            has_team_invitation=has_team_invitation,
            has_app_tokens=has_app_tokens,
            opt_in=opt_in,
            is_sso_connected=is_sso_connected,
            has_reviewed_platform=has_reviewed_platform,
            account_id=account_id,
            subscription_plan=subscription_plan,
            dunning_exists=dunning_exists,
            currency=currency,
        )

        get_v4_user_info_response_200_info.additional_properties = d
        return get_v4_user_info_response_200_info

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
