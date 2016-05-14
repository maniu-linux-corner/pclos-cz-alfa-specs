%define	tarname gcab
Name:           libgcab
Version:        0.6
Release:        1%{?dist}
Summary:        A GObject library to create cabinet files

License:        LGPL
URL:            https://git.gnome.org/browse/gcab/snapshot/gcab-%{version}.tar.xz
Source0:        https://git.gnome.org/browse/gcab/snapshot/gcab-%{version}.tar.xz

#BuildRequires:  
#Requires:       

%description
A GObject library to create cabinet files

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{tarname}-%{version}


%build
sh autogen.sh --prefix=/usr
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_libdir}/*.so.*
/usr/bin/gcab
/usr/lib64/girepository-1.0/GCab-1.0.typelib
/usr/share/gir-1.0/GCab-1.0.gir
/usr/share/man/man1/gcab.1.bz2
/usr/share/locale/*


%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
/usr/lib64/pkgconfig/libgcab-1.0.pc


%changelog
