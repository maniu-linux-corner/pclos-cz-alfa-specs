Name:           xed
Version:        1.2.2
Release:        2
Summary:        xed

License:        GPL
URL:            https://github.com/linuxmint/xed
Source0:        xed-%{version}.zip
Requires: xapps

%description


%package devel
Summary: %{name} devel files for
Group:    Development/C
Requires: %{name}
Provides: %name-devel = %{version}

%description devel

%prep
%setup -q


%build
sh autogen.sh --prefix=/usr/ --libdir=/usr/lib64
cp -a /usr/share/gtk-doc/data/gtk-doc.make .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install

# we don't want these
find %{buildroot} -name "*.la" -delete

%files
%{_bindir}/*
%{_datadir}/*
%{_libdir}/%{name}/*
%{_libexecdir}/%{name}/*

%files devel
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/xed.pc

%changelog
* Sat Jan  7 2017 mank
- import to pclinuxosczsk
