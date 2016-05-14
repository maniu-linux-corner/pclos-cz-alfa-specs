Name:		nemo-image-converter
Version:	3.0.0
Summary:	extension for nemo
Release:	%mkrel 1
License:	GPLv2+
URL:		https://github.com/linuxmint/nemo-extensions
Group:		Graphical desktop/Cinnamon
Source:		nemo-image-converter-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) 
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0) 
BuildRequires:	nemo-devel
Requires:	nemo 


%description
extension for Name


%prep
%setup -q -n nemo-image-converter-%{version}

%build
sh autogen.sh --prefix=/usr
%make

%install
%make_install

%files 
%defattr(-,root,root)
%{_libdir}/nemo/extensions-3.0/*
%{_datadir}/locale/*
%{_datadir}/%{name}/*



%changelog
* Sat Mar 26 2016 Mank <mank at pclinuxos.cz> 3.0.0-1mank2016
- update to 3.0.0
* Sat Oct 26 2015 Mank <mank at pclinuxos.cz> 2.8.0-1mank2015
- Create pkg


