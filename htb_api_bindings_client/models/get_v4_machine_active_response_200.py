from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_active_response_200_info_type_0 import GetV4MachineActiveResponse200InfoType0


T = TypeVar("T", bound="GetV4MachineActiveResponse200")


@_attrs_define
class GetV4MachineActiveResponse200:
    """
    Attributes:
        info (GetV4MachineActiveResponse200InfoType0 | None | Unset):
    """

    info: GetV4MachineActiveResponse200InfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machine_active_response_200_info_type_0 import GetV4MachineActiveResponse200InfoType0

        info: dict[str, Any] | None | Unset
        if isinstance(self.info, Unset):
            info = UNSET
        elif isinstance(self.info, GetV4MachineActiveResponse200InfoType0):
            info = self.info.to_dict()
        else:
            info = self.info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_active_response_200_info_type_0 import GetV4MachineActiveResponse200InfoType0

        d = dict(src_dict)

        def _parse_info(data: object) -> GetV4MachineActiveResponse200InfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                info_type_0 = GetV4MachineActiveResponse200InfoType0.from_dict(data)

                return info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineActiveResponse200InfoType0 | None | Unset, data)

        info = _parse_info(d.pop("info", UNSET))

        get_v4_machine_active_response_200 = cls(
            info=info,
        )

        get_v4_machine_active_response_200.additional_properties = d
        return get_v4_machine_active_response_200

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
