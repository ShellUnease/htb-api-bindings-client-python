from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_connections_servers_response_200_data_assigned import (
        GetV4ConnectionsServersResponse200DataAssigned,
    )
    from ..models.get_v4_connections_servers_response_200_data_options import (
        GetV4ConnectionsServersResponse200DataOptions,
    )


T = TypeVar("T", bound="GetV4ConnectionsServersResponse200Data")


@_attrs_define
class GetV4ConnectionsServersResponse200Data:
    """
    Attributes:
        disabled (bool | Unset):
        assigned (GetV4ConnectionsServersResponse200DataAssigned | Unset):
        options (GetV4ConnectionsServersResponse200DataOptions | Unset):
    """

    disabled: bool | Unset = UNSET
    assigned: GetV4ConnectionsServersResponse200DataAssigned | Unset = UNSET
    options: GetV4ConnectionsServersResponse200DataOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disabled = self.disabled

        assigned: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assigned, Unset):
            assigned = self.assigned.to_dict()

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_connections_servers_response_200_data_assigned import (
            GetV4ConnectionsServersResponse200DataAssigned,
        )
        from ..models.get_v4_connections_servers_response_200_data_options import (
            GetV4ConnectionsServersResponse200DataOptions,
        )

        d = dict(src_dict)
        disabled = d.pop("disabled", UNSET)

        _assigned = d.pop("assigned", UNSET)
        assigned: GetV4ConnectionsServersResponse200DataAssigned | Unset
        if isinstance(_assigned, Unset):
            assigned = UNSET
        else:
            assigned = GetV4ConnectionsServersResponse200DataAssigned.from_dict(_assigned)

        _options = d.pop("options", UNSET)
        options: GetV4ConnectionsServersResponse200DataOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = GetV4ConnectionsServersResponse200DataOptions.from_dict(_options)

        get_v4_connections_servers_response_200_data = cls(
            disabled=disabled,
            assigned=assigned,
            options=options,
        )

        get_v4_connections_servers_response_200_data.additional_properties = d
        return get_v4_connections_servers_response_200_data

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
