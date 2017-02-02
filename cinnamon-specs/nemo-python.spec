Name:		nemo-python
Version:	3.2.0
Summary:	python nemo
Release:	%mkrel 1
License:	GPLv2+
URL:		https://github.com/linuxmint/nemo-extensions
Group:		Graphical desktop/Cinnamon
Source:		nemo-python-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) 
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0) 
BuildRequires:	nemo-devel
Requires:	nemo 
Requires:	python

%description
python extension for Nemo for the Cinnamon desktop environment. 


%prep
%setup -q -n nemo-python-%{version}

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
%{_libdir}/nemo/extensions-3.0/libnemo-python.so
%{_libdir}/pkgconfig/nemo-python.pc

%changelog
* Sat Oct 26 2016 Mank <mank at pclinuxos dot cz> 2.8.0-1mank2016
- Create pkg


