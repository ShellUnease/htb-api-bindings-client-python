from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_video_creator_avatar_type_0 import (
        GetV4MachineWalkthroughsIdResponse200MessageVideoCreatorAvatarType0,
    )


T = TypeVar("T", bound="GetV4MachineWalkthroughsIdResponse200MessageVideo")


@_attrs_define
class GetV4MachineWalkthroughsIdResponse200MessageVideo:
    """
    Attributes:
        creator_id (float | Unset):
        creator_name (str | Unset):
        creator_avatar (GetV4MachineWalkthroughsIdResponse200MessageVideoCreatorAvatarType0 | None | Unset):
        youtube_id (str | Unset):
    """

    creator_id: float | Unset = UNSET
    creator_name: str | Unset = UNSET
    creator_avatar: GetV4MachineWalkthroughsIdResponse200MessageVideoCreatorAvatarType0 | None | Unset = UNSET
    youtube_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_video_creator_avatar_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageVideoCreatorAvatarType0,
        )

        creator_id = self.creator_id

        creator_name = self.creator_name

        creator_avatar: dict[str, Any] | None | Unset
        if isinstance(self.creator_avatar, Unset):
            creator_avatar = UNSET
        elif isinstance(self.creator_avatar, GetV4MachineWalkthroughsIdResponse200MessageVideoCreatorAvatarType0):
            creator_avatar = self.creator_avatar.to_dict()
        else:
            creator_avatar = self.creator_avatar

        youtube_id = self.youtube_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if creator_name is not UNSET:
            field_dict["creator_name"] = creator_name
        if creator_avatar is not UNSET:
            field_dict["creator_avatar"] = creator_avatar
        if youtube_id is not UNSET:
            field_dict["youtube_id"] = youtube_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_video_creator_avatar_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageVideoCreatorAvatarType0,
        )

        d = dict(src_dict)
        creator_id = d.pop("creator_id", UNSET)

        creator_name = d.pop("creator_name", UNSET)

        def _parse_creator_avatar(
            data: object,
        ) -> GetV4MachineWalkthroughsIdResponse200MessageVideoCreatorAvatarType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                creator_avatar_type_0 = GetV4MachineWalkthroughsIdResponse200MessageVideoCreatorAvatarType0.from_dict(
                    data
                )

                return creator_avatar_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineWalkthroughsIdResponse200MessageVideoCreatorAvatarType0 | None | Unset, data)

        creator_avatar = _parse_creator_avatar(d.pop("creator_avatar", UNSET))

        youtube_id = d.pop("youtube_id", UNSET)

        get_v4_machine_walkthroughs_id_response_200_message_video = cls(
            creator_id=creator_id,
            creator_name=creator_name,
            creator_avatar=creator_avatar,
            youtube_id=youtube_id,
        )

        get_v4_machine_walkthroughs_id_response_200_message_video.additional_properties = d
        return get_v4_machine_walkthroughs_id_response_200_message_video

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
