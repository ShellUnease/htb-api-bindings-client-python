from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_profile_id_response_200_info_auth_user_first_root_time_type_0 import (
        GetV4MachineProfileIdResponse200InfoAuthUserFirstRootTimeType0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_auth_user_first_user_time_type_0 import (
        GetV4MachineProfileIdResponse200InfoAuthUserFirstUserTimeType0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_feedback_for_chart import (
        GetV4MachineProfileIdResponse200InfoFeedbackForChart,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_info_status_type_0 import (
        GetV4MachineProfileIdResponse200InfoInfoStatusType0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_ip_type_0 import (
        GetV4MachineProfileIdResponse200InfoIpType0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_machine_pwned_date_type_0 import (
        GetV4MachineProfileIdResponse200InfoMachinePwnedDateType0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_maker import GetV4MachineProfileIdResponse200InfoMaker
    from ..models.get_v4_machine_profile_id_response_200_info_maker_2_type_0 import (
        GetV4MachineProfileIdResponse200InfoMaker2Type0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_own_rank_type_0 import (
        GetV4MachineProfileIdResponse200InfoOwnRankType0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_play_info import (
        GetV4MachineProfileIdResponse200InfoPlayInfo,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_required_subscription_type_0 import (
        GetV4MachineProfileIdResponse200InfoRequiredSubscriptionType0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_root_blood import (
        GetV4MachineProfileIdResponse200InfoRootBlood,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_switch_server_warning_type_0 import (
        GetV4MachineProfileIdResponse200InfoSwitchServerWarningType0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_synopsis_type_0 import (
        GetV4MachineProfileIdResponse200InfoSynopsisType0,
    )
    from ..models.get_v4_machine_profile_id_response_200_info_user_blood import (
        GetV4MachineProfileIdResponse200InfoUserBlood,
    )


T = TypeVar("T", bound="GetV4MachineProfileIdResponse200Info")


@_attrs_define
class GetV4MachineProfileIdResponse200Info:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        os (str | Unset):
        active (bool | Unset):
        retired (bool | Unset):
        release (str | Unset):
        points (float | Unset):
        static_points (float | Unset):
        user_owns_count (float | Unset):
        root_owns_count (float | Unset):
        reviews_count (float | Unset):
        play_info (GetV4MachineProfileIdResponse200InfoPlayInfo | Unset):
        maker (GetV4MachineProfileIdResponse200InfoMaker | Unset):
        sp_flag (float | Unset):
        is_todo (bool | Unset):
        recommended (bool | Unset):
        ip (GetV4MachineProfileIdResponse200InfoIpType0 | None | Unset):
        free (bool | Unset):
        auth_user_in_user_owns (bool | Unset):
        auth_user_in_root_owns (bool | Unset):
        auth_user_has_reviewed (bool | Unset):
        auth_user_has_submitted_matrix (bool | Unset):
        stars (float | Unset):
        avatar (str | Unset):
        feedback_for_chart (GetV4MachineProfileIdResponse200InfoFeedbackForChart | Unset):
        difficulty_text (str | Unset):
        maker2 (GetV4MachineProfileIdResponse200InfoMaker2Type0 | None | Unset):
        info_status (GetV4MachineProfileIdResponse200InfoInfoStatusType0 | None | Unset):
        machine_pwned_date (GetV4MachineProfileIdResponse200InfoMachinePwnedDateType0 | None | Unset):
        auth_user_first_user_time (GetV4MachineProfileIdResponse200InfoAuthUserFirstUserTimeType0 | None | Unset):
        auth_user_first_root_time (GetV4MachineProfileIdResponse200InfoAuthUserFirstRootTimeType0 | None | Unset):
        user_can_review (bool | Unset):
        synopsis (GetV4MachineProfileIdResponse200InfoSynopsisType0 | None | Unset):
        can_access_walkthrough (bool | Unset):
        has_changelog (bool | Unset):
        user_blood (GetV4MachineProfileIdResponse200InfoUserBlood | Unset):
        root_blood (GetV4MachineProfileIdResponse200InfoRootBlood | Unset):
        season_id (float | Unset):
        is_guided_enabled (bool | Unset):
        start_mode (str | Unset):
        show_go_vip (bool | Unset):
        show_go_vip_server (bool | Unset):
        own_rank (GetV4MachineProfileIdResponse200InfoOwnRankType0 | None | Unset):
        academy_modules (list[Any] | Unset):
        machine_mode (str | Unset):
        price_tier (float | Unset):
        required_subscription (GetV4MachineProfileIdResponse200InfoRequiredSubscriptionType0 | None | Unset):
        switch_server_warning (GetV4MachineProfileIdResponse200InfoSwitchServerWarningType0 | None | Unset):
        bot_has_blood (bool | Unset):
        is_single_flag (bool | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    os: str | Unset = UNSET
    active: bool | Unset = UNSET
    retired: bool | Unset = UNSET
    release: str | Unset = UNSET
    points: float | Unset = UNSET
    static_points: float | Unset = UNSET
    user_owns_count: float | Unset = UNSET
    root_owns_count: float | Unset = UNSET
    reviews_count: float | Unset = UNSET
    play_info: GetV4MachineProfileIdResponse200InfoPlayInfo | Unset = UNSET
    maker: GetV4MachineProfileIdResponse200InfoMaker | Unset = UNSET
    sp_flag: float | Unset = UNSET
    is_todo: bool | Unset = UNSET
    recommended: bool | Unset = UNSET
    ip: GetV4MachineProfileIdResponse200InfoIpType0 | None | Unset = UNSET
    free: bool | Unset = UNSET
    auth_user_in_user_owns: bool | Unset = UNSET
    auth_user_in_root_owns: bool | Unset = UNSET
    auth_user_has_reviewed: bool | Unset = UNSET
    auth_user_has_submitted_matrix: bool | Unset = UNSET
    stars: float | Unset = UNSET
    avatar: str | Unset = UNSET
    feedback_for_chart: GetV4MachineProfileIdResponse200InfoFeedbackForChart | Unset = UNSET
    difficulty_text: str | Unset = UNSET
    maker2: GetV4MachineProfileIdResponse200InfoMaker2Type0 | None | Unset = UNSET
    info_status: GetV4MachineProfileIdResponse200InfoInfoStatusType0 | None | Unset = UNSET
    machine_pwned_date: GetV4MachineProfileIdResponse200InfoMachinePwnedDateType0 | None | Unset = UNSET
    auth_user_first_user_time: GetV4MachineProfileIdResponse200InfoAuthUserFirstUserTimeType0 | None | Unset = UNSET
    auth_user_first_root_time: GetV4MachineProfileIdResponse200InfoAuthUserFirstRootTimeType0 | None | Unset = UNSET
    user_can_review: bool | Unset = UNSET
    synopsis: GetV4MachineProfileIdResponse200InfoSynopsisType0 | None | Unset = UNSET
    can_access_walkthrough: bool | Unset = UNSET
    has_changelog: bool | Unset = UNSET
    user_blood: GetV4MachineProfileIdResponse200InfoUserBlood | Unset = UNSET
    root_blood: GetV4MachineProfileIdResponse200InfoRootBlood | Unset = UNSET
    season_id: float | Unset = UNSET
    is_guided_enabled: bool | Unset = UNSET
    start_mode: str | Unset = UNSET
    show_go_vip: bool | Unset = UNSET
    show_go_vip_server: bool | Unset = UNSET
    own_rank: GetV4MachineProfileIdResponse200InfoOwnRankType0 | None | Unset = UNSET
    academy_modules: list[Any] | Unset = UNSET
    machine_mode: str | Unset = UNSET
    price_tier: float | Unset = UNSET
    required_subscription: GetV4MachineProfileIdResponse200InfoRequiredSubscriptionType0 | None | Unset = UNSET
    switch_server_warning: GetV4MachineProfileIdResponse200InfoSwitchServerWarningType0 | None | Unset = UNSET
    bot_has_blood: bool | Unset = UNSET
    is_single_flag: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machine_profile_id_response_200_info_auth_user_first_root_time_type_0 import (
            GetV4MachineProfileIdResponse200InfoAuthUserFirstRootTimeType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_auth_user_first_user_time_type_0 import (
            GetV4MachineProfileIdResponse200InfoAuthUserFirstUserTimeType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_info_status_type_0 import (
            GetV4MachineProfileIdResponse200InfoInfoStatusType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_ip_type_0 import (
            GetV4MachineProfileIdResponse200InfoIpType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_machine_pwned_date_type_0 import (
            GetV4MachineProfileIdResponse200InfoMachinePwnedDateType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_maker_2_type_0 import (
            GetV4MachineProfileIdResponse200InfoMaker2Type0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_own_rank_type_0 import (
            GetV4MachineProfileIdResponse200InfoOwnRankType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_required_subscription_type_0 import (
            GetV4MachineProfileIdResponse200InfoRequiredSubscriptionType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_switch_server_warning_type_0 import (
            GetV4MachineProfileIdResponse200InfoSwitchServerWarningType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_synopsis_type_0 import (
            GetV4MachineProfileIdResponse200InfoSynopsisType0,
        )

        id = self.id

        name = self.name

        os = self.os

        active = self.active

        retired = self.retired

        release = self.release

        points = self.points

        static_points = self.static_points

        user_owns_count = self.user_owns_count

        root_owns_count = self.root_owns_count

        reviews_count = self.reviews_count

        play_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.play_info, Unset):
            play_info = self.play_info.to_dict()

        maker: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maker, Unset):
            maker = self.maker.to_dict()

        sp_flag = self.sp_flag

        is_todo = self.is_todo

        recommended = self.recommended

        ip: dict[str, Any] | None | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        elif isinstance(self.ip, GetV4MachineProfileIdResponse200InfoIpType0):
            ip = self.ip.to_dict()
        else:
            ip = self.ip

        free = self.free

        auth_user_in_user_owns = self.auth_user_in_user_owns

        auth_user_in_root_owns = self.auth_user_in_root_owns

        auth_user_has_reviewed = self.auth_user_has_reviewed

        auth_user_has_submitted_matrix = self.auth_user_has_submitted_matrix

        stars = self.stars

        avatar = self.avatar

        feedback_for_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feedback_for_chart, Unset):
            feedback_for_chart = self.feedback_for_chart.to_dict()

        difficulty_text = self.difficulty_text

        maker2: dict[str, Any] | None | Unset
        if isinstance(self.maker2, Unset):
            maker2 = UNSET
        elif isinstance(self.maker2, GetV4MachineProfileIdResponse200InfoMaker2Type0):
            maker2 = self.maker2.to_dict()
        else:
            maker2 = self.maker2

        info_status: dict[str, Any] | None | Unset
        if isinstance(self.info_status, Unset):
            info_status = UNSET
        elif isinstance(self.info_status, GetV4MachineProfileIdResponse200InfoInfoStatusType0):
            info_status = self.info_status.to_dict()
        else:
            info_status = self.info_status

        machine_pwned_date: dict[str, Any] | None | Unset
        if isinstance(self.machine_pwned_date, Unset):
            machine_pwned_date = UNSET
        elif isinstance(self.machine_pwned_date, GetV4MachineProfileIdResponse200InfoMachinePwnedDateType0):
            machine_pwned_date = self.machine_pwned_date.to_dict()
        else:
            machine_pwned_date = self.machine_pwned_date

        auth_user_first_user_time: dict[str, Any] | None | Unset
        if isinstance(self.auth_user_first_user_time, Unset):
            auth_user_first_user_time = UNSET
        elif isinstance(self.auth_user_first_user_time, GetV4MachineProfileIdResponse200InfoAuthUserFirstUserTimeType0):
            auth_user_first_user_time = self.auth_user_first_user_time.to_dict()
        else:
            auth_user_first_user_time = self.auth_user_first_user_time

        auth_user_first_root_time: dict[str, Any] | None | Unset
        if isinstance(self.auth_user_first_root_time, Unset):
            auth_user_first_root_time = UNSET
        elif isinstance(self.auth_user_first_root_time, GetV4MachineProfileIdResponse200InfoAuthUserFirstRootTimeType0):
            auth_user_first_root_time = self.auth_user_first_root_time.to_dict()
        else:
            auth_user_first_root_time = self.auth_user_first_root_time

        user_can_review = self.user_can_review

        synopsis: dict[str, Any] | None | Unset
        if isinstance(self.synopsis, Unset):
            synopsis = UNSET
        elif isinstance(self.synopsis, GetV4MachineProfileIdResponse200InfoSynopsisType0):
            synopsis = self.synopsis.to_dict()
        else:
            synopsis = self.synopsis

        can_access_walkthrough = self.can_access_walkthrough

        has_changelog = self.has_changelog

        user_blood: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_blood, Unset):
            user_blood = self.user_blood.to_dict()

        root_blood: dict[str, Any] | Unset = UNSET
        if not isinstance(self.root_blood, Unset):
            root_blood = self.root_blood.to_dict()

        season_id = self.season_id

        is_guided_enabled = self.is_guided_enabled

        start_mode = self.start_mode

        show_go_vip = self.show_go_vip

        show_go_vip_server = self.show_go_vip_server

        own_rank: dict[str, Any] | None | Unset
        if isinstance(self.own_rank, Unset):
            own_rank = UNSET
        elif isinstance(self.own_rank, GetV4MachineProfileIdResponse200InfoOwnRankType0):
            own_rank = self.own_rank.to_dict()
        else:
            own_rank = self.own_rank

        academy_modules: list[Any] | Unset = UNSET
        if not isinstance(self.academy_modules, Unset):
            academy_modules = self.academy_modules

        machine_mode = self.machine_mode

        price_tier = self.price_tier

        required_subscription: dict[str, Any] | None | Unset
        if isinstance(self.required_subscription, Unset):
            required_subscription = UNSET
        elif isinstance(self.required_subscription, GetV4MachineProfileIdResponse200InfoRequiredSubscriptionType0):
            required_subscription = self.required_subscription.to_dict()
        else:
            required_subscription = self.required_subscription

        switch_server_warning: dict[str, Any] | None | Unset
        if isinstance(self.switch_server_warning, Unset):
            switch_server_warning = UNSET
        elif isinstance(self.switch_server_warning, GetV4MachineProfileIdResponse200InfoSwitchServerWarningType0):
            switch_server_warning = self.switch_server_warning.to_dict()
        else:
            switch_server_warning = self.switch_server_warning

        bot_has_blood = self.bot_has_blood

        is_single_flag = self.is_single_flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if active is not UNSET:
            field_dict["active"] = active
        if retired is not UNSET:
            field_dict["retired"] = retired
        if release is not UNSET:
            field_dict["release"] = release
        if points is not UNSET:
            field_dict["points"] = points
        if static_points is not UNSET:
            field_dict["static_points"] = static_points
        if user_owns_count is not UNSET:
            field_dict["user_owns_count"] = user_owns_count
        if root_owns_count is not UNSET:
            field_dict["root_owns_count"] = root_owns_count
        if reviews_count is not UNSET:
            field_dict["reviews_count"] = reviews_count
        if play_info is not UNSET:
            field_dict["playInfo"] = play_info
        if maker is not UNSET:
            field_dict["maker"] = maker
        if sp_flag is not UNSET:
            field_dict["sp_flag"] = sp_flag
        if is_todo is not UNSET:
            field_dict["isTodo"] = is_todo
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if ip is not UNSET:
            field_dict["ip"] = ip
        if free is not UNSET:
            field_dict["free"] = free
        if auth_user_in_user_owns is not UNSET:
            field_dict["authUserInUserOwns"] = auth_user_in_user_owns
        if auth_user_in_root_owns is not UNSET:
            field_dict["authUserInRootOwns"] = auth_user_in_root_owns
        if auth_user_has_reviewed is not UNSET:
            field_dict["authUserHasReviewed"] = auth_user_has_reviewed
        if auth_user_has_submitted_matrix is not UNSET:
            field_dict["authUserHasSubmittedMatrix"] = auth_user_has_submitted_matrix
        if stars is not UNSET:
            field_dict["stars"] = stars
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if feedback_for_chart is not UNSET:
            field_dict["feedbackForChart"] = feedback_for_chart
        if difficulty_text is not UNSET:
            field_dict["difficultyText"] = difficulty_text
        if maker2 is not UNSET:
            field_dict["maker2"] = maker2
        if info_status is not UNSET:
            field_dict["info_status"] = info_status
        if machine_pwned_date is not UNSET:
            field_dict["machinePwnedDate"] = machine_pwned_date
        if auth_user_first_user_time is not UNSET:
            field_dict["authUserFirstUserTime"] = auth_user_first_user_time
        if auth_user_first_root_time is not UNSET:
            field_dict["authUserFirstRootTime"] = auth_user_first_root_time
        if user_can_review is not UNSET:
            field_dict["user_can_review"] = user_can_review
        if synopsis is not UNSET:
            field_dict["synopsis"] = synopsis
        if can_access_walkthrough is not UNSET:
            field_dict["can_access_walkthrough"] = can_access_walkthrough
        if has_changelog is not UNSET:
            field_dict["has_changelog"] = has_changelog
        if user_blood is not UNSET:
            field_dict["userBlood"] = user_blood
        if root_blood is not UNSET:
            field_dict["rootBlood"] = root_blood
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if is_guided_enabled is not UNSET:
            field_dict["isGuidedEnabled"] = is_guided_enabled
        if start_mode is not UNSET:
            field_dict["start_mode"] = start_mode
        if show_go_vip is not UNSET:
            field_dict["show_go_vip"] = show_go_vip
        if show_go_vip_server is not UNSET:
            field_dict["show_go_vip_server"] = show_go_vip_server
        if own_rank is not UNSET:
            field_dict["ownRank"] = own_rank
        if academy_modules is not UNSET:
            field_dict["academy_modules"] = academy_modules
        if machine_mode is not UNSET:
            field_dict["machine_mode"] = machine_mode
        if price_tier is not UNSET:
            field_dict["priceTier"] = price_tier
        if required_subscription is not UNSET:
            field_dict["requiredSubscription"] = required_subscription
        if switch_server_warning is not UNSET:
            field_dict["switchServerWarning"] = switch_server_warning
        if bot_has_blood is not UNSET:
            field_dict["botHasBlood"] = bot_has_blood
        if is_single_flag is not UNSET:
            field_dict["isSingleFlag"] = is_single_flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_profile_id_response_200_info_auth_user_first_root_time_type_0 import (
            GetV4MachineProfileIdResponse200InfoAuthUserFirstRootTimeType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_auth_user_first_user_time_type_0 import (
            GetV4MachineProfileIdResponse200InfoAuthUserFirstUserTimeType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_feedback_for_chart import (
            GetV4MachineProfileIdResponse200InfoFeedbackForChart,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_info_status_type_0 import (
            GetV4MachineProfileIdResponse200InfoInfoStatusType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_ip_type_0 import (
            GetV4MachineProfileIdResponse200InfoIpType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_machine_pwned_date_type_0 import (
            GetV4MachineProfileIdResponse200InfoMachinePwnedDateType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_maker import GetV4MachineProfileIdResponse200InfoMaker
        from ..models.get_v4_machine_profile_id_response_200_info_maker_2_type_0 import (
            GetV4MachineProfileIdResponse200InfoMaker2Type0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_own_rank_type_0 import (
            GetV4MachineProfileIdResponse200InfoOwnRankType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_play_info import (
            GetV4MachineProfileIdResponse200InfoPlayInfo,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_required_subscription_type_0 import (
            GetV4MachineProfileIdResponse200InfoRequiredSubscriptionType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_root_blood import (
            GetV4MachineProfileIdResponse200InfoRootBlood,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_switch_server_warning_type_0 import (
            GetV4MachineProfileIdResponse200InfoSwitchServerWarningType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_synopsis_type_0 import (
            GetV4MachineProfileIdResponse200InfoSynopsisType0,
        )
        from ..models.get_v4_machine_profile_id_response_200_info_user_blood import (
            GetV4MachineProfileIdResponse200InfoUserBlood,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        active = d.pop("active", UNSET)

        retired = d.pop("retired", UNSET)

        release = d.pop("release", UNSET)

        points = d.pop("points", UNSET)

        static_points = d.pop("static_points", UNSET)

        user_owns_count = d.pop("user_owns_count", UNSET)

        root_owns_count = d.pop("root_owns_count", UNSET)

        reviews_count = d.pop("reviews_count", UNSET)

        _play_info = d.pop("playInfo", UNSET)
        play_info: GetV4MachineProfileIdResponse200InfoPlayInfo | Unset
        if isinstance(_play_info, Unset):
            play_info = UNSET
        else:
            play_info = GetV4MachineProfileIdResponse200InfoPlayInfo.from_dict(_play_info)

        _maker = d.pop("maker", UNSET)
        maker: GetV4MachineProfileIdResponse200InfoMaker | Unset
        if isinstance(_maker, Unset):
            maker = UNSET
        else:
            maker = GetV4MachineProfileIdResponse200InfoMaker.from_dict(_maker)

        sp_flag = d.pop("sp_flag", UNSET)

        is_todo = d.pop("isTodo", UNSET)

        recommended = d.pop("recommended", UNSET)

        def _parse_ip(data: object) -> GetV4MachineProfileIdResponse200InfoIpType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ip_type_0 = GetV4MachineProfileIdResponse200InfoIpType0.from_dict(data)

                return ip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoIpType0 | None | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        free = d.pop("free", UNSET)

        auth_user_in_user_owns = d.pop("authUserInUserOwns", UNSET)

        auth_user_in_root_owns = d.pop("authUserInRootOwns", UNSET)

        auth_user_has_reviewed = d.pop("authUserHasReviewed", UNSET)

        auth_user_has_submitted_matrix = d.pop("authUserHasSubmittedMatrix", UNSET)

        stars = d.pop("stars", UNSET)

        avatar = d.pop("avatar", UNSET)

        _feedback_for_chart = d.pop("feedbackForChart", UNSET)
        feedback_for_chart: GetV4MachineProfileIdResponse200InfoFeedbackForChart | Unset
        if isinstance(_feedback_for_chart, Unset):
            feedback_for_chart = UNSET
        else:
            feedback_for_chart = GetV4MachineProfileIdResponse200InfoFeedbackForChart.from_dict(_feedback_for_chart)

        difficulty_text = d.pop("difficultyText", UNSET)

        def _parse_maker2(data: object) -> GetV4MachineProfileIdResponse200InfoMaker2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                maker2_type_0 = GetV4MachineProfileIdResponse200InfoMaker2Type0.from_dict(data)

                return maker2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoMaker2Type0 | None | Unset, data)

        maker2 = _parse_maker2(d.pop("maker2", UNSET))

        def _parse_info_status(data: object) -> GetV4MachineProfileIdResponse200InfoInfoStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                info_status_type_0 = GetV4MachineProfileIdResponse200InfoInfoStatusType0.from_dict(data)

                return info_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoInfoStatusType0 | None | Unset, data)

        info_status = _parse_info_status(d.pop("info_status", UNSET))

        def _parse_machine_pwned_date(
            data: object,
        ) -> GetV4MachineProfileIdResponse200InfoMachinePwnedDateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                machine_pwned_date_type_0 = GetV4MachineProfileIdResponse200InfoMachinePwnedDateType0.from_dict(data)

                return machine_pwned_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoMachinePwnedDateType0 | None | Unset, data)

        machine_pwned_date = _parse_machine_pwned_date(d.pop("machinePwnedDate", UNSET))

        def _parse_auth_user_first_user_time(
            data: object,
        ) -> GetV4MachineProfileIdResponse200InfoAuthUserFirstUserTimeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_user_first_user_time_type_0 = (
                    GetV4MachineProfileIdResponse200InfoAuthUserFirstUserTimeType0.from_dict(data)
                )

                return auth_user_first_user_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoAuthUserFirstUserTimeType0 | None | Unset, data)

        auth_user_first_user_time = _parse_auth_user_first_user_time(d.pop("authUserFirstUserTime", UNSET))

        def _parse_auth_user_first_root_time(
            data: object,
        ) -> GetV4MachineProfileIdResponse200InfoAuthUserFirstRootTimeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_user_first_root_time_type_0 = (
                    GetV4MachineProfileIdResponse200InfoAuthUserFirstRootTimeType0.from_dict(data)
                )

                return auth_user_first_root_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoAuthUserFirstRootTimeType0 | None | Unset, data)

        auth_user_first_root_time = _parse_auth_user_first_root_time(d.pop("authUserFirstRootTime", UNSET))

        user_can_review = d.pop("user_can_review", UNSET)

        def _parse_synopsis(data: object) -> GetV4MachineProfileIdResponse200InfoSynopsisType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                synopsis_type_0 = GetV4MachineProfileIdResponse200InfoSynopsisType0.from_dict(data)

                return synopsis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoSynopsisType0 | None | Unset, data)

        synopsis = _parse_synopsis(d.pop("synopsis", UNSET))

        can_access_walkthrough = d.pop("can_access_walkthrough", UNSET)

        has_changelog = d.pop("has_changelog", UNSET)

        _user_blood = d.pop("userBlood", UNSET)
        user_blood: GetV4MachineProfileIdResponse200InfoUserBlood | Unset
        if isinstance(_user_blood, Unset):
            user_blood = UNSET
        else:
            user_blood = GetV4MachineProfileIdResponse200InfoUserBlood.from_dict(_user_blood)

        _root_blood = d.pop("rootBlood", UNSET)
        root_blood: GetV4MachineProfileIdResponse200InfoRootBlood | Unset
        if isinstance(_root_blood, Unset):
            root_blood = UNSET
        else:
            root_blood = GetV4MachineProfileIdResponse200InfoRootBlood.from_dict(_root_blood)

        season_id = d.pop("season_id", UNSET)

        is_guided_enabled = d.pop("isGuidedEnabled", UNSET)

        start_mode = d.pop("start_mode", UNSET)

        show_go_vip = d.pop("show_go_vip", UNSET)

        show_go_vip_server = d.pop("show_go_vip_server", UNSET)

        def _parse_own_rank(data: object) -> GetV4MachineProfileIdResponse200InfoOwnRankType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                own_rank_type_0 = GetV4MachineProfileIdResponse200InfoOwnRankType0.from_dict(data)

                return own_rank_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoOwnRankType0 | None | Unset, data)

        own_rank = _parse_own_rank(d.pop("ownRank", UNSET))

        academy_modules = cast(list[Any], d.pop("academy_modules", UNSET))

        machine_mode = d.pop("machine_mode", UNSET)

        price_tier = d.pop("priceTier", UNSET)

        def _parse_required_subscription(
            data: object,
        ) -> GetV4MachineProfileIdResponse200InfoRequiredSubscriptionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                required_subscription_type_0 = GetV4MachineProfileIdResponse200InfoRequiredSubscriptionType0.from_dict(
                    data
                )

                return required_subscription_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoRequiredSubscriptionType0 | None | Unset, data)

        required_subscription = _parse_required_subscription(d.pop("requiredSubscription", UNSET))

        def _parse_switch_server_warning(
            data: object,
        ) -> GetV4MachineProfileIdResponse200InfoSwitchServerWarningType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                switch_server_warning_type_0 = GetV4MachineProfileIdResponse200InfoSwitchServerWarningType0.from_dict(
                    data
                )

                return switch_server_warning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineProfileIdResponse200InfoSwitchServerWarningType0 | None | Unset, data)

        switch_server_warning = _parse_switch_server_warning(d.pop("switchServerWarning", UNSET))

        bot_has_blood = d.pop("botHasBlood", UNSET)

        is_single_flag = d.pop("isSingleFlag", UNSET)

        get_v4_machine_profile_id_response_200_info = cls(
            id=id,
            name=name,
            os=os,
            active=active,
            retired=retired,
            release=release,
            points=points,
            static_points=static_points,
            user_owns_count=user_owns_count,
            root_owns_count=root_owns_count,
            reviews_count=reviews_count,
            play_info=play_info,
            maker=maker,
            sp_flag=sp_flag,
            is_todo=is_todo,
            recommended=recommended,
            ip=ip,
            free=free,
            auth_user_in_user_owns=auth_user_in_user_owns,
            auth_user_in_root_owns=auth_user_in_root_owns,
            auth_user_has_reviewed=auth_user_has_reviewed,
            auth_user_has_submitted_matrix=auth_user_has_submitted_matrix,
            stars=stars,
            avatar=avatar,
            feedback_for_chart=feedback_for_chart,
            difficulty_text=difficulty_text,
            maker2=maker2,
            info_status=info_status,
            machine_pwned_date=machine_pwned_date,
            auth_user_first_user_time=auth_user_first_user_time,
            auth_user_first_root_time=auth_user_first_root_time,
            user_can_review=user_can_review,
            synopsis=synopsis,
            can_access_walkthrough=can_access_walkthrough,
            has_changelog=has_changelog,
            user_blood=user_blood,
            root_blood=root_blood,
            season_id=season_id,
            is_guided_enabled=is_guided_enabled,
            start_mode=start_mode,
            show_go_vip=show_go_vip,
            show_go_vip_server=show_go_vip_server,
            own_rank=own_rank,
            academy_modules=academy_modules,
            machine_mode=machine_mode,
            price_tier=price_tier,
            required_subscription=required_subscription,
            switch_server_warning=switch_server_warning,
            bot_has_blood=bot_has_blood,
            is_single_flag=is_single_flag,
        )

        get_v4_machine_profile_id_response_200_info.additional_properties = d
        return get_v4_machine_profile_id_response_200_info

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
