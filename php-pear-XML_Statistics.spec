%define		_class		XML
%define		_subclass	Statistics
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - obtain statistical information from an XML documents
Summary(pl.UTF-8):	%{_pearname} - uzyskiwanie statystyk z dokumentów XML
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0b8c4a4f6f317553483ffc3c7743518d
URL:		http://pear.php.net/package/XML_Statistics/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_Statistics is able to retrieve statistics about tags, attributes,
entities, processing instructions and CDaata chunks in any XML
document.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
XML_Statistics jest w stanie uzyskać statystykę dotyczącą znaczników,
atrybutów, instrukcji przetwarzających oraz elementów CDaata z
dowolnego dokumentu XML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
