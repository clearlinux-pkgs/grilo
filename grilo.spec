#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grilo
Version  : 0.3.4
Release  : 5
URL      : https://download.gnome.org/sources/grilo/0.3/grilo-0.3.4.tar.xz
Source0  : https://download.gnome.org/sources/grilo/0.3/grilo-0.3.4.tar.xz
Summary  : Grilo playlist utility
Group    : Development/Tools
License  : LGPL-2.1
Requires: grilo-bin
Requires: grilo-lib
Requires: grilo-locales
Requires: grilo-doc
Requires: grilo-data
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(oauth)
BuildRequires : totem-pl-parser-dev

%description
Thanks for using Grilo!
=== What is Grilo? ===
Grilo is a framework for browsing and searching media content from various
sources using a single API.

%package bin
Summary: bin components for the grilo package.
Group: Binaries
Requires: grilo-data

%description bin
bin components for the grilo package.


%package data
Summary: data components for the grilo package.
Group: Data

%description data
data components for the grilo package.


%package dev
Summary: dev components for the grilo package.
Group: Development
Requires: grilo-lib
Requires: grilo-bin
Requires: grilo-data
Provides: grilo-devel

%description dev
dev components for the grilo package.


%package doc
Summary: doc components for the grilo package.
Group: Documentation

%description doc
doc components for the grilo package.


%package lib
Summary: lib components for the grilo package.
Group: Libraries
Requires: grilo-data

%description lib
lib components for the grilo package.


%package locales
Summary: locales components for the grilo package.
Group: Default

%description locales
locales components for the grilo package.


%prep
%setup -q -n grilo-0.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503594875
%configure --disable-static --enable-grl-pls
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1503594875
rm -rf %{buildroot}
%make_install
%find_lang grilo

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/grilo-test-ui-0.3
/usr/bin/grl-inspect-0.3
/usr/bin/grl-launch-0.3

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Grl-0.3.typelib
/usr/lib64/girepository-1.0/GrlNet-0.3.typelib
/usr/lib64/girepository-1.0/GrlPls-0.3.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/grilo-0.3/grilo.h
/usr/include/grilo-0.3/grl-caps.h
/usr/include/grilo-0.3/grl-config.h
/usr/include/grilo-0.3/grl-data.h
/usr/include/grilo-0.3/grl-definitions.h
/usr/include/grilo-0.3/grl-error.h
/usr/include/grilo-0.3/grl-log.h
/usr/include/grilo-0.3/grl-media.h
/usr/include/grilo-0.3/grl-metadata-key.h
/usr/include/grilo-0.3/grl-multiple.h
/usr/include/grilo-0.3/grl-operation-options.h
/usr/include/grilo-0.3/grl-operation.h
/usr/include/grilo-0.3/grl-plugin.h
/usr/include/grilo-0.3/grl-range-value.h
/usr/include/grilo-0.3/grl-registry.h
/usr/include/grilo-0.3/grl-related-keys.h
/usr/include/grilo-0.3/grl-source.h
/usr/include/grilo-0.3/grl-util.h
/usr/include/grilo-0.3/grl-value-helper.h
/usr/include/grilo-0.3/net/grl-net-wc.h
/usr/include/grilo-0.3/net/grl-net.h
/usr/include/grilo-0.3/pls/grl-pls.h
/usr/lib64/libgrilo-0.3.so
/usr/lib64/libgrlnet-0.3.so
/usr/lib64/libgrlpls-0.3.so
/usr/lib64/pkgconfig/grilo-0.3.pc
/usr/lib64/pkgconfig/grilo-net-0.3.pc
/usr/lib64/pkgconfig/grilo-pls-0.3.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgrilo-0.3.so.0
/usr/lib64/libgrilo-0.3.so.0.1.3
/usr/lib64/libgrlnet-0.3.so.0
/usr/lib64/libgrlnet-0.3.so.0.0.3
/usr/lib64/libgrlpls-0.3.so.0
/usr/lib64/libgrlpls-0.3.so.0.0.0

%files locales -f grilo.lang
%defattr(-,root,root,-)

