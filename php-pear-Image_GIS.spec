%define		_class		Image
%define		_subclass	GIS
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(Image/Color.php)

Name:		php-pear-%{upstream_name}
Version:	1.1.2
Release:	%mkrel 3
Summary:	Visualization of GIS data
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Image_GIS/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires:	php-gd
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Generating maps on demand can be a hard job as most often you don't
have the maps you need in digital form. But you can generate your own
maps based on raw, digital data description files which are available
for free on the net. This package provides a parser for the most
common format for geographical data, the Arcinfo/E00 format as well as
renderers to produce images using GD or Scalable Vector Graphics
(SVG).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-3mdv2012.0
+ Revision: 742019
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-2
+ Revision: 679371
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-1mdv2011.0
+ Revision: 587644
- update to new version 1.1.2

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.1-11mdv2010.1
+ Revision: 473543
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-10mdv2010.0
+ Revision: 441196
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-9mdv2009.1
+ Revision: 322141
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-8mdv2009.0
+ Revision: 236896
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-7mdv2007.0
+ Revision: 81900
- Import php-pear-Image_GIS

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdk
- initial Mandriva package (PLD import)

