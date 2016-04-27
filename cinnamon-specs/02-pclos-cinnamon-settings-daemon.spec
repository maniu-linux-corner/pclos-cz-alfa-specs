%global _internal_version  53e0491
%global date 20160407

Name:           cinnamon-settings-daemon
Version:        3.0.0
Release:        %mkrel 1
Summary:        The daemon sharing settings from CINNAMON to GTK+/KDE applications
Group:          Graphical desktop/Cinnamon
License:        GPLv2+ and LGPLv2+
URL:            http://cinnamon.linuxmint.com
Source0:        cinnamon-settings-daemon-%{version}.tar.gz

#---------------------------------------------------------
BuildRequires:  dbus-glib-devel
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.99.3
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(libpulse) >= 0.9.16
BuildRequires:  pkgconfig(libpulse-mainloop-glib) >= 0.9.16
BuildRequires:  pkgconfig(libnotify) >= 0.7.3
BuildRequires:  intltool
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  gnome-common
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  cups-devel
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(lcms2) >= 2.2
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  libxkbfile-devel
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  %{_lib}upower-glib-devel
BuildRequires:  %{_lib}gnomekbd-devel
#--------------------------------------------------------
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A daemon to share settings from CINNAMON to other applications. It also
handles global keybindings, and many of desktop-wide settings.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       dbus-glib-devel


%description    devel
This package contains libraries and header files for
developing applications that use %{name}.
 

%prep
%setup -q -n cinnamon-settings-daemon-%{version}
#%apply_patches

sed -i -e 's@{ACLOCAL_FLAGS}@{ACLOCAL_FLAGS} -I m4@g' Makefile.am
echo "AC_CONFIG_MACRO_DIR([m4])" >> configure.ac

%build
NOCONFIGURE=1 autoreconf -fi
%configure2_5x --disable-static --enable-profiling 

%make V=1


%install
rm -rf %{buildroot}
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING
%config %{_sysconfdir}/dbus-1/system.d/org.cinnamon.SettingsDaemon.DateTimeMechanism.conf
%{_libdir}/cinnamon-settings-daemon-3.0/
%{_libexecdir}/cinnamon-settings-daemon
%{_libexecdir}/csd-backlight-helper
%{_libexecdir}/csd-datetime-mechanism
%{_libexecdir}/csd-locate-pointer
%{_libexecdir}/csd-printer
%{_libexecdir}/csd-list-wacom
%{_libexecdir}/csd-wacom-led-helper
%{_datadir}/applications/cinnamon-settings-daemon.desktop
%{_datadir}/cinnamon-settings-daemon/
%{_datadir}/dbus-1/system-services/org.cinnamon.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon*.xml
%{_datadir}/icons/hicolor/*/apps/csd-xrandr.*
%{_datadir}/polkit-1/actions/org.cinnamon.settings*.policy
%{_mandir}/man1/cinnamon-settings-daemon.1.*

%files devel
%defattr(-,root,root)
%{_includedir}/cinnamon-settings-daemon-3.0/
%{_libdir}/pkgconfig/cinnamon-settings-daemon.pc
%{_libexecdir}/csd-test-*
%{_datadir}/cinnamon-settings-daemon-3.0/

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :


%clean
rm -rf %{buildroot}

%changelog
* Wed Apr 20 2016 Mank <mank at pclinuxos dot cz> 2.8.4-1mank2016
- update
* Wed Dec 25 2015 Mank <mank at pclinuxos dot cz> 2.8.3-1mank2016
- update

* Wed Dec 25 2014 bb <bb> 2.0.8-1pclos2013
- update

* Tue Nov 12 2013 billybot <billybot> 2.0.7-1pclos2013
- update

* Mon Nov 11 2013 billybot <billybot> 2.0.6-1pclos2013
- update

* Sat Oct 26 2013 billybot <billybot> 2.0.5-1pclos2013
- update

* Fri Oct 25 2013 billybot <billybot> 2.0.4-1pclos2013
- update

* Wed Oct 23 2013 billybot <billybot> 2.0.3-1pclos2013
- update

* Sat Oct 19 2013 billybot <billybot> 2.0.1-1pclos2013
- import into pclos
