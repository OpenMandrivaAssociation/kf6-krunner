%define libname %mklibname KF6Runner
%define devname %mklibname KF6Runner -d
%define git 20230513

Name: kf6-krunner
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/krunner/-/archive/master/krunner-master.tar.bz2#/krunner-%{git}.tar.bz2
Summary: Framework for providing different actions given a string query
URL: https://invent.kde.org/frameworks/krunner
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6ThreadWeaver)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
Requires: %{libname} = %{EVRD}

%description
Framework for providing different actions given a string query

%package -n %{libname}
Summary: Framework for providing different actions given a string query
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Framework for providing different actions given a string query

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Framework for providing different actions given a string query

%prep
%autosetup -p1 -n krunner-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/krunner.*
%{_datadir}/dbus-1/interfaces/kf5_org.kde.krunner1.xml

%files -n %{devname}
%{_includedir}/KF6/KRunner
%{_libdir}/cmake/KF6Runner
%{_qtdir}/mkspecs/modules/qt_KRunner.pri
%{_datadir}/kdevappwizard/templates/runner.tar.bz2
%{_datadir}/kdevappwizard/templates/runnerpython.tar.bz2
%doc %{_qtdir}/doc/KF6Runner.*

%files -n %{libname}
%{_libdir}/libKF6Runner.so*
