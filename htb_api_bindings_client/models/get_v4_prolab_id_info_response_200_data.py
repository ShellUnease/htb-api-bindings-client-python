from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_prolab_id_info_response_200_data_cover_image_url_type_0 import (
        GetV4ProlabIdInfoResponse200DataCoverImageUrlType0,
    )
    from ..models.get_v4_prolab_id_info_response_200_data_lab_masters_item import (
        GetV4ProlabIdInfoResponse200DataLabMastersItem,
    )
    from ..models.get_v4_prolab_id_info_response_200_data_video_url_type_0 import (
        GetV4ProlabIdInfoResponse200DataVideoUrlType0,
    )
    from ..models.get_v4_prolab_id_info_response_200_data_writeup_type_0 import (
        GetV4ProlabIdInfoResponse200DataWriteupType0,
    )


T = TypeVar("T", bound="GetV4ProlabIdInfoResponse200Data")


@_attrs_define
class GetV4ProlabIdInfoResponse200Data:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        version (str | Unset):
        entry_points (list[str] | Unset):
        description (str | Unset):
        video_url (GetV4ProlabIdInfoResponse200DataVideoUrlType0 | None | Unset):
        pro_machines_count (float | Unset):
        pro_flags_count (float | Unset):
        state (str | Unset):
        mini (bool | Unset):
        identifier (str | Unset):
        cover_image_url (GetV4ProlabIdInfoResponse200DataCoverImageUrlType0 | None | Unset):
        lab_servers_count (float | Unset):
        active_users (float | Unset):
        lab_masters (list[GetV4ProlabIdInfoResponse200DataLabMastersItem] | Unset):
        writeup (GetV4ProlabIdInfoResponse200DataWriteupType0 | None | Unset):
        can_interact (bool | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    version: str | Unset = UNSET
    entry_points: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    video_url: GetV4ProlabIdInfoResponse200DataVideoUrlType0 | None | Unset = UNSET
    pro_machines_count: float | Unset = UNSET
    pro_flags_count: float | Unset = UNSET
    state: str | Unset = UNSET
    mini: bool | Unset = UNSET
    identifier: str | Unset = UNSET
    cover_image_url: GetV4ProlabIdInfoResponse200DataCoverImageUrlType0 | None | Unset = UNSET
    lab_servers_count: float | Unset = UNSET
    active_users: float | Unset = UNSET
    lab_masters: list[GetV4ProlabIdInfoResponse200DataLabMastersItem] | Unset = UNSET
    writeup: GetV4ProlabIdInfoResponse200DataWriteupType0 | None | Unset = UNSET
    can_interact: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_prolab_id_info_response_200_data_cover_image_url_type_0 import (
            GetV4ProlabIdInfoResponse200DataCoverImageUrlType0,
        )
        from ..models.get_v4_prolab_id_info_response_200_data_video_url_type_0 import (
            GetV4ProlabIdInfoResponse200DataVideoUrlType0,
        )
        from ..models.get_v4_prolab_id_info_response_200_data_writeup_type_0 import (
            GetV4ProlabIdInfoResponse200DataWriteupType0,
        )

        id = self.id

        name = self.name

        version = self.version

        entry_points: list[str] | Unset = UNSET
        if not isinstance(self.entry_points, Unset):
            entry_points = self.entry_points

        description = self.description

        video_url: dict[str, Any] | None | Unset
        if isinstance(self.video_url, Unset):
            video_url = UNSET
        elif isinstance(self.video_url, GetV4ProlabIdInfoResponse200DataVideoUrlType0):
            video_url = self.video_url.to_dict()
        else:
            video_url = self.video_url

        pro_machines_count = self.pro_machines_count

        pro_flags_count = self.pro_flags_count

        state = self.state

        mini = self.mini

        identifier = self.identifier

        cover_image_url: dict[str, Any] | None | Unset
        if isinstance(self.cover_image_url, Unset):
            cover_image_url = UNSET
        elif isinstance(self.cover_image_url, GetV4ProlabIdInfoResponse200DataCoverImageUrlType0):
            cover_image_url = self.cover_image_url.to_dict()
        else:
            cover_image_url = self.cover_image_url

        lab_servers_count = self.lab_servers_count

        active_users = self.active_users

        lab_masters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lab_masters, Unset):
            lab_masters = []
            for lab_masters_item_data in self.lab_masters:
                lab_masters_item = lab_masters_item_data.to_dict()
                lab_masters.append(lab_masters_item)

        writeup: dict[str, Any] | None | Unset
        if isinstance(self.writeup, Unset):
            writeup = UNSET
        elif isinstance(self.writeup, GetV4ProlabIdInfoResponse200DataWriteupType0):
            writeup = self.writeup.to_dict()
        else:
            writeup = self.writeup

        can_interact = self.can_interact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if entry_points is not UNSET:
            field_dict["entry_points"] = entry_points
        if description is not UNSET:
            field_dict["description"] = description
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if pro_machines_count is not UNSET:
            field_dict["pro_machines_count"] = pro_machines_count
        if pro_flags_count is not UNSET:
            field_dict["pro_flags_count"] = pro_flags_count
        if state is not UNSET:
            field_dict["state"] = state
        if mini is not UNSET:
            field_dict["mini"] = mini
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if lab_servers_count is not UNSET:
            field_dict["lab_servers_count"] = lab_servers_count
        if active_users is not UNSET:
            field_dict["active_users"] = active_users
        if lab_masters is not UNSET:
            field_dict["lab_masters"] = lab_masters
        if writeup is not UNSET:
            field_dict["writeup"] = writeup
        if can_interact is not UNSET:
            field_dict["can_interact"] = can_interact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_prolab_id_info_response_200_data_cover_image_url_type_0 import (
            GetV4ProlabIdInfoResponse200DataCoverImageUrlType0,
        )
        from ..models.get_v4_prolab_id_info_response_200_data_lab_masters_item import (
            GetV4ProlabIdInfoResponse200DataLabMastersItem,
        )
        from ..models.get_v4_prolab_id_info_response_200_data_video_url_type_0 import (
            GetV4ProlabIdInfoResponse200DataVideoUrlType0,
        )
        from ..models.get_v4_prolab_id_info_response_200_data_writeup_type_0 import (
            GetV4ProlabIdInfoResponse200DataWriteupType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        entry_points = cast(list[str], d.pop("entry_points", UNSET))

        description = d.pop("description", UNSET)

        def _parse_video_url(data: object) -> GetV4ProlabIdInfoResponse200DataVideoUrlType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_url_type_0 = GetV4ProlabIdInfoResponse200DataVideoUrlType0.from_dict(data)

                return video_url_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdInfoResponse200DataVideoUrlType0 | None | Unset, data)

        video_url = _parse_video_url(d.pop("video_url", UNSET))

        pro_machines_count = d.pop("pro_machines_count", UNSET)

        pro_flags_count = d.pop("pro_flags_count", UNSET)

        state = d.pop("state", UNSET)

        mini = d.pop("mini", UNSET)

        identifier = d.pop("identifier", UNSET)

        def _parse_cover_image_url(data: object) -> GetV4ProlabIdInfoResponse200DataCoverImageUrlType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cover_image_url_type_0 = GetV4ProlabIdInfoResponse200DataCoverImageUrlType0.from_dict(data)

                return cover_image_url_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdInfoResponse200DataCoverImageUrlType0 | None | Unset, data)

        cover_image_url = _parse_cover_image_url(d.pop("cover_image_url", UNSET))

        lab_servers_count = d.pop("lab_servers_count", UNSET)

        active_users = d.pop("active_users", UNSET)

        _lab_masters = d.pop("lab_masters", UNSET)
        lab_masters: list[GetV4ProlabIdInfoResponse200DataLabMastersItem] | Unset = UNSET
        if _lab_masters is not UNSET:
            lab_masters = []
            for lab_masters_item_data in _lab_masters:
                lab_masters_item = GetV4ProlabIdInfoResponse200DataLabMastersItem.from_dict(lab_masters_item_data)

                lab_masters.append(lab_masters_item)

        def _parse_writeup(data: object) -> GetV4ProlabIdInfoResponse200DataWriteupType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                writeup_type_0 = GetV4ProlabIdInfoResponse200DataWriteupType0.from_dict(data)

                return writeup_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdInfoResponse200DataWriteupType0 | None | Unset, data)

        writeup = _parse_writeup(d.pop("writeup", UNSET))

        can_interact = d.pop("can_interact", UNSET)

        get_v4_prolab_id_info_response_200_data = cls(
            id=id,
            name=name,
            version=version,
            entry_points=entry_points,
            description=description,
            video_url=video_url,
            pro_machines_count=pro_machines_count,
            pro_flags_count=pro_flags_count,
            state=state,
            mini=mini,
            identifier=identifier,
            cover_image_url=cover_image_url,
            lab_servers_count=lab_servers_count,
            active_users=active_users,
            lab_masters=lab_masters,
            writeup=writeup,
            can_interact=can_interact,
        )

        get_v4_prolab_id_info_response_200_data.additional_properties = d
        return get_v4_prolab_id_info_response_200_data

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
