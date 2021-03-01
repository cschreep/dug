from biolink.model import InformationContentEntity

from dug.parsers import DugElement, BiolinkEntityMapper


def test_biolink_mapper():

    name = "study_result"
    elem_type = "study_result"
    elem_id = "study-result:abc"
    desc = "the result of a study"
    mapper_schema = {
        name: {
            "target": "InformationContentEntity",
            "fields": {
                "id": "id",
                "name": "name",
            },
        }
    }

    mapper = BiolinkEntityMapper(["biolink:ClinicalTrial"], mapper_schema)

    source = DugElement(
        elem_id, name, desc, elem_type,
    )

    output = mapper.parse(source)
    assert isinstance(output, InformationContentEntity)
    assert output.category == ["biolink:ClinicalTrial"]
