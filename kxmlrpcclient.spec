%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Frameworks 5 XMLRPC services interaction module
Name:		kxmlrpcclient
Version:	5.18.0
Release:	1
License:	BSD
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5I18n)
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

%package i18n
Summary:	KXmlRpcClient translations
Group:		System/Internationalization
BuildArch:	noarch

%description i18n
KXmlRpcClient translations.

%files i18n -f libkxmlrpcclient5.lang

#----------------------------------------------------------------------------

%define KF5XmlRpcClient_major 5
%define libKF5XmlRpcClient %mklibname KF5XmlRpcClient %{KF5XmlRpcClient_major}

%package -n %{libKF5XmlRpcClient}
Summary:	KDE Frameworks 5 XMLRPC services interaction shared library
Group:		System/Libraries
Requires:	%{name}-i18n

%description -n %{libKF5XmlRpcClient}
KDE Frameworks 5 XMLRPC services interaction shared library.

%files -n %{libKF5XmlRpcClient}
%{_libdir}/libKF5XmlRpcClient.so.%{KF5XmlRpcClient_major}*

#----------------------------------------------------------------------------

%define devKF5XmlRpcClient %mklibname KF5XmlRpcClient -d

%package -n %{devKF5XmlRpcClient}
Summary:	Development files for KDE Frameworks 5 XMLRPC services interaction module
Group:		Development/KDE and Qt
Requires:	%{libKF5XmlRpcClient} = %{EVRD}

%description -n %{devKF5XmlRpcClient}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devKF5XmlRpcClient}
%{_includedir}/KF5/KXmlRpcClient
%{_includedir}/KF5/kxmlrpcclient_version.h
%{_libdir}/cmake/KF5XmlRpcClient
%{_libdir}/libKF5XmlRpcClient.so
%{_libdir}/qt5/mkspecs/modules/qt_KXmlRpcClient.pri

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libkxmlrpcclient5
