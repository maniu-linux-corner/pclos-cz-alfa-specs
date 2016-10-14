%global alt_name GPaste

Name:           gpaste
Version:        3.22.0
Release:        1%{?dist}
Summary:        Clipboard management system

Group:          User Interface/Desktops
License:        GPLv3+
URL:            https://github.com/Keruspe/GPaste
Source0:        http://www.imagination-land.org/files/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  appstream-util
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
#BuildRequires:  pkgconfig(gnome-keybindings)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
GPaste is a clipboard management system.

This package provides the D-Bus service and the command-line client.


%package libs
Summary:        Library to manage the clipboard history
Group:          System Environment/Libraries

%description libs
GPaste is a clipboard management system.

This package contains the shared library used by GPaste.


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package applet
Summary:        Tray icon to manage GPaste
Group:          User Interface/Desktops
Requires:       %{name}-ui = %{version}-%{release}

%description applet
GPaste is a clipboard management system.

This package provides the GPaste status icon.


%package ui
Summary:        Graphical interface for GPaste
Group:          User Interface/Desktops
Requires:       %{name} = %{version}-%{release}
Requires:       gnome-icon-theme

%description ui
GPaste is a clipboard management system.

This package provides a graphical interface for GPaste, as well as GNOME
integration (control center key bindings and search provider).


%package -n gnome-shell-extension-%{name}
Summary:        GNOME Shell extension for GPaste
Group:          User Interface/Desktops
Requires:       gnome-shell >= 3.18
Requires:       %{name}-ui = %{version}-%{release}
BuildArch:      noarch

%description -n gnome-shell-extension-%{name}
GPaste is a clipboard management system.

This package provides the GNOME Shell extension for GPaste.


%prep
%setup -q


%build
#NOCONFIGURE=1 ./autogen.sh -f
#autoreconf -fi
%configure \
  --disable-schemas-compile \
  --disable-silent-rules \
  --disable-unity \
  --enable-applet \
  --disable-gnome-shell-extension 
#//  --enable-vala \  
mkdir -p bindings/
touch bindings/gpaste-1.0.deps #bit hack
%make


%install
mkdir -p bindings/
touch bindings/gpaste-1.0.deps
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/*.la

# Install bash/zsh completion support
#install -Dpm 0644 data/completions/%{name}-client $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/%{name}-client
#install -Dpm 0644 data/completions/_%{name}-client $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_%{name}-client

# Remove Rpath
chrpath --delete \
    $RPM_BUILD_ROOT%{_bindir}/* \
    $RPM_BUILD_ROOT%{_libexecdir}/%{name}/*

%find_lang %{alt_name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GPaste.Applet.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GPaste.Ui.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/org.gnome.GPaste.Applet.desktop


%post libs -p /sbin/ldconfig


%postun libs -p /sbin/ldconfig


%postun
if [ $1 -eq 0 ]; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :


%files
%doc AUTHORS NEWS README.md THANKS
#%{_bindir}/%{name}
#%{_libdir}/gpaste/gpaste-settings
%{_bindir}/%{name}-client
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/gpaste-daemon
%{_datadir}/dbus-1/services/org.gnome.GPaste.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/bash-completion/
%{_datadir}/zsh/
%{_mandir}/man1/*.1.*
#%{_datadir}/appdata/org.gnome.GPaste.Settings.appdata.xml
#%{_datadir}/applications/org.gnome.GPaste.Settings.desktop
#%{_datadir}/dbus-1/services/org.gnome.GPaste.Settings.service

%files libs -f %{alt_name}.lang
#%{_libdir}/girepository-1.0/%{alt_name}-1.0.typelib
%{_libdir}/*.so.*


%files devel
#%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%files applet
%{_libexecdir}/%{name}/%{name}-applet
%{_datadir}/appdata/org.gnome.GPaste.Applet.appdata.xml
%{_datadir}/applications/org.gnome.GPaste.Applet.desktop
%{_datadir}/dbus-1/services/org.gnome.GPaste.Applet.service
%{_sysconfdir}/xdg/autostart/org.gnome.GPaste.Applet.desktop


%files ui
%{_libexecdir}/%{name}/gpaste-ui
%{_datadir}/applications/org.gnome.GPaste.Ui.desktop
%{_datadir}/appdata/org.gnome.GPaste.Ui.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.GPaste.Ui.service
#%{_datadir}/gnome-control-center/keybindings/*.xml
#%{_datadir}/gnome-shell/search-providers/*.ini


%files -n gnome-shell-extension-%{name}
#%{_datadir}/gnome-shell/extensions/GPaste@gnome-shell-extensions.gnome.org/


%changelog
* Fri Jan 15 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18.3-1
- Update to 3.18.3

* Fri Oct 16 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18.2-1
- Update to 3.18.2

* Sun Sep 27 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18.1.1-2
- Fix minimal GNOME Shell version for the extension subpackage

* Sun Sep 27 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18.1.1-1
- Update to 3.18.1.1

* Wed Sep 16 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16.3-1
- Update to 3.16.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16.2.1-1
- Update to 3.16.2.1

* Sun May 03 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16.1-1
- Update to 3.16.1

* Sun Apr 05 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16-1
- Update to 3.16

* Sun Apr 05 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.14.3-1
- Update to 3.14.3

* Mon Mar 16 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.14.2-1
- Update to 3.14.2

* Sun Jan 18 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.14.1-1
- Update to 3.14.1

* Sat Oct 11 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.14-1
- Update to 3.14

* Tue Oct 07 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.13-0.2.20140929git80428a8
- Update to a newer snapshot (GNOME 3.14 support)

* Wed Sep 24 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.13-0.1.20140917git8dae0be
- Update to a newer snapshot (GNOME 3.13.92 support)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-2
- Rebuilt for gobject-introspection 1.41.4

* Wed Jul 16 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.12.1-1
- Update to 3.12.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.12-1
- Update to 3.12

* Thu May 01 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1
- Drop gnome-shell dependency

* Wed Apr 02 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.10-2
- Add gnome-shell as dependency (the gpasted daemon requires the GNOME Shell
  GSetting schemas)

* Tue Mar 25 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.10-1
- Update to 3.10

* Wed Feb 12 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8-1
- Update to 3.8

* Thu Oct 17 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.6-1
- Update to 3.6

* Wed Sep 25 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5-1
- Update to 3.5

* Mon Sep 23 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5-0.2.20130922gitf124a2f
- Update to a newer snapshot

* Wed Sep 18 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5-0.1.20130918git6ab4033
- Update to a newer snapshot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Fri May 10 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-2
- Fix bash completion

* Fri May 10 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Sun Apr 07 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.99.2-3.20130331gitc93a4ac
- Add missing BuildRequires on pkgconfig(gnome-keybindings)

* Sun Apr 07 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.99.2-2.20130331gitc93a4ac
- Update to a newer snapshot
- Move bash completion script to /usr/share/bash-completion/completion/

* Mon Jan 28 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.99.2-1
- Update to 2.99.2
- Drop patch gpaste-2.99.1-fix_gpaste-settings

* Thu Jan 17 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.99.1-1
- Update to 2.99.1

* Sun Dec 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1
- Drop patch gpaste-2.9-gir.patch, fixed upstream

* Sun Sep 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.9-1
- Update to 2.9
- Enable GNOME fallback applet

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Thu May 03 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.8-1
- Update to 2.8

* Sun Apr 08 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5-2
- Fix Group and Requires tags in subpackages

* Fri Mar 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5-1
- Update to 2.5

* Sat Jan 07 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Fri Dec 09 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1-1
- Update to 2.1

* Tue Nov 29 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0-1
- Update to 2.0

* Sun Sep 25 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6-1
- Update to 1.6
- Remove no longer needed gpaste-1.5-DOS.patch patch

* Wed Sep 14 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5-1
- Update to 1.5
- Remove gpaste-1.3-remove_applet_refs.patch patch (there is no more reference
  to the GNOME 2 applet in documentation and completion files)
- Add gpaste-1.5-DSO.patch to fix DSO linking

* Sat Sep 03 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3-1
- Update to 1.3

* Sun Jul 10 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2-1
- Update to 1.2

* Sat Jun 25 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.99-1.17dd47git
- Initial RPM release
