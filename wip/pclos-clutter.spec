%define api		1.0
%define major		0
%define girmajor	1.0

%define libname		%mklibname %{name} %{api} %{major}
%define libnamedevel	%mklibname -d %{name} %{api}
%define girname		%mklibname %{name}-gir %{girmajor}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Software library for fast, visually rich GUIs
Name:		clutter
Version:	1.26.0
Release:	%mkrel 6
Source0:	clutter-%{version}+24.zip
License:	LGPLv2+
Group:		System/Libraries
Url:		http://clutter-project.org/
#-----------------------------------------------------------------
BuildRequires: cogl-devel
BuildRequires: gtk-doc
BuildRequires: x11-proto-devel
BuildRequires: %{_lib}atk1.0-devel
BuildRequires: %{_lib}cairo-devel
BuildRequires: %{_lib}fontconfig-devel
BuildRequires: %{_lib}freetype6-devel
BuildRequires: %{_lib}gdk_pixbuf2.0_0-devel
BuildRequires: %{_lib}girepository-devel
BuildRequires: %{_lib}glib2.0_0-devel
BuildRequires: %{_lib}gtk+3.0-devel
BuildRequires: %{_lib}json-glib-devel
BuildRequires: %{_lib}mesagl1-devel
BuildRequires: %{_lib}pango1.0-devel
BuildRequires: %{_lib}x11-devel
BuildRequires: %{_lib}xcomposite-devel
BuildRequires: %{_lib}xdamage-devel
BuildRequires: %{_lib}xext-devel
BuildRequires: %{_lib}xfixes-devel
BuildRequires: %{_lib}xi-devel
BuildRequires: %{_lib}xkbcommon-devel
#-----------------------------------------------------------------
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Clutter is an open source software library for creating fast, visually rich
graphical user interfaces. The most obvious example of potential usage is in
media center type applications. We hope however it can be used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but with an
API which hides the underlying GL complexity from the developer. The Clutter
API is intended to be easy to use, efficient and flexible. 

#--------------------------------------------------------------------
%files
%defattr(-, root, root)
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/lib%{name}-glx-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/Cally-%{girmajor}.typelib
%{_libdir}/girepository-1.0/Clutter-%{girmajor}.typelib
%{_libdir}/girepository-1.0/ClutterX11-%{girmajor}.typelib
%{_libdir}/girepository-1.0/ClutterGdk-%{girmajor}.typelib
%{_datadir}/locale
#--------------------------------------------------------------------

%package devel
Summary:	Development headers/libraries for %{name}
Group:		Development/Libraries
Obsoletes:	%{name}-devel < %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-glx-devel = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}


%description devel
Development headers/libraries for %{name} (see %{libname} package)

%files devel
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/html/%{name}
%{_libdir}/pkgconfig/cally-%{api}.pc
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-gdk-%{api}.pc
%{_libdir}/pkgconfig/%{name}-glx-%{api}.pc
%{_libdir}/pkgconfig/%{name}-cogl-%{api}.pc
%{_libdir}/pkgconfig/%{name}-x11-%{api}.pc
%{_libdir}/pkgconfig/%{name}-wayland-%{api}.pc
%{_libdir}/pkgconfig/%{name}-wayland-compositor-%{api}.pc
%{_libdir}/pkgconfig/%{name}-egl-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/lib%{name}-glx-%{api}.so
%dir %{_includedir}/%{name}-%{api}
%{_includedir}/%{name}-%{api}/cally
%{_includedir}/%{name}-%{api}/%{name}
%{_datadir}/gir-1.0/Cally-%{girmajor}.gir
%{_datadir}/gir-1.0/ClutterGdk-%{girmajor}.gir
%{_datadir}/gir-1.0/Clutter-%{girmajor}.gir
%{_datadir}/gir-1.0/ClutterX11-%{girmajor}.gir
#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}+24


%build
./autogen.sh


./configure --prefix=/usr \
	--libdir=/usr/lib64/ \
    --enable-introspection \
    --enable-egl-backend \
    --enable-gdk-backend \
    --enable-wayland-backend \
    --enable-x11-backend \
    --enable-evdev-input \
    --enable-wayland-compositor \
    --enable-gtk-doc


%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}-%{api}

# we don't want these
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%changelog
* Fri Jan 27 2017 Migelo <migelo at pclinuxos.cz> 1.26.0-6_pclos_cz
- disabled Wayland support

* Fri Oct 21 2016 Migelo 1.26.0-2_pclos_cz
- update

* Tue Apr 15 2014 bb <bb> 1.18.2-1pclos2014
- update

* Wed Feb 05 2014 bb <bb> 1.16.4-1pclos2014
- update

* Wed Dec 25 2013 bb <bb> 1.16.2-1pclos2013
- update

* Fri Oct 18 2013 bb <bb> 1.16.0-1pclos2013
- re-import into pclos for cinnamon
