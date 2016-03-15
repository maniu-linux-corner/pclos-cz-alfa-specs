Name:		nemo-share
Version:	2.8.0
Summary:	A file-roller extension for nemo
Release:	%mkrel 1
License:	GPLv2+
URL:		https://github.com/linuxmint/nemo-extensions
Group:		Graphical desktop/Cinnamon
Source:		nemo-share-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) 
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0) 
BuildRequires:	nemo-devel
Requires:	nemo 
Requires:	task-samba

%description
audio tab extension for Nemo for the Cinnamon desktop environment. 


%prep
%setup -q -n nemo-share-%{version}

%build
sh autogen.sh --prefix=/usr
%make

%install
%make_install

%files 
%defattr(-,root,root)
%{_libdir}/nemo/extensions-3.0/*
%{_datadir}/locale/*
%{_datadir}/nemo-share/*



%changelog
* Sat Oct 26 2013 Ken <mank at pclinuxos.cz> 2.8.0-1pclos2016
- Create pkg


