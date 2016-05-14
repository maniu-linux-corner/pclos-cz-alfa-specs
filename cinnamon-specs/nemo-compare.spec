Name:		nemo-compare
Version:	3.0.0
Summary:	extension for nemo
Release:	%mkrel 1
License:	GPLv2+
URL:		https://github.com/linuxmint/nemo-extensions
Group:		Graphical desktop/Cinnamon
Source:		%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) 
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0) 
BuildRequires:	nemo-devel
Requires:	nemo 


%description
extension for Name


%prep
%setup -q -n %{name}-%{version}

%install

install -D data/nemo-compare-preferences.desktop -t "%{buildroot}/usr/share/applications"
install -D data/nemo-compare-notification -t "%{buildroot}/usr/share/%{name}"
install -D src/* -t "%{buildroot}/usr/share/%{name}/"


%post
ln -s /usr/share/nemo-compare/nemo-compare.py "/usr/share/nemo-python/extensions/nemo-compare.py"
ln -s /usr/share/nemo-compare/nemo-compare-preferences.py "/usr/bin/nemo-compare-preferences"

%files 
%defattr(-,root,root)
%{_datadir}/%{name}/*
%{_datadir}/applications/nemo-compare-preferences.desktop





%changelog
* Sat Mar 26 2016 Mank <mank at pclinuxos.cz> 3.0.0-1mank2016
- update to 3.0.0
* Sat Oct 26 2015 Mank <mank at pclinuxos.cz> 2.8.0-1mank2015
- Create pkg


