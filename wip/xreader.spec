Name:           xreader
Version:        1.2.2
Release:        2
Summary:        x-reader

License:        GPL
URL:            https://github.com/linuxmint/xreader
Source0:        xreader-%{version}.tar.gz

%description
...

%prep
%setup -q


%build
sh autogen.sh --prefix=/usr --libdir=/usr/lib64/ --disable-caja --disable-nemo

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_bindir}/*
%{_datadir}/*
%{_includedir}/%{name}/*
%{_libdir}/%{name}/*
%{_libdir}/*
%{_libexecdir}/*

%changelog
* Sat Jan  7 2017 mank
- import to pclinuxosczsk
