from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_sherlocks_id_progress_response_200_data_own_rank_type_0 import (
        GetV4SherlocksIdProgressResponse200DataOwnRankType0,
    )


T = TypeVar("T", bound="GetV4SherlocksIdProgressResponse200Data")


@_attrs_define
class GetV4SherlocksIdProgressResponse200Data:
    """
    Attributes:
        is_owned (bool | Unset):
        progress (float | Unset):
        total_tasks (float | Unset):
        tasks_answered (float | Unset):
        own_rank (GetV4SherlocksIdProgressResponse200DataOwnRankType0 | None | Unset):
    """

    is_owned: bool | Unset = UNSET
    progress: float | Unset = UNSET
    total_tasks: float | Unset = UNSET
    tasks_answered: float | Unset = UNSET
    own_rank: GetV4SherlocksIdProgressResponse200DataOwnRankType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_sherlocks_id_progress_response_200_data_own_rank_type_0 import (
            GetV4SherlocksIdProgressResponse200DataOwnRankType0,
        )

        is_owned = self.is_owned

        progress = self.progress

        total_tasks = self.total_tasks

        tasks_answered = self.tasks_answered

        own_rank: dict[str, Any] | None | Unset
        if isinstance(self.own_rank, Unset):
            own_rank = UNSET
        elif isinstance(self.own_rank, GetV4SherlocksIdProgressResponse200DataOwnRankType0):
            own_rank = self.own_rank.to_dict()
        else:
            own_rank = self.own_rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_owned is not UNSET:
            field_dict["is_owned"] = is_owned
        if progress is not UNSET:
            field_dict["progress"] = progress
        if total_tasks is not UNSET:
            field_dict["total_tasks"] = total_tasks
        if tasks_answered is not UNSET:
            field_dict["tasks_answered"] = tasks_answered
        if own_rank is not UNSET:
            field_dict["own_rank"] = own_rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_sherlocks_id_progress_response_200_data_own_rank_type_0 import (
            GetV4SherlocksIdProgressResponse200DataOwnRankType0,
        )

        d = dict(src_dict)
        is_owned = d.pop("is_owned", UNSET)

        progress = d.pop("progress", UNSET)

        total_tasks = d.pop("total_tasks", UNSET)

        tasks_answered = d.pop("tasks_answered", UNSET)

        def _parse_own_rank(data: object) -> GetV4SherlocksIdProgressResponse200DataOwnRankType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                own_rank_type_0 = GetV4SherlocksIdProgressResponse200DataOwnRankType0.from_dict(data)

                return own_rank_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4SherlocksIdProgressResponse200DataOwnRankType0 | None | Unset, data)

        own_rank = _parse_own_rank(d.pop("own_rank", UNSET))

        get_v4_sherlocks_id_progress_response_200_data = cls(
            is_owned=is_owned,
            progress=progress,
            total_tasks=total_tasks,
            tasks_answered=tasks_answered,
            own_rank=own_rank,
        )

        get_v4_sherlocks_id_progress_response_200_data.additional_properties = d
        return get_v4_sherlocks_id_progress_response_200_data

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
