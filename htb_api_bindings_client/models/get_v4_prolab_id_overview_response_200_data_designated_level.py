from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4ProlabIdOverviewResponse200DataDesignatedLevel")


@_attrs_define
class GetV4ProlabIdOverviewResponse200DataDesignatedLevel:
    """
    Attributes:
        category (str | Unset):
        level (float | Unset):
        description (str | Unset):
        team (str | Unset):
    """

    category: str | Unset = UNSET
    level: float | Unset = UNSET
    description: str | Unset = UNSET
    team: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        level = self.level

        description = self.description

        team = self.team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if level is not UNSET:
            field_dict["level"] = level
        if description is not UNSET:
            field_dict["description"] = description
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        level = d.pop("level", UNSET)

        description = d.pop("description", UNSET)

        team = d.pop("team", UNSET)

        get_v4_prolab_id_overview_response_200_data_designated_level = cls(
            category=category,
            level=level,
            description=description,
            team=team,
        )

        get_v4_prolab_id_overview_response_200_data_designated_level.additional_properties = d
        return get_v4_prolab_id_overview_response_200_data_designated_level

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
