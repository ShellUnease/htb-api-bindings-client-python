from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_sherlocks_id_play_response_200_data_blood import GetV4SherlocksIdPlayResponse200DataBlood
    from ..models.get_v4_sherlocks_id_play_response_200_data_creators_item import (
        GetV4SherlocksIdPlayResponse200DataCreatorsItem,
    )
    from ..models.get_v4_sherlocks_id_play_response_200_data_play_info import (
        GetV4SherlocksIdPlayResponse200DataPlayInfo,
    )


T = TypeVar("T", bound="GetV4SherlocksIdPlayResponse200Data")


@_attrs_define
class GetV4SherlocksIdPlayResponse200Data:
    """
    Attributes:
        id (float | Unset):
        scenario (str | Unset):
        creators (list[GetV4SherlocksIdPlayResponse200DataCreatorsItem] | Unset):
        blood (GetV4SherlocksIdPlayResponse200DataBlood | Unset):
        file_name (str | Unset):
        file_size (str | Unset):
        play_info (GetV4SherlocksIdPlayResponse200DataPlayInfo | Unset):
    """

    id: float | Unset = UNSET
    scenario: str | Unset = UNSET
    creators: list[GetV4SherlocksIdPlayResponse200DataCreatorsItem] | Unset = UNSET
    blood: GetV4SherlocksIdPlayResponse200DataBlood | Unset = UNSET
    file_name: str | Unset = UNSET
    file_size: str | Unset = UNSET
    play_info: GetV4SherlocksIdPlayResponse200DataPlayInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        scenario = self.scenario

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

        blood: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blood, Unset):
            blood = self.blood.to_dict()

        file_name = self.file_name

        file_size = self.file_size

        play_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.play_info, Unset):
            play_info = self.play_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if scenario is not UNSET:
            field_dict["scenario"] = scenario
        if creators is not UNSET:
            field_dict["creators"] = creators
        if blood is not UNSET:
            field_dict["blood"] = blood
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if play_info is not UNSET:
            field_dict["play_info"] = play_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_sherlocks_id_play_response_200_data_blood import GetV4SherlocksIdPlayResponse200DataBlood
        from ..models.get_v4_sherlocks_id_play_response_200_data_creators_item import (
            GetV4SherlocksIdPlayResponse200DataCreatorsItem,
        )
        from ..models.get_v4_sherlocks_id_play_response_200_data_play_info import (
            GetV4SherlocksIdPlayResponse200DataPlayInfo,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        scenario = d.pop("scenario", UNSET)

        _creators = d.pop("creators", UNSET)
        creators: list[GetV4SherlocksIdPlayResponse200DataCreatorsItem] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = GetV4SherlocksIdPlayResponse200DataCreatorsItem.from_dict(creators_item_data)

                creators.append(creators_item)

        _blood = d.pop("blood", UNSET)
        blood: GetV4SherlocksIdPlayResponse200DataBlood | Unset
        if isinstance(_blood, Unset):
            blood = UNSET
        else:
            blood = GetV4SherlocksIdPlayResponse200DataBlood.from_dict(_blood)

        file_name = d.pop("file_name", UNSET)

        file_size = d.pop("file_size", UNSET)

        _play_info = d.pop("play_info", UNSET)
        play_info: GetV4SherlocksIdPlayResponse200DataPlayInfo | Unset
        if isinstance(_play_info, Unset):
            play_info = UNSET
        else:
            play_info = GetV4SherlocksIdPlayResponse200DataPlayInfo.from_dict(_play_info)

        get_v4_sherlocks_id_play_response_200_data = cls(
            id=id,
            scenario=scenario,
            creators=creators,
            blood=blood,
            file_name=file_name,
            file_size=file_size,
            play_info=play_info,
        )

        get_v4_sherlocks_id_play_response_200_data.additional_properties = d
        return get_v4_sherlocks_id_play_response_200_data

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
