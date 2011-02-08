Summary:	Tools for setting up a Fedora maintainer environment
Name:		fedora-packager
Version:	0.5.2.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
URL:		https://fedorahosted.org/fedora-packager
Source0:	https://fedorahosted.org/releases/f/e/fedora-packager/%{name}-%{version}.tar.bz2
# Source0-md5:	7a8a325e4d30ab5463e599e17079b780
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:	bodhi-client
Requires:	curl
Requires:	koji
#Requires:	mock
Requires:	openssh-clients
Requires:	python-offtrac
Requires:	python-pyOpenSSL
Requires:	python-pycurl
#Requires:	redhat-rpm-config
Requires:	rpm-build
#Requires:	rpmdevtools
#Requires:	rpmlint
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of utilities useful for a Fedora packager in setting up their
environment.

%package -n fedpkg
Summary:	Fedora utility for working with dist-git
Group:		Applications/Databases
Requires:	curl
Requires:	fedora-packager = %{version}-%{release}
Requires:	python-argparse
Requires:	python-git >= 0.2.0
Requires:	python-kitchen

%description -n fedpkg
Provides the fedpkg command for working with dist-git.

%package -n bash-completion-fedpkg
Summary:	bash-completion for fedpkg
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla fedpkg
Group:		Applications/Shells
Requires:	bash-completion
Requires:	fedpkg = %{version}-%{release}

%description -n bash-completion-fedpkg
bash-completion for fedpkg.

%description -n bash-completion-fedpkg -l pl.UTF-8
bashowe uzupełnianie nazw dla fedpkg.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

mv $RPM_BUILD_ROOT/etc/bash_completion.d/fedpkg{.bash,}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/fedora-burn-yubikey
%exclude %{_bindir}/fedpkg
# R: fedora.client.fas2
%{py_sitescriptdir}/fedora_cert

%files -n fedpkg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fedpkg
%{py_sitescriptdir}/pyfedpkg

%files -n bash-completion-fedpkg
%defattr(644,root,root,755)
/etc/bash_completion.d/*
