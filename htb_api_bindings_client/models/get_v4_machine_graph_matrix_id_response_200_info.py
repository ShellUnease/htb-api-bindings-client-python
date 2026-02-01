from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_graph_matrix_id_response_200_info_aggregate import (
        GetV4MachineGraphMatrixIdResponse200InfoAggregate,
    )
    from ..models.get_v4_machine_graph_matrix_id_response_200_info_maker import (
        GetV4MachineGraphMatrixIdResponse200InfoMaker,
    )
    from ..models.get_v4_machine_graph_matrix_id_response_200_info_user import (
        GetV4MachineGraphMatrixIdResponse200InfoUser,
    )


T = TypeVar("T", bound="GetV4MachineGraphMatrixIdResponse200Info")


@_attrs_define
class GetV4MachineGraphMatrixIdResponse200Info:
    """
    Attributes:
        aggregate (GetV4MachineGraphMatrixIdResponse200InfoAggregate | Unset):
        maker (GetV4MachineGraphMatrixIdResponse200InfoMaker | Unset):
        user (GetV4MachineGraphMatrixIdResponse200InfoUser | Unset):
    """

    aggregate: GetV4MachineGraphMatrixIdResponse200InfoAggregate | Unset = UNSET
    maker: GetV4MachineGraphMatrixIdResponse200InfoMaker | Unset = UNSET
    user: GetV4MachineGraphMatrixIdResponse200InfoUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aggregate, Unset):
            aggregate = self.aggregate.to_dict()

        maker: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maker, Unset):
            maker = self.maker.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregate is not UNSET:
            field_dict["aggregate"] = aggregate
        if maker is not UNSET:
            field_dict["maker"] = maker
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_graph_matrix_id_response_200_info_aggregate import (
            GetV4MachineGraphMatrixIdResponse200InfoAggregate,
        )
        from ..models.get_v4_machine_graph_matrix_id_response_200_info_maker import (
            GetV4MachineGraphMatrixIdResponse200InfoMaker,
        )
        from ..models.get_v4_machine_graph_matrix_id_response_200_info_user import (
            GetV4MachineGraphMatrixIdResponse200InfoUser,
        )

        d = dict(src_dict)
        _aggregate = d.pop("aggregate", UNSET)
        aggregate: GetV4MachineGraphMatrixIdResponse200InfoAggregate | Unset
        if isinstance(_aggregate, Unset):
            aggregate = UNSET
        else:
            aggregate = GetV4MachineGraphMatrixIdResponse200InfoAggregate.from_dict(_aggregate)

        _maker = d.pop("maker", UNSET)
        maker: GetV4MachineGraphMatrixIdResponse200InfoMaker | Unset
        if isinstance(_maker, Unset):
            maker = UNSET
        else:
            maker = GetV4MachineGraphMatrixIdResponse200InfoMaker.from_dict(_maker)

        _user = d.pop("user", UNSET)
        user: GetV4MachineGraphMatrixIdResponse200InfoUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = GetV4MachineGraphMatrixIdResponse200InfoUser.from_dict(_user)

        get_v4_machine_graph_matrix_id_response_200_info = cls(
            aggregate=aggregate,
            maker=maker,
            user=user,
        )

        get_v4_machine_graph_matrix_id_response_200_info.additional_properties = d
        return get_v4_machine_graph_matrix_id_response_200_info

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
