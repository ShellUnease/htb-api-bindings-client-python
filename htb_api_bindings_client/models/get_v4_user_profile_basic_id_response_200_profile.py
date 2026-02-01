from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v4_user_profile_basic_id_response_200_profile_avatar_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileAvatarType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_country_code_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileCountryCodeType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_cpe_id_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileCpeIdType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_cv_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileCvType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_github_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileGithubType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_linkedin_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileLinkedinType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_phone_number_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfilePhoneNumberType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_rank_requirement_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileRankRequirementType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_ranking_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileRankingType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_team_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileTeamType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_twitter_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileTwitterType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_university_name_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileUniversityNameType0,
    )
    from ..models.get_v4_user_profile_basic_id_response_200_profile_university_type_0 import (
        GetV4UserProfileBasicIdResponse200ProfileUniversityType0,
    )


T = TypeVar("T", bound="GetV4UserProfileBasicIdResponse200Profile")


@_attrs_define
class GetV4UserProfileBasicIdResponse200Profile:
    """
    Attributes:
        id (float | Unset):
        sso_id (bool | Unset):
        name (str | Unset):
        system_owns (float | Unset):
        user_owns (float | Unset):
        user_bloods (float | Unset):
        system_bloods (float | Unset):
        challenge_bloods (float | Unset):
        team (GetV4UserProfileBasicIdResponse200ProfileTeamType0 | None | Unset):
        respects (float | Unset):
        rank (str | Unset):
        rank_id (float | Unset):
        current_rank_progress (float | Unset):
        next_rank (str | Unset):
        next_rank_points (float | Unset):
        rank_ownership (float | Unset):
        rank_requirement (GetV4UserProfileBasicIdResponse200ProfileRankRequirementType0 | None | Unset):
        ranking (GetV4UserProfileBasicIdResponse200ProfileRankingType0 | None | Unset):
        avatar (GetV4UserProfileBasicIdResponse200ProfileAvatarType0 | None | Unset):
        timezone (str | Unset):
        is_vip (bool | Unset):
        is_dedicated_vip (bool | Unset):
        public (bool | Unset):
        country_name (str | Unset):
        country_code (GetV4UserProfileBasicIdResponse200ProfileCountryCodeType0 | None | Unset):
        points (float | Unset):
        joined_date (str | Unset):
        university (GetV4UserProfileBasicIdResponse200ProfileUniversityType0 | None | Unset):
        university_name (GetV4UserProfileBasicIdResponse200ProfileUniversityNameType0 | None | Unset):
        github (GetV4UserProfileBasicIdResponse200ProfileGithubType0 | None | Unset):
        linkedin (GetV4UserProfileBasicIdResponse200ProfileLinkedinType0 | None | Unset):
        twitter (GetV4UserProfileBasicIdResponse200ProfileTwitterType0 | None | Unset):
        server (str | Unset):
        full_name (str | Unset):
        phone_number (GetV4UserProfileBasicIdResponse200ProfilePhoneNumberType0 | None | Unset):
        cv (GetV4UserProfileBasicIdResponse200ProfileCvType0 | None | Unset):
        cpe_id (GetV4UserProfileBasicIdResponse200ProfileCpeIdType0 | None | Unset):
        user_respects (float | Unset):
        user_follows (float | Unset):
        followed_by_count (float | Unset):
    """

    id: float | Unset = UNSET
    sso_id: bool | Unset = UNSET
    name: str | Unset = UNSET
    system_owns: float | Unset = UNSET
    user_owns: float | Unset = UNSET
    user_bloods: float | Unset = UNSET
    system_bloods: float | Unset = UNSET
    challenge_bloods: float | Unset = UNSET
    team: GetV4UserProfileBasicIdResponse200ProfileTeamType0 | None | Unset = UNSET
    respects: float | Unset = UNSET
    rank: str | Unset = UNSET
    rank_id: float | Unset = UNSET
    current_rank_progress: float | Unset = UNSET
    next_rank: str | Unset = UNSET
    next_rank_points: float | Unset = UNSET
    rank_ownership: float | Unset = UNSET
    rank_requirement: GetV4UserProfileBasicIdResponse200ProfileRankRequirementType0 | None | Unset = UNSET
    ranking: GetV4UserProfileBasicIdResponse200ProfileRankingType0 | None | Unset = UNSET
    avatar: GetV4UserProfileBasicIdResponse200ProfileAvatarType0 | None | Unset = UNSET
    timezone: str | Unset = UNSET
    is_vip: bool | Unset = UNSET
    is_dedicated_vip: bool | Unset = UNSET
    public: bool | Unset = UNSET
    country_name: str | Unset = UNSET
    country_code: GetV4UserProfileBasicIdResponse200ProfileCountryCodeType0 | None | Unset = UNSET
    points: float | Unset = UNSET
    joined_date: str | Unset = UNSET
    university: GetV4UserProfileBasicIdResponse200ProfileUniversityType0 | None | Unset = UNSET
    university_name: GetV4UserProfileBasicIdResponse200ProfileUniversityNameType0 | None | Unset = UNSET
    github: GetV4UserProfileBasicIdResponse200ProfileGithubType0 | None | Unset = UNSET
    linkedin: GetV4UserProfileBasicIdResponse200ProfileLinkedinType0 | None | Unset = UNSET
    twitter: GetV4UserProfileBasicIdResponse200ProfileTwitterType0 | None | Unset = UNSET
    server: str | Unset = UNSET
    full_name: str | Unset = UNSET
    phone_number: GetV4UserProfileBasicIdResponse200ProfilePhoneNumberType0 | None | Unset = UNSET
    cv: GetV4UserProfileBasicIdResponse200ProfileCvType0 | None | Unset = UNSET
    cpe_id: GetV4UserProfileBasicIdResponse200ProfileCpeIdType0 | None | Unset = UNSET
    user_respects: float | Unset = UNSET
    user_follows: float | Unset = UNSET
    followed_by_count: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v4_user_profile_basic_id_response_200_profile_avatar_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileAvatarType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_country_code_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileCountryCodeType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_cpe_id_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileCpeIdType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_cv_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileCvType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_github_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileGithubType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_linkedin_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileLinkedinType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_phone_number_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfilePhoneNumberType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_rank_requirement_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileRankRequirementType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_ranking_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileRankingType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_team_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileTeamType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_twitter_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileTwitterType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_university_name_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileUniversityNameType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_university_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileUniversityType0,
        )

        id = self.id

        sso_id = self.sso_id

        name = self.name

        system_owns = self.system_owns

        user_owns = self.user_owns

        user_bloods = self.user_bloods

        system_bloods = self.system_bloods

        challenge_bloods = self.challenge_bloods

        team: dict[str, Any] | None | Unset
        if isinstance(self.team, Unset):
            team = UNSET
        elif isinstance(self.team, GetV4UserProfileBasicIdResponse200ProfileTeamType0):
            team = self.team.to_dict()
        else:
            team = self.team

        respects = self.respects

        rank = self.rank

        rank_id = self.rank_id

        current_rank_progress = self.current_rank_progress

        next_rank = self.next_rank

        next_rank_points = self.next_rank_points

        rank_ownership = self.rank_ownership

        rank_requirement: dict[str, Any] | None | Unset
        if isinstance(self.rank_requirement, Unset):
            rank_requirement = UNSET
        elif isinstance(self.rank_requirement, GetV4UserProfileBasicIdResponse200ProfileRankRequirementType0):
            rank_requirement = self.rank_requirement.to_dict()
        else:
            rank_requirement = self.rank_requirement

        ranking: dict[str, Any] | None | Unset
        if isinstance(self.ranking, Unset):
            ranking = UNSET
        elif isinstance(self.ranking, GetV4UserProfileBasicIdResponse200ProfileRankingType0):
            ranking = self.ranking.to_dict()
        else:
            ranking = self.ranking

        avatar: dict[str, Any] | None | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        elif isinstance(self.avatar, GetV4UserProfileBasicIdResponse200ProfileAvatarType0):
            avatar = self.avatar.to_dict()
        else:
            avatar = self.avatar

        timezone = self.timezone

        is_vip = self.is_vip

        is_dedicated_vip = self.is_dedicated_vip

        public = self.public

        country_name = self.country_name

        country_code: dict[str, Any] | None | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        elif isinstance(self.country_code, GetV4UserProfileBasicIdResponse200ProfileCountryCodeType0):
            country_code = self.country_code.to_dict()
        else:
            country_code = self.country_code

        points = self.points

        joined_date = self.joined_date

        university: dict[str, Any] | None | Unset
        if isinstance(self.university, Unset):
            university = UNSET
        elif isinstance(self.university, GetV4UserProfileBasicIdResponse200ProfileUniversityType0):
            university = self.university.to_dict()
        else:
            university = self.university

        university_name: dict[str, Any] | None | Unset
        if isinstance(self.university_name, Unset):
            university_name = UNSET
        elif isinstance(self.university_name, GetV4UserProfileBasicIdResponse200ProfileUniversityNameType0):
            university_name = self.university_name.to_dict()
        else:
            university_name = self.university_name

        github: dict[str, Any] | None | Unset
        if isinstance(self.github, Unset):
            github = UNSET
        elif isinstance(self.github, GetV4UserProfileBasicIdResponse200ProfileGithubType0):
            github = self.github.to_dict()
        else:
            github = self.github

        linkedin: dict[str, Any] | None | Unset
        if isinstance(self.linkedin, Unset):
            linkedin = UNSET
        elif isinstance(self.linkedin, GetV4UserProfileBasicIdResponse200ProfileLinkedinType0):
            linkedin = self.linkedin.to_dict()
        else:
            linkedin = self.linkedin

        twitter: dict[str, Any] | None | Unset
        if isinstance(self.twitter, Unset):
            twitter = UNSET
        elif isinstance(self.twitter, GetV4UserProfileBasicIdResponse200ProfileTwitterType0):
            twitter = self.twitter.to_dict()
        else:
            twitter = self.twitter

        server = self.server

        full_name = self.full_name

        phone_number: dict[str, Any] | None | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        elif isinstance(self.phone_number, GetV4UserProfileBasicIdResponse200ProfilePhoneNumberType0):
            phone_number = self.phone_number.to_dict()
        else:
            phone_number = self.phone_number

        cv: dict[str, Any] | None | Unset
        if isinstance(self.cv, Unset):
            cv = UNSET
        elif isinstance(self.cv, GetV4UserProfileBasicIdResponse200ProfileCvType0):
            cv = self.cv.to_dict()
        else:
            cv = self.cv

        cpe_id: dict[str, Any] | None | Unset
        if isinstance(self.cpe_id, Unset):
            cpe_id = UNSET
        elif isinstance(self.cpe_id, GetV4UserProfileBasicIdResponse200ProfileCpeIdType0):
            cpe_id = self.cpe_id.to_dict()
        else:
            cpe_id = self.cpe_id

        user_respects = self.user_respects

        user_follows = self.user_follows

        followed_by_count = self.followed_by_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sso_id is not UNSET:
            field_dict["sso_id"] = sso_id
        if name is not UNSET:
            field_dict["name"] = name
        if system_owns is not UNSET:
            field_dict["system_owns"] = system_owns
        if user_owns is not UNSET:
            field_dict["user_owns"] = user_owns
        if user_bloods is not UNSET:
            field_dict["user_bloods"] = user_bloods
        if system_bloods is not UNSET:
            field_dict["system_bloods"] = system_bloods
        if challenge_bloods is not UNSET:
            field_dict["challenge_bloods"] = challenge_bloods
        if team is not UNSET:
            field_dict["team"] = team
        if respects is not UNSET:
            field_dict["respects"] = respects
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_id is not UNSET:
            field_dict["rank_id"] = rank_id
        if current_rank_progress is not UNSET:
            field_dict["current_rank_progress"] = current_rank_progress
        if next_rank is not UNSET:
            field_dict["next_rank"] = next_rank
        if next_rank_points is not UNSET:
            field_dict["next_rank_points"] = next_rank_points
        if rank_ownership is not UNSET:
            field_dict["rank_ownership"] = rank_ownership
        if rank_requirement is not UNSET:
            field_dict["rank_requirement"] = rank_requirement
        if ranking is not UNSET:
            field_dict["ranking"] = ranking
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if is_vip is not UNSET:
            field_dict["isVip"] = is_vip
        if is_dedicated_vip is not UNSET:
            field_dict["isDedicatedVip"] = is_dedicated_vip
        if public is not UNSET:
            field_dict["public"] = public
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if points is not UNSET:
            field_dict["points"] = points
        if joined_date is not UNSET:
            field_dict["joined_date"] = joined_date
        if university is not UNSET:
            field_dict["university"] = university
        if university_name is not UNSET:
            field_dict["university_name"] = university_name
        if github is not UNSET:
            field_dict["github"] = github
        if linkedin is not UNSET:
            field_dict["linkedin"] = linkedin
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if server is not UNSET:
            field_dict["server"] = server
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if cv is not UNSET:
            field_dict["cv"] = cv
        if cpe_id is not UNSET:
            field_dict["cpe_id"] = cpe_id
        if user_respects is not UNSET:
            field_dict["user_respects"] = user_respects
        if user_follows is not UNSET:
            field_dict["user_follows"] = user_follows
        if followed_by_count is not UNSET:
            field_dict["followed_by_count"] = followed_by_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v4_user_profile_basic_id_response_200_profile_avatar_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileAvatarType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_country_code_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileCountryCodeType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_cpe_id_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileCpeIdType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_cv_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileCvType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_github_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileGithubType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_linkedin_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileLinkedinType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_phone_number_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfilePhoneNumberType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_rank_requirement_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileRankRequirementType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_ranking_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileRankingType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_team_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileTeamType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_twitter_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileTwitterType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_university_name_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileUniversityNameType0,
        )
        from ..models.get_v4_user_profile_basic_id_response_200_profile_university_type_0 import (
            GetV4UserProfileBasicIdResponse200ProfileUniversityType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        sso_id = d.pop("sso_id", UNSET)

        name = d.pop("name", UNSET)

        system_owns = d.pop("system_owns", UNSET)

        user_owns = d.pop("user_owns", UNSET)

        user_bloods = d.pop("user_bloods", UNSET)

        system_bloods = d.pop("system_bloods", UNSET)

        challenge_bloods = d.pop("challenge_bloods", UNSET)

        def _parse_team(data: object) -> GetV4UserProfileBasicIdResponse200ProfileTeamType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_0 = GetV4UserProfileBasicIdResponse200ProfileTeamType0.from_dict(data)

                return team_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileTeamType0 | None | Unset, data)

        team = _parse_team(d.pop("team", UNSET))

        respects = d.pop("respects", UNSET)

        rank = d.pop("rank", UNSET)

        rank_id = d.pop("rank_id", UNSET)

        current_rank_progress = d.pop("current_rank_progress", UNSET)

        next_rank = d.pop("next_rank", UNSET)

        next_rank_points = d.pop("next_rank_points", UNSET)

        rank_ownership = d.pop("rank_ownership", UNSET)

        def _parse_rank_requirement(
            data: object,
        ) -> GetV4UserProfileBasicIdResponse200ProfileRankRequirementType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rank_requirement_type_0 = GetV4UserProfileBasicIdResponse200ProfileRankRequirementType0.from_dict(data)

                return rank_requirement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileRankRequirementType0 | None | Unset, data)

        rank_requirement = _parse_rank_requirement(d.pop("rank_requirement", UNSET))

        def _parse_ranking(data: object) -> GetV4UserProfileBasicIdResponse200ProfileRankingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ranking_type_0 = GetV4UserProfileBasicIdResponse200ProfileRankingType0.from_dict(data)

                return ranking_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileRankingType0 | None | Unset, data)

        ranking = _parse_ranking(d.pop("ranking", UNSET))

        def _parse_avatar(data: object) -> GetV4UserProfileBasicIdResponse200ProfileAvatarType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                avatar_type_0 = GetV4UserProfileBasicIdResponse200ProfileAvatarType0.from_dict(data)

                return avatar_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileAvatarType0 | None | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        timezone = d.pop("timezone", UNSET)

        is_vip = d.pop("isVip", UNSET)

        is_dedicated_vip = d.pop("isDedicatedVip", UNSET)

        public = d.pop("public", UNSET)

        country_name = d.pop("country_name", UNSET)

        def _parse_country_code(
            data: object,
        ) -> GetV4UserProfileBasicIdResponse200ProfileCountryCodeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_code_type_0 = GetV4UserProfileBasicIdResponse200ProfileCountryCodeType0.from_dict(data)

                return country_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileCountryCodeType0 | None | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        points = d.pop("points", UNSET)

        joined_date = d.pop("joined_date", UNSET)

        def _parse_university(data: object) -> GetV4UserProfileBasicIdResponse200ProfileUniversityType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                university_type_0 = GetV4UserProfileBasicIdResponse200ProfileUniversityType0.from_dict(data)

                return university_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileUniversityType0 | None | Unset, data)

        university = _parse_university(d.pop("university", UNSET))

        def _parse_university_name(
            data: object,
        ) -> GetV4UserProfileBasicIdResponse200ProfileUniversityNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                university_name_type_0 = GetV4UserProfileBasicIdResponse200ProfileUniversityNameType0.from_dict(data)

                return university_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileUniversityNameType0 | None | Unset, data)

        university_name = _parse_university_name(d.pop("university_name", UNSET))

        def _parse_github(data: object) -> GetV4UserProfileBasicIdResponse200ProfileGithubType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                github_type_0 = GetV4UserProfileBasicIdResponse200ProfileGithubType0.from_dict(data)

                return github_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileGithubType0 | None | Unset, data)

        github = _parse_github(d.pop("github", UNSET))

        def _parse_linkedin(data: object) -> GetV4UserProfileBasicIdResponse200ProfileLinkedinType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                linkedin_type_0 = GetV4UserProfileBasicIdResponse200ProfileLinkedinType0.from_dict(data)

                return linkedin_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileLinkedinType0 | None | Unset, data)

        linkedin = _parse_linkedin(d.pop("linkedin", UNSET))

        def _parse_twitter(data: object) -> GetV4UserProfileBasicIdResponse200ProfileTwitterType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                twitter_type_0 = GetV4UserProfileBasicIdResponse200ProfileTwitterType0.from_dict(data)

                return twitter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileTwitterType0 | None | Unset, data)

        twitter = _parse_twitter(d.pop("twitter", UNSET))

        server = d.pop("server", UNSET)

        full_name = d.pop("full_name", UNSET)

        def _parse_phone_number(
            data: object,
        ) -> GetV4UserProfileBasicIdResponse200ProfilePhoneNumberType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_0 = GetV4UserProfileBasicIdResponse200ProfilePhoneNumberType0.from_dict(data)

                return phone_number_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfilePhoneNumberType0 | None | Unset, data)

        phone_number = _parse_phone_number(d.pop("phone_number", UNSET))

        def _parse_cv(data: object) -> GetV4UserProfileBasicIdResponse200ProfileCvType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cv_type_0 = GetV4UserProfileBasicIdResponse200ProfileCvType0.from_dict(data)

                return cv_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileCvType0 | None | Unset, data)

        cv = _parse_cv(d.pop("cv", UNSET))

        def _parse_cpe_id(data: object) -> GetV4UserProfileBasicIdResponse200ProfileCpeIdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cpe_id_type_0 = GetV4UserProfileBasicIdResponse200ProfileCpeIdType0.from_dict(data)

                return cpe_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV4UserProfileBasicIdResponse200ProfileCpeIdType0 | None | Unset, data)

        cpe_id = _parse_cpe_id(d.pop("cpe_id", UNSET))

        user_respects = d.pop("user_respects", UNSET)

        user_follows = d.pop("user_follows", UNSET)

        followed_by_count = d.pop("followed_by_count", UNSET)

        get_v4_user_profile_basic_id_response_200_profile = cls(
            id=id,
            sso_id=sso_id,
            name=name,
            system_owns=system_owns,
            user_owns=user_owns,
            user_bloods=user_bloods,
            system_bloods=system_bloods,
            challenge_bloods=challenge_bloods,
            team=team,
            respects=respects,
            rank=rank,
            rank_id=rank_id,
            current_rank_progress=current_rank_progress,
            next_rank=next_rank,
            next_rank_points=next_rank_points,
            rank_ownership=rank_ownership,
            rank_requirement=rank_requirement,
            ranking=ranking,
            avatar=avatar,
            timezone=timezone,
            is_vip=is_vip,
            is_dedicated_vip=is_dedicated_vip,
            public=public,
            country_name=country_name,
            country_code=country_code,
            points=points,
            joined_date=joined_date,
            university=university,
            university_name=university_name,
            github=github,
            linkedin=linkedin,
            twitter=twitter,
            server=server,
            full_name=full_name,
            phone_number=phone_number,
            cv=cv,
            cpe_id=cpe_id,
            user_respects=user_respects,
            user_follows=user_follows,
            followed_by_count=followed_by_count,
        )

        get_v4_user_profile_basic_id_response_200_profile.additional_properties = d
        return get_v4_user_profile_basic_id_response_200_profile

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
