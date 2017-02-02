%define api		1.0
%define clutterapi	1.0
%define major		0
%define libname		%mklibname %{name} %{api} %{major}
%define libnamedevel	%mklibname -d %{name}

%define gi_major	1.0
%define girname		%mklibname %{name}-gir %{gi_major}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GTK Support for Clutter
Name:		clutter-gtk
Version:	1.8.2
Release:	%mkrel 5
Source0:	clutter-gtk-1.8.2.zip
License:	LGPLv2+
Group:		System/Libraries
Url:		http://clutter-project.org/
#------------------------------------------------
BuildRequires: pkgconfig(clutter-1.0) >= 1.26.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires: pkgconfig(gl)
BuildRequires: gobject-introspection-devel
BuildRequires: gettext-devel
BuildRequires: gnome-common
BuildRequires: gtk-doc
#---------------------------------------------
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A library providing facilities to integrate Clutter into GTK+
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

#----------------------------------------------------------------------------
%files
%defattr(-, root, root)
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/GtkClutter-%{api}.typelib
%{_datadir}/locale

#----------------------------------------------------------------------------

%package devel
Summary:	Development headers/libraries for %{name}
Group:		Development/Libraries
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{_lib}clutter-gtk%{api}-devel = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}


%description devel
Development headers/libraries for %{name}.

%files devel
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/html/%{name}-%{clutterapi}
%{_libdir}/pkgconfig/%{name}-%{api}.pc

%{_libdir}/lib%{name}-%{api}.so
%{_includedir}/%{name}-%{clutterapi}/%{name}
%{_datadir}/gir-1.0/GtkClutter-%{api}.gir

#----------------------------------------------------------------------------

%prep
%setup -q

%build
./autogen.sh
./configure --prefix=/usr --libdir=/usr/lib64/ --enable-gtk-doc
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang cluttergtk-%{api}


%clean
rm -rf %{buildroot}

%changelog
* Fri Oct 21 2016 Migelo 1.8.2-2_pclos_cz
- update

* Tue Apr 15 2014 bb <bb> 1.5.2-1pclos2014
- update

* Sat Oct 19 2013 billybot <billybot> 1.4.4-1pclos2013
- re-import for cinnamon
