%{?scl:%scl_package perl-Sub-Install}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Sub-Install
Version:        0.927
Release:        4.sc1%{?dist}
Summary:        Install subroutines into packages easily
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sub-Install/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Sub-Install-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(id -nu)
BuildArch:      noarch
# ================= Module Build ============================
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# ================= Run-time ================================
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# ================= Test Suite ==============================
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.94
%if !%{defined perl_bootstrap}
# Test::Output -> Sub::Exporter -> Sub::Install
BuildRequires:  %{?scl_prefix}perl(Test::Output)
%endif
# ================= Run-time ================================
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(B)

%description
This module makes it easy to install subroutines into packages without the
unsightly mess of no strict or typeglobs lying about where just anyone
can see them.

%prep
%setup -q -n Sub-Install-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%clean
rm -rf %{buildroot}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Sub/
%{_mandir}/man3/Sub::Install.3pm*

%changelog
* Mon Nov 25 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.927-4
- Re-rebuild of bootstrapped packages

* Wed Nov 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.927-3
- Rebuilt for SCL

* Wed Nov 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.927-2
- Update BRs

* Wed Nov 13 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.927-1
- Update to 0.927

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.926-10
- Perl 5.18 re-rebuild of bootstrapped packages

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.926-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.926-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.926-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Paul Howarth <paul@city-fan.org> - 0.926-6
- Be more selective about what to exclude when bootstrapping
- Don't use macros for commands
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot
- Make %%files list more explicit
- Fix typo in %%description

* Mon Aug 20 2012 Petr Pisar <ppisar@redhat.com> - 0.926-5
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.926-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 0.926-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 0.926-2
- Perl 5.16 rebuild

* Mon Mar 12 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.926-1
- Update to 0.926

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.925-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.925-9
- Perl mass rebuild
- add perl_bootstrap macro
- add missing BR ExtUtils::MakeMaker

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.925-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.925-7
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.925-6
- Mass rebuild with perl-5.12.0

* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.925-5
- add license

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.925-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.925-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.925-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.925-1
- update to 0.925

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.924-3
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.924-2
- rebuild for new perl
- fix license tag

* Wed Nov 22 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.924-1
- update to 0.924
- add perl(Test::Perl::Critic) to BR's

* Wed Sep 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.922-2
- bump

* Sat Sep 02 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.922-1
- Specfile autogenerated by cpanspec 1.69.1.
