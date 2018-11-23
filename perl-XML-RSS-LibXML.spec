#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-RSS-LibXML
Version  : 0.3105
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/XML-RSS-LibXML-0.3105.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/XML-RSS-LibXML-0.3105.tar.gz
Summary  : 'XML::RSS with XML::LibXML'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-RSS-LibXML-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# NAME
XML::RSS::LibXML - XML::RSS with XML::LibXML
# SYNOPSIS
use XML::RSS::LibXML;
my $rss = XML::RSS::LibXML->new;
$rss->parsefile($file);

%package dev
Summary: dev components for the perl-XML-RSS-LibXML package.
Group: Development
Provides: perl-XML-RSS-LibXML-devel = %{version}-%{release}

%description dev
dev components for the perl-XML-RSS-LibXML package.


%package license
Summary: license components for the perl-XML-RSS-LibXML package.
Group: Default

%description license
license components for the perl-XML-RSS-LibXML package.


%prep
%setup -q -n XML-RSS-LibXML-0.3105

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-RSS-LibXML
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-RSS-LibXML/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML/ImplBase.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML/MagicElement.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML/Namespaces.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML/Null.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML/V0_9.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML/V0_91.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML/V0_92.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML/V1_0.pm
/usr/lib/perl5/vendor_perl/5.28.0/XML/RSS/LibXML/V2_0.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::RSS::LibXML.3
/usr/share/man/man3/XML::RSS::LibXML::ImplBase.3
/usr/share/man/man3/XML::RSS::LibXML::MagicElement.3
/usr/share/man/man3/XML::RSS::LibXML::Namespaces.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-RSS-LibXML/LICENSE
