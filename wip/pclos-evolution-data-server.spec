%define api_version 1.2
%define ui_api_version 3.0
%define dir_version 3.22

%define camelmajor 59
%define camel_libname %mklibname camel %{api_version} %{camelmajor}

%define ebookmajor 16
%define ebook_libname %mklibname ebook %{api_version} %{ebookmajor}

%define ecalmajor 19
%define ecal_libname %mklibname ecal %{api_version} %{ecalmajor}

%define edatabookmajor 25
%define edatabook_libname %mklibname edata-book %{api_version} %{edatabookmajor}

%define edatacalmajor 28
%define edatacal_libname %mklibname edata-cal %{api_version} %{edatacalmajor}

%define edataservermajor 22
%define edataserver_libname %mklibname edataserver %{api_version} %{edataservermajor}
%define edataserver_libnamedev %mklibname -d edataserver %{api_version}

%define edataserveruimajor 1
%define edataserverui_libname %mklibname edataserverui %{ui_api_version} %{edataserveruimajor}

%define ebackendmajor 10
%define ebackend_libname %mklibname ebackend %{api_version} %{ebackendmajor}

%define gi_major 1.2
%define girname %mklibname %{name}-gir %{gi_major}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		evolution-data-server
Summary:	Evolution Data Server
Version:	3.22.1
Release:	%mkrel 1
License: 	LGPLv2+
Group:		System/Libraries
Source0: 	evolution-data-server-3.22.1.tar.xz
URL: 		http://www.gnome.org/projects/evolution/

### Build Dependencies ###
Provides: 	devel(libedbus-private)
BuildRequires: %{_lib}atk1.0-devel
BuildRequires: %{_lib}cairo-devel
BuildRequires: %{_lib}db4.8-devel
BuildRequires: %{_lib}ext2fs-devel
BuildRequires: %{_lib}gcr-devel
BuildRequires: %{_lib}gdata-devel
BuildRequires: %{_lib}gdk_pixbuf2.0_0-devel
BuildRequires: %{_lib}girepository-devel
BuildRequires: %{_lib}glib2.0-devel
BuildRequires: %{_lib}glib2.0_0
BuildRequires: %{_lib}gnome-keyring-devel
BuildRequires: %{_lib}gtk+3.0-devel
BuildRequires: %{_lib}ical-devel
BuildRequires: %{_lib}krb53-devel
BuildRequires: %{_lib}ldap2.4_2-devel
BuildRequires: %{_lib}nspr-devel
BuildRequires: %{_lib}nss-devel
BuildRequires: %{_lib}pango1.0-devel
BuildRequires: %{_lib}soup-devel
BuildRequires: %{_lib}sqlite3-devel
BuildRequires: %{_lib}xml2-devel

%description
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package devel
Summary:	Libraries and include files for using Evolution Data Server
Group:		Development/Libraries
Requires:	%{name} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libedataserver-devel = %version-%release
AutoReq: No

%description devel
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.


%prep
%setup -q

%build
#sh autogen.sh --disable-uoa --disable-weather

%configure2_5x \
	--with-krb5=%{_prefix} \
	--with-krb5-libs=%{_libdir} \
	--with-libdb=%{_prefix} \
	--with-openldap=yes \
	--with-static-ldap=no \
	--disable-weather \
	--disable-static \
	--enable-gtk-doc=no \
	--disable-uoa \
	--enable-goa \
	--enable-vala-bindings \
	--enable-introspection=yes \
	--disable-glibtest \
	--with-systemduserunitdir=no \
	--disable-google-auth # todo figure what is with GAuth


%make

%install
rm -rf %buildroot
%makeinstall_std

# remove libtool archives for importers and the like
find $RPM_BUILD_ROOT/%{_libdir} -name '*.la' -exec rm {} \;

# give the libraries some executable bits 
find $RPM_BUILD_ROOT -name '*.so.*' -exec chmod +x {} \;

%find_lang %{name}-%{dir_version}

%files -f %{name}-%{dir_version}.lang
%doc COPYING NEWS
%{_libdir}/%{name}
%{_libexecdir}/camel-index-control-%{api_version}
%{_libexecdir}/evolution-addressbook-factory
%{_libexecdir}/evolution-calendar-factory
%{_libexecdir}/evolution-source-registry
%attr(2755,root,mail) %{_libexecdir}/camel-lock-helper-%{api_version}
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.AddressBook.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Calendar.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Sources.service
%{_datadir}/GConf/gsettings/*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pixmaps/%{name}
/usr/lib64/camel-gpg-photo-saver
%{_libdir}/libcamel-%{api_version}.so.%{camelmajor}*
%{_libdir}/libebook-%{api_version}.so.%{ebookmajor}*
%{_libdir}/libecal-%{api_version}.so.%{ecalmajor}*
%{_libdir}/libedata-book-%{api_version}.so.%{edatabookmajor}*
%{_libdir}/libedata-cal-%{api_version}.so.%{edatacalmajor}*
%{_libdir}/libedataserver-%{api_version}.so.%{edataservermajor}*
%{_libdir}/libedataserverui-%{api_version}.so.%{edataserveruimajor}*
%{_libdir}/girepository-1.0/EDataServer-%{gi_major}.typelib
#%{_libdir}/girepository-1.0/ECalendar-%{gi_major}.typelib
%{_libdir}/girepository-1.0/EBook-%{gi_major}.typelib
%{_libdir}/libebackend-%{api_version}.so.%{ebackendmajor}*
%{_libdir}/evolution-addressbook-factory-subprocess
%{_libdir}/evolution-calendar-factory-subprocess
%{_libdir}/evolution-scan-gconf-tree-xml
%{_libdir}/evolution-user-prompter
%{_libdir}/girepository-1.0/EBookContacts-1.2.typelib
%{_libdir}/libebook-contacts-1.2.so.2
%{_libdir}/libebook-contacts-1.2.so.2.0.0
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.UserPrompter.service


%files devel
#%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/EDataServer-%{gi_major}.gir
#%{_datadir}/gir-1.0/ECalendar-%{gi_major}.gir
%{_datadir}/gir-1.0/EBook-%{gi_major}.gir
%{_datadir}/gir-1.0/EBookContacts-%{gi_major}.gir
%{_datadir}/gir-1.0/Camel-1.2.gir
#/usr/lib/systemd/*
%{_datadir}/vala/vapi/

%clean
rm -rf %buildroot

%changelog
