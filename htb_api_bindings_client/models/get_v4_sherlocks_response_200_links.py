from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_sherlocks_response_200_links_prev_type_0 import GetV4SherlocksResponse200LinksPrevType0


T = TypeVar("T", bound="GetV4SherlocksResponse200Links")


@_attrs_define
class GetV4SherlocksResponse200Links:
    """
    Attributes:
        first (str | Unset):
        last (str | Unset):
        prev (GetV4SherlocksResponse200LinksPrevType0 | None | Unset):
        next_ (str | Unset):
    """

    first: str | Unset = UNSET
    last: str | Unset = UNSET
    prev: GetV4SherlocksResponse200LinksPrevType0 | None | Unset = UNSET
    next_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_sherlocks_response_200_links_prev_type_0 import GetV4SherlocksResponse200LinksPrevType0

        first = self.first

        last = self.last

        prev: dict[str, Any] | None | Unset
        if isinstance(self.prev, Unset):
            prev = UNSET
        elif isinstance(self.prev, GetV4SherlocksResponse200LinksPrevType0):
            prev = self.prev.to_dict()
        else:
            prev = self.prev

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if prev is not UNSET:
            field_dict["prev"] = prev
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_sherlocks_response_200_links_prev_type_0 import GetV4SherlocksResponse200LinksPrevType0

        d = dict(src_dict)
        first = d.pop("first", UNSET)

        last = d.pop("last", UNSET)

        def _parse_prev(data: object) -> GetV4SherlocksResponse200LinksPrevType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prev_type_0 = GetV4SherlocksResponse200LinksPrevType0.from_dict(data)

                return prev_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SherlocksResponse200LinksPrevType0 | None | Unset, data)

        prev = _parse_prev(d.pop("prev", UNSET))

        next_ = d.pop("next", UNSET)

        get_v4_sherlocks_response_200_links = cls(
            first=first,
            last=last,
            prev=prev,
            next_=next_,
        )

        get_v4_sherlocks_response_200_links.additional_properties = d
        return get_v4_sherlocks_response_200_links

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
