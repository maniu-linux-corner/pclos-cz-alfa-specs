%define api		2.0
%define clutterapi	2.0
%define gir_major	2.0
%define major		0

%define gstapi		1.0



%define libname		%mklibname %{name} %{api} %{major}
%define devname		%mklibname -d %{name} %{api}
%define girname		%mklibname %{name}-gir %{gir_major}
%define gstname		gstreamer%{gstapi}-gstclutter

%define url_ver %(echo %{version} | cut -d. -f1,2)

Summary:	GST video texture actor and audio player object for Clutter
Name:		clutter-gst
Version:	2.0.18
Release:	%mkrel 3
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
License:	LGPLv2+
Group:		System/Libraries
Url:		http://clutter-project.org/
#-----------------------------------------------------
BuildConflicts: %{_lib}gstbasevideo-devel
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
#-----------------------------------------------------
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.


%package devel
Summary:	Development headers/libraries for %{name}
Group:		Development/Libraries
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{name}%{api}-devel = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-doc < 1.5.2

%description devel
Development headers/libraries for %{name}.

%prep
%setup -q
%apply_patches

%build
./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --libdir=/usr/lib64/

sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%files
%defattr(-, root, root)
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/ClutterGst-%{gir_major}.typelib
%{_libdir}/gstreamer-1.0/libgstclutter.so

%files devel
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/html/%{name}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so
%{_datadir}/gir-1.0/ClutterGst-%{gir_major}.gir
%{_includedir}/clutter-gst-2.0/clutter-gst/


%clean
rm -rf %{buildroot}

%changelog
* Fri Oct 21 2016 Migelo 2.0.18-2_pclos_cz
- update

* Tue Apr 15 2014 bb <bb> 2.0.10-1pclos2014
- update

* Sat Oct 19 2013 billybot <billybot> 1.6.0-1pclos2013
- update

