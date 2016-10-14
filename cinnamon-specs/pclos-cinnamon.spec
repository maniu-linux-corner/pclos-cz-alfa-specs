%global _internal_version  677b05e
%define date 20130930
%define pandir %{buildroot}/%{_datadir}/icons/hicolor/scalable/actions/

Name:           cinnamon
Version:        3.0.1
Release:        %mkrel 1
Summary:        Window management and application launching for Cinnamon
Group:          Graphical desktop/Cinnamon
License:        GPLv2+ and LGPLv2+
URL:            http://cinnamon.linuxmint.com
Source0:        %{name}-%{version}.tar.gz
Source1:	default-32.jpg
Source2:	default-64.jpg
Source3:	cinnamon-pclos.gschema.override
Source4:        cinnamon-nm-applet.desktop
Source5:        10cinnamon
Source6:        11cinnamon2d
Source7:	cinnamon-applications.menu
Source8:	cinnamon-settings.desktop
Source9:	pclos-org.cinnamon.settings-users.policy
Source10:	32-polkit-cinnamon-authentication-agent-1.desktop
Source11:	64-polkit-cinnamon-authentication-agent-1.desktop
Source12:	cinnamon.session
Source14:	cinnamon2d.session
#Patch0:         autostart.patch
#Patch3:         cinnamon-settings-apps.patch
#Patch4:         keyboard_applet.patch
#Patch5:         input_keybindings.patch
#Patch6:         bluetooth.patch
#Patch7:		no-network-manager.patch
#Patch8:		cinnamon-2.0.14-menu-localization.patch
#Patch9:		cinnamon-2.0.14-icon-menu-fix.patch
%global clutter_version 1.7.5
%global gobject_introspection_version 0.10.1
%global muffin_version 1.9.1
%global eds_version 2.91.6
%global json_glib_version 0.13.2
%global polkit_version 0.100
#--------------------------------------------------------------------------------------
BuildRequires:  pkgconfig(clutter-x11-1.0) >= %{clutter_version}
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_version}
#BuildRequires:  pkgconfig(libnm-glib)
#BuildRequires:  pkgconfig(libnm-util)
BuildRequires:  pkgconfig(polkit-agent-1) >= %{polkit_version}
BuildRequires:  libgudev-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  intltool
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcroco-0.6) >= 0.6.2
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xfixes) >= 5.0
BuildRequires:  librsvg2-devel
BuildRequires:  pkgconfig(libmuffin) >= %{muffin_version}
BuildRequires:  libpulseaudio-devel
BuildRequires:  gnome-bluetooth-devel >= 2.91
BuildRequires:  gnome-bluetooth >= 2.91
BuildRequires: 	gtk-doc gnome-common
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
#BuildRequires:  pkgconfig(cjs-internals-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(cinnamon-desktop)
#BuildRequires:  %{_lib}nm-glib-vpn-devel
BuildRequires:  x11-driver-input-wacom-devel
BuildRequires:	gettext-devel
Requires:       gnome-menus >= 3.0.0-2
Requires:       gobject-introspection >= %{gobject_introspection_version}
Requires:       json-glib >= %{json_glib_version}
Requires:       upower
Requires:       polkit >= 0.100
Requires:       at-spi2-atk
Requires:       python-gobject
Requires:       dbus-python
Requires:       python-lxml
Requires:       gnome-python-gconf
Requires:       python-imaging
Requires:       python-pam
Requires:       python-pexpect
Requires:       python-pillow
Requires:       cinnamon-control-center
Requires:	cinnamon-desktop
Requires:       cinnamon-screensaver
Requires:       cinnamon-session
Requires:	cinnamon-settings-daemon
Requires:       cinnamon-translations
Requires:       muffin >= %{muffin_version}
Requires:	nemo
Requires:	accountsservice
Requires:       gnome-themes-standard
Requires:       gobject-introspection
Requires:	caribou
Requires:       cjs
Requires:	cogl
Requires:	clutter
Requires:	%{_lib}mozjs185_1.0
Requires:	dconf
Requires:	dconf-editor
Requires:	python-gobject3
Requires:	colord
Requires:	canberra-gtk
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Cinnamon is a Linux desktop which provides advanced
 innovative features and a traditional user experience.

The desktop layout is similar to Gnome 2. 
The underlying technology is forked from Gnome Shell.
The emphasis is put on making users feel at home and providing
 them with an easy to use and comfortable desktop experience.

%prep
%setup -q

rm -f configure
rm -rf debian/

sed -i 's/RequiredComponents=\(.*\)$/RequiredComponents=\1polkit-gnome-authentication-agent-1;/' \
    files/usr/share/cinnamon-session/sessions/cinnamon*.session

NOCONFIGURE=1 ./autogen.sh --prefix=/usr \
               --sysconfdir=/etc \
               --libexecdir=/usr/lib64/cinnamon \
               --localstatedir=/var \
               --disable-static \
               --disable-schemas-compile \
               --enable-compile-warnings=yes

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=deprecated-declarations"
%configure2_5x \
--disable-static \
--disable-rpath \
--enable-compile-warnings=yes \
--enable-introspection=yes \
--disable-networkmanager \
--disable-schemas-compile

sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
%make V=1

%install
rm -rf %{buildroot}
%makeinstall_std

# Remove .la file
rm -rf %{buildroot}/%{_libdir}/cinnamon/libcinnamon.la

install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT/%{_datadir}/applications/


desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/cinnamon.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/cinnamon2d.desktop
#desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/cinnamon-add-panel-launcher.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/cinnamon-settings-users.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/cinnamon-menu-editor.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/cinnamon-nm-applet.desktop

install -m 0644 %SOURCE8 $RPM_BUILD_ROOT/%{_datadir}/applications/cinnamon-settings.desktop


# fix hard coded path
#%ifarch x86_64
#sed -i -e 's@/usr/lib/cinnamon-control-center@/usr/lib64/cinnamon-control-center@g' \
#$RPM_BUILD_ROOT/%{_prefix}/lib/cinnamon-settings/bin/capi.py
#%endif

# install policy file
install -m 0755 -d $RPM_BUILD_ROOT/%{_datadir}/polkit-1/actions/
install -D -p -m 0644 %{SOURCE9} $RPM_BUILD_ROOT/%{_datadir}/polkit-1/actions/org.cinnamon.settings-users.policy

# install polkik autostart desktop file
%ifarch %{ix86}
install -D -p -m 0644 %{SOURCE10} $RPM_BUILD_ROOT/%{_datadir}/applications/
%else
install -D -p -m 0644 %{SOURCE11} $RPM_BUILD_ROOT/%{_datadir}/applications/
%endif

mkdir -p %{buildroot}/%{_sysconfdir}/X11/wmsession.d

install -pm 0644 %SOURCE5 %SOURCE6 %{buildroot}/%{_sysconfdir}/X11/wmsession.d

mkdir -p %{buildroot}/%{_datadir}/backgrounds/cinnamon
%ifarch %{ix86}
install -m 0644 %SOURCE1 %{buildroot}/%{_datadir}/backgrounds/cinnamon/default.jpg
%else
install -m 0644 %SOURCE2 %{buildroot}/%{_datadir}/backgrounds/cinnamon/default.jpg
%endif

install -D -m 0644 %SOURCE3 $RPM_BUILD_ROOT/%{_datadir}/glib-2.0/schemas/cinnamon-pclos.gschema.override

install -m 0644 %SOURCE7 $RPM_BUILD_ROOT/%{_sysconfdir}/xdg/menus/cinnamon-applications.menu

install -m 0744 %SOURCE12 $RPM_BUILD_ROOT/%{_datadir}/cinnamon-session/sessions/cinnamon.session

install -m 0744 %SOURCE14 $RPM_BUILD_ROOT/%{_datadir}/cinnamon-session/sessions/cinnamon2d.session


#notneeded
#rm -rf %{buildroot}/%{_datadir}/icons/hicolor/
rm %{pandir}/pan-down-symbolic.svg %{pandir}/pan-end-symbolic-rtl.svg %{pandir}/pan-end-symbolic.svg %{pandir}/pan-start-symbolic-rtl.svg %{pandir}/pan-start-symbolic.svg %{pandir}/pan-up-symbolic.svg;

rm -rf %{buildroot}/%{_datadir}/xsessions

#network manager not used in pclos
rm -rf %{buildroot}%{_datadir}/cinnamon/applets/network@cinnamon.org


%find_lang %{name}
%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README NEWS AUTHORS
%{_bindir}/*
%{_sysconfdir}/xdg/menus/*
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/org.Cinnamon.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.Cinnamon.Melange.service
%{_datadir}/dbus-1/services/org.Cinnamon.Slideshow.service
%{_datadir}/desktop-directories/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/cinnamon-session/sessions/*
%{_datadir}/cinnamon/
%{_libdir}/cinnamon/
%{_libdir}/cinnamon*/
%{_mandir}/man1/*
%{_sysconfdir}/X11/wmsession.d/*cinnamon*
%{_datadir}/backgrounds/cinnamon/default.jpg
%{_datadir}/polkit-1/actions/org.cinnamon.settings-users.policy
%{_datadir}/gtk-doc/*
%{_datadir}/icons/hicolor/*

%post
%make_session

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
%make_session


%clean
rm -rf %{buildroot}

%changelog
* Wed Dec 25 2016 Mank <mank at pclinuxos dot cz> 2.8.6-1mank2016
- update

* Tue Apr 15 2014 bb <bb> 2.0.14-2pclos2014
- rebuild against updated libs

* Wed Dec 25 2013 bb <bb> 2.0.14-1pclos2013
- update

* Wed Nov 13 2013 billybot <billybot> 2.0.12-1pclos2013
- update

* Tue Nov 12 2013 billybot <billybot> 2.0.11-3plcos2013
- build without network manager development files

* Tue Nov 12 2013 billybot <billybot> 2.0.11-2pclos2013
- remove network manager applet not used in pclos to 
- help startup time to desktop

* Tue Nov 12 2013 billybot <billybot> 2.0.11-1pclos2013
- update

* Mon Nov 11 2013 billybot <billybot> 2.0.10-2plos2013
- adjust default apps in control center for pclos

* Mon Nov 04 2013 billybot <billybot> 2.0.10-1pclos2013
- update

* Thu Oct 31 2013 billybot <billybot> 2.0.7-1pclos2013
- update

* Sun Oct 27 2013 billybot <billybot> 2.0.6-2pclos2013
- add polkit-1 policy for users and groups
- add more required dependencies

* Sat Oct 26 2013 billybot <billybot> 2.0.6-1pclos2013
- update

* Sat Oct 26 2013 billybot <billybot> 2.0.5-2pclos2013
- add missing Dep.caribou

* Fri Oct 25 2013 billybot <billybot> 2.0.5-1pclos2013
- update

* Wed Oct 23 2013 billybot <billybot> 2.0.4-1pclos2013
- update

* Wed Oct 23 2013 billybot <billybot> 2.0.3-1pclos2013
- update

* Sat Oct 19 2013 billybot <billybot> 2.0.2-1pclos2013
- import into pclos
