%define upstream_name    String-RewritePrefix
%define upstream_version 0.007

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Rewrite strings based on a set of known prefixes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/String/String-RewritePrefix-%{upstream_version}.tar.gz

BuildRequires: perl(Sub::Exporter)
BuildRequires: perl-devel

%define debug_package %{nil}


%description
Rewrite strings based on a set of known prefixes

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.6.0-2mdv2011.0
+ Revision: 657835
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 596651
- update to 0.006

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 472327
- adding missing buildrequires:
- update to 0.005

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 380952
- import perl-String-RewritePrefix


* Fri May 29 2009 cpan2dist 0.004-1mdv
- initial mdv release, generated with cpan2dist


