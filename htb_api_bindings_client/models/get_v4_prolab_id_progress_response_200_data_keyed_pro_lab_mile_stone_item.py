from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4ProlabIdProgressResponse200DataKeyedProLabMileStoneItem")


@_attrs_define
class GetV4ProlabIdProgressResponse200DataKeyedProLabMileStoneItem:
    """
    Attributes:
        percent (float | Unset):
        icon (str | Unset):
        text (str | Unset):
        description (str | Unset):
        is_milestone_reached (bool | Unset):
        rarity (float | Unset):
    """

    percent: float | Unset = UNSET
    icon: str | Unset = UNSET
    text: str | Unset = UNSET
    description: str | Unset = UNSET
    is_milestone_reached: bool | Unset = UNSET
    rarity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percent = self.percent

        icon = self.icon

        text = self.text

        description = self.description

        is_milestone_reached = self.is_milestone_reached

        rarity = self.rarity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent is not UNSET:
            field_dict["percent"] = percent
        if icon is not UNSET:
            field_dict["icon"] = icon
        if text is not UNSET:
            field_dict["text"] = text
        if description is not UNSET:
            field_dict["description"] = description
        if is_milestone_reached is not UNSET:
            field_dict["isMilestoneReached"] = is_milestone_reached
        if rarity is not UNSET:
            field_dict["rarity"] = rarity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percent = d.pop("percent", UNSET)

        icon = d.pop("icon", UNSET)

        text = d.pop("text", UNSET)

        description = d.pop("description", UNSET)

        is_milestone_reached = d.pop("isMilestoneReached", UNSET)

        rarity = d.pop("rarity", UNSET)

        get_v4_prolab_id_progress_response_200_data_keyed_pro_lab_mile_stone_item = cls(
            percent=percent,
            icon=icon,
            text=text,
            description=description,
            is_milestone_reached=is_milestone_reached,
            rarity=rarity,
        )

        get_v4_prolab_id_progress_response_200_data_keyed_pro_lab_mile_stone_item.additional_properties = d
        return get_v4_prolab_id_progress_response_200_data_keyed_pro_lab_mile_stone_item

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
