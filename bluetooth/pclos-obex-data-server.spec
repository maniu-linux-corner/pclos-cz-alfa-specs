Name:		obex-data-server
Version:	0.4.6
Release:	%mkrel 3
Summary:	D-Bus service for Obex access
Group:		System/Servers
License:	GPLv2+
Source0:	http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
Patch0:     obex-data-server-0.4.6-build-fixes-1.patch
Url:		http://tadas.dailyda.com/blog
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	dbus-glib-devel
BuildRequires:	bluez-devel
BuildRequires:	openobex-devel
BuildRequires:	gtk2-devel
BuildRequires:	libusb-devel
BuildRequires:	libtool
Obsoletes:	%name < %version

%description
obex-data-server is a D-Bus service to allow sending and receiving files
using the ObexFTP and Obex Push protocols, common on mobile phones and
other Bluetooth-equipped devices.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --enable-system-config --enable-bip=gdk-pixbuf
%make

cat << EOF > README
Bug tracking system is at:
http://bugs.muiline.com/view_all_bug_page.php

Web page is at:
http://tadas.dailyda.com/blog/

SVN tree:
svn://svn.muiline.com/obex-data-server/trunk/

SVN browsing:
http://svn.muiline.com/cgi-bin/viewvc.cgi/obex-data-server/trunk/

EOF

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS README COPYING dbus-api.txt
%{_bindir}/obex-data-server
%{_datadir}/dbus-1/services/obex-data-server.service
%config %{_sysconfdir}/obex-data-server/*.xml
%{_mandir}/man1/obex-data-server.1.*
/etc/dbus-1/system.d/obex-data-server.conf



%changelog
* Mon Aug 26 2013 billybot <billybot> 0.4.6-2pclos2013
- rebuild against updated libs

* Fri Apr 29 2011 Texstar <texstar at gmail.com> 0.4.6-1pclos2011
- 0.4.6

* Fri Aug 13 2010 Texstar <texstar at gmail.com> 0.4.5-2pclos2010
- rebuild

* Fri Dec 04 2009 pcserver <pcserver at hush.com> 0.4.5-1pclos2010
- gcc update
- sync with mdv

