%define major	8
%define gmajor	1.0
%define libname	%mklibname %{name} %{major}
%define girname	%mklibname %{name}-gir %{gmajor}

%define libnameappstream_builder	%mklibname appstream-builder %{major}
%define girnameappstream_builder	%mklibname appstream-builder-gir %{gmajor}

%define devname	%mklibname %{name} -d

%define url_ver	%(echo %{version} | cut -d. -f1,2)

Name:		appstream-glib
Version:	0.5.3
Release:	%mkrel 1
Summary:	Library for reading and writing AppStream metadata
Group:		System/Libraries
License:	LGPLv2+
URL:		http://people.freedesktop.org/~hughsient/appstream-glib/
Source0:	http://people.freedesktop.org/~hughsient/appstream-glib/releases/%{name}-%{version}.tar.xz
#---------------------------------------
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: libgcab-devel
BuildRequires: %{_lib}archive-devel
BuildRequires: %{_lib}cairo-devel
BuildRequires: %{_lib}fontconfig-devel
BuildRequires: %{_lib}freetype6-devel
BuildRequires: %{_lib}gdk_pixbuf2.0_0-devel
BuildRequires: %{_lib}girepository-devel
BuildRequires: %{_lib}glib2.0-devel
BuildRequires: %{_lib}gtk+3.0-devel
BuildRequires: %{_lib}pango1.0-devel
BuildRequires: %{_lib}popt-devel
BuildRequires: %{_lib}rpm-devel
BuildRequires: %{_lib}soup-devel
BuildRequires: %{_lib}sqlite3-devel
BuildRequires: libtool-base
BuildRequires: libxml2-utils
BuildRequires: %{_lib}yaml-devel
#---------------------------------------

%description
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.

%package -n appstream-util
Summary:	Utility to do simple operations on AppStream metadata
Group:		System/Packaging

%description -n appstream-util
Utility to do simple operations on AppStream metadata.

Sub-commands understood by this utility include: 'install', 'uninstall',
'dump' and 'convert'.

%package -n %{libname}
Summary:	Library for reading and writing AppStream metadata
Group:		System/Libraries

%description -n %{libname}
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.


%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x --disable-static --disable-rpm
%make V=1

%install
%makeinstall_std

# Remove unwanted la files
find %{buildroot} -name "*.la" -delete

%{find_lang} %{name}

%files -n appstream-util
%{_bindir}/appstream-util
%{_bindir}/appstream-builder
%{_datadir}/bash-completion/completions/appstream-util
%{_datadir}/bash-completion/completions/appstream-builder
#%{_libdir}/asb-plugins/libasb_plugin_*.so
%{_libdir}/asb-plugins-4/*
%{_mandir}/man1/appstream-builder.1*
%{_mandir}/man1/appstream-util.1*
%{_datadir}/locale

%files -n %{libname}
%doc AUTHORS NEWS
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*
%{_libdir}/libappstream-builder.so.%{major}
%{_libdir}/libappstream-builder.so.%{major}.*
%{_libdir}/girepository-1.0/AppStreamGlib-%{gmajor}.typelib
%{_libdir}/girepository-1.0/AppStreamBuilder-%{gmajor}.typelib

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/appstream-glib/
%{_includedir}/lib%{name}/
%{_includedir}/libappstream-builder/
%{_libdir}/lib%{name}.so
%{_libdir}/libappstream-builder.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/appstream-builder.pc
%{_datadir}/gir-1.0/AppStreamGlib-%{gmajor}.gir
%{_datadir}/gir-1.0/AppStreamBuilder-%{gmajor}.gir
%{_datadir}/aclocal/appstream-xml.m4
%{_datadir}/installed-tests/appstream-glib
%{_datadir}/aclocal/appdata-xml.m4

%changelog
* Thu Nov 10 2015 Mank <mank@pclinuxos.cz> 0.5.3-1pclos2015
- update
* Thu Nov 06 2014 bb <bb> 0.2.5-1pclos2014
- import
