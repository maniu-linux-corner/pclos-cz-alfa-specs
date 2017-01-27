Name:           xviewer
Version:        1.2.2
Release:        1
Summary:        x-view

License:        GPL
URL:            https://github.com/linuxmint/xviewer
Source0:        xviewer-%{version}.zip

%description
...

%prep
%setup -q


%build

autoreconf -fi

%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_bindir}/*
%{_datadir}/*
%{_includedir}/*
%{_libdir}/*


%changelog
* Sat Jan  7 2017 mank
- import to pclinuxosczsk
