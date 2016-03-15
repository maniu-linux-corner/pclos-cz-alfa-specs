Name:		obexd
Version:	0.48
Release:	%mkrel 1
Summary:	D-Bus service for Obex Client access
Group:		Communications
License:	GPLv2+
Source0:	http://www.kernel.org/pub/linux/bluetooth/obexd-%{version}.tar.xz
Url:		http://www.bluez.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	glib2-devel
BuildRequires:	dbus-devel
BuildRequires:	bluez-devel >= 4.0
BuildRequires:	openobex-devel
BuildRequires:  %{_lib}ical-devel

%description
obexd contains obex-client, a D-Bus service to allow sending files
using the Obex Push protocol, common on mobile phones and
other Bluetooth-equipped devices.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README AUTHORS doc/client-api.txt
%{_libexecdir}/obex-client
%{_datadir}/dbus-1/services/obex-client.service
%{_libdir}/obexd
%{_datadir}/dbus-1/services/obexd.service



%changelog
* Mon Aug 26 2013 billybot <billybot> 0.47-1pclos2013
- update

* Fri Aug 13 2010 Texstar <texstar at gmail.com> 0.30-1pclos2010
- 0.30

* Thu Dec 17 2009 Texstar <texstar at gmail.com> 0.20-2pclos2010
- rebuild
