%global gtk3_version           2.99.3
%global dbus_version           0.90
%global dbus_glib_version      0.74
%global redhat_menus_version   5.0.1
%global cinnamon_desktop_version 1.9.1
%global libgnomekbd_version    2.91.1

Summary: Cinnamon Screensaver
Name:    cinnamon-screensaver
Version: 2.8.0
Release: %mkrel 1
License: GPLv2+ and LGPLv2+
URL:     http://cinnamon.linuxmint.com
Group:   Graphical desktop/Cinnamon
Source0: http://leigh123linux.fedorapeople.org/pub/cinnamon-screensaver/source/%{name}-%{version}.tar.gz
Requires: gsettings-desktop-schemas >= 0.1.7
Requires: gnome-keyring
#---------------------------------------------------------------------------
BuildRequires: pkgconfig(gtk+-3.0) => %{gtk3_version}
BuildRequires: pkgconfig(dbus-1) >= %{dbus_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires: pam-devel
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama) 
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(libgnomekbd) >= %{libgnomekbd_version}
BuildRequires: pkgconfig(xproto)
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: pkgconfig(xxf86misc)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xtst)
BuildRequires: desktop-file-utils
BuildRequires:  libxklavier-devel
#------------------------------------------------------------------------
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
cinnamon-screensaver is a screen saver and locker.

%prep
%setup -q
echo "ACLOCAL_AMFLAGS = -I m4" >> Makefile.am
echo "AC_CONFIG_MACRO_DIR([m4])" >> configure.ac

NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x --with-mit-ext=no --without-console-kit
%make V=1

%install
rm -rf %{buildroot}
%makeinstall_std


desktop-file-install                                     \
  --delete-original                                      \
  --remove-only-show-in=Xfce                             \
  --set-key=AutostartCondition \
  --set-value="GNOME3 if-session cinnamon" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications          \
  $RPM_BUILD_ROOT%{_datadir}/applications/cinnamon-screensaver.desktop



%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%{_datadir}/cinnamon-screensaver/screensavers/*
%{_bindir}/cinnamon-screensaver*
%{_datadir}/applications/cinnamon-screensaver.desktop
%{_datadir}/dbus-1/services/org.cinnamon.ScreenSaver.service
%{_libexecdir}/cinnamon-screensaver-dialog
%config %{_sysconfdir}/pam.d/cinnamon-screensaver
%{_mandir}/man1/cinnamon-screensaver*.1.*

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%clean
rm -rf %{buildroot}


%changelog
* Thu Oct 31 2013 billybot <billybot> 2.0.3-1pclos2013
- update

* Wed Oct 23 2013 billybot <billybot> 2.0.2-1pclos2013
- udpate

* Sat Oct 19 2013 billybot <billybot> 2.0.0-1pclos2013
- import into pclos
