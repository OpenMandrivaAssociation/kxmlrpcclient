%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Frameworks 5 XMLRPC services interaction module
Name:		kxmlrpcclient
Version:	5.114.0
Release:	1
License:	BSD
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Concurrent)
# For QCH format docs
BuildRequires: qt5-assistant
BuildRequires: doxygen

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
%{_datadir}/qlogging-categories5/kxmlrpcclient.categories
%{_datadir}/qlogging-categories5/kxmlrpcclient.renamecategories

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
%{_libdir}/cmake/KF5XmlRpcClient
%{_libdir}/libKF5XmlRpcClient.so
%{_libdir}/qt5/mkspecs/modules/qt_KXmlRpcClient.pri

#----------------------------------------------------------------------------
%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devKF5XmlRpcClient} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libkxmlrpcclient5
