from biolink.model import InformationContentEntity

from dug.parsers import DugElement, BiolinkEntityMapperFactory


def test_biolink_mapper():

    elem_name = "study_result"
    elem_type = "study_result_type"
    elem_id = "study-result:abc"
    desc = "the result of a study"
    mapper_schema = {
        elem_name: {
            "target": "InformationContentEntity",
            "fields": {
                "id": "id",
                "name": "name",
            },
            "categories": ["biolink:ClinicalTrial"],
        }
    }

    mapper = BiolinkEntityMapperFactory(mapper_schema)

    source = DugElement(
        elem_id, elem_name, desc, elem_type,
    )

    output = mapper(source)

    assert isinstance(output, InformationContentEntity)
    assert output.id == elem_id
    assert output.name == elem_name
    assert output.category == ["biolink:ClinicalTrial"]

