Name:           xplayer
Version:        1.2.2
Release:        2
Summary:        xplayer

License:        GPL
URL:            https://github.com/linuxmint/xplayer/
Source0:        xplayer-%{version}.tar.gz

%description
...

%prep
%setup -q


%build
NOCONFIGURE=1 gnome-autogen.sh
%configure2_5x --disable-static --disable-run-in-source-tree --disable-vegas-plugin --enable-vala=yes
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_bindir}/*
%{_datadir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_includedir}/*
%changelog
* Sat Jan  7 2017 mank
- import to pclosczsk
