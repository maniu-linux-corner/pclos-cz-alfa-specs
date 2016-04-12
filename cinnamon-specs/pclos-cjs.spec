%global _internal_version  8711f3b
%define api             1.0
%define major           0
%define girmajor        1.0
%define libname         %mklibname %{name} %{major}
%define develname       %mklibname -d %{name}
%define girname         %mklibname %{name}-gir %{girmajor}

Name:          cjs
Version:       2.8.0
Release:       %mkrel 1
Summary:       Javascript Bindings for Cinnamon
Group:         System/Libraries
License:       MIT and (MPLv1.1 or GPLv2+ or LGPLv2+)
URL:           http://cinnamon.linuxmint.com
Source0: http://leigh123linux.fedorapeople.org/pub/cjs/source/cjs-%{version}.tar.gz
BuildRequires: %{_lib}cairo-devel
BuildRequires: %{_lib}dbus-1-devel
BuildRequires: %{_lib}dbus-glib-1_2-devel
BuildRequires: %{_lib}ffi5-devel
BuildRequires: %{_lib}girepository-devel
BuildRequires: %{_lib}glib2.0-devel
BuildRequires: %{_lib}glib2.0_0
BuildRequires: %{_lib}mozjs24-devel
BuildRequires: %{_lib}nspr-devel
BuildRequires: %{_lib}readline-devel


BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: gnome-common
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{libname}

%description
Cjs allows using Cinnamon libraries from Javascript. It's based on the
Spidermonkey Javascript engine from Mozilla and the GObject introspection
framework.

%package -n %{libname}
Group:          System/Libraries
Summary:        JavaScript bindings based on gobject-introspection

%description -n %{libname}
This package contains JavaScript bindings based on gobject-introspection.

%package -n %{develname}
Summary: Development package for %{name}
Group: Development/Libraries
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Files for development with %{name}.


%prep
%setup -q 
sed -i -e 's@{ACLOCAL_FLAGS}@{ACLOCAL_FLAGS} -I m4@g' Makefile.am
echo "AC_CONFIG_MACRO_DIR([m4])" >> configure.ac
NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make V=1

%install
rm -rf %{buildroot}
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%defattr(-, root, root)
%doc COPYING COPYING.LGPL NEWS README
%{_bindir}/cjs
%{_bindir}/cjs-console


%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.*
%{_libdir}/cjs/
#%{_libdir}/cjs-1.0/

%files -n %{develname}
%defattr(-, root, root)
%{_includedir}/cjs-1.0/
%{_libdir}/pkgconfig/cjs-1.0.pc
%{_libdir}/pkgconfig/cjs-internals-1.0.pc
%{_libdir}/*.so

%clean
rm -rf %{buildroot}


%changelog
* Tue Apr 15 2016 Mank <mank at pclinuxos dot cz> 2.8.0-1mank2016
- update

* Tue Apr 15 2014 bb <bb> 2.2.0-1pclos2014
- update

* Fri Oct 18 2013 bb <bb> 2.0.0-1pclos2013
- import into pclos
