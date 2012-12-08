%define upstream_name	 Class-Singleton
%define upstream_version 1.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A Singleton class for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is the Class::Singleton module. A Singleton describes an object class that
can have only one instance in any system. This module implements a Singleton
class from which other classes can be derived.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.400.0-4mdv2012.0
+ Revision: 765091
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.400.0-3
+ Revision: 763535
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.400.0-2
+ Revision: 667045
- mass rebuild

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2010.1
+ Revision: 505696
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4-3mdv2010.0
+ Revision: 426428
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.4-2mdv2009.0
+ Revision: 223573
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.4-1mdv2008.1
+ Revision: 136684
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-1mdv2008.0
+ Revision: 98034
- new version

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.03-4mdv2008.0
+ Revision: 67715
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.03-3mdv2008.0
+ Revision: 23417
- rebuild


* Fri Jan 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.03-2mdk
- Rebuild.

* Wed Aug 25 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-1mdk
- Initial MDK release.

