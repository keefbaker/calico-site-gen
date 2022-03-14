import yaml
import os
import generate_config


def get_yaml(filename):
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/{filename}") as stream:
        return yaml.safe_load(stream)


def test_service_basic():
    config = get_yaml("basic.yaml")
    expected_results = get_yaml("results_check/service.yaml")
    actual_results = generate_config.generate_service(config)
    assert expected_results == actual_results


def test_service_complex():
    config = get_yaml("complex.yaml")
    expected_results = get_yaml("results_check/servicecomplex.yaml")
    actual_results = generate_config.generate_service(config)
    assert expected_results == actual_results
