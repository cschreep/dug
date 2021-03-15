from biolink.model import InformationContentEntity

from dug.parsers import DugElement, BiolinkEntityMapperFactory


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
            "categories": ["biolink:ClinicalTrial"],
        }
    }

    mapper = BiolinkEntityMapperFactory(mapper_schema)

    source = DugElement(
        elem_id, name, desc, elem_type,
    )

    output = mapper(source)
    assert isinstance(output, InformationContentEntity)
    assert output.category == ["biolink:ClinicalTrial"]
