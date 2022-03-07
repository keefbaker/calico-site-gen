import yaml
import os
import generate_config

def get_yaml(filename):
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/{filename}") as stream:
        return yaml.safe_load(stream)

def test_virtual_service_basic():
    config = get_yaml("basic.yaml")
    expected_results = get_yaml("results_check/virtual_service.yaml")
    actual_results = generate_config.generate_virtual_service(config, 'istio-egressgateway.istio-system.svc.cluster.local')
    assert expected_results == actual_results