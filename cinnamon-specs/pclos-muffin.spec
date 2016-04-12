%global _internal_version  cb72525

Name:          muffin
Version:       2.8.4
Release:       %mkrel 1
Summary:       Window and compositing manager based on Clutter
Group:         Graphical desktop/Cinnamon
License:       GPLv2+
URL:           https://github.com/linuxmint/muffin
Source0:       muffin-%{version}.tar.gz
#Patch0:        cogl_ABI.patch
#Patch1:        automake.patch
#Patch2:        gtkdoc.patch
#----------------------------------------------------------
BuildRequires: pkgconfig(clutter-1.0) >= 1.7.5
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.3.3
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: zenity
BuildRequires: gnome-doc-utils
BuildRequires: desktop-file-utils
# Bootstrap requirements
BuildRequires: gtk-doc gnome-common intltool
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libcanberra-gtk)
BuildRequires: pkgconfig(cinnamon-desktop)

BuildRequires: gettext-devel
BuildRequires: pkgconfig(egl)
#---------------------------------------
Requires: dbus-x11
Requires: zenity
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Muffin is a window and compositing manager that displays and manages
your desktop via OpenGL. Muffin combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

While Muffin can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as Cinnamon. 
For this reason, Muffin is very extensible via plugins, which
are used both to add fancy visual effects and to rework the window
management behaviors to meet the needs of the environment.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: muffin-devel = %{version}-%{release}

%description devel
Header files and libraries for developing Muffin plugins. Also includes
utilities for testing Metacity/Muffin themes.

%prep
%setup -q
#%apply_patches

%build
cp /usr/share/gtk-doc/data/gtk-doc.make .
autoreconf -fi
%configure2_5x --disable-static --enable-compile-warnings=minimum

sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

SHOULD_HAVE_DEFINED="HAVE_SM HAVE_SHAPE HAVE_RANDR HAVE_STARTUP_NOTIFICATION"

for I in $SHOULD_HAVE_DEFINED; do
  if ! grep -q "define $I" config.h; then
    echo "$I was not defined in config.h"
    grep "$I" config.h
    exit 1
  else
    echo "$I was defined as it should have been"
    grep "$I" config.h
  fi
done

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#Remove libtool archives.
rm -rf %{buildroot}/%{_libdir}/*.la

%find_lang %{name}

# Muffin contains a .desktop file so we just need to validate it
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS HACKING doc/theme-format.txt
%doc %{_mandir}/man1/muffin.1.*
%doc %{_mandir}/man1/muffin-message.1.*
%{_bindir}/muffin
%{_bindir}/muffin-message
%{_datadir}/applications/*.desktop
%{_datadir}/muffin/
%{_libdir}/libmuffin.so.*
%{_libdir}/muffin/Meta-Muffin.0.typelib
%{_libdir}/muffin/plugins
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.gschema.xml

%files devel
%defattr(-,root,root)
%{_bindir}/muffin-theme-viewer
%{_bindir}/muffin-window-demo
%{_includedir}/muffin/
%{_libdir}/libmuffin.so
%{_libdir}/muffin/Meta-Muffin.0.gir
%{_libdir}/pkgconfig/*
%doc %{_mandir}/man1/muffin-theme-viewer.1.*
%doc %{_mandir}/man1/muffin-window-demo.1.*
%{_datadir}/gtk-doc/

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%clean
rm -rf %{buildroot}


%changelog
* Tue Apr 15 2016 Mank <Mank at pclinuxos dot cz> 2.8.4-1mank2016
- update

* Tue Apr 15 2014 bb <bb> 2.0.5-2pclos2104
- update
- patch for cogl

* Tue Nov 12 2013 billybot <billybot> 2.0.5-1pclos2013
- update

* Wed Oct 23 2013 billybot <billybot> 2.0.3-1pclos2013
- update

* Fri Oct 18 2013 billybot <billybot> 2.0.1-1pclos2013
- import into pclos
