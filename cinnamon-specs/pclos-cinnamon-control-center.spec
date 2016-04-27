%global _internal_version  db6f1e5
%global glib2_version 2.31.0
%global gtk3_version 3.5.13
%global csd_version 1.0.0
%global gnome_desktop_version 3.5.91
%global desktop_file_utils_version 0.9
%global gnome_menus_version 2.11.1
%global libXrandr_version 1.2.99

Summary: Utilities to configure the Cinnamon desktop
Name:    cinnamon-control-center
Version: 3.0.0
Release: %mkrel 1
Group:  Graphical desktop/Cinnamon
License: GPLv2+ and LGPLv2+ and MIT and ISC
URL:     http://cinnamon.linuxmint.com
Source0: cinnamon-control-center-%{version}.tar.gz
Source1: cinnamon-control-center-sounds-1.0.0.tar.xz
#Patch0:   region.patch
Requires: cinnamon-settings-daemon >= %{csd_version}
Requires: hicolor-icon-theme
Requires: gnome-icon-theme
Requires: gnome-menus >= %{gnome_menus_version}
Requires: cinnamon-desktop
Requires: cinnamon-translations
Requires: dbus-x11
Obsoletes: %{name}-filesystem <= %{version}-%{release}
Requires: libxrandr >= %{libXrandr_version}
Requires: iso-codes
Requires: gnome-icon-theme-symbolic
#Requires: cups-pk-helper
Requires: glxinfo
Requires: xdriinfo
#---------------------------------------------------------------
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= 2.23.0
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(cinnamon-desktop)
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xrandr) >= %{libXrandr_version}
BuildRequires: pkgconfig(libgnome-menu-3.0) >= %{gnome_menus_version}
BuildRequires: cinnamon-settings-daemon-devel >= %{csd_version}
BuildRequires: intltool >= 0.37.1
BuildRequires: pkgconfig(xxf86misc)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: gnome-doc-utils
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(dbus-1) >= 0.90
BuildRequires: pkgconfig(dbus-glib-1) >= 0.70
BuildRequires: chrpath
BuildRequires: pkgconfig(libpulse) >= 2.0
BuildRequires: pkgconfig(libpulse-mainloop-glib) >= 2.0
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(libnm-glib) >= 0.9
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: gnome-common
BuildRequires: cups-devel
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(colord)
BuildRequires: pkgconfig(libnotify)
BuildRequires: gnome-doc-utils
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(libgnomekbd)
BuildRequires: pkgconfig(libxklavier)
#----------------------------------------------------------
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains configuration utilities for the Cinnamon desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse
properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header files and libraries for developing Muffin plugins. Also includes
utilities for testing Metacity/Muffin themes.


%prep
%setup -q
tar -xJf %{SOURCE1}
#%apply_patches

%build
autoreconf -vfi
%configure2_5x \
        --disable-static \
        --disable-update-mimedb \
        --with-libsocialweb=no \
        --enable-ibus \
        --enable-bluetooth

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

%make V=1

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-edit                                       \
  --set-icon=cinnamon-preferences-color                 \
  $RPM_BUILD_ROOT%{_datadir}/applications/cinnamon-color-panel.desktop
desktop-file-install                                    \
  --delete-original                                     \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
  $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

# remove useless libtool archive files
find $RPM_BUILD_ROOT -name '*.la' -delete

# remove rpath
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/cinnamon-control-center-1/panels/*.so
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/cinnamon-control-center

# install sound files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/cinnamon-control-center/sounds/
install -pm 0644 sounds/* $RPM_BUILD_ROOT/%{_datadir}/cinnamon-control-center/sounds/


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_datadir}/cinnamon-control-center/ui/
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/*
%{_datadir}/icons/hicolor/*/*/*
#%{_datadir}/cinnamon-control-center/icons/
%{_datadir}/cinnamon-control-center/sounds/*.oga
# list all binaries explicitly, so we notice if one goes missing
%{_bindir}/cinnamon-control-center
#%{_bindir}/cinnamon-sound-applet
#%config %{_sysconfdir}/xdg/autostart/cinnamon-sound-applet.desktop
%config %{_sysconfdir}/xdg/menus/cinnamoncc.menu
%{_libdir}/libcinnamon-control-center.so.1*
%dir %{_libdir}/cinnamon-control-center-1/
%{_libdir}/cinnamon-control-center-1/panels/libcolor.so
%{_libdir}/cinnamon-control-center-1/panels/libdisplay.so
#%{_libdir}/cinnamon-control-center-1/panels/libnetwork.so
#%{_libdir}/cinnamon-control-center-1/panels/libpower.so
%{_libdir}/cinnamon-control-center-1/panels/libregion.so
#%{_libdir}/cinnamon-control-center-1/panels/libscreen.so
#%{_libdir}/cinnamon-control-center-1/panels/libsoundnua.so
#%{_libdir}/cinnamon-control-center-1/panels/libuniversal-access.so
%{_libdir}/cinnamon-control-center-1/panels/libdate_time.so
%{_libdir}/cinnamon-control-center-1/panels/libwacom-properties.so
%{_datadir}/cinnamon-control-center/datetime/backward
%{_datadir}/locale/*
%{_datadir}/polkit-1/rules.d/cinnamon-control-center.rules

%files devel
%defattr(-,root,root)
%{_includedir}/cinnamon-control-center-1/
%{_libdir}/libcinnamon-control-center.so
%{_libdir}/pkgconfig/libcinnamon-control-center.pc


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%clean
rm -rf %{buildroot}

%changelog
* Wed Dec 24 2016 Mank <mank at pclinuxos dot cz> 2.8.1-1mank2016
- update

* Wed Dec 24 2013 bb <bb> 2.0.9-1pclos2013
- update

* Mon Nov 11 2013 billybot <billybot> 2.0.7-1pclos2013
- update

* Sat Oct 26 2013 billybot <billybot> 2.0.5-1pclos2013
- update

* Wed Oct 23 2013 billybot <billybot> 2.0.4-1pclos2013
- update

* Wed Oct 23 2013 billybot <billybot> 2.0.3-1pclos2013
- update

* Sat Oct 19 2013 billybot <billybot> 2.0.2-1pclos2013
- import into pclos
