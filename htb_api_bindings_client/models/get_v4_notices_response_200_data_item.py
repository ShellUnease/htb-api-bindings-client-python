from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4NoticesResponse200DataItem")


@_attrs_define
class GetV4NoticesResponse200DataItem:
    """
    Attributes:
        id (float | Unset):
        type_ (str | Unset):
        message (str | Unset):
        url (str | Unset):
        url_exact (bool | Unset):
        dismissible (bool | Unset):
    """

    id: float | Unset = UNSET
    type_: str | Unset = UNSET
    message: str | Unset = UNSET
    url: str | Unset = UNSET
    url_exact: bool | Unset = UNSET
    dismissible: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        message = self.message

        url = self.url

        url_exact = self.url_exact

        dismissible = self.dismissible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if message is not UNSET:
            field_dict["message"] = message
        if url is not UNSET:
            field_dict["url"] = url
        if url_exact is not UNSET:
            field_dict["url_exact"] = url_exact
        if dismissible is not UNSET:
            field_dict["dismissible"] = dismissible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        message = d.pop("message", UNSET)

        url = d.pop("url", UNSET)

        url_exact = d.pop("url_exact", UNSET)

        dismissible = d.pop("dismissible", UNSET)

        get_v4_notices_response_200_data_item = cls(
            id=id,
            type_=type_,
            message=message,
            url=url,
            url_exact=url_exact,
            dismissible=dismissible,
        )

        get_v4_notices_response_200_data_item.additional_properties = d
        return get_v4_notices_response_200_data_item

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
