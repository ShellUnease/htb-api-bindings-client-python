from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_sherlocks_categories_list_response_200_info_item_icon_type_0 import (
        GetV4SherlocksCategoriesListResponse200InfoItemIconType0,
    )


T = TypeVar("T", bound="GetV4SherlocksCategoriesListResponse200InfoItem")


@_attrs_define
class GetV4SherlocksCategoriesListResponse200InfoItem:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        icon (GetV4SherlocksCategoriesListResponse200InfoItemIconType0 | None | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    icon: GetV4SherlocksCategoriesListResponse200InfoItemIconType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_sherlocks_categories_list_response_200_info_item_icon_type_0 import (
            GetV4SherlocksCategoriesListResponse200InfoItemIconType0,
        )

        id = self.id

        name = self.name

        icon: dict[str, Any] | None | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        elif isinstance(self.icon, GetV4SherlocksCategoriesListResponse200InfoItemIconType0):
            icon = self.icon.to_dict()
        else:
            icon = self.icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_sherlocks_categories_list_response_200_info_item_icon_type_0 import (
            GetV4SherlocksCategoriesListResponse200InfoItemIconType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_icon(data: object) -> GetV4SherlocksCategoriesListResponse200InfoItemIconType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                icon_type_0 = GetV4SherlocksCategoriesListResponse200InfoItemIconType0.from_dict(data)

                return icon_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SherlocksCategoriesListResponse200InfoItemIconType0 | None | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        get_v4_sherlocks_categories_list_response_200_info_item = cls(
            id=id,
            name=name,
            icon=icon,
        )

        get_v4_sherlocks_categories_list_response_200_info_item.additional_properties = d
        return get_v4_sherlocks_categories_list_response_200_info_item

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
