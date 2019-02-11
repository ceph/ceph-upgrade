from __future__ import print_function
import argparse
import os
import sys
import logging

from ceph_upgrade.decorators import catches
from ceph_upgrade import log, conf


class Upgrade(object):
    _help = """
ceph-upgrade: Perform system upgrades like taking over ceph-disk OSDs with ceph-volume.

Log Path: {log_path}

{warning}
    """

    def __init__(self, argv=None, parse=True):
        self.mapper = {}
        if argv is None:
            self.argv = sys.argv
        else:
            self.argv = argv
        if parse:
            self.main(self.argv)

    def help(self, warning=False):
        warning = 'See "ceph-upgrade --help" for full list of options.' if warning else ''
        return self._help.format(
            warning=warning,
            log_path=conf.log_path,
        )

    def load_log_path(self):
        conf.log_path = os.getenv('CEPH_UPGRADE_LOG_PATH', '/var/log/ceph')

    def _get_split_args(self):
        subcommands = self.mapper.keys()
        slice_on_index = len(self.argv) + 1
        pruned_args = self.argv[1:]
        for count, arg in enumerate(pruned_args):
            if arg in subcommands:
                slice_on_index = count
                break
        return pruned_args[:slice_on_index], pruned_args[slice_on_index:]

    @catches()
    def main(self, argv):
        self.load_log_path()
        main_args, subcommand_args = self._get_split_args()
        # no flags where passed in, return the help menu instead of waiting for
        # argparse which will end up complaning that there are no args
        if len(argv) <= 1:
            print(self.help(warning=True))
            raise SystemExit(0)
        parser = argparse.ArgumentParser(
            prog='ceph-upgrade',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=self.help(),
        )
        parser.add_argument(
            '--cluster',
            default='ceph',
            help='Cluster name (defaults to "ceph")',
        )
        parser.add_argument(
            '--log-level',
            default='debug',
            help='Change the file log level (defaults to debug)',
        )
        parser.add_argument(
            '--log-path',
            default='/var/log/ceph/',
            help='Change the log path (defaults to /var/log/ceph)',
        )
        args = parser.parse_args(main_args)
        conf.log_path = args.log_path
        if os.path.isdir(conf.log_path):
            conf.log_path = os.path.join(args.log_path, 'ceph-upgrade.log')
        log.setup()
        logger = logging.getLogger(__name__)
        logger.info("Running command: ceph-upgrade %s %s", " ".join(main_args), " ".join(subcommand_args))
