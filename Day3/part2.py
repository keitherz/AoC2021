from solver import Solver
from typing import List, TypedDict
from enum import Enum


class ReportsList(TypedDict):
    set: List[str]
    clr: List[str]


class RatingType(Enum):
    OXYGEN_GENERATOR = 0
    CO2_SCRUBBER = 1


def segregate_reports(reports: List[str], index: int) -> ReportsList:
    reports_list = ReportsList(set=[], clr=[])
    for report in reports:
        if report[index] == '1':
            reports_list['set'].append(report)
        elif report[index] == '0':
            reports_list['clr'].append(report)
        else:
            raise Exception("Unhandled bit value!")
    return reports_list


def get_reports_for_rating_type(reports_list: ReportsList, type: RatingType) -> List[str]:
    reports: List[str] = []

    if type == RatingType.OXYGEN_GENERATOR:
        if len(reports_list['set']) >= len(reports_list['clr']):
            reports = reports_list['set']
        else:
            reports = reports_list['clr']
    elif type == RatingType.CO2_SCRUBBER:
        if len(reports_list['set']) < len(reports_list['clr']):
            reports = reports_list['set']
        else:
            reports = reports_list['clr']
    else:
        raise Exception("Unhandled rating type!")

    return reports


def get_rating(reports: List[str], type: RatingType) -> int:
    rating: int = None
    index: int = 0

    while rating == None:
        reports_list = segregate_reports(reports, index)
        reports = get_reports_for_rating_type(reports_list, type)

        if len(reports) == 1:
            rating = int(reports[0], 2)

        index += 1

    return rating


class Part2(Solver):
    def __init__(self):
        self.reports: List[str] = []

    def process(self, input: str) -> None:
        self.reports.append(input)

    def finish(self) -> int:
        oxygen_generator_rating: int = get_rating(
            self.reports, RatingType.OXYGEN_GENERATOR)
        co2_scrubber_rating: int = get_rating(
            self.reports, RatingType.CO2_SCRUBBER)

        return oxygen_generator_rating * co2_scrubber_rating
