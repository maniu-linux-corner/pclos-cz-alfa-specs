%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global         add_to_doc_files()      \
        mkdir -p %{buildroot}%{_docdir}/%{name}-%{version} ||: ; \
        cp -p %1  %{buildroot}%{_docdir}/%{name}-%{version}/$(echo '%1' | sed -e 's!/!.!g')

Name:           webkitgtk4
Version:        2.12.0
Release:        %mkrel 1
Summary:        GTK+ Web content engine library
Group:          System/Libraries
License:        LGPLv2+ and BSD
URL:            http://www.webkitgtk.org/
Source0:        http://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
#Patch0:         webkit-1.1.14-nspluginwrapper.patch
#Patch1:         webkitgtk-aarch64.patch
#Patch2:         webkitgtk-2.4.1-cloop_fix.patch
#Patch5:         webkitgtk-2.4.8-plugin_none.patch
#Patch7:         webkitgtk-2.4.8-gmutexlocker.patch
#Patch8:         webkitgtk-2.4.8-user-agent.patch
#Patch9:         webkitgtk-2.4.8-g_object_destroyed.patch
#Patch10:        webkitgtk-2.4.8-late-certificate-validation.patch
BuildRequires: gperf ruby
BuildRequires: %{_lib}secret-devel

%description
WebKitGTK+ is the port of the portable web rendering engine WebKit to the
GTK+ platform.

This package contains WebKitGTK+ for GTK+ 3.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Group:          Documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains developer documentation for %{name}.

%prep
%setup -qn "webkitgtk-%{version}"
#%patch0 -p1 -b .nspluginwrapper
#%patch1 -p1 -b .aarch64
#%patch2 -p1 -b .cloop_fix
#%patch5 -p1 -b .plugin_none
#%patch7 -p1 -b .gmutex_locker
#%patch8 -p1 -b .user_agent
#%patch9 -p1 -b .g_object_destroyed
#%patch10 -p1 -b .certificate_validation

%build

# Use linker flags to reduce memory consumption
%global optflags %{optflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads


#todo update hunspell? USE_SYSTEM_MALLOC
mkdir -p build
cd build
cmake -DENABLE_WEBKIT=ON -DPORT=GTK -DUSE_LIBHYPHEN=OFF -DCMAKE_INSTALL_PREFIX=%{buildroot}/  ..

mkdir -p DerivedSources/webkit
mkdir -p DerivedSources/WebCore
mkdir -p DerivedSources/ANGLE
mkdir -p DerivedSources/WebKit2
mkdir -p DerivedSources/webkitdom/
mkdir -p DerivedSources/InjectedBundle
mkdir -p DerivedSources/Platform

make -j1 V=1

%install
rm -rf %buildroot
make install DESTDIR=%{buildroot}

install -d -m 755 %{buildroot}%{_libexecdir}/%{name}
install -m 755 Programs/GtkLauncher %{buildroot}%{_libexecdir}/%{name}

# Remove lib64 rpaths
chrpath --delete %{buildroot}%{_bindir}/jsc-3
chrpath --delete %{buildroot}%{_libdir}/libwebkitgtk-3.0.so
chrpath --delete %{buildroot}%{_libexecdir}/%{name}/GtkLauncher

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang WebKitGTK-3.0

## Finally, copy over and rename the various files for %%doc inclusion.
%add_to_doc_files Source/WebKit/LICENSE
%add_to_doc_files Source/WebKit/gtk/NEWS
%add_to_doc_files Source/WebCore/icu/LICENSE
%add_to_doc_files Source/WebCore/LICENSE-APPLE
%add_to_doc_files Source/WebCore/LICENSE-LGPL-2
%add_to_doc_files Source/WebCore/LICENSE-LGPL-2.1
%add_to_doc_files Source/JavaScriptCore/COPYING.LIB
%add_to_doc_files Source/JavaScriptCore/THANKS
%add_to_doc_files Source/JavaScriptCore/AUTHORS
%add_to_doc_files Source/JavaScriptCore/icu/README
%add_to_doc_files Source/JavaScriptCore/icu/LICENSE


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :


%files -f WebKitGTK-3.0.lang
%doc %{_pkgdocdir}/
%{_libdir}/libwebkitgtk-4.0.so.*
%{_libdir}/libjavascriptcoregtk-4.0.so.*
%{_libdir}/girepository-1.0/WebKit-4.0.typelib
%{_libdir}/girepository-1.0/JavaScriptCore-4.0.typelib
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/GtkLauncher
%{_datadir}/webkitgtk-4.0

%files  devel
%defattr(-,root,root,-)
%{_bindir}/jsc-3
%{_includedir}/webkitgtk-4.0
%{_libdir}/libwebkitgtk-4.0.so
%{_libdir}/libjavascriptcoregtk-4.0.so
%{_libdir}/pkgconfig/webkitgtk-4.0.pc
%{_libdir}/pkgconfig/javascriptcoregtk-4.0.pc
%{_datadir}/gir-1.0/WebKit-4.0.gir
%{_datadir}/gir-1.0/JavaScriptCore-4.0.gir

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/webkitgtk
%{_datadir}/gtk-doc/html/webkitdomgtk


%changelog
* Mon Apr 06 2015 bb <bb> 2.4.8-2pclos2015
- rebuild with fixed rpm-build packages
- so correct provides and dependcies work

* Sun Mar 29 2015 bb <bb> 2.4.8-1pclos2015
- update

* Mon Dec 23 2013 bb <bb> 1.10.0-1pclos2013
- update

* Sat Sep 07 2013 billybot <billybot> 1.8.3-1pclos2013
- 1.8.3

