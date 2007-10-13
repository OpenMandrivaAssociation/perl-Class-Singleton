%define module	Class-Singleton
%define name	perl-%{module}
%define version	1.4
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A Singleton class for Perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is the Class::Singleton module. A Singleton describes an object class that
can have only one instance in any system. This module implements a Singleton
class from which other classes can be derived.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*

