from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_connections_servers_response_200_data_options_au import (
        GetV4ConnectionsServersResponse200DataOptionsAU,
    )
    from ..models.get_v4_connections_servers_response_200_data_options_eu import (
        GetV4ConnectionsServersResponse200DataOptionsEU,
    )
    from ..models.get_v4_connections_servers_response_200_data_options_sg import (
        GetV4ConnectionsServersResponse200DataOptionsSG,
    )
    from ..models.get_v4_connections_servers_response_200_data_options_us import (
        GetV4ConnectionsServersResponse200DataOptionsUS,
    )


T = TypeVar("T", bound="GetV4ConnectionsServersResponse200DataOptions")


@_attrs_define
class GetV4ConnectionsServersResponse200DataOptions:
    """
    Attributes:
        eu (GetV4ConnectionsServersResponse200DataOptionsEU | Unset):
        us (GetV4ConnectionsServersResponse200DataOptionsUS | Unset):
        au (GetV4ConnectionsServersResponse200DataOptionsAU | Unset):
        sg (GetV4ConnectionsServersResponse200DataOptionsSG | Unset):
    """

    eu: GetV4ConnectionsServersResponse200DataOptionsEU | Unset = UNSET
    us: GetV4ConnectionsServersResponse200DataOptionsUS | Unset = UNSET
    au: GetV4ConnectionsServersResponse200DataOptionsAU | Unset = UNSET
    sg: GetV4ConnectionsServersResponse200DataOptionsSG | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eu, Unset):
            eu = self.eu.to_dict()

        us: dict[str, Any] | Unset = UNSET
        if not isinstance(self.us, Unset):
            us = self.us.to_dict()

        au: dict[str, Any] | Unset = UNSET
        if not isinstance(self.au, Unset):
            au = self.au.to_dict()

        sg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sg, Unset):
            sg = self.sg.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eu is not UNSET:
            field_dict["EU"] = eu
        if us is not UNSET:
            field_dict["US"] = us
        if au is not UNSET:
            field_dict["AU"] = au
        if sg is not UNSET:
            field_dict["SG"] = sg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_connections_servers_response_200_data_options_au import (
            GetV4ConnectionsServersResponse200DataOptionsAU,
        )
        from ..models.get_v4_connections_servers_response_200_data_options_eu import (
            GetV4ConnectionsServersResponse200DataOptionsEU,
        )
        from ..models.get_v4_connections_servers_response_200_data_options_sg import (
            GetV4ConnectionsServersResponse200DataOptionsSG,
        )
        from ..models.get_v4_connections_servers_response_200_data_options_us import (
            GetV4ConnectionsServersResponse200DataOptionsUS,
        )

        d = dict(src_dict)
        _eu = d.pop("EU", UNSET)
        eu: GetV4ConnectionsServersResponse200DataOptionsEU | Unset
        if isinstance(_eu, Unset):
            eu = UNSET
        else:
            eu = GetV4ConnectionsServersResponse200DataOptionsEU.from_dict(_eu)

        _us = d.pop("US", UNSET)
        us: GetV4ConnectionsServersResponse200DataOptionsUS | Unset
        if isinstance(_us, Unset):
            us = UNSET
        else:
            us = GetV4ConnectionsServersResponse200DataOptionsUS.from_dict(_us)

        _au = d.pop("AU", UNSET)
        au: GetV4ConnectionsServersResponse200DataOptionsAU | Unset
        if isinstance(_au, Unset):
            au = UNSET
        else:
            au = GetV4ConnectionsServersResponse200DataOptionsAU.from_dict(_au)

        _sg = d.pop("SG", UNSET)
        sg: GetV4ConnectionsServersResponse200DataOptionsSG | Unset
        if isinstance(_sg, Unset):
            sg = UNSET
        else:
            sg = GetV4ConnectionsServersResponse200DataOptionsSG.from_dict(_sg)

        get_v4_connections_servers_response_200_data_options = cls(
            eu=eu,
            us=us,
            au=au,
            sg=sg,
        )

        get_v4_connections_servers_response_200_data_options.additional_properties = d
        return get_v4_connections_servers_response_200_data_options

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
