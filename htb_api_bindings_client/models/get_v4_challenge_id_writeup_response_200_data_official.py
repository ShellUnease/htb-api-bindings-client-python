from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_challenge_id_writeup_response_200_data_official_video_url_type_0 import (
        GetV4ChallengeIdWriteupResponse200DataOfficialVideoUrlType0,
    )


T = TypeVar("T", bound="GetV4ChallengeIdWriteupResponse200DataOfficial")


@_attrs_define
class GetV4ChallengeIdWriteupResponse200DataOfficial:
    """
    Attributes:
        filename (str | Unset):
        sha256 (str | Unset):
        url (str | Unset):
        video_url (GetV4ChallengeIdWriteupResponse200DataOfficialVideoUrlType0 | None | Unset):
    """

    filename: str | Unset = UNSET
    sha256: str | Unset = UNSET
    url: str | Unset = UNSET
    video_url: GetV4ChallengeIdWriteupResponse200DataOfficialVideoUrlType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_challenge_id_writeup_response_200_data_official_video_url_type_0 import (
            GetV4ChallengeIdWriteupResponse200DataOfficialVideoUrlType0,
        )

        filename = self.filename

        sha256 = self.sha256

        url = self.url

        video_url: dict[str, Any] | None | Unset
        if isinstance(self.video_url, Unset):
            video_url = UNSET
        elif isinstance(self.video_url, GetV4ChallengeIdWriteupResponse200DataOfficialVideoUrlType0):
            video_url = self.video_url.to_dict()
        else:
            video_url = self.video_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if url is not UNSET:
            field_dict["url"] = url
        if video_url is not UNSET:
            field_dict["video_url"] = video_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_challenge_id_writeup_response_200_data_official_video_url_type_0 import (
            GetV4ChallengeIdWriteupResponse200DataOfficialVideoUrlType0,
        )

        d = dict(src_dict)
        filename = d.pop("filename", UNSET)

        sha256 = d.pop("sha256", UNSET)

        url = d.pop("url", UNSET)

        def _parse_video_url(
            data: object,
        ) -> GetV4ChallengeIdWriteupResponse200DataOfficialVideoUrlType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_url_type_0 = GetV4ChallengeIdWriteupResponse200DataOfficialVideoUrlType0.from_dict(data)

                return video_url_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeIdWriteupResponse200DataOfficialVideoUrlType0 | None | Unset, data)

        video_url = _parse_video_url(d.pop("video_url", UNSET))

        get_v4_challenge_id_writeup_response_200_data_official = cls(
            filename=filename,
            sha256=sha256,
            url=url,
            video_url=video_url,
        )

        get_v4_challenge_id_writeup_response_200_data_official.additional_properties = d
        return get_v4_challenge_id_writeup_response_200_data_official

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
