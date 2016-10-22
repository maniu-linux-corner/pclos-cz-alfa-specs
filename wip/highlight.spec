Name:           highlight
Version:        3.32
Release:        1%{?dist}
Summary:        Fast and flexible source code highlighter (CLI version)

License:        GPLv3
URL:            http://www.andre-simon.de/doku/highlight/highlight.html
Source0:        highlight-3.32.zip

BuildRequires:  lua

%description


%prep
%setup -q


%build
make QMAKE=qmake-qt5

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" QMAKE=qmake-qt5 install

%files
/etc/highlight/*
%{_datadir}/doc/highlight/*
%{_bindir}/highlight
%{_datadir}/highlight/langDefs/*
%{_datadir}/highlight/plugins/*
%{_datadir}/highlight/themes/*
%{_datadir}/man/man1/*

%changelog
