from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_machines_id_tasks_response_200_data_item_prerequisite_id_type_0 import (
        GetV4MachinesIdTasksResponse200DataItemPrerequisiteIdType0,
    )
    from ..models.get_v4_machines_id_tasks_response_200_data_item_task_type import (
        GetV4MachinesIdTasksResponse200DataItemTaskType,
    )
    from ..models.get_v4_machines_id_tasks_response_200_data_item_type import (
        GetV4MachinesIdTasksResponse200DataItemType,
    )


T = TypeVar("T", bound="GetV4MachinesIdTasksResponse200DataItem")


@_attrs_define
class GetV4MachinesIdTasksResponse200DataItem:
    """
    Attributes:
        id (float | Unset):
        title (str | Unset):
        description (str | Unset):
        hint (str | Unset):
        type_ (GetV4MachinesIdTasksResponse200DataItemType | Unset):
        task_type (GetV4MachinesIdTasksResponse200DataItemTaskType | Unset):
        prerequisite_id (GetV4MachinesIdTasksResponse200DataItemPrerequisiteIdType0 | None | Unset):
        completed (bool | Unset):
        masked_flag (str | Unset):
        options (list[Any] | Unset):
    """

    id: float | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    hint: str | Unset = UNSET
    type_: GetV4MachinesIdTasksResponse200DataItemType | Unset = UNSET
    task_type: GetV4MachinesIdTasksResponse200DataItemTaskType | Unset = UNSET
    prerequisite_id: GetV4MachinesIdTasksResponse200DataItemPrerequisiteIdType0 | None | Unset = UNSET
    completed: bool | Unset = UNSET
    masked_flag: str | Unset = UNSET
    options: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_machines_id_tasks_response_200_data_item_prerequisite_id_type_0 import (
            GetV4MachinesIdTasksResponse200DataItemPrerequisiteIdType0,
        )

        id = self.id

        title = self.title

        description = self.description

        hint = self.hint

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        task_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.to_dict()

        prerequisite_id: dict[str, Any] | None | Unset
        if isinstance(self.prerequisite_id, Unset):
            prerequisite_id = UNSET
        elif isinstance(self.prerequisite_id, GetV4MachinesIdTasksResponse200DataItemPrerequisiteIdType0):
            prerequisite_id = self.prerequisite_id.to_dict()
        else:
            prerequisite_id = self.prerequisite_id

        completed = self.completed

        masked_flag = self.masked_flag

        options: list[Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

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
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if prerequisite_id is not UNSET:
            field_dict["prerequisite_id"] = prerequisite_id
        if completed is not UNSET:
            field_dict["completed"] = completed
        if masked_flag is not UNSET:
            field_dict["masked_flag"] = masked_flag
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_machines_id_tasks_response_200_data_item_prerequisite_id_type_0 import (
            GetV4MachinesIdTasksResponse200DataItemPrerequisiteIdType0,
        )
        from ..models.get_v4_machines_id_tasks_response_200_data_item_task_type import (
            GetV4MachinesIdTasksResponse200DataItemTaskType,
        )
        from ..models.get_v4_machines_id_tasks_response_200_data_item_type import (
            GetV4MachinesIdTasksResponse200DataItemType,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        hint = d.pop("hint", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GetV4MachinesIdTasksResponse200DataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GetV4MachinesIdTasksResponse200DataItemType.from_dict(_type_)

        _task_type = d.pop("task_type", UNSET)
        task_type: GetV4MachinesIdTasksResponse200DataItemTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = GetV4MachinesIdTasksResponse200DataItemTaskType.from_dict(_task_type)

        def _parse_prerequisite_id(
            data: object,
        ) -> GetV4MachinesIdTasksResponse200DataItemPrerequisiteIdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prerequisite_id_type_0 = GetV4MachinesIdTasksResponse200DataItemPrerequisiteIdType0.from_dict(data)

                return prerequisite_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4MachinesIdTasksResponse200DataItemPrerequisiteIdType0 | None | Unset, data)

        prerequisite_id = _parse_prerequisite_id(d.pop("prerequisite_id", UNSET))

        completed = d.pop("completed", UNSET)

        masked_flag = d.pop("masked_flag", UNSET)

        options = cast(list[Any], d.pop("options", UNSET))

        get_v4_machines_id_tasks_response_200_data_item = cls(
            id=id,
            title=title,
            description=description,
            hint=hint,
            type_=type_,
            task_type=task_type,
            prerequisite_id=prerequisite_id,
            completed=completed,
            masked_flag=masked_flag,
            options=options,
        )

        get_v4_machines_id_tasks_response_200_data_item.additional_properties = d
        return get_v4_machines_id_tasks_response_200_data_item

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
