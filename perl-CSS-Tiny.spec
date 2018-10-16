#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CSS
%define		pnam	Tiny
%include	/usr/lib/rpm/macros.perl
Summary:	CSS::Tiny - Read/Write .css files with as little code as possible
Summary(pl.UTF-8):	CSS::Tiny - odczyt/zapis plików .css przy użyciu jak najmniejszego kodu
Name:		perl-CSS-Tiny
Version:	1.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CSS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	044e777384d22941bc6c104dcfa18035
URL:		http://search.cpan.org/dist/CSS-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSS::Tiny is a Perl class to read and write .css stylesheets with as 
little code as possible, reducing load time and memory overhead.
CSS.pm requires about 2.6 meg of RAM to load, which is a large amount
of overhead if you only want to do trivial things.

%description -l pl.UTF-8
CSS::Tiny to klasa Perla do odczytu i zapisu arkuszy styli .css przy
użyciu jak najmniejszej ilości kodu, co zmniejsza czas ładowania i
narzut pamięciowy. CSS.pm wymaga około 2.6MB RAM, co jest znacznym
narzutem, jeśli chce się zrobić coś prostego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/CSS/Tiny.pm
%{_mandir}/man3/CSS::Tiny.3pm*
