Name:           dummy-gnome-polkit-cinnamon
Version:        1.0.0
Release:        1%{?dist}
Summary:        Gnome polkit files for cinnamon

License:        GPL
URL:            pclinuxos.cz
Source0:        polkit-gnome-authentication-agent-1.desktop
BuildArch:	noarch
Requires:       polkit-gnome

%description
Cinnamon fix for polkit

%prep

%install
install -D %{SOURCE0} $RPM_BUILD_ROOT/etc/xdg/autostart/polkit-gnome-authentication-agent-1-for-cinnamon.desktop

%files
/etc/xdg/autostart/polkit-gnome-authentication-agent-1-for-cinnamon.desktop



%changelog
