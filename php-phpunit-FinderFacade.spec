%define		status		stable
%define		pearname	FinderFacade
%include	/usr/lib/rpm/macros.php
Summary:	Convenience wrapper for Symfony's Finder component
Name:		php-phpunit-FinderFacade
Version:	1.1.0
Release:	1
License:	The BSD 3-Clause License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	7e48494599e302d37e97ec5317a85f1f
URL:		http://pear.phpunit.de/package/FinderFacade/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-symfony2-Finder >= 2.2.0
Requires:	php-theseer-fDOMDocument >= 1.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convenience wrapper for Symfony's Finder component.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

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
%dir %{php_pear_dir}/SebastianBergmann
%{php_pear_dir}/SebastianBergmann/FinderFacade