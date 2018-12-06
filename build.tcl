#!/usr/bin/tclsh

package require http
package require tls

set arch "x86_64"
set fileurl "http://ftp.tc.edu.tw/pub/Apache/couchdb/source/2.3.0/apache-couchdb-2.3.0.tar.gz"
set base "apache-couchdb-2.3.0"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb couchdb.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove source package
file delete $base.tar.gz

