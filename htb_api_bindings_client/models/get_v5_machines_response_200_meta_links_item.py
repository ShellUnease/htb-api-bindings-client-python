from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_machines_response_200_meta_links_item_url_type_0 import (
        GetV5MachinesResponse200MetaLinksItemUrlType0,
    )


T = TypeVar("T", bound="GetV5MachinesResponse200MetaLinksItem")


@_attrs_define
class GetV5MachinesResponse200MetaLinksItem:
    """
    Attributes:
        url (GetV5MachinesResponse200MetaLinksItemUrlType0 | None | Unset):
        label (str | Unset):
        active (bool | Unset):
    """

    url: GetV5MachinesResponse200MetaLinksItemUrlType0 | None | Unset = UNSET
    label: str | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v5_machines_response_200_meta_links_item_url_type_0 import (
            GetV5MachinesResponse200MetaLinksItemUrlType0,
        )

        url: dict[str, Any] | None | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        elif isinstance(self.url, GetV5MachinesResponse200MetaLinksItemUrlType0):
            url = self.url.to_dict()
        else:
            url = self.url

        label = self.label

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if label is not UNSET:
            field_dict["label"] = label
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_machines_response_200_meta_links_item_url_type_0 import (
            GetV5MachinesResponse200MetaLinksItemUrlType0,
        )

        d = dict(src_dict)

        def _parse_url(data: object) -> GetV5MachinesResponse200MetaLinksItemUrlType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                url_type_0 = GetV5MachinesResponse200MetaLinksItemUrlType0.from_dict(data)

                return url_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV5MachinesResponse200MetaLinksItemUrlType0 | None | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        label = d.pop("label", UNSET)

        active = d.pop("active", UNSET)

        get_v5_machines_response_200_meta_links_item = cls(
            url=url,
            label=label,
            active=active,
        )

        get_v5_machines_response_200_meta_links_item.additional_properties = d
        return get_v5_machines_response_200_meta_links_item

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
