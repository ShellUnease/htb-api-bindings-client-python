from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_machines_response_200_data_item_active_type_0 import (
        GetV5MachinesResponse200DataItemActiveType0,
    )
    from ..models.get_v5_machines_response_200_data_item_feedback_for_chart import (
        GetV5MachinesResponse200DataItemFeedbackForChart,
    )
    from ..models.get_v5_machines_response_200_data_item_first_creator import (
        GetV5MachinesResponse200DataItemFirstCreator,
    )
    from ..models.get_v5_machines_response_200_data_item_ip_type_0 import GetV5MachinesResponse200DataItemIpType0
    from ..models.get_v5_machines_response_200_data_item_labels_item import GetV5MachinesResponse200DataItemLabelsItem
    from ..models.get_v5_machines_response_200_data_item_play_info import GetV5MachinesResponse200DataItemPlayInfo
    from ..models.get_v5_machines_response_200_data_item_required_subscription_type_0 import (
        GetV5MachinesResponse200DataItemRequiredSubscriptionType0,
    )
    from ..models.get_v5_machines_response_200_data_item_retiring import GetV5MachinesResponse200DataItemRetiring


T = TypeVar("T", bound="GetV5MachinesResponse200DataItem")


@_attrs_define
class GetV5MachinesResponse200DataItem:
    """
    Attributes:
        id (float | Unset):
        avatar (str | Unset):
        name (str | Unset):
        os (str | Unset):
        points (float | Unset):
        rating (float | Unset):
        rating_count (float | Unset):
        release_date (str | Unset):
        retired_date (str | Unset):
        free (bool | Unset):
        difficulty (float | Unset):
        difficulty_text (str | Unset):
        user_owns_count (float | Unset):
        auth_user_in_user_owns (bool | Unset):
        root_owns_count (float | Unset):
        auth_user_has_reviewed (bool | Unset):
        auth_user_in_root_owns (bool | Unset):
        todo (bool | Unset):
        competitive (bool | Unset):
        active (GetV5MachinesResponse200DataItemActiveType0 | None | Unset):
        feedback_for_chart (GetV5MachinesResponse200DataItemFeedbackForChart | Unset):
        ip (GetV5MachinesResponse200DataItemIpType0 | None | Unset):
        play_info (GetV5MachinesResponse200DataItemPlayInfo | Unset):
        labels (list[GetV5MachinesResponse200DataItemLabelsItem] | Unset):
        recommended (bool | Unset):
        price_tier (float | Unset):
        required_subscription (GetV5MachinesResponse200DataItemRequiredSubscriptionType0 | None | Unset):
        first_creator (GetV5MachinesResponse200DataItemFirstCreator | Unset):
        cocreators (list[Any] | Unset):
        retiring (GetV5MachinesResponse200DataItemRetiring | Unset):
        state (str | Unset):
        task_completion_percentage (str | Unset):
        sp_flag (float | Unset):
        is_single_flag (bool | Unset):
    """

    id: float | Unset = UNSET
    avatar: str | Unset = UNSET
    name: str | Unset = UNSET
    os: str | Unset = UNSET
    points: float | Unset = UNSET
    rating: float | Unset = UNSET
    rating_count: float | Unset = UNSET
    release_date: str | Unset = UNSET
    retired_date: str | Unset = UNSET
    free: bool | Unset = UNSET
    difficulty: float | Unset = UNSET
    difficulty_text: str | Unset = UNSET
    user_owns_count: float | Unset = UNSET
    auth_user_in_user_owns: bool | Unset = UNSET
    root_owns_count: float | Unset = UNSET
    auth_user_has_reviewed: bool | Unset = UNSET
    auth_user_in_root_owns: bool | Unset = UNSET
    todo: bool | Unset = UNSET
    competitive: bool | Unset = UNSET
    active: GetV5MachinesResponse200DataItemActiveType0 | None | Unset = UNSET
    feedback_for_chart: GetV5MachinesResponse200DataItemFeedbackForChart | Unset = UNSET
    ip: GetV5MachinesResponse200DataItemIpType0 | None | Unset = UNSET
    play_info: GetV5MachinesResponse200DataItemPlayInfo | Unset = UNSET
    labels: list[GetV5MachinesResponse200DataItemLabelsItem] | Unset = UNSET
    recommended: bool | Unset = UNSET
    price_tier: float | Unset = UNSET
    required_subscription: GetV5MachinesResponse200DataItemRequiredSubscriptionType0 | None | Unset = UNSET
    first_creator: GetV5MachinesResponse200DataItemFirstCreator | Unset = UNSET
    cocreators: list[Any] | Unset = UNSET
    retiring: GetV5MachinesResponse200DataItemRetiring | Unset = UNSET
    state: str | Unset = UNSET
    task_completion_percentage: str | Unset = UNSET
    sp_flag: float | Unset = UNSET
    is_single_flag: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v5_machines_response_200_data_item_active_type_0 import (
            GetV5MachinesResponse200DataItemActiveType0,
        )
        from ..models.get_v5_machines_response_200_data_item_ip_type_0 import GetV5MachinesResponse200DataItemIpType0
        from ..models.get_v5_machines_response_200_data_item_required_subscription_type_0 import (
            GetV5MachinesResponse200DataItemRequiredSubscriptionType0,
        )

        id = self.id

        avatar = self.avatar

        name = self.name

        os = self.os

        points = self.points

        rating = self.rating

        rating_count = self.rating_count

        release_date = self.release_date

        retired_date = self.retired_date

        free = self.free

        difficulty = self.difficulty

        difficulty_text = self.difficulty_text

        user_owns_count = self.user_owns_count

        auth_user_in_user_owns = self.auth_user_in_user_owns

        root_owns_count = self.root_owns_count

        auth_user_has_reviewed = self.auth_user_has_reviewed

        auth_user_in_root_owns = self.auth_user_in_root_owns

        todo = self.todo

        competitive = self.competitive

        active: dict[str, Any] | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        elif isinstance(self.active, GetV5MachinesResponse200DataItemActiveType0):
            active = self.active.to_dict()
        else:
            active = self.active

        feedback_for_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feedback_for_chart, Unset):
            feedback_for_chart = self.feedback_for_chart.to_dict()

        ip: dict[str, Any] | None | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        elif isinstance(self.ip, GetV5MachinesResponse200DataItemIpType0):
            ip = self.ip.to_dict()
        else:
            ip = self.ip

        play_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.play_info, Unset):
            play_info = self.play_info.to_dict()

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        recommended = self.recommended

        price_tier = self.price_tier

        required_subscription: dict[str, Any] | None | Unset
        if isinstance(self.required_subscription, Unset):
            required_subscription = UNSET
        elif isinstance(self.required_subscription, GetV5MachinesResponse200DataItemRequiredSubscriptionType0):
            required_subscription = self.required_subscription.to_dict()
        else:
            required_subscription = self.required_subscription

        first_creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_creator, Unset):
            first_creator = self.first_creator.to_dict()

        cocreators: list[Any] | Unset = UNSET
        if not isinstance(self.cocreators, Unset):
            cocreators = self.cocreators

        retiring: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retiring, Unset):
            retiring = self.retiring.to_dict()

        state = self.state

        task_completion_percentage = self.task_completion_percentage

        sp_flag = self.sp_flag

        is_single_flag = self.is_single_flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if points is not UNSET:
            field_dict["points"] = points
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_count is not UNSET:
            field_dict["ratingCount"] = rating_count
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if retired_date is not UNSET:
            field_dict["retiredDate"] = retired_date
        if free is not UNSET:
            field_dict["free"] = free
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if difficulty_text is not UNSET:
            field_dict["difficultyText"] = difficulty_text
        if user_owns_count is not UNSET:
            field_dict["userOwnsCount"] = user_owns_count
        if auth_user_in_user_owns is not UNSET:
            field_dict["authUserInUserOwns"] = auth_user_in_user_owns
        if root_owns_count is not UNSET:
            field_dict["rootOwnsCount"] = root_owns_count
        if auth_user_has_reviewed is not UNSET:
            field_dict["authUserHasReviewed"] = auth_user_has_reviewed
        if auth_user_in_root_owns is not UNSET:
            field_dict["authUserInRootOwns"] = auth_user_in_root_owns
        if todo is not UNSET:
            field_dict["todo"] = todo
        if competitive is not UNSET:
            field_dict["competitive"] = competitive
        if active is not UNSET:
            field_dict["active"] = active
        if feedback_for_chart is not UNSET:
            field_dict["feedbackForChart"] = feedback_for_chart
        if ip is not UNSET:
            field_dict["ip"] = ip
        if play_info is not UNSET:
            field_dict["playInfo"] = play_info
        if labels is not UNSET:
            field_dict["labels"] = labels
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if price_tier is not UNSET:
            field_dict["priceTier"] = price_tier
        if required_subscription is not UNSET:
            field_dict["requiredSubscription"] = required_subscription
        if first_creator is not UNSET:
            field_dict["firstCreator"] = first_creator
        if cocreators is not UNSET:
            field_dict["cocreators"] = cocreators
        if retiring is not UNSET:
            field_dict["retiring"] = retiring
        if state is not UNSET:
            field_dict["state"] = state
        if task_completion_percentage is not UNSET:
            field_dict["taskCompletionPercentage"] = task_completion_percentage
        if sp_flag is not UNSET:
            field_dict["spFlag"] = sp_flag
        if is_single_flag is not UNSET:
            field_dict["isSingleFlag"] = is_single_flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_machines_response_200_data_item_active_type_0 import (
            GetV5MachinesResponse200DataItemActiveType0,
        )
        from ..models.get_v5_machines_response_200_data_item_feedback_for_chart import (
            GetV5MachinesResponse200DataItemFeedbackForChart,
        )
        from ..models.get_v5_machines_response_200_data_item_first_creator import (
            GetV5MachinesResponse200DataItemFirstCreator,
        )
        from ..models.get_v5_machines_response_200_data_item_ip_type_0 import GetV5MachinesResponse200DataItemIpType0
        from ..models.get_v5_machines_response_200_data_item_labels_item import (
            GetV5MachinesResponse200DataItemLabelsItem,
        )
        from ..models.get_v5_machines_response_200_data_item_play_info import GetV5MachinesResponse200DataItemPlayInfo
        from ..models.get_v5_machines_response_200_data_item_required_subscription_type_0 import (
            GetV5MachinesResponse200DataItemRequiredSubscriptionType0,
        )
        from ..models.get_v5_machines_response_200_data_item_retiring import GetV5MachinesResponse200DataItemRetiring

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        avatar = d.pop("avatar", UNSET)

        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        points = d.pop("points", UNSET)

        rating = d.pop("rating", UNSET)

        rating_count = d.pop("ratingCount", UNSET)

        release_date = d.pop("releaseDate", UNSET)

        retired_date = d.pop("retiredDate", UNSET)

        free = d.pop("free", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        difficulty_text = d.pop("difficultyText", UNSET)

        user_owns_count = d.pop("userOwnsCount", UNSET)

        auth_user_in_user_owns = d.pop("authUserInUserOwns", UNSET)

        root_owns_count = d.pop("rootOwnsCount", UNSET)

        auth_user_has_reviewed = d.pop("authUserHasReviewed", UNSET)

        auth_user_in_root_owns = d.pop("authUserInRootOwns", UNSET)

        todo = d.pop("todo", UNSET)

        competitive = d.pop("competitive", UNSET)

        def _parse_active(data: object) -> GetV5MachinesResponse200DataItemActiveType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                active_type_0 = GetV5MachinesResponse200DataItemActiveType0.from_dict(data)

                return active_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV5MachinesResponse200DataItemActiveType0 | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        _feedback_for_chart = d.pop("feedbackForChart", UNSET)
        feedback_for_chart: GetV5MachinesResponse200DataItemFeedbackForChart | Unset
        if isinstance(_feedback_for_chart, Unset):
            feedback_for_chart = UNSET
        else:
            feedback_for_chart = GetV5MachinesResponse200DataItemFeedbackForChart.from_dict(_feedback_for_chart)

        def _parse_ip(data: object) -> GetV5MachinesResponse200DataItemIpType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ip_type_0 = GetV5MachinesResponse200DataItemIpType0.from_dict(data)

                return ip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV5MachinesResponse200DataItemIpType0 | None | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        _play_info = d.pop("playInfo", UNSET)
        play_info: GetV5MachinesResponse200DataItemPlayInfo | Unset
        if isinstance(_play_info, Unset):
            play_info = UNSET
        else:
            play_info = GetV5MachinesResponse200DataItemPlayInfo.from_dict(_play_info)

        _labels = d.pop("labels", UNSET)
        labels: list[GetV5MachinesResponse200DataItemLabelsItem] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = GetV5MachinesResponse200DataItemLabelsItem.from_dict(labels_item_data)

                labels.append(labels_item)

        recommended = d.pop("recommended", UNSET)

        price_tier = d.pop("priceTier", UNSET)

        def _parse_required_subscription(
            data: object,
        ) -> GetV5MachinesResponse200DataItemRequiredSubscriptionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                required_subscription_type_0 = GetV5MachinesResponse200DataItemRequiredSubscriptionType0.from_dict(data)

                return required_subscription_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV5MachinesResponse200DataItemRequiredSubscriptionType0 | None | Unset, data)

        required_subscription = _parse_required_subscription(d.pop("requiredSubscription", UNSET))

        _first_creator = d.pop("firstCreator", UNSET)
        first_creator: GetV5MachinesResponse200DataItemFirstCreator | Unset
        if isinstance(_first_creator, Unset):
            first_creator = UNSET
        else:
            first_creator = GetV5MachinesResponse200DataItemFirstCreator.from_dict(_first_creator)

        cocreators = cast(list[Any], d.pop("cocreators", UNSET))

        _retiring = d.pop("retiring", UNSET)
        retiring: GetV5MachinesResponse200DataItemRetiring | Unset
        if isinstance(_retiring, Unset):
            retiring = UNSET
        else:
            retiring = GetV5MachinesResponse200DataItemRetiring.from_dict(_retiring)

        state = d.pop("state", UNSET)

        task_completion_percentage = d.pop("taskCompletionPercentage", UNSET)

        sp_flag = d.pop("spFlag", UNSET)

        is_single_flag = d.pop("isSingleFlag", UNSET)

        get_v5_machines_response_200_data_item = cls(
            id=id,
            avatar=avatar,
            name=name,
            os=os,
            points=points,
            rating=rating,
            rating_count=rating_count,
            release_date=release_date,
            retired_date=retired_date,
            free=free,
            difficulty=difficulty,
            difficulty_text=difficulty_text,
            user_owns_count=user_owns_count,
            auth_user_in_user_owns=auth_user_in_user_owns,
            root_owns_count=root_owns_count,
            auth_user_has_reviewed=auth_user_has_reviewed,
            auth_user_in_root_owns=auth_user_in_root_owns,
            todo=todo,
            competitive=competitive,
            active=active,
            feedback_for_chart=feedback_for_chart,
            ip=ip,
            play_info=play_info,
            labels=labels,
            recommended=recommended,
            price_tier=price_tier,
            required_subscription=required_subscription,
            first_creator=first_creator,
            cocreators=cocreators,
            retiring=retiring,
            state=state,
            task_completion_percentage=task_completion_percentage,
            sp_flag=sp_flag,
            is_single_flag=is_single_flag,
        )

        get_v5_machines_response_200_data_item.additional_properties = d
        return get_v5_machines_response_200_data_item

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
