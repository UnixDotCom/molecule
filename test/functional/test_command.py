#  Copyright (c) 2015-2017 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import os
import pytest
import sh


@pytest.fixture
def scenario_to_test(request):
    return request.param


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, scenario_name', [
        ('driver/docker', 'docker', 'default'),
        ('driver/lxc', 'lxc', 'default'),
        ('driver/lxd', 'lxd', 'default'),
        ('driver/openstack', 'openstack', 'default'),
        ('driver/static', 'docker', 'docker'),
        ('driver/static', 'openstack', 'openstack'),
        ('driver/static', 'vagrant', 'vagrant'),
        ('driver/vagrant', 'vagrant', 'default'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_check(scenario_to_test, with_scenario, skip_test,
                       scenario_name):
    cmd = sh.molecule.bake('check', {'scenario-name': scenario_name})
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, scenario_name', [
        ('driver/docker', 'docker', 'default'),
        ('driver/lxc', 'lxc', 'default'),
        ('driver/lxd', 'lxd', 'default'),
        ('driver/openstack', 'openstack', 'default'),
        ('driver/static', 'docker', 'docker'),
        ('driver/static', 'openstack', 'openstack'),
        ('driver/static', 'vagrant', 'vagrant'),
        ('driver/vagrant', 'vagrant', 'default'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_converge(scenario_to_test, with_scenario, skip_test,
                          scenario_name):
    cmd = sh.molecule.bake('converge', {'scenario-name': scenario_name})
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, scenario_name', [
        ('driver/docker', 'docker', 'default'),
        ('driver/lxc', 'lxc', 'default'),
        ('driver/lxd', 'lxd', 'default'),
        ('driver/openstack', 'openstack', 'default'),
        ('driver/static', 'docker', 'docker'),
        ('driver/static', 'openstack', 'openstack'),
        ('driver/static', 'vagrant', 'vagrant'),
        ('driver/vagrant', 'vagrant', 'default'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_create(scenario_to_test, with_scenario, skip_test,
                        scenario_name):
    cmd = sh.molecule.bake('create', {'scenario-name': scenario_name})
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test', [
        ('dependency', 'docker'),
        ('dependency', 'lxc'),
        ('dependency', 'lxd'),
        ('dependency', 'openstack'),
        ('dependency', 'vagrant'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_dependency_ansible_galaxy(scenario_to_test, with_scenario,
                                           skip_test):
    cmd = sh.molecule.bake('dependency', {'scenario-name', 'ansible-galaxy'})
    pytest.helpers.run_command(cmd)

    dependency_role = os.path.join('molecule', 'ansible-galaxy', '.molecule',
                                   'roles', 'timezone')
    assert os.path.isdir(dependency_role)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test', [
        ('dependency', 'docker'),
        ('dependency', 'lxc'),
        ('dependency', 'lxd'),
        ('dependency', 'openstack'),
        ('dependency', 'vagrant'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_dependency_gilt(scenario_to_test, with_scenario, skip_test):
    cmd = sh.molecule.bake('dependency', {'scenario-name': 'gilt'})
    pytest.helpers.run_command(cmd)

    dependency_role = os.path.join('molecule', 'ansible-galaxy', '.molecule',
                                   'roles', 'timezone')
    assert os.path.isdir(dependency_role)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, scenario_name', [
        ('driver/docker', 'docker', 'default'),
        ('driver/lxc', 'lxc', 'default'),
        ('driver/lxd', 'lxd', 'default'),
        ('driver/openstack', 'openstack', 'default'),
        ('driver/static', 'docker', 'docker'),
        ('driver/static', 'openstack', 'openstack'),
        ('driver/static', 'vagrant', 'vagrant'),
        ('driver/vagrant', 'vagrant', 'default'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_destroy(scenario_to_test, with_scenario, skip_test,
                         scenario_name):
    cmd = sh.molecule.bake('destroy', {'scenario-name': scenario_name})
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, scenario_name', [
        ('driver/docker', 'docker', 'default'),
        ('driver/lxc', 'lxc', 'default'),
        ('driver/lxd', 'lxd', 'default'),
        ('driver/openstack', 'openstack', 'default'),
        ('driver/static', 'docker', 'docker'),
        ('driver/static', 'openstack', 'openstack'),
        ('driver/static', 'vagrant', 'vagrant'),
        ('driver/vagrant', 'vagrant', 'default'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_idempotence(scenario_to_test, with_scenario, skip_test,
                             scenario_name):
    pytest.helpers.idempotence(scenario_name)


@pytest.mark.parametrize(
    'driver_name, skip_test', [
        ('docker', 'docker'),
        ('lxc', 'lxc'),
        ('lxd', 'lxd'),
        ('openstack', 'openstack'),
        ('vagrant', 'vagrant'),
    ],
    indirect=['skip_test'])
def test_command_init_role(temp_dir, driver_name, skip_test):
    pytest.helpers.init_role(temp_dir, driver_name)


@pytest.mark.parametrize(
    'driver_name, skip_test', [
        ('docker', 'docker'),
        ('lxc', 'lxc'),
        ('lxd', 'lxd'),
        ('openstack', 'openstack'),
        ('vagrant', 'vagrant'),
    ],
    indirect=['skip_test'])
def test_command_init_scenario(temp_dir, driver_name, skip_test):
    pytest.helpers.init_role(temp_dir, driver_name)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, scenario_name', [
        ('driver/docker', 'docker', 'default'),
        ('driver/lxc', 'lxc', 'default'),
        ('driver/lxd', 'lxd', 'default'),
        ('driver/openstack', 'openstack', 'default'),
        ('driver/static', 'docker', 'docker'),
        ('driver/static', 'openstack', 'openstack'),
        ('driver/static', 'vagrant', 'vagrant'),
        ('driver/vagrant', 'vagrant', 'default'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_lint(scenario_to_test, with_scenario, skip_test,
                      scenario_name):
    cmd = sh.molecule.bake('lint', {'scenario-name': scenario_name})
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    'scenario_to_test, expected',
    [
        ('driver/docker', """
Instance Name          Driver Name    Provisioner Name    Scenario Name    Created    Converged
---------------------  -------------  ------------------  ---------------  ---------  -----------
instance-1-default     Docker         Ansible             default          False      False
instance-1-multi-node  Docker         Ansible             multi-node       False      False
instance-2-multi-node  Docker         Ansible             multi-node       False      False
""".strip()),  # noqa
        ('driver/lxc', """
Instance Name          Driver Name    Provisioner Name    Scenario Name    Created    Converged
---------------------  -------------  ------------------  ---------------  ---------  -----------
instance-1-default     Lxc            Ansible             default          False      False
instance-1-multi-node  Lxc            Ansible             multi-node       False      False
instance-2-multi-node  Lxc            Ansible             multi-node       False      False
""".strip()),  # noqa
        ('driver/lxd', """
Instance Name          Driver Name    Provisioner Name    Scenario Name    Created    Converged
---------------------  -------------  ------------------  ---------------  ---------  -----------
instance-1-default     Lxd            Ansible             default          False      False
instance-1-multi-node  Lxd            Ansible             multi-node       False      False
instance-2-multi-node  Lxd            Ansible             multi-node       False      False
""".strip()),  # noqa
        ('driver/openstack', """
Instance Name          Driver Name    Provisioner Name    Scenario Name    Created    Converged
---------------------  -------------  ------------------  ---------------  ---------  -----------
instance-1-default     Openstack      Ansible             default          False      False
instance-1-multi-node  Openstack      Ansible             multi-node       False      False
instance-2-multi-node  Openstack      Ansible             multi-node       False      False
""".strip()),  # noqa
        ('driver/static', """
Instance Name              Driver Name    Provisioner Name    Scenario Name    Created    Converged
-------------------------  -------------  ------------------  ---------------  ---------  -----------
static-instance-docker     Static         Ansible             docker           False      True
static-instance-openstack  Static         Ansible             openstack        False      True
static-instance-vagrant    Static         Ansible             vagrant          False      True
""".strip()),  # noqa
        ('driver/vagrant', """
Instance Name          Driver Name    Provisioner Name    Scenario Name    Created    Converged
---------------------  -------------  ------------------  ---------------  ---------  -----------
instance-1-default     Vagrant        Ansible             default          False      False
instance-1-multi-node  Vagrant        Ansible             multi-node       False      False
instance-2-multi-node  Vagrant        Ansible             multi-node       False      False
""".strip()),  # noqa
    ],
    indirect=['scenario_to_test'])
def test_command_list(scenario_to_test, with_scenario, expected):
    pytest.helpers.list(expected)


@pytest.mark.parametrize(
    'scenario_to_test, expected', [
        ('driver/docker', """
instance-1-default     Docker  Ansible  default     False  False
instance-1-multi-node  Docker  Ansible  multi-node  False  False
instance-2-multi-node  Docker  Ansible  multi-node  False  False
""".strip()),
        ('driver/lxc', """
instance-1-default     Lxc  Ansible  default     False  False
instance-1-multi-node  Lxc  Ansible  multi-node  False  False
instance-2-multi-node  Lxc  Ansible  multi-node  False  False
""".strip()),
        ('driver/lxd', """
instance-1-default     Lxd  Ansible  default     False  False
instance-1-multi-node  Lxd  Ansible  multi-node  False  False
instance-2-multi-node  Lxd  Ansible  multi-node  False  False
""".strip()),
        ('driver/openstack', """
instance-1-default     Openstack  Ansible  default     False  False
instance-1-multi-node  Openstack  Ansible  multi-node  False  False
instance-2-multi-node  Openstack  Ansible  multi-node  False  False
""".strip()),
        ('driver/static', """
static-instance-docker     Static  Ansible  docker     False  True
static-instance-openstack  Static  Ansible  openstack  False  True
static-instance-vagrant    Static  Ansible  vagrant    False  True
""".strip()),
        ('driver/vagrant', """
instance-1-default     Vagrant  Ansible  default     False  False
instance-1-multi-node  Vagrant  Ansible  multi-node  False  False
instance-2-multi-node  Vagrant  Ansible  multi-node  False  False
""".strip()),
    ],
    indirect=['scenario_to_test'])
def test_command_list_with_format_plain(scenario_to_test, with_scenario,
                                        expected):
    pytest.helpers.list_with_format_plain(expected)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, instance, regexp, scenario_name', [
        ('driver/docker', 'docker', 'instance-1', '.*instance-1-multi-node.*',
         'multi-node'),
        ('driver/docker', 'docker', 'instance-2', '.*instance-2-multi-node.*',
         'multi-node'),
        ('driver/lxc', 'lxc', 'instance-1', '.*instance-1-multi-node.*',
         'multi-node'),
        ('driver/lxc', 'lxc', 'instance-2', '.*instance-2-multi-node.*',
         'multi-node'),
        ('driver/lxd', 'lxd', 'instance-1', '.*instance-1-multi-node.*',
         'multi-node'),
        ('driver/lxd', 'lxd', 'instance-2', '.*instance-2-multi-node.*',
         'multi-node'),
        ('driver/openstack', 'openstack', 'instance-1',
         '.*instance-1-multi-node.*', 'multi-node'),
        ('driver/openstack', 'openstack', 'instance-2',
         '.*instance-2-multi-node.*', 'multi-node'),
        ('driver/static', 'docker', 'static-instance-vagrant',
         '.*static-instance-vagrant.*', 'docker'),
        ('driver/static', 'openstack', 'static-instance-vagrant',
         '.*static-instance-vagrant.*', 'openstack'),
        ('driver/static', 'vagrant', 'static-instance-vagrant',
         '.*static-instance-vagrant.*', 'vagrant'),
        ('driver/vagrant', 'vagrant', 'instance-1',
         '.*instance-1-multi-node.*', 'multi-node'),
        ('driver/vagrant', 'vagrant', 'instance-2',
         '.*instance-2-multi-node.*', 'multi-node'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_login(scenario_to_test, with_scenario, skip_test, instance,
                       regexp, scenario_name):
    pytest.helpers.login(instance, regexp, scenario_name)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, scenario_name', [
        ('driver/docker', 'docker', 'default'),
        ('driver/lxc', 'lxc', 'default'),
        ('driver/lxd', 'lxd', 'default'),
        ('driver/openstack', 'openstack', 'default'),
        ('driver/static', 'docker', 'docker'),
        ('driver/static', 'openstack', 'openstack'),
        ('driver/static', 'vagrant', 'vagrant'),
        ('driver/vagrant', 'vagrant', 'default'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_syntax(scenario_to_test, with_scenario, skip_test,
                        scenario_name):
    cmd = sh.molecule.bake('syntax', {'scenario-name': scenario_name})
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, scenario_name', [
        ('driver/docker', 'docker', None),
        ('driver/lxc', 'lxc', None),
        ('driver/lxd', 'lxd', None),
        ('driver/openstack', 'openstack', None),
        ('driver/static', 'docker', 'docker'),
        ('driver/static', 'openstack', 'openstack'),
        ('driver/static', 'vagrant', 'vagrant'),
        ('driver/vagrant', 'vagrant', None),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_test(scenario_to_test, with_scenario, skip_test,
                      scenario_name):
    pytest.helpers.test(scenario_name)


@pytest.mark.parametrize(
    'scenario_to_test, skip_test, scenario_name', [
        ('driver/docker', 'docker', 'default'),
        ('driver/lxc', 'lxc', 'default'),
        ('driver/lxd', 'lxd', 'default'),
        ('driver/openstack', 'openstack', 'default'),
        ('driver/static', 'docker', 'docker'),
        ('driver/static', 'openstack', 'openstack'),
        ('driver/static', 'vagrant', 'vagrant'),
        ('driver/vagrant', 'vagrant', 'default'),
    ],
    indirect=['scenario_to_test', 'skip_test'])
def test_command_verify(scenario_to_test, with_scenario, skip_test,
                        scenario_name):
    pytest.helpers.verify(scenario_name)
