Name:		datefudge
Version:	1.22
#Release:	1%%{?dist}
Release:	0.1%{?dist}
Summary:	Fake the system date

License:	GPLv2+
URL:		http://packages.qa.debian.org/d/datefudge.html
Source0:	http://cdn.debian.net/debian/pool/main/d/datefudge/%{name}_%{version}.tar.xz

BuildRequires:  gcc
%description
This program (and preload library) fakes the system date so that 
programs think the wall clock is ... different. The faking is not 
complete; time-stamp on files are not affected in any way. This 
package is useful if you want to test the date handling of your 
programs without changing the system clock. 

%prep
%setup -q
sed "s/VERSION := \$\(.*\)/VERSION := %{version}/g" -i Makefile
sed 's/-o root -g root/-p/g' -i Makefile

%build
LDFLAGS="%{__global_ldflags}" CFLAGS="%{optflags}" make libdir=%{_libexecdir} %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} libdir=%{_libexecdir}
chmod +x %{buildroot}/%{_libexecdir}/%{name}/datefudge.so #for stripping

%files
%{_libexecdir}/%{name}

%doc README COPYING
%{_mandir}/man1/datefudge.1*
%{_bindir}/datefudge

%changelog
* Fri Dec 21 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.22-1
- New upstream release

* Fri Sep 23 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.21-1
- Initial release for epel7
