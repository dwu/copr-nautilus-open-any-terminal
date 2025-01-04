%global debug_package %{nil}
%undefine _missing_build_ids_terminate_build

Name:           nautilus-open-any-terminal
Version:        0.6.0
Release:        1%{?dist}
Summary:        An extension for nautilus, which adds an context-entry for opening other terminal emulators than gnome-terminal

License:        GPL-3.0-only
URL:            https://github.com/Stunkymonkey/nautilus-open-any-terminal
Source0:        %{name}-%{version}.tar.gz
# SOURCE URL:   https://github.com/Stunkymonkey/nautilus-open-any-terminal/archive/refs/tags/<version>.tar.gz

ExclusiveArch:  x86_64

Requires:       nautilus-python

BuildRequires:  gettext
BuildRequires:  make


%description
nautilus-open-any-terminal is an extension for nautilus, which adds an
context-entry for opening other terminal emulators than gnome-terminal.

%prep
%autosetup -n nautilus-open-any-terminal-%{version}


%build
%make_build


%install
%make_install
rm -rf %{buildroot}%{_datadir}/caja-python


%post
glib-compile-schemas /usr/share/glib-2.0/schemas


%files
%{_datadir}/nautilus-python/extensions/nautilus_open_any_terminal.py
%{_datadir}/glib-2.0/schemas/com.github.stunkymonkey.nautilus-open-any-terminal.gschema.xml
%{_datadir}/locale/*/LC_MESSAGES/nautilus-open-any-terminal.mo


%changelog
* Sat Jan 04 2025 Daniel Wutke <dwu.public@gmail.com> 0.6.0-1
- Package version 0.6.0 with tito

%autochangelog
