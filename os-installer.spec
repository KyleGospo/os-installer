Name:           os-installer
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        A simple operating system installer

License:        GPLv3+
URL:            https://gitlab.gnome.org/p3732/os-installer
Source:         %{url}/-/archive/main/os-installer-main.tar

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gweather4)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(udisks)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  python3-yaml

# Disable debug packages
%define debug_package %{nil}

%description
A simple operating system installer, intended to be used with live install systems. Provides bootstrapping through language, keyboard, internet connection and disk selection. Allows defining of optional additional software to be installed.

%prep
%autosetup -n os-installer-main

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/com.github.p3732.OS-Installer.desktop
%{_datadir}/appdata/com.github.p3732.OS-Installer.appdata.xml
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/icons/hicolor/scalable/apps/com.github.p3732.OS-Installer.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.github.p3732.OS-Installer-symbolic.svg
%{_datadir}/glib-2.0/schemas/com.github.p3732.OS-Installer.gschema.xml
