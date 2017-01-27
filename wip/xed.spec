Name:           xed
Version:        1.2.2
Release:        1
Summary:        xed

License:        GPL
URL:            https://github.com/linuxmint/xed
Source0:        xed-%{version}.zip

%description


%prep
%setup -q


%build
sh autogen.sh --prefix=/usr/ --libdir=/usr/lib64
cp -a /usr/share/gtk-doc/data/gtk-doc.make .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_bindir}/*
%{_datadir}/*
%{_includedir}/%{name}/*
%{_libdir}/%{name}/*
%{_libexecdir}/%{name}/*
/usr/lib64/pkgconfig/xed.pc

%changelog
* Sat Jan  7 2017 mank
- import to pclinuxosczsk
