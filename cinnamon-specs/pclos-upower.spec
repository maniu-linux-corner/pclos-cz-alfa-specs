%define realversion 0.99.3

%define name	upower
%define oname	UPower
%define version	0.99.3
%define release	%mkrel 1
%define major 3
%define libname %mklibname upower-glib %major
%define develname %mklibname -d upower-glib
%define oldlibname %mklibname devkit-power-gobject 1
%define olddevelname %mklibname -d devkit-power-gobject

Name: %name
Version: %version
Release: %release
Summary: Power Management Service
License: GPLv2+
Group: System/Kernel and hardware
URL:     http://upower.freedesktop.org/
Source0: http://upower.freedesktop.org/releases/%{name}-%{realversion}.tar.xz
Provides: %{oname} = %{version}-%{release}
BuildRequires: libgudev-devel
BuildRequires: dbus-glib-devel
BuildRequires: polkit-1-devel >= 0.91
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: libusb-devel
BuildRequires: libxslt-proc
BuildRequires: docbook-style-xsl
BuildRequires: gobject-introspection-devel
BuildRequires: libimobiledevice-devel
BuildRequires: gtk-doc
Requires: pm-utils
Obsoletes: devicekit-power
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
%{oname} provides a daemon, API and command line tools for
managing power devices attached to the system.

%package -n %libname
Summary: Shared Library of %{oname}
Group: System/Libraries
Requires: %name >= %version-%release
Obsoletes: %oldlibname

%description -n %libname
%{oname} provides a daemon, API and command line tools for
managing power devices attached to the system.


%package -n %develname
Summary: Headers and libraries for %{oname}
Group: Development/Libraries
Provides: %{oname}-devel = %{version}-%{release}
Requires: %{name}
Requires: %libname = %version-%release
Obsoletes: %olddevelname

%description -n %develname
Headers and libraries for %{oname}

%prep
%setup -q -n %{name}-%{realversion}

%build
%configure2_5x --disable-dependency-tracking --enable-gtk-doc=no --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -fr %buildroot%{_libdir}/*.la

%find_lang %name

%clean
rm -rf %{buildroot}


%files -f %name.lang
%defattr(-,root,root,-)

%doc README AUTHORS NEWS HACKING
%dir %_sysconfdir/UPower/
%config(noreplace) %_sysconfdir/UPower/UPower.conf
%{_sysconfdir}/dbus-1/system.d/*.conf
/lib/udev/rules.d/*.rules

%{_bindir}/*
%{_libexecdir}/upowerd

%{_mandir}/man1/*
%{_mandir}/man7/*
%{_mandir}/man8/*

#%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/dbus-1/system-services/*.service

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libupower-glib.so.%{major}*
%{_libdir}/girepository-1.0/UPowerGlib-1.0.typelib

%files -n %develname
%{_datadir}/dbus-1/interfaces/*.xml
%{_libdir}/*.so
%{_libdir}/pkgconfig/upower-glib.pc
%{_datadir}/gir-1.0/UPowerGlib-1.0.gir
%{_includedir}/libupower-glib


%changelog
* Tue May 26 2014 bb <bb> 0.9.20-3pclos2014
- rebuild against updated libs

* Fri Jun 21 2013 Texstar <texstar at gmail.com> 0.9.20-2pclos2013
- back down to working version

* Thu Jun 20 2013 Texstar <texstar at gmail.com> 0.9.20-1pclos2013
- update

* Mon Oct 08 2012 Neal <nealbrks0 at gmail dot com> 0.9.18-1pclos2012
- process

* Sun Oct 07 2012 Ken <lxgator at gmail.com> 0.9.18-1pclos2012
- 0.9.18

* Tue Jul 19 2011 Texstar <texstar at gmail.com> 0.9.12-1pclos2011
- 0.9.12

* Thu Jul 07 2011 Texstar <texstar at gmail.com> 0.9.11-1pclos2011
- 0.9.11

