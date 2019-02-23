#
# Apache CouchDB spec
#

Name:		apache-couchdb
Version:	2.3.0
Release:	0
Summary:	Apache CouchDB Server
Group:		Applications/Servers
License:	Apache 2.0
URL:		http://www.couchdb.org
Source0:	%{name}-%{version}.tar.gz
Source1:	couchdb.service

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
install -D -m 644 %{S:1} %{buildroot}%{_unitdir}/couchdb.service


%files
/opt/couchdb
%{_unitdir}/couchdb.service

%pre -n apache-couchdb
if ! id -u couchdb > /dev/null 2>&1; then
    useradd -U -s /bin/nologin -d /opt/couchdb couchdb || /bin/true
fi
%service_add_pre couchdb.service

%post -n apache-couchdb
chown -R couchdb:couchdb /opt/couchdb
%service_add_post couchdb.service

%preun -n apache-couchdb
%service_del_preun couchdb.service

%postun -n apache-couchdb
%service_del_postun couchdb.service


%changelog
* Sun Jul 22 2018 Danilo CHang <ray2501@gmail.com>
- Update for openSUSE

* Thu Dec 22 2016 Craig Dunn <craig@craigdunn.org>
- Initial couchdb package for CentOS
