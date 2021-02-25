from biolink.model import InformationContentEntity

from dug.parsers import DugElement, BiolinkMapper


def test_biolink_mapper():
    rules = {
        "id": "id",
        "name": "name",
    }

    mapper_schema = {
        "dest_classname": "InformationContentEntity",
        "rules": rules,
        "category": ["biolink:ClinicalFinding"],
    }
    mapper = BiolinkMapper(**mapper_schema)
    elem_id = "abc"
    name = "some element"
    desc = "element description"
    elem_type = "element_type"

    source = DugElement(
        elem_id, name, desc, elem_type,
    )

    output = mapper.parse(source)
    assert isinstance(output, InformationContentEntity)
    assert output.category == mapper_schema['category']

