from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_challenge_info_id_response_200_challenge_auth_user_solve_time_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeAuthUserSolveTimeType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_creator_avatar_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeCreatorAvatarType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_difficulty_chart import (
        GetV4ChallengeInfoIdResponse200ChallengeDifficultyChart,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_docker_ip_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeDockerIpType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_docker_ports_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeDockerPortsType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_docker_status_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeDockerStatusType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_time_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeFirstBloodTimeType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_user_avatar_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserAvatarType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_user_id_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserIdType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_user_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserType0,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_play_info import (
        GetV4ChallengeInfoIdResponse200ChallengePlayInfo,
    )
    from ..models.get_v4_challenge_info_id_response_200_challenge_user_submitted_difficulty_type_0 import (
        GetV4ChallengeInfoIdResponse200ChallengeUserSubmittedDifficultyType0,
    )


T = TypeVar("T", bound="GetV4ChallengeInfoIdResponse200Challenge")


@_attrs_define
class GetV4ChallengeInfoIdResponse200Challenge:
    """
    Attributes:
        id (float | Unset):
        name (str | Unset):
        retired (bool | Unset):
        state (str | Unset):
        difficulty (str | Unset):
        points (str | Unset):
        difficulty_chart (GetV4ChallengeInfoIdResponse200ChallengeDifficultyChart | Unset):
        solves (float | Unset):
        auth_user_solve_time (GetV4ChallengeInfoIdResponse200ChallengeAuthUserSolveTimeType0 | None | Unset):
        likes (float | Unset):
        dislikes (float | Unset):
        stars (float | Unset):
        description (str | Unset):
        category_name (str | Unset):
        first_blood_user_id (GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserIdType0 | None | Unset):
        first_blood_user (GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserType0 | None | Unset):
        first_blood_time (GetV4ChallengeInfoIdResponse200ChallengeFirstBloodTimeType0 | None | Unset):
        first_blood_user_avatar (GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserAvatarType0 | None | Unset):
        creator_id (float | Unset):
        creator_name (str | Unset):
        creator_avatar (GetV4ChallengeInfoIdResponse200ChallengeCreatorAvatarType0 | None | Unset):
        is_respected (bool | Unset):
        creator2_id (float | Unset):
        creator2_name (str | Unset):
        creator2_avatar (str | Unset):
        is_respected_2 (bool | Unset):
        download (bool | Unset):
        file_name (str | Unset):
        file_size (str | Unset):
        sha256 (str | Unset):
        docker (bool | Unset):
        docker_ip (GetV4ChallengeInfoIdResponse200ChallengeDockerIpType0 | None | Unset):
        docker_ports (GetV4ChallengeInfoIdResponse200ChallengeDockerPortsType0 | None | Unset):
        docker_status (GetV4ChallengeInfoIdResponse200ChallengeDockerStatusType0 | None | Unset):
        play_info (GetV4ChallengeInfoIdResponse200ChallengePlayInfo | Unset):
        release_date (str | Unset):
        released (float | Unset):
        auth_user_solve (bool | Unset):
        like_by_auth_user (bool | Unset):
        dislike_by_auth_user (bool | Unset):
        is_todo (bool | Unset):
        recommended (float | Unset):
        auth_user_has_reviewed (bool | Unset):
        user_can_review (bool | Unset):
        can_access_walkthough (bool | Unset):
        tags (list[Any] | Unset):
        play_methods (list[str] | Unset):
        reviews_count (float | Unset):
        has_changelog (bool | Unset):
        show_go_vip (bool | Unset):
        user_submitted_difficulty (GetV4ChallengeInfoIdResponse200ChallengeUserSubmittedDifficultyType0 | None | Unset):
        avatar_url (str | Unset):
    """

    id: float | Unset = UNSET
    name: str | Unset = UNSET
    retired: bool | Unset = UNSET
    state: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    points: str | Unset = UNSET
    difficulty_chart: GetV4ChallengeInfoIdResponse200ChallengeDifficultyChart | Unset = UNSET
    solves: float | Unset = UNSET
    auth_user_solve_time: GetV4ChallengeInfoIdResponse200ChallengeAuthUserSolveTimeType0 | None | Unset = UNSET
    likes: float | Unset = UNSET
    dislikes: float | Unset = UNSET
    stars: float | Unset = UNSET
    description: str | Unset = UNSET
    category_name: str | Unset = UNSET
    first_blood_user_id: GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserIdType0 | None | Unset = UNSET
    first_blood_user: GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserType0 | None | Unset = UNSET
    first_blood_time: GetV4ChallengeInfoIdResponse200ChallengeFirstBloodTimeType0 | None | Unset = UNSET
    first_blood_user_avatar: GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserAvatarType0 | None | Unset = UNSET
    creator_id: float | Unset = UNSET
    creator_name: str | Unset = UNSET
    creator_avatar: GetV4ChallengeInfoIdResponse200ChallengeCreatorAvatarType0 | None | Unset = UNSET
    is_respected: bool | Unset = UNSET
    creator2_id: float | Unset = UNSET
    creator2_name: str | Unset = UNSET
    creator2_avatar: str | Unset = UNSET
    is_respected_2: bool | Unset = UNSET
    download: bool | Unset = UNSET
    file_name: str | Unset = UNSET
    file_size: str | Unset = UNSET
    sha256: str | Unset = UNSET
    docker: bool | Unset = UNSET
    docker_ip: GetV4ChallengeInfoIdResponse200ChallengeDockerIpType0 | None | Unset = UNSET
    docker_ports: GetV4ChallengeInfoIdResponse200ChallengeDockerPortsType0 | None | Unset = UNSET
    docker_status: GetV4ChallengeInfoIdResponse200ChallengeDockerStatusType0 | None | Unset = UNSET
    play_info: GetV4ChallengeInfoIdResponse200ChallengePlayInfo | Unset = UNSET
    release_date: str | Unset = UNSET
    released: float | Unset = UNSET
    auth_user_solve: bool | Unset = UNSET
    like_by_auth_user: bool | Unset = UNSET
    dislike_by_auth_user: bool | Unset = UNSET
    is_todo: bool | Unset = UNSET
    recommended: float | Unset = UNSET
    auth_user_has_reviewed: bool | Unset = UNSET
    user_can_review: bool | Unset = UNSET
    can_access_walkthough: bool | Unset = UNSET
    tags: list[Any] | Unset = UNSET
    play_methods: list[str] | Unset = UNSET
    reviews_count: float | Unset = UNSET
    has_changelog: bool | Unset = UNSET
    show_go_vip: bool | Unset = UNSET
    user_submitted_difficulty: GetV4ChallengeInfoIdResponse200ChallengeUserSubmittedDifficultyType0 | None | Unset = (
        UNSET
    )
    avatar_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_challenge_info_id_response_200_challenge_auth_user_solve_time_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeAuthUserSolveTimeType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_creator_avatar_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeCreatorAvatarType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_docker_ip_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeDockerIpType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_docker_ports_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeDockerPortsType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_docker_status_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeDockerStatusType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_time_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeFirstBloodTimeType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_user_avatar_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserAvatarType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_user_id_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserIdType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_user_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_user_submitted_difficulty_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeUserSubmittedDifficultyType0,
        )

        id = self.id

        name = self.name

        retired = self.retired

        state = self.state

        difficulty = self.difficulty

        points = self.points

        difficulty_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.difficulty_chart, Unset):
            difficulty_chart = self.difficulty_chart.to_dict()

        solves = self.solves

        auth_user_solve_time: dict[str, Any] | None | Unset
        if isinstance(self.auth_user_solve_time, Unset):
            auth_user_solve_time = UNSET
        elif isinstance(self.auth_user_solve_time, GetV4ChallengeInfoIdResponse200ChallengeAuthUserSolveTimeType0):
            auth_user_solve_time = self.auth_user_solve_time.to_dict()
        else:
            auth_user_solve_time = self.auth_user_solve_time

        likes = self.likes

        dislikes = self.dislikes

        stars = self.stars

        description = self.description

        category_name = self.category_name

        first_blood_user_id: dict[str, Any] | None | Unset
        if isinstance(self.first_blood_user_id, Unset):
            first_blood_user_id = UNSET
        elif isinstance(self.first_blood_user_id, GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserIdType0):
            first_blood_user_id = self.first_blood_user_id.to_dict()
        else:
            first_blood_user_id = self.first_blood_user_id

        first_blood_user: dict[str, Any] | None | Unset
        if isinstance(self.first_blood_user, Unset):
            first_blood_user = UNSET
        elif isinstance(self.first_blood_user, GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserType0):
            first_blood_user = self.first_blood_user.to_dict()
        else:
            first_blood_user = self.first_blood_user

        first_blood_time: dict[str, Any] | None | Unset
        if isinstance(self.first_blood_time, Unset):
            first_blood_time = UNSET
        elif isinstance(self.first_blood_time, GetV4ChallengeInfoIdResponse200ChallengeFirstBloodTimeType0):
            first_blood_time = self.first_blood_time.to_dict()
        else:
            first_blood_time = self.first_blood_time

        first_blood_user_avatar: dict[str, Any] | None | Unset
        if isinstance(self.first_blood_user_avatar, Unset):
            first_blood_user_avatar = UNSET
        elif isinstance(
            self.first_blood_user_avatar, GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserAvatarType0
        ):
            first_blood_user_avatar = self.first_blood_user_avatar.to_dict()
        else:
            first_blood_user_avatar = self.first_blood_user_avatar

        creator_id = self.creator_id

        creator_name = self.creator_name

        creator_avatar: dict[str, Any] | None | Unset
        if isinstance(self.creator_avatar, Unset):
            creator_avatar = UNSET
        elif isinstance(self.creator_avatar, GetV4ChallengeInfoIdResponse200ChallengeCreatorAvatarType0):
            creator_avatar = self.creator_avatar.to_dict()
        else:
            creator_avatar = self.creator_avatar

        is_respected = self.is_respected

        creator2_id = self.creator2_id

        creator2_name = self.creator2_name

        creator2_avatar = self.creator2_avatar

        is_respected_2 = self.is_respected_2

        download = self.download

        file_name = self.file_name

        file_size = self.file_size

        sha256 = self.sha256

        docker = self.docker

        docker_ip: dict[str, Any] | None | Unset
        if isinstance(self.docker_ip, Unset):
            docker_ip = UNSET
        elif isinstance(self.docker_ip, GetV4ChallengeInfoIdResponse200ChallengeDockerIpType0):
            docker_ip = self.docker_ip.to_dict()
        else:
            docker_ip = self.docker_ip

        docker_ports: dict[str, Any] | None | Unset
        if isinstance(self.docker_ports, Unset):
            docker_ports = UNSET
        elif isinstance(self.docker_ports, GetV4ChallengeInfoIdResponse200ChallengeDockerPortsType0):
            docker_ports = self.docker_ports.to_dict()
        else:
            docker_ports = self.docker_ports

        docker_status: dict[str, Any] | None | Unset
        if isinstance(self.docker_status, Unset):
            docker_status = UNSET
        elif isinstance(self.docker_status, GetV4ChallengeInfoIdResponse200ChallengeDockerStatusType0):
            docker_status = self.docker_status.to_dict()
        else:
            docker_status = self.docker_status

        play_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.play_info, Unset):
            play_info = self.play_info.to_dict()

        release_date = self.release_date

        released = self.released

        auth_user_solve = self.auth_user_solve

        like_by_auth_user = self.like_by_auth_user

        dislike_by_auth_user = self.dislike_by_auth_user

        is_todo = self.is_todo

        recommended = self.recommended

        auth_user_has_reviewed = self.auth_user_has_reviewed

        user_can_review = self.user_can_review

        can_access_walkthough = self.can_access_walkthough

        tags: list[Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        play_methods: list[str] | Unset = UNSET
        if not isinstance(self.play_methods, Unset):
            play_methods = self.play_methods

        reviews_count = self.reviews_count

        has_changelog = self.has_changelog

        show_go_vip = self.show_go_vip

        user_submitted_difficulty: dict[str, Any] | None | Unset
        if isinstance(self.user_submitted_difficulty, Unset):
            user_submitted_difficulty = UNSET
        elif isinstance(
            self.user_submitted_difficulty, GetV4ChallengeInfoIdResponse200ChallengeUserSubmittedDifficultyType0
        ):
            user_submitted_difficulty = self.user_submitted_difficulty.to_dict()
        else:
            user_submitted_difficulty = self.user_submitted_difficulty

        avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if retired is not UNSET:
            field_dict["retired"] = retired
        if state is not UNSET:
            field_dict["state"] = state
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if points is not UNSET:
            field_dict["points"] = points
        if difficulty_chart is not UNSET:
            field_dict["difficulty_chart"] = difficulty_chart
        if solves is not UNSET:
            field_dict["solves"] = solves
        if auth_user_solve_time is not UNSET:
            field_dict["authUserSolveTime"] = auth_user_solve_time
        if likes is not UNSET:
            field_dict["likes"] = likes
        if dislikes is not UNSET:
            field_dict["dislikes"] = dislikes
        if stars is not UNSET:
            field_dict["stars"] = stars
        if description is not UNSET:
            field_dict["description"] = description
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if first_blood_user_id is not UNSET:
            field_dict["first_blood_user_id"] = first_blood_user_id
        if first_blood_user is not UNSET:
            field_dict["first_blood_user"] = first_blood_user
        if first_blood_time is not UNSET:
            field_dict["first_blood_time"] = first_blood_time
        if first_blood_user_avatar is not UNSET:
            field_dict["first_blood_user_avatar"] = first_blood_user_avatar
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if creator_name is not UNSET:
            field_dict["creator_name"] = creator_name
        if creator_avatar is not UNSET:
            field_dict["creator_avatar"] = creator_avatar
        if is_respected is not UNSET:
            field_dict["isRespected"] = is_respected
        if creator2_id is not UNSET:
            field_dict["creator2_id"] = creator2_id
        if creator2_name is not UNSET:
            field_dict["creator2_name"] = creator2_name
        if creator2_avatar is not UNSET:
            field_dict["creator2_avatar"] = creator2_avatar
        if is_respected_2 is not UNSET:
            field_dict["isRespected2"] = is_respected_2
        if download is not UNSET:
            field_dict["download"] = download
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if docker is not UNSET:
            field_dict["docker"] = docker
        if docker_ip is not UNSET:
            field_dict["docker_ip"] = docker_ip
        if docker_ports is not UNSET:
            field_dict["docker_ports"] = docker_ports
        if docker_status is not UNSET:
            field_dict["docker_status"] = docker_status
        if play_info is not UNSET:
            field_dict["play_info"] = play_info
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if released is not UNSET:
            field_dict["released"] = released
        if auth_user_solve is not UNSET:
            field_dict["authUserSolve"] = auth_user_solve
        if like_by_auth_user is not UNSET:
            field_dict["likeByAuthUser"] = like_by_auth_user
        if dislike_by_auth_user is not UNSET:
            field_dict["dislikeByAuthUser"] = dislike_by_auth_user
        if is_todo is not UNSET:
            field_dict["isTodo"] = is_todo
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if auth_user_has_reviewed is not UNSET:
            field_dict["authUserHasReviewed"] = auth_user_has_reviewed
        if user_can_review is not UNSET:
            field_dict["user_can_review"] = user_can_review
        if can_access_walkthough is not UNSET:
            field_dict["can_access_walkthough"] = can_access_walkthough
        if tags is not UNSET:
            field_dict["tags"] = tags
        if play_methods is not UNSET:
            field_dict["play_methods"] = play_methods
        if reviews_count is not UNSET:
            field_dict["reviews_count"] = reviews_count
        if has_changelog is not UNSET:
            field_dict["has_changelog"] = has_changelog
        if show_go_vip is not UNSET:
            field_dict["show_go_vip"] = show_go_vip
        if user_submitted_difficulty is not UNSET:
            field_dict["user_submitted_difficulty"] = user_submitted_difficulty
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_challenge_info_id_response_200_challenge_auth_user_solve_time_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeAuthUserSolveTimeType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_creator_avatar_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeCreatorAvatarType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_difficulty_chart import (
            GetV4ChallengeInfoIdResponse200ChallengeDifficultyChart,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_docker_ip_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeDockerIpType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_docker_ports_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeDockerPortsType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_docker_status_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeDockerStatusType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_time_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeFirstBloodTimeType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_user_avatar_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserAvatarType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_user_id_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserIdType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_first_blood_user_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserType0,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_play_info import (
            GetV4ChallengeInfoIdResponse200ChallengePlayInfo,
        )
        from ..models.get_v4_challenge_info_id_response_200_challenge_user_submitted_difficulty_type_0 import (
            GetV4ChallengeInfoIdResponse200ChallengeUserSubmittedDifficultyType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        retired = d.pop("retired", UNSET)

        state = d.pop("state", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        points = d.pop("points", UNSET)

        _difficulty_chart = d.pop("difficulty_chart", UNSET)
        difficulty_chart: GetV4ChallengeInfoIdResponse200ChallengeDifficultyChart | Unset
        if isinstance(_difficulty_chart, Unset):
            difficulty_chart = UNSET
        else:
            difficulty_chart = GetV4ChallengeInfoIdResponse200ChallengeDifficultyChart.from_dict(_difficulty_chart)

        solves = d.pop("solves", UNSET)

        def _parse_auth_user_solve_time(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengeAuthUserSolveTimeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_user_solve_time_type_0 = GetV4ChallengeInfoIdResponse200ChallengeAuthUserSolveTimeType0.from_dict(
                    data
                )

                return auth_user_solve_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeAuthUserSolveTimeType0 | None | Unset, data)

        auth_user_solve_time = _parse_auth_user_solve_time(d.pop("authUserSolveTime", UNSET))

        likes = d.pop("likes", UNSET)

        dislikes = d.pop("dislikes", UNSET)

        stars = d.pop("stars", UNSET)

        description = d.pop("description", UNSET)

        category_name = d.pop("category_name", UNSET)

        def _parse_first_blood_user_id(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserIdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                first_blood_user_id_type_0 = GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserIdType0.from_dict(
                    data
                )

                return first_blood_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserIdType0 | None | Unset, data)

        first_blood_user_id = _parse_first_blood_user_id(d.pop("first_blood_user_id", UNSET))

        def _parse_first_blood_user(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                first_blood_user_type_0 = GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserType0.from_dict(data)

                return first_blood_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserType0 | None | Unset, data)

        first_blood_user = _parse_first_blood_user(d.pop("first_blood_user", UNSET))

        def _parse_first_blood_time(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengeFirstBloodTimeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                first_blood_time_type_0 = GetV4ChallengeInfoIdResponse200ChallengeFirstBloodTimeType0.from_dict(data)

                return first_blood_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeFirstBloodTimeType0 | None | Unset, data)

        first_blood_time = _parse_first_blood_time(d.pop("first_blood_time", UNSET))

        def _parse_first_blood_user_avatar(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserAvatarType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                first_blood_user_avatar_type_0 = (
                    GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserAvatarType0.from_dict(data)
                )

                return first_blood_user_avatar_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeFirstBloodUserAvatarType0 | None | Unset, data)

        first_blood_user_avatar = _parse_first_blood_user_avatar(d.pop("first_blood_user_avatar", UNSET))

        creator_id = d.pop("creator_id", UNSET)

        creator_name = d.pop("creator_name", UNSET)

        def _parse_creator_avatar(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengeCreatorAvatarType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                creator_avatar_type_0 = GetV4ChallengeInfoIdResponse200ChallengeCreatorAvatarType0.from_dict(data)

                return creator_avatar_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeCreatorAvatarType0 | None | Unset, data)

        creator_avatar = _parse_creator_avatar(d.pop("creator_avatar", UNSET))

        is_respected = d.pop("isRespected", UNSET)

        creator2_id = d.pop("creator2_id", UNSET)

        creator2_name = d.pop("creator2_name", UNSET)

        creator2_avatar = d.pop("creator2_avatar", UNSET)

        is_respected_2 = d.pop("isRespected2", UNSET)

        download = d.pop("download", UNSET)

        file_name = d.pop("file_name", UNSET)

        file_size = d.pop("file_size", UNSET)

        sha256 = d.pop("sha256", UNSET)

        docker = d.pop("docker", UNSET)

        def _parse_docker_ip(data: object) -> GetV4ChallengeInfoIdResponse200ChallengeDockerIpType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                docker_ip_type_0 = GetV4ChallengeInfoIdResponse200ChallengeDockerIpType0.from_dict(data)

                return docker_ip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeDockerIpType0 | None | Unset, data)

        docker_ip = _parse_docker_ip(d.pop("docker_ip", UNSET))

        def _parse_docker_ports(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengeDockerPortsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                docker_ports_type_0 = GetV4ChallengeInfoIdResponse200ChallengeDockerPortsType0.from_dict(data)

                return docker_ports_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeDockerPortsType0 | None | Unset, data)

        docker_ports = _parse_docker_ports(d.pop("docker_ports", UNSET))

        def _parse_docker_status(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengeDockerStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                docker_status_type_0 = GetV4ChallengeInfoIdResponse200ChallengeDockerStatusType0.from_dict(data)

                return docker_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeDockerStatusType0 | None | Unset, data)

        docker_status = _parse_docker_status(d.pop("docker_status", UNSET))

        _play_info = d.pop("play_info", UNSET)
        play_info: GetV4ChallengeInfoIdResponse200ChallengePlayInfo | Unset
        if isinstance(_play_info, Unset):
            play_info = UNSET
        else:
            play_info = GetV4ChallengeInfoIdResponse200ChallengePlayInfo.from_dict(_play_info)

        release_date = d.pop("release_date", UNSET)

        released = d.pop("released", UNSET)

        auth_user_solve = d.pop("authUserSolve", UNSET)

        like_by_auth_user = d.pop("likeByAuthUser", UNSET)

        dislike_by_auth_user = d.pop("dislikeByAuthUser", UNSET)

        is_todo = d.pop("isTodo", UNSET)

        recommended = d.pop("recommended", UNSET)

        auth_user_has_reviewed = d.pop("authUserHasReviewed", UNSET)

        user_can_review = d.pop("user_can_review", UNSET)

        can_access_walkthough = d.pop("can_access_walkthough", UNSET)

        tags = cast(list[Any], d.pop("tags", UNSET))

        play_methods = cast(list[str], d.pop("play_methods", UNSET))

        reviews_count = d.pop("reviews_count", UNSET)

        has_changelog = d.pop("has_changelog", UNSET)

        show_go_vip = d.pop("show_go_vip", UNSET)

        def _parse_user_submitted_difficulty(
            data: object,
        ) -> GetV4ChallengeInfoIdResponse200ChallengeUserSubmittedDifficultyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_submitted_difficulty_type_0 = (
                    GetV4ChallengeInfoIdResponse200ChallengeUserSubmittedDifficultyType0.from_dict(data)
                )

                return user_submitted_difficulty_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4ChallengeInfoIdResponse200ChallengeUserSubmittedDifficultyType0 | None | Unset, data)

        user_submitted_difficulty = _parse_user_submitted_difficulty(d.pop("user_submitted_difficulty", UNSET))

        avatar_url = d.pop("avatar_url", UNSET)

        get_v4_challenge_info_id_response_200_challenge = cls(
            id=id,
            name=name,
            retired=retired,
            state=state,
            difficulty=difficulty,
            points=points,
            difficulty_chart=difficulty_chart,
            solves=solves,
            auth_user_solve_time=auth_user_solve_time,
            likes=likes,
            dislikes=dislikes,
            stars=stars,
            description=description,
            category_name=category_name,
            first_blood_user_id=first_blood_user_id,
            first_blood_user=first_blood_user,
            first_blood_time=first_blood_time,
            first_blood_user_avatar=first_blood_user_avatar,
            creator_id=creator_id,
            creator_name=creator_name,
            creator_avatar=creator_avatar,
            is_respected=is_respected,
            creator2_id=creator2_id,
            creator2_name=creator2_name,
            creator2_avatar=creator2_avatar,
            is_respected_2=is_respected_2,
            download=download,
            file_name=file_name,
            file_size=file_size,
            sha256=sha256,
            docker=docker,
            docker_ip=docker_ip,
            docker_ports=docker_ports,
            docker_status=docker_status,
            play_info=play_info,
            release_date=release_date,
            released=released,
            auth_user_solve=auth_user_solve,
            like_by_auth_user=like_by_auth_user,
            dislike_by_auth_user=dislike_by_auth_user,
            is_todo=is_todo,
            recommended=recommended,
            auth_user_has_reviewed=auth_user_has_reviewed,
            user_can_review=user_can_review,
            can_access_walkthough=can_access_walkthough,
            tags=tags,
            play_methods=play_methods,
            reviews_count=reviews_count,
            has_changelog=has_changelog,
            show_go_vip=show_go_vip,
            user_submitted_difficulty=user_submitted_difficulty,
            avatar_url=avatar_url,
        )

        get_v4_challenge_info_id_response_200_challenge.additional_properties = d
        return get_v4_challenge_info_id_response_200_challenge

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
