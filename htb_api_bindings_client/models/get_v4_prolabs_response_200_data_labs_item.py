from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_prolabs_response_200_data_labs_item_cover_img_url_type_0 import (
        GetV4ProlabsResponse200DataLabsItemCoverImgUrlType0,
    )


T = TypeVar("T", bound="GetV4ProlabsResponse200DataLabsItem")


@_attrs_define
class GetV4ProlabsResponse200DataLabsItem:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        release_at (str | Unset):
        pro_machines_count (float | Unset):
        pro_flags_count (float | Unset):
        state (str | Unset):
        mini (bool | Unset):
        identifier (str | Unset):
        content_id (str | Unset):
        ownership (float | Unset):
        user_eligible_for_certificate (bool | Unset):
        new (bool | Unset):
        skill_level (str | Unset):
        designated_category (str | Unset):
        team (str | Unset):
        level (float | Unset):
        lab_servers_count (float | Unset):
        cover_img_url (GetV4ProlabsResponse200DataLabsItemCoverImgUrlType0 | None | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    release_at: str | Unset = UNSET
    pro_machines_count: float | Unset = UNSET
    pro_flags_count: float | Unset = UNSET
    state: str | Unset = UNSET
    mini: bool | Unset = UNSET
    identifier: str | Unset = UNSET
    content_id: str | Unset = UNSET
    ownership: float | Unset = UNSET
    user_eligible_for_certificate: bool | Unset = UNSET
    new: bool | Unset = UNSET
    skill_level: str | Unset = UNSET
    designated_category: str | Unset = UNSET
    team: str | Unset = UNSET
    level: float | Unset = UNSET
    lab_servers_count: float | Unset = UNSET
    cover_img_url: GetV4ProlabsResponse200DataLabsItemCoverImgUrlType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_prolabs_response_200_data_labs_item_cover_img_url_type_0 import (
            GetV4ProlabsResponse200DataLabsItemCoverImgUrlType0,
        )

        id = self.id

        name = self.name

        release_at = self.release_at

        pro_machines_count = self.pro_machines_count

        pro_flags_count = self.pro_flags_count

        state = self.state

        mini = self.mini

        identifier = self.identifier

        content_id = self.content_id

        ownership = self.ownership

        user_eligible_for_certificate = self.user_eligible_for_certificate

        new = self.new

        skill_level = self.skill_level

        designated_category = self.designated_category

        team = self.team

        level = self.level

        lab_servers_count = self.lab_servers_count

        cover_img_url: dict[str, Any] | None | Unset
        if isinstance(self.cover_img_url, Unset):
            cover_img_url = UNSET
        elif isinstance(self.cover_img_url, GetV4ProlabsResponse200DataLabsItemCoverImgUrlType0):
            cover_img_url = self.cover_img_url.to_dict()
        else:
            cover_img_url = self.cover_img_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if release_at is not UNSET:
            field_dict["release_at"] = release_at
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
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if ownership is not UNSET:
            field_dict["ownership"] = ownership
        if user_eligible_for_certificate is not UNSET:
            field_dict["user_eligible_for_certificate"] = user_eligible_for_certificate
        if new is not UNSET:
            field_dict["new"] = new
        if skill_level is not UNSET:
            field_dict["skill_level"] = skill_level
        if designated_category is not UNSET:
            field_dict["designated_category"] = designated_category
        if team is not UNSET:
            field_dict["team"] = team
        if level is not UNSET:
            field_dict["level"] = level
        if lab_servers_count is not UNSET:
            field_dict["lab_servers_count"] = lab_servers_count
        if cover_img_url is not UNSET:
            field_dict["cover_img_url"] = cover_img_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_prolabs_response_200_data_labs_item_cover_img_url_type_0 import (
            GetV4ProlabsResponse200DataLabsItemCoverImgUrlType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        release_at = d.pop("release_at", UNSET)

        pro_machines_count = d.pop("pro_machines_count", UNSET)

        pro_flags_count = d.pop("pro_flags_count", UNSET)

        state = d.pop("state", UNSET)

        mini = d.pop("mini", UNSET)

        identifier = d.pop("identifier", UNSET)

        content_id = d.pop("content_id", UNSET)

        ownership = d.pop("ownership", UNSET)

        user_eligible_for_certificate = d.pop("user_eligible_for_certificate", UNSET)

        new = d.pop("new", UNSET)

        skill_level = d.pop("skill_level", UNSET)

        designated_category = d.pop("designated_category", UNSET)

        team = d.pop("team", UNSET)

        level = d.pop("level", UNSET)

        lab_servers_count = d.pop("lab_servers_count", UNSET)

        def _parse_cover_img_url(data: object) -> GetV4ProlabsResponse200DataLabsItemCoverImgUrlType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cover_img_url_type_0 = GetV4ProlabsResponse200DataLabsItemCoverImgUrlType0.from_dict(data)

                return cover_img_url_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabsResponse200DataLabsItemCoverImgUrlType0 | None | Unset, data)

        cover_img_url = _parse_cover_img_url(d.pop("cover_img_url", UNSET))

        get_v4_prolabs_response_200_data_labs_item = cls(
            id=id,
            name=name,
            release_at=release_at,
            pro_machines_count=pro_machines_count,
            pro_flags_count=pro_flags_count,
            state=state,
            mini=mini,
            identifier=identifier,
            content_id=content_id,
            ownership=ownership,
            user_eligible_for_certificate=user_eligible_for_certificate,
            new=new,
            skill_level=skill_level,
            designated_category=designated_category,
            team=team,
            level=level,
            lab_servers_count=lab_servers_count,
            cover_img_url=cover_img_url,
        )

        get_v4_prolabs_response_200_data_labs_item.additional_properties = d
        return get_v4_prolabs_response_200_data_labs_item

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
