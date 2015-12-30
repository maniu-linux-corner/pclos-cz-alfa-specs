%global po_package cinnamon-session-3.0
%global _internal_version  d5e4dd9

Summary: Cinnamon session manager
Name:    cinnamon-session
Version: 2.8.2
Release: %mkrel 1
URL:     http://cinnamon.linuxmint.com
Source0: cinnamon-session-%{version}.tar.gz
#Patch0:  remove_sessionmigration.patch
#Patch1:  cinnamon-session-upower.patch
License: GPLv2+ and LGPLv2+
Group:   Graphical desktop/Cinnamon
Requires: gsettings-desktop-schemas >= 0.1.7
Requires: dbus-x11
Requires: polkit-gnome
#-------------------------------------------------
BuildRequires: pkgconfig(gtk+-3.0) >= 2.99.0
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libnotify) >= 0.7.0
BuildRequires: pkgconfig(pango)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xtrans)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: usermode
BuildRequires: pkgconfig(pangox)
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xtst)
BuildRequires: xmlto
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(polkit-gobject-1)
#-----------------------------------------------
Requires: dconf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Cinnamon-session manages a Cinnamon desktop or GDM login session. It starts up
the other core components and handles logout and saving the session.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1 -b .upower_deprecated
NOCONFIGURE=1 autoreconf -fi

%build
%configure2_5x --enable-docbook-docs \
           --docdir=%{_datadir}/doc/%{name}

%make V=1

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

#desktop-file-install                                     \
 # --delete-original                                      \
  #--set-icon=cinnamon-session-properties                 \
  #--dir $RPM_BUILD_ROOT%{_datadir}/applications          \
  #$RPM_BUILD_ROOT%{_datadir}/applications/cinnamon-session-properties.desktop


%find_lang %{po_package}


%files -f %{po_package}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README
%doc %{_mandir}/man*/*
#%{_datadir}/applications/cinnamon-session-properties.desktop
%{_bindir}/*
%{_libexecdir}/cinnamon-session-check-accelerated
%{_libexecdir}/cinnamon-session-check-accelerated-helper
%{_datadir}/cinnamon-session/
%{_datadir}/icons/hicolor/*/apps/cinnamon-session-properties.png
%{_datadir}/icons/hicolor/scalable/apps/cinnamon-session-properties.svg
%{_datadir}/glib-2.0/schemas/org.cinnamon.SessionManager.gschema.xml

%post
/usr/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  /usr/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%clean
rm -rf %{buildroot}


%changelog
* Tue Nov 12 2013 billybot <billybot> 2.0.5-1pclos2013
- update

* Fri Oct 17 2013 billybot <billybot> 2.0.1-1pclos2013
- import into pclos
