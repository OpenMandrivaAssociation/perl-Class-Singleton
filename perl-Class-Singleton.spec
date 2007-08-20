%define module	Class-Singleton
%define name	perl-%{module}
%define version	1.03
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A Singleton class for Perl
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel

%description
This is the Class::Singleton module. A Singleton describes an object class that
can have only one instance in any system. This module implements a Singleton
class from which other classes can be derived.

%prep
%setup -q -n %{module}-%{version}
chmod 644 Singleton.pm

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/*
%{_mandir}/*/*

