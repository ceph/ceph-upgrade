import pytest
from ceph_upgrade import main


class TestVolume(object):

    def test_main_spits_help_with_no_arguments(self, capsys):
        with pytest.raises(SystemExit):
            main.Upgrade(argv=[])
        stdout, stderr = capsys.readouterr()
        assert 'Log Path' in stdout

    def test_warn_about_using_help_for_full_options(self, capsys):
        with pytest.raises(SystemExit):
            main.Upgrade(argv=[])
        stdout, stderr = capsys.readouterr()
        assert 'See "ceph-upgrade --help" for full list' in stdout

    def test_flags_are_parsed_with_help(self, capsys):
        with pytest.raises(SystemExit):
            main.Upgrade(argv=['ceph-volume', '--help'])
        stdout, stderr = capsys.readouterr()
        assert '--cluster' in stdout
        assert '--log-path' in stdout
