from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_official import (
        GetV4MachineWalkthroughsIdResponse200MessageOfficial,
    )
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_under_review_type_0 import (
        GetV4MachineWalkthroughsIdResponse200MessageUnderReviewType0,
    )
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_video import (
        GetV4MachineWalkthroughsIdResponse200MessageVideo,
    )
    from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item import (
        GetV4MachineWalkthroughsIdResponse200MessageWriteupsItem,
    )


T = TypeVar("T", bound="GetV4MachineWalkthroughsIdResponse200Message")


@_attrs_define
class GetV4MachineWalkthroughsIdResponse200Message:
    """
    Attributes:
        official (GetV4MachineWalkthroughsIdResponse200MessageOfficial | Unset):
        video (GetV4MachineWalkthroughsIdResponse200MessageVideo | Unset):
        writeups (list[GetV4MachineWalkthroughsIdResponse200MessageWriteupsItem] | Unset):
        under_review (GetV4MachineWalkthroughsIdResponse200MessageUnderReviewType0 | None | Unset):
    """

    official: GetV4MachineWalkthroughsIdResponse200MessageOfficial | Unset = UNSET
    video: GetV4MachineWalkthroughsIdResponse200MessageVideo | Unset = UNSET
    writeups: list[GetV4MachineWalkthroughsIdResponse200MessageWriteupsItem] | Unset = UNSET
    under_review: GetV4MachineWalkthroughsIdResponse200MessageUnderReviewType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_under_review_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageUnderReviewType0,
        )

        official: dict[str, Any] | Unset = UNSET
        if not isinstance(self.official, Unset):
            official = self.official.to_dict()

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        writeups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.writeups, Unset):
            writeups = []
            for writeups_item_data in self.writeups:
                writeups_item = writeups_item_data.to_dict()
                writeups.append(writeups_item)

        under_review: dict[str, Any] | None | Unset
        if isinstance(self.under_review, Unset):
            under_review = UNSET
        elif isinstance(self.under_review, GetV4MachineWalkthroughsIdResponse200MessageUnderReviewType0):
            under_review = self.under_review.to_dict()
        else:
            under_review = self.under_review

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if official is not UNSET:
            field_dict["official"] = official
        if video is not UNSET:
            field_dict["video"] = video
        if writeups is not UNSET:
            field_dict["writeups"] = writeups
        if under_review is not UNSET:
            field_dict["under_review"] = under_review

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_official import (
            GetV4MachineWalkthroughsIdResponse200MessageOfficial,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_under_review_type_0 import (
            GetV4MachineWalkthroughsIdResponse200MessageUnderReviewType0,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_video import (
            GetV4MachineWalkthroughsIdResponse200MessageVideo,
        )
        from ..models.get_v4_machine_walkthroughs_id_response_200_message_writeups_item import (
            GetV4MachineWalkthroughsIdResponse200MessageWriteupsItem,
        )

        d = dict(src_dict)
        _official = d.pop("official", UNSET)
        official: GetV4MachineWalkthroughsIdResponse200MessageOfficial | Unset
        if isinstance(_official, Unset):
            official = UNSET
        else:
            official = GetV4MachineWalkthroughsIdResponse200MessageOfficial.from_dict(_official)

        _video = d.pop("video", UNSET)
        video: GetV4MachineWalkthroughsIdResponse200MessageVideo | Unset
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = GetV4MachineWalkthroughsIdResponse200MessageVideo.from_dict(_video)

        _writeups = d.pop("writeups", UNSET)
        writeups: list[GetV4MachineWalkthroughsIdResponse200MessageWriteupsItem] | Unset = UNSET
        if _writeups is not UNSET:
            writeups = []
            for writeups_item_data in _writeups:
                writeups_item = GetV4MachineWalkthroughsIdResponse200MessageWriteupsItem.from_dict(writeups_item_data)

                writeups.append(writeups_item)

        def _parse_under_review(
            data: object,
        ) -> GetV4MachineWalkthroughsIdResponse200MessageUnderReviewType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                under_review_type_0 = GetV4MachineWalkthroughsIdResponse200MessageUnderReviewType0.from_dict(data)

                return under_review_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineWalkthroughsIdResponse200MessageUnderReviewType0 | None | Unset, data)

        under_review = _parse_under_review(d.pop("under_review", UNSET))

        get_v4_machine_walkthroughs_id_response_200_message = cls(
            official=official,
            video=video,
            writeups=writeups,
            under_review=under_review,
        )

        get_v4_machine_walkthroughs_id_response_200_message.additional_properties = d
        return get_v4_machine_walkthroughs_id_response_200_message

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
