from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_prolab_id_overview_response_200_data_designated_level import (
        GetV4ProlabIdOverviewResponse200DataDesignatedLevel,
    )
    from ..models.get_v4_prolab_id_overview_response_200_data_excerpt_type_0 import (
        GetV4ProlabIdOverviewResponse200DataExcerptType0,
    )
    from ..models.get_v4_prolab_id_overview_response_200_data_lab_masters_item import (
        GetV4ProlabIdOverviewResponse200DataLabMastersItem,
    )
    from ..models.get_v4_prolab_id_overview_response_200_data_overview_image_url_type_0 import (
        GetV4ProlabIdOverviewResponse200DataOverviewImageUrlType0,
    )


T = TypeVar("T", bound="GetV4ProlabIdOverviewResponse200Data")


@_attrs_define
class GetV4ProlabIdOverviewResponse200Data:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        version (str | Unset):
        excerpt (GetV4ProlabIdOverviewResponse200DataExcerptType0 | None | Unset):
        pro_machines_count (float | Unset):
        pro_flags_count (float | Unset):
        social_links (list[Any] | Unset):
        state (str | Unset):
        mini (bool | Unset):
        identifier (str | Unset):
        content_id (str | Unset):
        new_version (bool | Unset):
        overview_image_url (GetV4ProlabIdOverviewResponse200DataOverviewImageUrlType0 | None | Unset):
        skill_level (str | Unset):
        designated_level (GetV4ProlabIdOverviewResponse200DataDesignatedLevel | Unset):
        lab_masters (list[GetV4ProlabIdOverviewResponse200DataLabMastersItem] | Unset):
        user_eligible_to_play (bool | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    version: str | Unset = UNSET
    excerpt: GetV4ProlabIdOverviewResponse200DataExcerptType0 | None | Unset = UNSET
    pro_machines_count: float | Unset = UNSET
    pro_flags_count: float | Unset = UNSET
    social_links: list[Any] | Unset = UNSET
    state: str | Unset = UNSET
    mini: bool | Unset = UNSET
    identifier: str | Unset = UNSET
    content_id: str | Unset = UNSET
    new_version: bool | Unset = UNSET
    overview_image_url: GetV4ProlabIdOverviewResponse200DataOverviewImageUrlType0 | None | Unset = UNSET
    skill_level: str | Unset = UNSET
    designated_level: GetV4ProlabIdOverviewResponse200DataDesignatedLevel | Unset = UNSET
    lab_masters: list[GetV4ProlabIdOverviewResponse200DataLabMastersItem] | Unset = UNSET
    user_eligible_to_play: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_prolab_id_overview_response_200_data_excerpt_type_0 import (
            GetV4ProlabIdOverviewResponse200DataExcerptType0,
        )
        from ..models.get_v4_prolab_id_overview_response_200_data_overview_image_url_type_0 import (
            GetV4ProlabIdOverviewResponse200DataOverviewImageUrlType0,
        )

        id = self.id

        name = self.name

        version = self.version

        excerpt: dict[str, Any] | None | Unset
        if isinstance(self.excerpt, Unset):
            excerpt = UNSET
        elif isinstance(self.excerpt, GetV4ProlabIdOverviewResponse200DataExcerptType0):
            excerpt = self.excerpt.to_dict()
        else:
            excerpt = self.excerpt

        pro_machines_count = self.pro_machines_count

        pro_flags_count = self.pro_flags_count

        social_links: list[Any] | Unset = UNSET
        if not isinstance(self.social_links, Unset):
            social_links = self.social_links

        state = self.state

        mini = self.mini

        identifier = self.identifier

        content_id = self.content_id

        new_version = self.new_version

        overview_image_url: dict[str, Any] | None | Unset
        if isinstance(self.overview_image_url, Unset):
            overview_image_url = UNSET
        elif isinstance(self.overview_image_url, GetV4ProlabIdOverviewResponse200DataOverviewImageUrlType0):
            overview_image_url = self.overview_image_url.to_dict()
        else:
            overview_image_url = self.overview_image_url

        skill_level = self.skill_level

        designated_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.designated_level, Unset):
            designated_level = self.designated_level.to_dict()

        lab_masters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lab_masters, Unset):
            lab_masters = []
            for lab_masters_item_data in self.lab_masters:
                lab_masters_item = lab_masters_item_data.to_dict()
                lab_masters.append(lab_masters_item)

        user_eligible_to_play = self.user_eligible_to_play

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt
        if pro_machines_count is not UNSET:
            field_dict["pro_machines_count"] = pro_machines_count
        if pro_flags_count is not UNSET:
            field_dict["pro_flags_count"] = pro_flags_count
        if social_links is not UNSET:
            field_dict["social_links"] = social_links
        if state is not UNSET:
            field_dict["state"] = state
        if mini is not UNSET:
            field_dict["mini"] = mini
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if new_version is not UNSET:
            field_dict["new_version"] = new_version
        if overview_image_url is not UNSET:
            field_dict["overview_image_url"] = overview_image_url
        if skill_level is not UNSET:
            field_dict["skill_level"] = skill_level
        if designated_level is not UNSET:
            field_dict["designated_level"] = designated_level
        if lab_masters is not UNSET:
            field_dict["lab_masters"] = lab_masters
        if user_eligible_to_play is not UNSET:
            field_dict["user_eligible_to_play"] = user_eligible_to_play

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_prolab_id_overview_response_200_data_designated_level import (
            GetV4ProlabIdOverviewResponse200DataDesignatedLevel,
        )
        from ..models.get_v4_prolab_id_overview_response_200_data_excerpt_type_0 import (
            GetV4ProlabIdOverviewResponse200DataExcerptType0,
        )
        from ..models.get_v4_prolab_id_overview_response_200_data_lab_masters_item import (
            GetV4ProlabIdOverviewResponse200DataLabMastersItem,
        )
        from ..models.get_v4_prolab_id_overview_response_200_data_overview_image_url_type_0 import (
            GetV4ProlabIdOverviewResponse200DataOverviewImageUrlType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        def _parse_excerpt(data: object) -> GetV4ProlabIdOverviewResponse200DataExcerptType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                excerpt_type_0 = GetV4ProlabIdOverviewResponse200DataExcerptType0.from_dict(data)

                return excerpt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdOverviewResponse200DataExcerptType0 | None | Unset, data)

        excerpt = _parse_excerpt(d.pop("excerpt", UNSET))

        pro_machines_count = d.pop("pro_machines_count", UNSET)

        pro_flags_count = d.pop("pro_flags_count", UNSET)

        social_links = cast(list[Any], d.pop("social_links", UNSET))

        state = d.pop("state", UNSET)

        mini = d.pop("mini", UNSET)

        identifier = d.pop("identifier", UNSET)

        content_id = d.pop("content_id", UNSET)

        new_version = d.pop("new_version", UNSET)

        def _parse_overview_image_url(
            data: object,
        ) -> GetV4ProlabIdOverviewResponse200DataOverviewImageUrlType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overview_image_url_type_0 = GetV4ProlabIdOverviewResponse200DataOverviewImageUrlType0.from_dict(data)

                return overview_image_url_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdOverviewResponse200DataOverviewImageUrlType0 | None | Unset, data)

        overview_image_url = _parse_overview_image_url(d.pop("overview_image_url", UNSET))

        skill_level = d.pop("skill_level", UNSET)

        _designated_level = d.pop("designated_level", UNSET)
        designated_level: GetV4ProlabIdOverviewResponse200DataDesignatedLevel | Unset
        if isinstance(_designated_level, Unset):
            designated_level = UNSET
        else:
            designated_level = GetV4ProlabIdOverviewResponse200DataDesignatedLevel.from_dict(_designated_level)

        _lab_masters = d.pop("lab_masters", UNSET)
        lab_masters: list[GetV4ProlabIdOverviewResponse200DataLabMastersItem] | Unset = UNSET
        if _lab_masters is not UNSET:
            lab_masters = []
            for lab_masters_item_data in _lab_masters:
                lab_masters_item = GetV4ProlabIdOverviewResponse200DataLabMastersItem.from_dict(lab_masters_item_data)

                lab_masters.append(lab_masters_item)

        user_eligible_to_play = d.pop("user_eligible_to_play", UNSET)

        get_v4_prolab_id_overview_response_200_data = cls(
            id=id,
            name=name,
            version=version,
            excerpt=excerpt,
            pro_machines_count=pro_machines_count,
            pro_flags_count=pro_flags_count,
            social_links=social_links,
            state=state,
            mini=mini,
            identifier=identifier,
            content_id=content_id,
            new_version=new_version,
            overview_image_url=overview_image_url,
            skill_level=skill_level,
            designated_level=designated_level,
            lab_masters=lab_masters,
            user_eligible_to_play=user_eligible_to_play,
        )

        get_v4_prolab_id_overview_response_200_data.additional_properties = d
        return get_v4_prolab_id_overview_response_200_data

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
