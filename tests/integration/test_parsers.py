import pytest
from biolink.model import InformationContentEntity

from dug.parsers import DbGaPParser, load_mapper_from_config, DugElement
from tests.integration.conftest import TEST_DATA_DIR


@pytest.mark.skip("Finish this test")
def test_db_gap_parser():
    parser = DbGaPParser()

    parse_file = TEST_DATA_DIR / "dbgap_sample_file.csv"
    parser.parse(parse_file)


@pytest.mark.skip("Finish this test")
def test_topmed_tag_parser():
    pass


def test_load_mapper_from_config():
    config_file = TEST_DATA_DIR / 'biolink_mapper_sample.yaml'
    mapper = load_mapper_from_config(config_file)

    name = "study_result"
    elem_type = "study_result"
    elem_id = "study-result:abc"
    desc = "the result of a study"

    source = DugElement(
        elem_id, name, desc, elem_type,
    )

    output = mapper(source)
    assert isinstance(output, InformationContentEntity)
    assert output.category == ["biolink:ClinicalTrial"]



