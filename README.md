# istio-site-generator

[![Pytest](https://github.com/keefbaker/istio-site-gen/actions/workflows/test.yml/badge.svg)](https://github.com/keefbaker/istio-site-gen/actions/workflows/test.yml)

Allows for the generation of manifests for sending sites through
istio egress gateways for monitoring, control and ease of network policies in calico

## Usage

Run the script followed by the filename of the config file you want to use.

```
python3 generate_config.py config_example.yaml
```

The config example shows you what options there are, it is a very simple script.

In order for this to block sites adequately, you namespace must be labeled with istio-injection=enabled and your calico policy applied to the namespace should look similar to this:

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-egress-to-istio-system-and-kube-dns
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: "kube-system"
    ports:
    - protocol: UDP
      port: 53
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: "istio-system"
```