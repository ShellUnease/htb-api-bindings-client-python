from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_prolab_id_progress_response_200_data_keyed_pro_lab_mile_stone_item import (
        GetV4ProlabIdProgressResponse200DataKeyedProLabMileStoneItem,
    )


T = TypeVar("T", bound="GetV4ProlabIdProgressResponse200Data")


@_attrs_define
class GetV4ProlabIdProgressResponse200Data:
    """
    Attributes:
        ownership (float | Unset):
        ownership_required_for_certification (float | Unset):
        keyed_pro_lab_mile_stone (list[GetV4ProlabIdProgressResponse200DataKeyedProLabMileStoneItem] | Unset):
        user_eligible_for_certificate (bool | Unset):
    """

    ownership: float | Unset = UNSET
    ownership_required_for_certification: float | Unset = UNSET
    keyed_pro_lab_mile_stone: list[GetV4ProlabIdProgressResponse200DataKeyedProLabMileStoneItem] | Unset = UNSET
    user_eligible_for_certificate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ownership = self.ownership

        ownership_required_for_certification = self.ownership_required_for_certification

        keyed_pro_lab_mile_stone: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keyed_pro_lab_mile_stone, Unset):
            keyed_pro_lab_mile_stone = []
            for keyed_pro_lab_mile_stone_item_data in self.keyed_pro_lab_mile_stone:
                keyed_pro_lab_mile_stone_item = keyed_pro_lab_mile_stone_item_data.to_dict()
                keyed_pro_lab_mile_stone.append(keyed_pro_lab_mile_stone_item)

        user_eligible_for_certificate = self.user_eligible_for_certificate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ownership is not UNSET:
            field_dict["ownership"] = ownership
        if ownership_required_for_certification is not UNSET:
            field_dict["ownership_required_for_certification"] = ownership_required_for_certification
        if keyed_pro_lab_mile_stone is not UNSET:
            field_dict["keyed_pro_lab_mile_stone"] = keyed_pro_lab_mile_stone
        if user_eligible_for_certificate is not UNSET:
            field_dict["user_eligible_for_certificate"] = user_eligible_for_certificate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_prolab_id_progress_response_200_data_keyed_pro_lab_mile_stone_item import (
            GetV4ProlabIdProgressResponse200DataKeyedProLabMileStoneItem,
        )

        d = dict(src_dict)
        ownership = d.pop("ownership", UNSET)

        ownership_required_for_certification = d.pop("ownership_required_for_certification", UNSET)

        _keyed_pro_lab_mile_stone = d.pop("keyed_pro_lab_mile_stone", UNSET)
        keyed_pro_lab_mile_stone: list[GetV4ProlabIdProgressResponse200DataKeyedProLabMileStoneItem] | Unset = UNSET
        if _keyed_pro_lab_mile_stone is not UNSET:
            keyed_pro_lab_mile_stone = []
            for keyed_pro_lab_mile_stone_item_data in _keyed_pro_lab_mile_stone:
                keyed_pro_lab_mile_stone_item = GetV4ProlabIdProgressResponse200DataKeyedProLabMileStoneItem.from_dict(
                    keyed_pro_lab_mile_stone_item_data
                )

                keyed_pro_lab_mile_stone.append(keyed_pro_lab_mile_stone_item)

        user_eligible_for_certificate = d.pop("user_eligible_for_certificate", UNSET)

        get_v4_prolab_id_progress_response_200_data = cls(
            ownership=ownership,
            ownership_required_for_certification=ownership_required_for_certification,
            keyed_pro_lab_mile_stone=keyed_pro_lab_mile_stone,
            user_eligible_for_certificate=user_eligible_for_certificate,
        )

        get_v4_prolab_id_progress_response_200_data.additional_properties = d
        return get_v4_prolab_id_progress_response_200_data

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
