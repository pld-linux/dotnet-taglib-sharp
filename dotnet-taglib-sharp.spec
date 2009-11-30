#
# TODO: Make build as noarch
# TODO: Rename to dotnet-taglib-sharp?
#
%include	/usr/lib/rpm/macros.mono
Summary:	Metadata library for most common movie and music formats
Name:		taglib-sharp
Version:	2.0.3.2
Release:	2
License:	LGPLv2
Group:		Development
#Source0:	http://www.taglib-sharp.com/Download/%{name}-%{version}.tar.gz
Source0:	http://download.banshee-project.org/taglib-sharp/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7c6e613e803b31d3d62e4def0359fcb4
URL:		http://taglib-sharp.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	monodoc
BuildRequires:	pkgconfig
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TagLib# is a metadata or "tag" reader and writer library that supports
the most common movie and music formats, abstracting away format
specificity. TagLib# offers either a common API for all formats or
access to specific APIs for a given format.

%package devel
Summary:	Header files for taglib-sharp library
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotektaglib-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for taglib-sharp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliote taglib-sharp.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-docs \
	--libdir=/usr/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_prefix}/lib/mono/gac/taglib-sharp
%{_prefix}/lib/mono/gac/policy.2.0.taglib-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/taglib-sharp
%{_datadir}/pkgconfig/taglib-sharp.pc
