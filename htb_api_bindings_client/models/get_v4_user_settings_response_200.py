from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_user_settings_response_200_name_change_delay_type_0 import (
        GetV4UserSettingsResponse200NameChangeDelayType0,
    )


T = TypeVar("T", bound="GetV4UserSettingsResponse200")


@_attrs_define
class GetV4UserSettingsResponse200:
    """
    Attributes:
        email (str | Unset):
        public (float | Unset):
        name_change_delay (GetV4UserSettingsResponse200NameChangeDelayType0 | None | Unset):
        hide_machine_tags (float | Unset):
    """

    email: str | Unset = UNSET
    public: float | Unset = UNSET
    name_change_delay: GetV4UserSettingsResponse200NameChangeDelayType0 | None | Unset = UNSET
    hide_machine_tags: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_user_settings_response_200_name_change_delay_type_0 import (
            GetV4UserSettingsResponse200NameChangeDelayType0,
        )

        email = self.email

        public = self.public

        name_change_delay: dict[str, Any] | None | Unset
        if isinstance(self.name_change_delay, Unset):
            name_change_delay = UNSET
        elif isinstance(self.name_change_delay, GetV4UserSettingsResponse200NameChangeDelayType0):
            name_change_delay = self.name_change_delay.to_dict()
        else:
            name_change_delay = self.name_change_delay

        hide_machine_tags = self.hide_machine_tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if public is not UNSET:
            field_dict["public"] = public
        if name_change_delay is not UNSET:
            field_dict["name_change_delay"] = name_change_delay
        if hide_machine_tags is not UNSET:
            field_dict["hide_machine_tags"] = hide_machine_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_user_settings_response_200_name_change_delay_type_0 import (
            GetV4UserSettingsResponse200NameChangeDelayType0,
        )

        d = dict(src_dict)
        email = d.pop("email", UNSET)

        public = d.pop("public", UNSET)

        def _parse_name_change_delay(data: object) -> GetV4UserSettingsResponse200NameChangeDelayType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_change_delay_type_0 = GetV4UserSettingsResponse200NameChangeDelayType0.from_dict(data)

                return name_change_delay_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserSettingsResponse200NameChangeDelayType0 | None | Unset, data)

        name_change_delay = _parse_name_change_delay(d.pop("name_change_delay", UNSET))

        hide_machine_tags = d.pop("hide_machine_tags", UNSET)

        get_v4_user_settings_response_200 = cls(
            email=email,
            public=public,
            name_change_delay=name_change_delay,
            hide_machine_tags=hide_machine_tags,
        )

        get_v4_user_settings_response_200.additional_properties = d
        return get_v4_user_settings_response_200

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
