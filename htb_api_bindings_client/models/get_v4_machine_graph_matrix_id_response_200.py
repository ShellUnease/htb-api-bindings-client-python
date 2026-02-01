from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_graph_matrix_id_response_200_info import GetV4MachineGraphMatrixIdResponse200Info


T = TypeVar("T", bound="GetV4MachineGraphMatrixIdResponse200")


@_attrs_define
class GetV4MachineGraphMatrixIdResponse200:
    """
    Attributes:
        info (GetV4MachineGraphMatrixIdResponse200Info | Unset):
    """

    info: GetV4MachineGraphMatrixIdResponse200Info | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_graph_matrix_id_response_200_info import GetV4MachineGraphMatrixIdResponse200Info

        d = dict(src_dict)
        _info = d.pop("info", UNSET)
        info: GetV4MachineGraphMatrixIdResponse200Info | Unset
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = GetV4MachineGraphMatrixIdResponse200Info.from_dict(_info)

        get_v4_machine_graph_matrix_id_response_200 = cls(
            info=info,
        )

        get_v4_machine_graph_matrix_id_response_200.additional_properties = d
        return get_v4_machine_graph_matrix_id_response_200

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
