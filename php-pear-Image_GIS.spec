%define		_class		Image
%define		_subclass	GIS
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

%define		_requires_exceptions pear(Image/Color.php)

Summary:	%{_pearname} - visualization of GIS data
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	%mkrel 9
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/Image_GIS/
Requires:	php-gd
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Generating maps on demand can be a hard job as most often you don't
have the maps you need in digital form. But you can generate your own
maps based on raw, digital data description files which are available
for free on the net. This package provides a parser for the most
common format for geographical data, the Arcinfo/E00 format as well as
renderers to produce images using GD or Scalable Vector Graphics
(SVG).

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/{Parser,Renderer}

install %{_pearname}-%{version}/%{_subclass}.php %{buildroot}%{_datadir}/pear/%{_class}/
install %{_pearname}-%{version}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Parser/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Parser
install %{_pearname}-%{version}/%{_subclass}/Renderer/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Renderer

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_datadir}/pear/%{_class}/%{_subclass}
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Parser
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Renderer
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Parser/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Renderer/*.php

%{_datadir}/pear/packages/%{_pearname}.xml


