#
# Apache CouchDB spec
#

Name:		apache-couchdb
Version:	2.1.2
Release:	0
Summary:	Apache CouchDB Server
Group:		Applications/Servers
License:	Apache 2.0
URL:		http://www.couchdb.org
Source0:	%{name}-%{version}.tar.gz

# These dependencies are for EL based platforms.
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: curl-devel
BuildRequires: help2man
BuildRequires: js-devel >= 1.8.5
BuildRequires: libicu-devel
BuildRequires: libtool
BuildRequires: perl-Test-Harness
BuildRequires: erlang
BuildRequires: erlang-reltool
BuildRequires: gcc-c++


%description
Apache CouchDB Server


%prep
/bin/rm -rf %{buildroot}

%setup -q


%build
./configure
make release 


%install
mkdir -p %{buildroot}/opt
cp -r rel/couchdb %{buildroot}/opt/couchdb


%files
/opt/couchdb

%post
useradd -U -s /bin/nologin -d /opt/couchdb couchdb || /bin/true
chown -R couchdb:couchdb /opt/couchdb


IS_SYSTEMD=$((pidof systemd 2>&1 > /dev/null)  && echo "yes" || echo "no")
if [ "$IS_SYSTEMD" == "yes" ]; then
cat <<EOF > /etc/systemd/system/couchdb.service
[Unit]
Description=Apache CouchDB Server

[Service]
ExecStart=/opt/couchdb/bin/couchdb
User=couchdb
Type=simple

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
fi

%changelog
* Sun Jul 22 2018 Danilo CHang <ray2501@gmail.com>
- Update for openSUSE

* Thu Dec 22 2016 Craig Dunn <craig@craigdunn.org>
- Initial couchdb package for CentOS
