%define		status		stable
%define		pearname	FinderFacade
Summary:	Convenience wrapper for Symfony's Finder component
Name:		php-phpunit-FinderFacade
Version:	1.1.0
Release:	3
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	7e48494599e302d37e97ec5317a85f1f
Patch0:		autoload.patch
URL:		https://github.com/sebastianbergmann/finder-facade
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear >= 1.3.14-2
Requires:	php-symfony2-Finder >= 2.7.7
Requires:	php-theseer-fDOMDocument >= 1.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear Symfony/Component/.*

%description
Convenience wrapper for Symfony's Finder component.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup
%patch0 -p1

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/FinderFacade/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/SebastianBergmann/FinderFacade
