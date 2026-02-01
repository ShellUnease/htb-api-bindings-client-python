from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v5_connections_response_200_data_item_assigned_server import (
        GetV5ConnectionsResponse200DataItemAssignedServer,
    )


T = TypeVar("T", bound="GetV5ConnectionsResponse200DataItem")


@_attrs_define
class GetV5ConnectionsResponse200DataItem:
    """
    Attributes:
        type_ (str | Unset):
        location_type_friendly (str | Unset):
        assigned_server (GetV5ConnectionsResponse200DataItemAssignedServer | Unset):
    """

    type_: str | Unset = UNSET
    location_type_friendly: str | Unset = UNSET
    assigned_server: GetV5ConnectionsResponse200DataItemAssignedServer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        location_type_friendly = self.location_type_friendly

        assigned_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assigned_server, Unset):
            assigned_server = self.assigned_server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if location_type_friendly is not UNSET:
            field_dict["location_type_friendly"] = location_type_friendly
        if assigned_server is not UNSET:
            field_dict["assigned_server"] = assigned_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v5_connections_response_200_data_item_assigned_server import (
            GetV5ConnectionsResponse200DataItemAssignedServer,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        location_type_friendly = d.pop("location_type_friendly", UNSET)

        _assigned_server = d.pop("assigned_server", UNSET)
        assigned_server: GetV5ConnectionsResponse200DataItemAssignedServer | Unset
        if isinstance(_assigned_server, Unset):
            assigned_server = UNSET
        else:
            assigned_server = GetV5ConnectionsResponse200DataItemAssignedServer.from_dict(_assigned_server)

        get_v5_connections_response_200_data_item = cls(
            type_=type_,
            location_type_friendly=location_type_friendly,
            assigned_server=assigned_server,
        )

        get_v5_connections_response_200_data_item.additional_properties = d
        return get_v5_connections_response_200_data_item

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
