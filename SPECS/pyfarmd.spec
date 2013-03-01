%global github_user thesharp
%global github_repo pyfarmd
%global github_tag 1.0

%global __pip pip

Name:           %{github_repo}
Version:        %{github_tag}
Release:        1.vortex%{?dist}
Summary:        Python daemon for running lots of applications across many boxes
Vendor:         Vortex RPM

Group:          System Environment/Daemons
License:        MIT
URL:            http://github.com/%{github_user}/%{github_repo}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  git
Requires:       python-daemonize, python-setproctitle, python-simplejson, python-simplemail

%description
pyfarmd is a daemon which will parse the config file and start all the shit from it.
It will also kill all the unnecessary shit which should be dead.
It works on multiple hosts.

%prep
git clone git@github.com:%{github_user}/%{github_repo}
cd %{github_repo}
git reset --hard %{github_tag}
rm -rf .git
cd ..
mv %{github_repo} %{github_repo}-%{github_tag}
tar xf %{github_repo}-%{github_tag}.tar.gz
cd %{github_repo}-%{github_tag}

%install
cd %{github_repo}-%{github_tag}
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr/sbin
mv %{buildroot}/usr/etc/%{name}.conf %{buildroot}/etc/%{name}.conf
mv %{buildroot}/usr/bin/%{name} %{buildroot}/usr/sbin/%{name}
rm -rf %{buildroot}/usr/lib

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/pyfarmdctl
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Fri Mar  1 2013 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.0-1.vortex
- Initial packaging.

