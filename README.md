# Logstash

Master: [![Build Status](https://travis-ci.org/sansible/logstash.svg?branch=master)](https://travis-ci.org/sansible/logstash)  
Develop: [![Build Status](https://travis-ci.org/sansible/logstash.svg?branch=develop)](https://travis-ci.org/sansible/logstash)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs Logstash for the ELK stack.

For more information on Logstash please visit [elastic logstash](https://www.elastic.co/products/logstash).




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

This role will install `sansible.users_and_groups` for managing `logstash`
user.

To install run `ansible-galaxy install sansible.logstash` or add this to your
`roles.yml`

```YAML
- name: sansible.logstash
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs Logstash and all it's dependencies.
* `configure` - Configure and ensures that the Logstash service is running.




## Examples

To install:

```YAML
- name: Elk Logstash
  hosts: "{{ hosts }}"

  roles:
    - role: sansible.logstash
```

With your own config files:


```YAML
- name: Elk Logstash
  hosts: "{{ hosts }}"

  roles:
    - role: sansible.logstash
      logstash:
        default_config: no

  tasks:
    - name: Configure logstash
      become: yes
      template:
        src: "{{ item }}.j2"
        dest: "/etc/logstash/conf.d/{{ item }}"
      with_items:
        - templates/01-inputs.conf
        - templates/10-filters.conf
        - templates/90-outputs.conf
      notify:
        - restart logstash
```
