Name:		nemo-extensions-fileroller
Version:	2.8.0
Summary:	A file-roller extension for nemo
Release:	%mkrel 1
License:	GPLv2+
URL:		https://github.com/linuxmint/nemo-extensions
Group:		Graphical desktop/Cinnamon
Source:		nemo-fileroller-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) 
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0) 
BuildRequires:	nemo-devel
Requires:	nemo 
Requires:   file-roller

%description
Fileroller extension for Nemo for the Cinnamon desktop environment. 


%prep
%setup -q -n nemo-fileroller-%{version}

%build
sh autogen.sh

%configure2_5x --disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/nemo/extensions-3.0/*.la

%clean
rm -rf %{buildroot}


%files 
%defattr(-,root,root)
%doc ChangeLog NEWS README COPYING
%{_libdir}/nemo/extensions-3.0/libnemo-fileroller.so


%changelog
* Sat Oct 26 2016 Mank <mank at pclinuxos.cz> 2.8.0-1mank2016
- Update
* Sat Oct 26 2013 Ken <lxgator at gmail.com> 2.0.0-1pclos2013
- Create pkg


