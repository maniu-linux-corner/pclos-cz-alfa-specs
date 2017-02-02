%define api		3.0
%define clutterapi	3.0
%define gir_major	3.0
%define major		0

%define gstapi		1.0

%define oname clutter-gst

%define libname		%mklibname %{oname} %{api} %{major}
%define devname		%mklibname -d %{name}
%define girname		%mklibname %{name}-gir %{gir_major}
%define gstname		gstreamer%{gstapi}-gstclutter3

%define url_ver %(echo %{version} | cut -d. -f1,2)

Summary:	GST video texture actor and audio player object for Clutter
Name:		clutter-gst3
Version:	3.0.22
Release:	%mkrel 3
Source0:	clutter-gst3-3.0.22.zip
License:	LGPLv2+
Group:		Graphics/Utilities
Url:		http://clutter-project.org/
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)

%description
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package %{name}
Summary:	GST video texture actor and audio player object for Clutter
Group:		Graphics/Utilities
Requires:	gstreamer1.0-plugins-base

%description %{name}
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package devel
Summary:	Development headers/libraries for %{name}
Group:		Development/X11
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{name}%{api}-devel = %{version}-%{release}
Provides:	%{_lib}clutter-gst%{api}-devel = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers/libraries for %{name}.

%prep
%setup -qn clutter-gst3-%{version}


%build
./autogen.sh
./configure --prefix=/usr --libdir=/usr/lib64/ --sysconfdir=/etc \
    --enable-gtk-doc
%make

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%files 
%{_libdir}/lib%{oname}-%{api}.so.*
%{_libdir}/girepository-1.0/ClutterGst-%{gir_major}.typelib
%{_libdir}/gstreamer-1.0/libgstclutter-%{api}.so

%files devel
%doc %{_datadir}/gtk-doc/html/%{oname}-%{api}
%{_libdir}/pkgconfig/%{oname}-%{api}.pc
%{_libdir}/lib%{oname}-%{api}.so
%{_includedir}/clutter-gst-%{clutterapi}/%{oname}
%{_datadir}/gir-1.0/ClutterGst-%{gir_major}.gir


%changelog
