from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV4PwnboxUsageResponse200")


@_attrs_define
class GetV4PwnboxUsageResponse200:
    """
    Attributes:
        minutes (float | Unset):
        sessions (float | Unset):
        allowed (float | Unset):
        remaining (float | Unset):
        used (float | Unset):
        total (float | Unset):
        active_minutes (float | Unset):
    """

    minutes: float | Unset = UNSET
    sessions: float | Unset = UNSET
    allowed: float | Unset = UNSET
    remaining: float | Unset = UNSET
    used: float | Unset = UNSET
    total: float | Unset = UNSET
    active_minutes: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minutes = self.minutes

        sessions = self.sessions

        allowed = self.allowed

        remaining = self.remaining

        used = self.used

        total = self.total

        active_minutes = self.active_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if used is not UNSET:
            field_dict["used"] = used
        if total is not UNSET:
            field_dict["total"] = total
        if active_minutes is not UNSET:
            field_dict["active_minutes"] = active_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minutes = d.pop("minutes", UNSET)

        sessions = d.pop("sessions", UNSET)

        allowed = d.pop("allowed", UNSET)

        remaining = d.pop("remaining", UNSET)

        used = d.pop("used", UNSET)

        total = d.pop("total", UNSET)

        active_minutes = d.pop("active_minutes", UNSET)

        get_v4_pwnbox_usage_response_200 = cls(
            minutes=minutes,
            sessions=sessions,
            allowed=allowed,
            remaining=remaining,
            used=used,
            total=total,
            active_minutes=active_minutes,
        )

        get_v4_pwnbox_usage_response_200.additional_properties = d
        return get_v4_pwnbox_usage_response_200

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
