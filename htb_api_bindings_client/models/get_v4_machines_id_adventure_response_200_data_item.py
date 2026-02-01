from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machines_id_adventure_response_200_data_item_description_type_0 import (
        GetV4MachinesIdAdventureResponse200DataItemDescriptionType0,
    )
    from ..models.get_v4_machines_id_adventure_response_200_data_item_flag_rating_type_0 import (
        GetV4MachinesIdAdventureResponse200DataItemFlagRatingType0,
    )
    from ..models.get_v4_machines_id_adventure_response_200_data_item_hint_type_0 import (
        GetV4MachinesIdAdventureResponse200DataItemHintType0,
    )
    from ..models.get_v4_machines_id_adventure_response_200_data_item_id_type_0 import (
        GetV4MachinesIdAdventureResponse200DataItemIdType0,
    )
    from ..models.get_v4_machines_id_adventure_response_200_data_item_type import (
        GetV4MachinesIdAdventureResponse200DataItemType,
    )


T = TypeVar("T", bound="GetV4MachinesIdAdventureResponse200DataItem")


@_attrs_define
class GetV4MachinesIdAdventureResponse200DataItem:
    """
    Attributes:
        id (GetV4MachinesIdAdventureResponse200DataItemIdType0 | None | Unset):
        title (str | Unset):
        description (GetV4MachinesIdAdventureResponse200DataItemDescriptionType0 | None | Unset):
        hint (GetV4MachinesIdAdventureResponse200DataItemHintType0 | None | Unset):
        type_ (GetV4MachinesIdAdventureResponse200DataItemType | Unset):
        completed (bool | Unset):
        flag_rating (GetV4MachinesIdAdventureResponse200DataItemFlagRatingType0 | None | Unset):
        masked_flag (str | Unset):
    """

    id: GetV4MachinesIdAdventureResponse200DataItemIdType0 | None | Unset = UNSET
    title: str | Unset = UNSET
    description: GetV4MachinesIdAdventureResponse200DataItemDescriptionType0 | None | Unset = UNSET
    hint: GetV4MachinesIdAdventureResponse200DataItemHintType0 | None | Unset = UNSET
    type_: GetV4MachinesIdAdventureResponse200DataItemType | Unset = UNSET
    completed: bool | Unset = UNSET
    flag_rating: GetV4MachinesIdAdventureResponse200DataItemFlagRatingType0 | None | Unset = UNSET
    masked_flag: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machines_id_adventure_response_200_data_item_description_type_0 import (
            GetV4MachinesIdAdventureResponse200DataItemDescriptionType0,
        )
        from ..models.get_v4_machines_id_adventure_response_200_data_item_flag_rating_type_0 import (
            GetV4MachinesIdAdventureResponse200DataItemFlagRatingType0,
        )
        from ..models.get_v4_machines_id_adventure_response_200_data_item_hint_type_0 import (
            GetV4MachinesIdAdventureResponse200DataItemHintType0,
        )
        from ..models.get_v4_machines_id_adventure_response_200_data_item_id_type_0 import (
            GetV4MachinesIdAdventureResponse200DataItemIdType0,
        )

        id: dict[str, Any] | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, GetV4MachinesIdAdventureResponse200DataItemIdType0):
            id = self.id.to_dict()
        else:
            id = self.id

        title = self.title

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, GetV4MachinesIdAdventureResponse200DataItemDescriptionType0):
            description = self.description.to_dict()
        else:
            description = self.description

        hint: dict[str, Any] | None | Unset
        if isinstance(self.hint, Unset):
            hint = UNSET
        elif isinstance(self.hint, GetV4MachinesIdAdventureResponse200DataItemHintType0):
            hint = self.hint.to_dict()
        else:
            hint = self.hint

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        completed = self.completed

        flag_rating: dict[str, Any] | None | Unset
        if isinstance(self.flag_rating, Unset):
            flag_rating = UNSET
        elif isinstance(self.flag_rating, GetV4MachinesIdAdventureResponse200DataItemFlagRatingType0):
            flag_rating = self.flag_rating.to_dict()
        else:
            flag_rating = self.flag_rating

        masked_flag = self.masked_flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if hint is not UNSET:
            field_dict["hint"] = hint
        if type_ is not UNSET:
            field_dict["type"] = type_
        if completed is not UNSET:
            field_dict["completed"] = completed
        if flag_rating is not UNSET:
            field_dict["flag_rating"] = flag_rating
        if masked_flag is not UNSET:
            field_dict["masked_flag"] = masked_flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machines_id_adventure_response_200_data_item_description_type_0 import (
            GetV4MachinesIdAdventureResponse200DataItemDescriptionType0,
        )
        from ..models.get_v4_machines_id_adventure_response_200_data_item_flag_rating_type_0 import (
            GetV4MachinesIdAdventureResponse200DataItemFlagRatingType0,
        )
        from ..models.get_v4_machines_id_adventure_response_200_data_item_hint_type_0 import (
            GetV4MachinesIdAdventureResponse200DataItemHintType0,
        )
        from ..models.get_v4_machines_id_adventure_response_200_data_item_id_type_0 import (
            GetV4MachinesIdAdventureResponse200DataItemIdType0,
        )
        from ..models.get_v4_machines_id_adventure_response_200_data_item_type import (
            GetV4MachinesIdAdventureResponse200DataItemType,
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> GetV4MachinesIdAdventureResponse200DataItemIdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                id_type_0 = GetV4MachinesIdAdventureResponse200DataItemIdType0.from_dict(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachinesIdAdventureResponse200DataItemIdType0 | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        title = d.pop("title", UNSET)

        def _parse_description(
            data: object,
        ) -> GetV4MachinesIdAdventureResponse200DataItemDescriptionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                description_type_0 = GetV4MachinesIdAdventureResponse200DataItemDescriptionType0.from_dict(data)

                return description_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachinesIdAdventureResponse200DataItemDescriptionType0 | None | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_hint(data: object) -> GetV4MachinesIdAdventureResponse200DataItemHintType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hint_type_0 = GetV4MachinesIdAdventureResponse200DataItemHintType0.from_dict(data)

                return hint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachinesIdAdventureResponse200DataItemHintType0 | None | Unset, data)

        hint = _parse_hint(d.pop("hint", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: GetV4MachinesIdAdventureResponse200DataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GetV4MachinesIdAdventureResponse200DataItemType.from_dict(_type_)

        completed = d.pop("completed", UNSET)

        def _parse_flag_rating(
            data: object,
        ) -> GetV4MachinesIdAdventureResponse200DataItemFlagRatingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                flag_rating_type_0 = GetV4MachinesIdAdventureResponse200DataItemFlagRatingType0.from_dict(data)

                return flag_rating_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachinesIdAdventureResponse200DataItemFlagRatingType0 | None | Unset, data)

        flag_rating = _parse_flag_rating(d.pop("flag_rating", UNSET))

        masked_flag = d.pop("masked_flag", UNSET)

        get_v4_machines_id_adventure_response_200_data_item = cls(
            id=id,
            title=title,
            description=description,
            hint=hint,
            type_=type_,
            completed=completed,
            flag_rating=flag_rating,
            masked_flag=masked_flag,
        )

        get_v4_machines_id_adventure_response_200_data_item.additional_properties = d
        return get_v4_machines_id_adventure_response_200_data_item

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
