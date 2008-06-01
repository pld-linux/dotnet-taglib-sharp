#
# TODO: Make build as noarch
#
Summary:	Metadata library for most common movie and music formats
Name:		taglib-sharp
Version:	2.0.3.0
Release:	1
License:	LGPLv2
Group:		Development
URL:		http://taglib-sharp.com/
Source0:	http://www.taglib-sharp.com/Download/%name-%{version}.tar.gz
# Source0-md5:	aa2c344760c8f4d878957fd4600155a5
BuildRequires:	mono-csharp
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TagLib# is a metadata or "tag" reader and writer library that supports
the most common movie and music formats, abstracting away format
specificity. TagLib# offers either a common API for all formats or
access to specific APIs for a given format.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--disable-docs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pkgconfig
mv $RPM_BUILD_ROOT%{_libdir}/pkgconfig/* $RPM_BUILD_ROOT%{_datadir}/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_prefix}/lib/mono/taglib-sharp
%{_prefix}/lib/mono/gac/taglib-sharp
%{_prefix}/lib/mono/gac/policy.2.0.taglib-sharp
%{_prefix}/share/pkgconfig/taglib-sharp.pc
