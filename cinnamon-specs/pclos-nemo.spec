
%define gir_major 3.0
%define gir_name        %mklibname %{name}-gir %{gir_major}
%define libnemo_extension    %mklibname %{name}-extension
%define libname_devel   %mklibname %{name} -d
%define date 20130917

Name:           nemo
Summary:        File manager for Cinnamon
Version:        3.0.0
Release:        %mkrel 1
License:        GPLv2+ and LGPLv2+
Group:          Graphical desktop/Cinnamon
URL:            https://github.com/linuxmint/nemo
Source0:        nemo-%{version}.tar.gz
Source1:        nemo.css
Source2:        gtk.css
Source3:        gtk-dark.css
Source4:        org.nemo.gschema.xml
Source5:	pclos-nemo.desktop
Requires:       gvfs
Requires:       gnome-icon-theme
Requires:       cinnamon-desktop
Requires:       cinnamon-translations
Requires:	gksu
#--------------------------------------------------
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  rarian
BuildRequires:  desktop-file-utils
BuildRequires: %{_lib}atk1.0-devel
BuildRequires: %{_lib}cairo-devel
BuildRequires: %{_lib}exempi3-devel
BuildRequires: %{_lib}exif12-devel
BuildRequires: %{_lib}gail3.0-devel
BuildRequires: %{_lib}gdk_pixbuf2.0_0-devel
BuildRequires: %{_lib}girepository-devel
BuildRequires: %{_lib}glib2.0_0
BuildRequires: %{_lib}glib2.0_0-devel
BuildRequires: %{_lib}gtk+3.0-devel
BuildRequires: %{_lib}notify-devel
BuildRequires: %{_lib}pango1.0-devel
BuildRequires: %{_lib}x11-devel
BuildRequires: %{_lib}xml2-devel
BuildRequires: cinnamon-desktop-devel
BuildRequires: gnome-themes-standard
#--------------------------------------------------
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Nemo is the file manager and graphical shell for the Cinnamon desktop
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote filesystems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the Cinnamon desktop.

%package devel
Summary: Support for developing nemo extensions
License: LGPLv2+
Group: Development/Libraries

%description devel
This package provides libraries and header files needed
for developing nemo extensions.


%prep
%setup -q -n %{name}-%{version}
#%apply_patches
NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x --disable-more-warnings \
           --disable-update-mimedb \
           --disable-schemas-compile \
           --disable-static \
           --disable-tracker \
           --disable-debug 


sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool
%make V=1

%install
rm -rf %{buildroot}
%makeinstall_std

install -D -m 0644 %{SOURCE4} $RPM_BUILD_ROOT/%{_datadir}/glib-2.0/schemas

desktop-file-install --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  --add-only-show-in GNOME                                  \
  $RPM_BUILD_ROOT%{_datadir}/applications/*

install -m 0644 %SOURCE5 $RPM_BUILD_ROOT%{_datadir}/applications/nemo.desktop

# create extensions directoy
mkdir -p $RPM_BUILD_ROOT%{_libdir}/nemo/extensions-3.0/

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/nemo/extensions-3.0/*.la
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/.icon-theme.cache

# theme
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/Adwaita-Nemo/gtk-3.0/apps
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/Adwaita-Nemo/gtk-3.0/apps/
install -D -p -m 0644 %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/themes/Adwaita-Nemo/gtk-3.0/
ln -s %{_datadir}/themes/Adwaita/backgrounds $RPM_BUILD_ROOT%{_datadir}/themes/Adwaita-Nemo/
ln -s %{_datadir}/themes/Adwaita/gtk-2.0 $RPM_BUILD_ROOT%{_datadir}/themes/Adwaita-Nemo/
ln -s %{_datadir}/themes/Adwaita/gtk-3.0/{gtk.gresource,settings.ini} $RPM_BUILD_ROOT%{_datadir}/themes/Adwaita-Nemo/gtk-3.0/
ln -s %{_datadir}/themes/Adwaita/metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/Adwaita-Nemo/
ln -s %{_datadir}/themes/Adwaita/index.theme $RPM_BUILD_ROOT%{_datadir}/themes/Adwaita-Nemo/index.theme


%find_lang %name

%files  -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB NEWS
%{_datadir}/nemo/
%{_datadir}/applications/*
%{_datadir}/mime/packages/nemo.xml
%{_bindir}/*
%{_libdir}/nemo-extensions-list
%{_datadir}/icons/hicolor/*/apps/nemo.png
%{_datadir}/icons/hicolor/*/actions/nemo-eject.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/dbus-1/services/org.Nemo.service
%{_mandir}/man1/nemo-connect-server.1.*
%{_mandir}/man1/nemo.1.*
%{_libexecdir}/nemo-convert-metadata
%{_datadir}/glib-2.0/schemas
%{_datadir}/gtksourceview-*/language-specs/nemo_action.lang
%dir %{_libdir}/nemo
%dir %{_libdir}/nemo/extensions-3.0/
#%{_datadir}/dbus-1/services/org.freedesktop.NemoFileManager1.service
%{_datadir}/dbus-1/services/org.nemo.freedesktop.FileManager1.service
%{_datadir}/polkit-1/actions/org.nemo.root.policy
%{_libdir}/libnemo-extension.so.*
%{_datadir}/themes/Adwaita-Nemo/
%{_libdir}/girepository-1.0/*.typelib
%{_datadir}/icons/hicolor/*
 
%files devel
%defattr(-,root,root)
%{_includedir}/nemo/
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir

%posttrans
/usr/bin/glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
/usr/bin/glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &>/dev/null || :


%clean
rm -rf %{buildroot}


%changelog
* Fri Jan 03 2016 Mank <mank at pclinuxos dot cz> 2.8.0-1mank2016
- update to 2.8.0
- remove gksu patch

* Fri Jan 03 2014 bb <bb> 2.0.8-2pclos2013
- add gksu patch
- add req. gksu
- adjust BR

* Wed Dec 25 2013 bb <bb> 2.0.8-1pclos2013
- update

* Tue Nov 12 2013 billybot <billybot> 2.0.5-1pclos2013
- update

* Wed Oct 23 2013 billybot <billybot> 2.0.2-1pclos2013
- update

* Sat Oct 19 2013 billybot <billybot> 2.0.0-1pclos2013
- import into pclos
