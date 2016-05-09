# ELK Logstash

This roles installs Logstash for the ELK stack.

For more information on Logstash please visit [elastic logstash](https://www.elastic.co/products/logstash).

## Example Playbook

To install:

```YAML
- name: Elk Logstash
  hosts: "{{ hosts }}"

  roles:
    - role: elk_logstash
```

To configure:

```YAML
- name: Configure ELK Logstash
  hosts: "{{ hosts }}"

  vars_files:
    - ../js_roles/elk_logstash/defaults/main.yml

  handlers:
    - include: ../js_roles/elk_logstash/handlers/main.yml

  tasks:
    - name: Configure Kibana
      include: ../js_roles/elk_logstash/tasks/configure.yml
```
