Name:		nemo-dropbox
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

%build
sh autogen.sh --prefix=/usr
%configure

%install
%make_install




%files 
%defattr(-,root,root)
%{_bindir}/dropbox
%{_datadir}/%{name}/*
%{_libdir}/nemo/extensions-3.0/*
%{_datadir}/applications/dropbox.desktop
%{_datadir}/icons/hicolor/*
/usr/share/man/man1/dropbox.1.bz2

%changelog
* Sat Mar 26 2016 Mank <mank at pclinuxos.cz> 3.0.0-1mank2016
- update to 3.0.0
* Sat Oct 26 2015 Mank <mank at pclinuxos.cz> 2.8.0-1mank2015
- Create pkg


