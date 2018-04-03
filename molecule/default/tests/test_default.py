import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_installed_packages(host):
    assert host.package('logstash').is_installed
    assert host.package('logstash').version == '1:5.6.8-1'


def test_files(host):
    to_add = [
        '/etc/default/logstash',
        '/etc/logstash/conf.d/01-inputs.conf',
        '/etc/logstash/conf.d/10-filters.conf',
        '/etc/logstash/conf.d/90-outputs.conf',
    ]
    for config in to_add:
        assert host.file(config).exists


def test_service(host):
    assert host.service('logstash').is_enabled
    assert host.service('logstash').is_running
