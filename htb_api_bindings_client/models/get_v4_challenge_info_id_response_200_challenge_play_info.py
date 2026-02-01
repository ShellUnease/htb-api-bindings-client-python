from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_expires_at_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengePlayInfoExpiresAtType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_ip_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengePlayInfoIpType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_ports_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengePlayInfoPortsType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_status_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengePlayInfoStatusType0,
    )


T = TypeVar("T", bound="GetV4ChallengeInfoIdResponse200ChallengePlayInfo")


@_attrs_define
class GetV4ChallengeInfoIdResponse200ChallengePlayInfo:
    """
    Attributes:
        status (GetV4ChallengeInfoIdResponse200ChallengePlayInfoStatusType0 | None | Unset):
        expires_at (GetV4ChallengeInfoIdResponse200ChallengePlayInfoExpiresAtType0 | None | Unset):
        ip (GetV4ChallengeInfoIdResponse200ChallengePlayInfoIpType0 | None | Unset):
        ports (GetV4ChallengeInfoIdResponse200ChallengePlayInfoPortsType0 | None | Unset):
    """

    status: GetV4ChallengeInfoIdResponse200ChallengePlayInfoStatusType0 | None | Unset = UNSET
    expires_at: GetV4ChallengeInfoIdResponse200ChallengePlayInfoExpiresAtType0 | None | Unset = UNSET
    ip: GetV4ChallengeInfoIdResponse200ChallengePlayInfoIpType0 | None | Unset = UNSET
    ports: GetV4ChallengeInfoIdResponse200ChallengePlayInfoPortsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_expires_at_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengePlayInfoExpiresAtType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_ip_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengePlayInfoIpType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_ports_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengePlayInfoPortsType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_status_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengePlayInfoStatusType0,
        )

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, GetV4ChallengeInfoIdResponse200ChallengePlayInfoStatusType0):
            status = self.status.to_dict()
        else:
            status = self.status

        expires_at: dict[str, Any] | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, GetV4ChallengeInfoIdResponse200ChallengePlayInfoExpiresAtType0):
            expires_at = self.expires_at.to_dict()
        else:
            expires_at = self.expires_at

        ip: dict[str, Any] | None | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        elif isinstance(self.ip, GetV4ChallengeInfoIdResponse200ChallengePlayInfoIpType0):
            ip = self.ip.to_dict()
        else:
            ip = self.ip

        ports: dict[str, Any] | None | Unset
        if isinstance(self.ports, Unset):
            ports = UNSET
        elif isinstance(self.ports, GetV4ChallengeInfoIdResponse200ChallengePlayInfoPortsType0):
            ports = self.ports.to_dict()
        else:
            ports = self.ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_expires_at_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengePlayInfoExpiresAtType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_ip_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengePlayInfoIpType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_ports_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengePlayInfoPortsType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_play_info_status_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengePlayInfoStatusType0,
        )

        d = dict(src_dict)

        def _parse_status(data: object) -> GetV4ChallengeInfoIdResponse200ChallengePlayInfoStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_0 = GetV4ChallengeInfoIdResponse200ChallengePlayInfoStatusType0.from_dict(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengePlayInfoStatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_expires_at(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengePlayInfoExpiresAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                expires_at_type_0 = GetV4ChallengeInfoIdResponse200ChallengePlayInfoExpiresAtType0.from_dict(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengePlayInfoExpiresAtType0 | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_ip(data: object) -> GetV4ChallengeInfoIdResponse200ChallengePlayInfoIpType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ip_type_0 = GetV4ChallengeInfoIdResponse200ChallengePlayInfoIpType0.from_dict(data)

                return ip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengePlayInfoIpType0 | None | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        def _parse_ports(data: object) -> GetV4ChallengeInfoIdResponse200ChallengePlayInfoPortsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ports_type_0 = GetV4ChallengeInfoIdResponse200ChallengePlayInfoPortsType0.from_dict(data)

                return ports_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengePlayInfoPortsType0 | None | Unset, data)

        ports = _parse_ports(d.pop("ports", UNSET))

        get_v4_challenge_info_id_response_200_challenge_play_info = cls(
            status=status,
            expires_at=expires_at,
            ip=ip,
            ports=ports,
        )

        get_v4_challenge_info_id_response_200_challenge_play_info.additional_properties = d
        return get_v4_challenge_info_id_response_200_challenge_play_info

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
