from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4MachineGraphMatrixIdResponse200InfoUser")


@_attrs_define
class GetV4MachineGraphMatrixIdResponse200InfoUser:
    """
    Attributes:
        enum (float | Unset):
        real (float | Unset):
        cve (float | Unset):
        custom (float | Unset):
        ctf (float | Unset):
    """

    enum: float | Unset = UNSET
    real: float | Unset = UNSET
    cve: float | Unset = UNSET
    custom: float | Unset = UNSET
    ctf: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enum = self.enum

        real = self.real

        cve = self.cve

        custom = self.custom

        ctf = self.ctf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enum is not UNSET:
            field_dict["enum"] = enum
        if real is not UNSET:
            field_dict["real"] = real
        if cve is not UNSET:
            field_dict["cve"] = cve
        if custom is not UNSET:
            field_dict["custom"] = custom
        if ctf is not UNSET:
            field_dict["ctf"] = ctf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enum = d.pop("enum", UNSET)

        real = d.pop("real", UNSET)

        cve = d.pop("cve", UNSET)

        custom = d.pop("custom", UNSET)

        ctf = d.pop("ctf", UNSET)

        get_v4_machine_graph_matrix_id_response_200_info_user = cls(
            enum=enum,
            real=real,
            cve=cve,
            custom=custom,
            ctf=ctf,
        )

        get_v4_machine_graph_matrix_id_response_200_info_user.additional_properties = d
        return get_v4_machine_graph_matrix_id_response_200_info_user

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
