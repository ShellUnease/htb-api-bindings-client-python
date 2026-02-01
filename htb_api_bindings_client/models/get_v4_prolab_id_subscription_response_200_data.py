from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_prolab_id_subscription_response_200_data_ends_at_type_0 import (
        GetV4ProlabIdSubscriptionResponse200DataEndsAtType0,
    )
    from ..models.get_v4_prolab_id_subscription_response_200_data_name_type_0 import (
        GetV4ProlabIdSubscriptionResponse200DataNameType0,
    )
    from ..models.get_v4_prolab_id_subscription_response_200_data_renews_at_type_0 import (
        GetV4ProlabIdSubscriptionResponse200DataRenewsAtType0,
    )
    from ..models.get_v4_prolab_id_subscription_response_200_data_subscription_period_type_0 import (
        GetV4ProlabIdSubscriptionResponse200DataSubscriptionPeriodType0,
    )
    from ..models.get_v4_prolab_id_subscription_response_200_data_type_type_0 import (
        GetV4ProlabIdSubscriptionResponse200DataTypeType0,
    )


T = TypeVar("T", bound="GetV4ProlabIdSubscriptionResponse200Data")


@_attrs_define
class GetV4ProlabIdSubscriptionResponse200Data:
    """
    Attributes:
        active (bool | Unset):
        type_ (GetV4ProlabIdSubscriptionResponse200DataTypeType0 | None | Unset):
        name (GetV4ProlabIdSubscriptionResponse200DataNameType0 | None | Unset):
        renews_at (GetV4ProlabIdSubscriptionResponse200DataRenewsAtType0 | None | Unset):
        ends_at (GetV4ProlabIdSubscriptionResponse200DataEndsAtType0 | None | Unset):
        subscription_period (GetV4ProlabIdSubscriptionResponse200DataSubscriptionPeriodType0 | None | Unset):
    """

    active: bool | Unset = UNSET
    type_: GetV4ProlabIdSubscriptionResponse200DataTypeType0 | None | Unset = UNSET
    name: GetV4ProlabIdSubscriptionResponse200DataNameType0 | None | Unset = UNSET
    renews_at: GetV4ProlabIdSubscriptionResponse200DataRenewsAtType0 | None | Unset = UNSET
    ends_at: GetV4ProlabIdSubscriptionResponse200DataEndsAtType0 | None | Unset = UNSET
    subscription_period: GetV4ProlabIdSubscriptionResponse200DataSubscriptionPeriodType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_prolab_id_subscription_response_200_data_ends_at_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataEndsAtType0,
        )
        from ..models.get_v4_prolab_id_subscription_response_200_data_name_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataNameType0,
        )
        from ..models.get_v4_prolab_id_subscription_response_200_data_renews_at_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataRenewsAtType0,
        )
        from ..models.get_v4_prolab_id_subscription_response_200_data_subscription_period_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataSubscriptionPeriodType0,
        )
        from ..models.get_v4_prolab_id_subscription_response_200_data_type_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataTypeType0,
        )

        active = self.active

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, GetV4ProlabIdSubscriptionResponse200DataTypeType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        name: dict[str, Any] | None | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, GetV4ProlabIdSubscriptionResponse200DataNameType0):
            name = self.name.to_dict()
        else:
            name = self.name

        renews_at: dict[str, Any] | None | Unset
        if isinstance(self.renews_at, Unset):
            renews_at = UNSET
        elif isinstance(self.renews_at, GetV4ProlabIdSubscriptionResponse200DataRenewsAtType0):
            renews_at = self.renews_at.to_dict()
        else:
            renews_at = self.renews_at

        ends_at: dict[str, Any] | None | Unset
        if isinstance(self.ends_at, Unset):
            ends_at = UNSET
        elif isinstance(self.ends_at, GetV4ProlabIdSubscriptionResponse200DataEndsAtType0):
            ends_at = self.ends_at.to_dict()
        else:
            ends_at = self.ends_at

        subscription_period: dict[str, Any] | None | Unset
        if isinstance(self.subscription_period, Unset):
            subscription_period = UNSET
        elif isinstance(self.subscription_period, GetV4ProlabIdSubscriptionResponse200DataSubscriptionPeriodType0):
            subscription_period = self.subscription_period.to_dict()
        else:
            subscription_period = self.subscription_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if renews_at is not UNSET:
            field_dict["renews_at"] = renews_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if subscription_period is not UNSET:
            field_dict["subscription_period"] = subscription_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_prolab_id_subscription_response_200_data_ends_at_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataEndsAtType0,
        )
        from ..models.get_v4_prolab_id_subscription_response_200_data_name_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataNameType0,
        )
        from ..models.get_v4_prolab_id_subscription_response_200_data_renews_at_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataRenewsAtType0,
        )
        from ..models.get_v4_prolab_id_subscription_response_200_data_subscription_period_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataSubscriptionPeriodType0,
        )
        from ..models.get_v4_prolab_id_subscription_response_200_data_type_type_0 import (
            GetV4ProlabIdSubscriptionResponse200DataTypeType0,
        )

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        def _parse_type_(data: object) -> GetV4ProlabIdSubscriptionResponse200DataTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_0 = GetV4ProlabIdSubscriptionResponse200DataTypeType0.from_dict(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdSubscriptionResponse200DataTypeType0 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_name(data: object) -> GetV4ProlabIdSubscriptionResponse200DataNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_0 = GetV4ProlabIdSubscriptionResponse200DataNameType0.from_dict(data)

                return name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdSubscriptionResponse200DataNameType0 | None | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_renews_at(data: object) -> GetV4ProlabIdSubscriptionResponse200DataRenewsAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                renews_at_type_0 = GetV4ProlabIdSubscriptionResponse200DataRenewsAtType0.from_dict(data)

                return renews_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdSubscriptionResponse200DataRenewsAtType0 | None | Unset, data)

        renews_at = _parse_renews_at(d.pop("renews_at", UNSET))

        def _parse_ends_at(data: object) -> GetV4ProlabIdSubscriptionResponse200DataEndsAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ends_at_type_0 = GetV4ProlabIdSubscriptionResponse200DataEndsAtType0.from_dict(data)

                return ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdSubscriptionResponse200DataEndsAtType0 | None | Unset, data)

        ends_at = _parse_ends_at(d.pop("ends_at", UNSET))

        def _parse_subscription_period(
            data: object,
        ) -> GetV4ProlabIdSubscriptionResponse200DataSubscriptionPeriodType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscription_period_type_0 = GetV4ProlabIdSubscriptionResponse200DataSubscriptionPeriodType0.from_dict(
                    data
                )

                return subscription_period_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ProlabIdSubscriptionResponse200DataSubscriptionPeriodType0 | None | Unset, data)

        subscription_period = _parse_subscription_period(d.pop("subscription_period", UNSET))

        get_v4_prolab_id_subscription_response_200_data = cls(
            active=active,
            type_=type_,
            name=name,
            renews_at=renews_at,
            ends_at=ends_at,
            subscription_period=subscription_period,
        )

        get_v4_prolab_id_subscription_response_200_data.additional_properties = d
        return get_v4_prolab_id_subscription_response_200_data

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
