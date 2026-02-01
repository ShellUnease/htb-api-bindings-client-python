from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machine_recommended_response_200_card_1_maker import (
        GetV4MachineRecommendedResponse200Card1Maker,
    )
    from ..models.get_v4_machine_recommended_response_200_card_1_maker_2_type_0 import (
        GetV4MachineRecommendedResponse200Card1Maker2Type0,
    )


T = TypeVar("T", bound="GetV4MachineRecommendedResponse200Card1")


@_attrs_define
class GetV4MachineRecommendedResponse200Card1:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        os (str | Unset):
        release (str | Unset):
        retired (float | Unset):
        difficulty_text (str | Unset):
        avatar (str | Unset):
        maker (GetV4MachineRecommendedResponse200Card1Maker | Unset):
        maker2 (GetV4MachineRecommendedResponse200Card1Maker2Type0 | None | Unset):
        points (float | Unset):
        is_todo (bool | Unset):
        type_card (str | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    os: str | Unset = UNSET
    release: str | Unset = UNSET
    retired: float | Unset = UNSET
    difficulty_text: str | Unset = UNSET
    avatar: str | Unset = UNSET
    maker: GetV4MachineRecommendedResponse200Card1Maker | Unset = UNSET
    maker2: GetV4MachineRecommendedResponse200Card1Maker2Type0 | None | Unset = UNSET
    points: float | Unset = UNSET
    is_todo: bool | Unset = UNSET
    type_card: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machine_recommended_response_200_card_1_maker_2_type_0 import (
            GetV4MachineRecommendedResponse200Card1Maker2Type0,
        )

        id = self.id

        name = self.name

        os = self.os

        release = self.release

        retired = self.retired

        difficulty_text = self.difficulty_text

        avatar = self.avatar

        maker: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maker, Unset):
            maker = self.maker.to_dict()

        maker2: dict[str, Any] | None | Unset
        if isinstance(self.maker2, Unset):
            maker2 = UNSET
        elif isinstance(self.maker2, GetV4MachineRecommendedResponse200Card1Maker2Type0):
            maker2 = self.maker2.to_dict()
        else:
            maker2 = self.maker2

        points = self.points

        is_todo = self.is_todo

        type_card = self.type_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if release is not UNSET:
            field_dict["release"] = release
        if retired is not UNSET:
            field_dict["retired"] = retired
        if difficulty_text is not UNSET:
            field_dict["difficultyText"] = difficulty_text
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if maker is not UNSET:
            field_dict["maker"] = maker
        if maker2 is not UNSET:
            field_dict["maker2"] = maker2
        if points is not UNSET:
            field_dict["points"] = points
        if is_todo is not UNSET:
            field_dict["isTodo"] = is_todo
        if type_card is not UNSET:
            field_dict["typeCard"] = type_card

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machine_recommended_response_200_card_1_maker import (
            GetV4MachineRecommendedResponse200Card1Maker,
        )
        from ..models.get_v4_machine_recommended_response_200_card_1_maker_2_type_0 import (
            GetV4MachineRecommendedResponse200Card1Maker2Type0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        release = d.pop("release", UNSET)

        retired = d.pop("retired", UNSET)

        difficulty_text = d.pop("difficultyText", UNSET)

        avatar = d.pop("avatar", UNSET)

        _maker = d.pop("maker", UNSET)
        maker: GetV4MachineRecommendedResponse200Card1Maker | Unset
        if isinstance(_maker, Unset):
            maker = UNSET
        else:
            maker = GetV4MachineRecommendedResponse200Card1Maker.from_dict(_maker)

        def _parse_maker2(data: object) -> GetV4MachineRecommendedResponse200Card1Maker2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                maker2_type_0 = GetV4MachineRecommendedResponse200Card1Maker2Type0.from_dict(data)

                return maker2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachineRecommendedResponse200Card1Maker2Type0 | None | Unset, data)

        maker2 = _parse_maker2(d.pop("maker2", UNSET))

        points = d.pop("points", UNSET)

        is_todo = d.pop("isTodo", UNSET)

        type_card = d.pop("typeCard", UNSET)

        get_v4_machine_recommended_response_200_card_1 = cls(
            id=id,
            name=name,
            os=os,
            release=release,
            retired=retired,
            difficulty_text=difficulty_text,
            avatar=avatar,
            maker=maker,
            maker2=maker2,
            points=points,
            is_todo=is_todo,
            type_card=type_card,
        )

        get_v4_machine_recommended_response_200_card_1.additional_properties = d
        return get_v4_machine_recommended_response_200_card_1

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
