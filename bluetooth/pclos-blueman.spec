Name: 		blueman
Version: 	2.0.3
Release: 	%mkrel 3
Summary: 	Full featured bluetooth manager for GNOME/GTK
License: 	GPLv2+
Group: 		Communications
Url: 		http://blueman-project.org/
Source0: 	http://launchpad.net/blueman/1.0/1.10/+download/%{name}-%{version}.tar.xz
Patch0:		dhcpclient_priority
#Patch1:		01_dont_autostart_lxde.patch
#Patch2:		02_dont_crash_on_non-bluetooth_card.patch
BuildRequires:  desktop-file-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  glib2-devel
BuildRequires:  libGConf2-devel
BuildRequires:  pygtk2.0-devel
BuildRequires:  intltool
BuildRequires:	startup-notification-devel
BuildRequires:	python-gobject
BuildRequires:	python-notify
BuildRequires:	bluez-devel
BuildRequires:	python-devel
BuildRequires:	python-pyrex
BuildRequires:	python-dbus
Requires:	python >= 2.7
Requires:	obex-data-server
Requires:	python-notify
Requires:	pygtk2.0
Requires:	gnome-python-gconf
Requires:	python-dbus
Requires:	python-gobject
Requires:	polkit-gnome
Obsoletes:	python-blueman
BuildRoot: 	%_tmppath/%{name}-%{version}


%description
Blueman is designed to provide simple, yet effective means for 
controlling BlueZ API and simplifying bluetooth tasks such as:

* Connecting to 3G/EDGE/GPRS via dial-up
* Connecting to/Creating bluetooth networks
* Connecting to input devices
* Connecting to audio devices
* Sending/Receiving/Browsing files via OBEX
* Pairing

Blueman also integrates with Network Manager 0.7, so any Dialup/Network
 connections will be made available (via HAL) to Network Manager.

%prep
%setup -q
#%apply_patches

%build
autoreconf -fi
%configure2_5x --disable-static --disable-sendto

%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-System-Configuration-Hardware" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}-manager.desktop

%find_lang %{name}

# we don't want these
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%clean_desktop_database
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_sysconfdir}/dbus-1/system.d/org.blueman.Mechanism.conf
%{_sysconfdir}/xdg/autostart/blueman.desktop
%{_bindir}/blueman-adapters
%{_bindir}/blueman-applet
%{_bindir}/blueman-assistant
%{_bindir}/blueman-browse
%{_bindir}/blueman-manager
%{_bindir}/blueman-sendto
%{_bindir}/blueman-services

%{python_sitelib}

%{_libdir}/blueman-mechanism

#%{_libdir}/nautilus-sendto/plugins/libnstblueman.so

%{_libdir}/python2.7/site-packages/_blueman.so

%{_datadir}/applications/blueman-manager.desktop
%{_datadir}/blueman/ui
%{_datadir}/dbus-1
%{_datadir}/icons
%{_datadir}/man
%{_datadir}/polkit-1/actions/org.blueman.policy
/usr/bin/blueman-report
/usr/lib64/blueman-rfcomm-watcher
/usr/share/Thunar/sendto/thunar-sendto-blueman.desktop
/usr/share/applications/blueman-adapters.desktop
/usr/share/doc/blueman/CHANGELOG.md
/usr/share/doc/blueman/COPYING
/usr/share/doc/blueman/FAQ
/usr/share/doc/blueman/README.md
/usr/share/glib-2.0/schemas/org.blueman.gschema.xml
/usr/share/pixmaps/blueman/*



%changelog
* Fri Jul 24 2015 bb <bb> 1.23-2pclos2014
- update from git 201406261335

* Mon Sep 30 2013 bb <bb> 1.23-1pclos2013
- update
- Pulsepatch merged upstream

* Mon Aug 26 2013 bb <bb> 1.21-6pclos2013
- remove .la file

* Fri Aug 16 2013 bb <billybot> 1.21-5pclos2013
- update python 2.7




