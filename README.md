HCS Systems Configuration
=========================

HCS uses a tool called [Bcfg2][bcfg2] to help us manage the configuration of
each of our systems. This allows us to spin up machines of different classes via
a cookie-cutter like process, without having giant installation scripts, or
worrying whether similar machines are actually configured differently.

Similar tools include [Puppet][puppet] and [Chef][chef]. We use Bcfg2 largely as
a historical accident, although it has quite a few features to recommend it.

[bcfg2]: https://trac.mcs.anl.gov/projects/bcfg2
[puppet]: http://puppetlabs.com/
[chef]: http://www.opscode.com/chef/

Documentation
-------------

This configuration is written against the (as of this writing, unreleased)
[1.3.0][docs] version of Bcfg2, and is installed on our systems via the official
testing Ubuntu [PPA][ppa].

If you're new to Bcfg2, I recommend reading a bit of the intro material from the
documentation, and then dive in to the [Ubuntu guide][ubuntu], which will guide
you along the process of configuring a fresh Ubuntu install. From there, the
best way of learning is by doing. Take a look at the [server plugins][plugins]
documentation, which is where most of the interesting work goes on. The
[Metadata][metadata], [Bundler][bundler], and [Cfg][cfg] pages are especially
worth familiarizing yourself with.

If you're ever unsure about what's going on, Bcfg2 comes with an excellent
debugging utility called [`bcfg2-info`][bcfg2-info], which allows you to examine
the output that would be sent to any client, print out various metadata, list
clients and groups, etc. It's super effective!

[1.3.0]: http://docs.bcfg2.org/dev/
[ppa]: https://launchpad.net/~bcfg2/+archive/precisetesting
[ubuntu]: http://docs.bcfg2.org/dev/appendix/guides/ubuntu.html
[plugins]: http://docs.bcfg2.org/dev/server/plugins/index.html
[metadata]: http://docs.bcfg2.org/dev/server/plugins/grouping/metadata.html
[bundler]: http://docs.bcfg2.org/dev/server/plugins/structures/bundler/index.html
[cfg]: http://docs.bcfg2.org/dev/server/plugins/generators/cfg.html
[bcfg2-info]: http://docs.bcfg2.org/dev/server/bcfg2-info.html

Encryption
----------

Some configuration, such as SSL private keys, SSH host keys, passwords, and
more, are very sensitive, and are not the sort of thing you want floating around
in a public repository like this one. Luckily, Bcfg2 supports [encrypted
files][encrypt], which allow us to keep our small number of secrets, well,
secret! These are decrypted automatically on the configuration server before
being sent to the host. If you need to add a new file, the `bcfg2-crypt` utility
installed alongside `bcfg2-server` might prove of use. The encryption password
can be found either on the configuration servers themselves, or stored as
`bcfg2-crypt-key` in the secrets repository.

[encrypt]: http://docs.bcfg2.org/dev/server/plugins/generators/cfg.html#encrypted-files
