from setuptools import setup, find_packages


setup(
    name='ceph-upgrade',
    version='0.0.1',
    packages=find_packages(),
    author='',
    author_email='contact@redhat.com',
    description='Perform system upgrades like taking over ceph-disk OSDs with ceph-volume',
    license='LGPLv2+',
    keywords='ceph upgrade osd disk devices lvm',
    url="https://github.com/ceph/ceph-upgrade",
    zip_safe = False,
    tests_require=[
        'pytest >=2.1.3',
        'tox',
    ],
    entry_points = dict(
        console_scripts = [
            'ceph-upgrade = ceph_upgrade.main:Upgrade',
        ],
    ),
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
