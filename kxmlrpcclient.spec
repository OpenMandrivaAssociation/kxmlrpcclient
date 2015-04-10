%define fw_version 5.9

Summary:	KDE Frameworks 5 XMLRPC services interaction module
Name:		kxmlrpcclient
Version:	5.9.0
Release:	1
License:	BSD
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/frameworks/%{fw_version}/%{name}-%{version}.tar.xz
BuildRequires:	extra-cmake-modules
BuildRequires:	kf5i18n-devel >= %{version}
BuildRequires:	kf5kio-devel >= %{version}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)

%description
KDE Frameworks 5 XMLRPC services interaction module.

KXmlRpcClient contains simple XML-RPC Client support. It is a complete
client and is quite easy to use. Only one interface is exposed to the
world, kxmlrpcclient/client.h and of that interface, you only need to
use 3 methods: setUrl, setUserAgent and call.

A small note on authentication. If you will be accessing an XML-RPC server
which uses HTTP-AUTH, simply set the user and pass in the URL. To use
Digest authentication, call setDigestAuthEnabled(true).

#----------------------------------------------------------------------------

%define kf5xmlrpcclient_major 5
%define libkf5xmlrpcclient %mklibname kf5xmlrpcclient %{kf5xmlrpcclient_major}

%package -n %{libkf5xmlrpcclient}
Summary:	KDE Frameworks 5 XMLRPC services interaction shared library
Group:		System/Libraries

%description -n %{libkf5xmlrpcclient}
KDE Frameworks 5 XMLRPC services interaction shared library.

%files -n %{libkf5xmlrpcclient}
%{_kde5_libdir}/libKF5XmlRpcClient.so.%{kf5xmlrpcclient_major}*

#----------------------------------------------------------------------------

%define devkf5xmlrpcclient %mklibname kf5xmlrpcclient -d

%package -n %{devkf5xmlrpcclient}
Summary:	Development files for KDE Frameworks 5 XMLRPC services interaction module
Group:		Development/KDE and Qt
Requires:	%{libkf5xmlrpcclient} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	kf5xmlrpcclient-devel = %{version}

%description -n %{devkf5xmlrpcclient}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devkf5xmlrpcclient}
%{_kde5_includedir}/KF5/KXmlRpcClient
%{_kde5_includedir}/KF5/kxmlrpcclient_version.h
%{_kde5_libdir}/cmake/KF5XmlRpcClient
%{_kde5_libdir}/libKF5XmlRpcClient.so
%{_kde5_mkspecsdir}/*.pri

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

