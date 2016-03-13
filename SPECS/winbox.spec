Summary: Mikrotik RouterOS GUI Configurator (wine)
Name: winbox
Version: 3.1
Release: 1%{?dist}
URL: http://www.mikrotik.com
License: custom
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-root
Requires: wine
#Source0:  http://download2.mikrotik.com/routeros/winbox/%{version}/%{name}.exe
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}%{_datadir}/pixmaps/

install -m 755 %{name} ${RPM_BUILD_ROOT}%{_bindir}
install -Dpm 644 %{name}.exe ${RPM_BUILD_ROOT}%{_datadir}/%{name}/%{name}.exe
install -Dpm 644 %{name}.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
install -Dpm 644 %{name}.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) 
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.exe
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Mar 13 2016 Ivaylo Kuzev <ivkuzevg@gmail.com> - 3.1-1
- Initial spec
