%define upstream_name	 Class-Singleton
%define upstream_version 1.5

Summary:	A Singleton class for Perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
This is the Class::Singleton module. A Singleton describes an object class that
can have only one instance in any system. This module implements a Singleton
class from which other classes can be derived.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/man3/*
