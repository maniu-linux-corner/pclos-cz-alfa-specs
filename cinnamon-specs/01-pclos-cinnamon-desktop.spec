%global _internal_version                 d84ac12
%global gtk3_version                      3.3.6
%global glib2_version                     2.33.3
%global startup_notification_version      0.5
%global gtk_doc_version                   1.9
%global po_package                        cinnamon-desktop-3.0
%global date				  20130905

%define major   4
%define girmajor   1.0
%define libname %mklibname %{name} %{major}
%define libdev  %mklibname %{name} -d
%define girlib    %mklibname %{name}-gir %{girmajor}


Summary: Shared code among cinnamon-session, nemo, etc
Name:    cinnamon-desktop
Version: 2.8.0
Release: %mkrel 1
License: GPLv2+ and LGPLv2+ add MIT
Group:   Graphical desktop/Cinnamon
URL:     http://cinnamon.linuxmint.com
Source0: cinnamon-desktop-%{version}.tar.gz
Requires: gnome-themes-standard
#---------------------------------------------------------------------------------
BuildRequires: gnome-common
BuildRequires: gobject-introspection-devel
BuildRequires: x11-data-xkbdata
BuildRequires: gtk-doc >= %{gtk_doc_version}
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: %{_lib}glib2.0_0-devel >= %{glib2_version}
BuildRequires: %{_lib}startup-notification-1-devel >= %{startup_notification_version}
BuildRequires: %{_lib}xkbfile-devel
BuildRequires: %{_lib}gtk+3.0-devel >= %{gtk3_version}
#---------------------------------------------------------------------------------
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
The cinnamon-desktop package contains an internal library
(libcinnamondesktop) used to implement some portions of the CINNAMON
desktop, and also some data files and other shared components of the
CINNAMON user environment.

#--------------------------------------------------------------------

%package devel
Summary:  Libraries and headers for libcinnamon-desktop
License:  LGPLv2+
Group:    Development/Libraries
Requires: %{name} = %{version}
Requires: glib2-devel >= %{glib2_version}
Requires: startup-notification-devel >= %{startup_notification_version}
Requires: %{_lib}gtk+3.0-devel >= %{gtk3_version}


%description devel
Libraries and header files for the CINNAMON-internal private library
libcinnamondesktop.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure --with-pnp-ids-path="%{_datadir}/misc/pnp.ids"
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make V=1 

%install
rm -rf %{buildroot}
%{make_install}

# stuff we don't want
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%find_lang %{po_package} --all-name --with-gnome


%files -f %{po_package}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LIB README
%{_datadir}/glib-2.0/schemas/org.cinnamon.*.xml
%{_libexecdir}/cinnamon-rr-debug
%{_bindir}/cinnamon-desktop-migrate-mediakeys
%{_libdir}/libcinnamon-desktop*.so.%{major}*
%{_libdir}/girepository-1.0/C*-3.0.typelib

%files devel
%defattr(-,root,root)
%{_libdir}/libcinnamon-desktop.so
%{_libdir}/pkgconfig/cinnamon-desktop.pc
%{_includedir}/cinnamon-desktop/
%{_datadir}/gir-1.0/C*-3.0.gir

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%clean
rm -rf %{buildroot}


%changelog
* Wed Dec 25 2016 Mank <mank at pclinuxos dot cz> 2.8.0-1pclos2016
- update

* Wed Dec 25 2013 bb <bb> 2.0.4-1pclos2013
- update

* Mon Nov 04 2013 billybot <billybot> 2.0.3-1pclos2013
- update

* Fri Oct 25 2013 billybot <billybot> 2.0.2-1pclos2013
- update

* Fri Oct 18 2013 billybot <billybot> 2.0.1-1pclos2013
- import into pclos
