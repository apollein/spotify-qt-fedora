Name:	spotify-qt
Version:	3.9
Release:	1%{?dist}
Summary:	Spotify third-party client written in Qt
License:	GPLv3+
URL:	https://github.com/kraxarn/spotify-qt/
Source0:	https://github.com/kraxarn/spotify-qt/archive/v%{version}.tar.gz

BuildArch:	x86_64
Requires:	qt5-qtbase
Requires:	qt5-qtsvg
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtsvg-devel
Requires:	hicolor-icon-theme
Requires:	qt5-qtbase-gui
BuildRequires:	git
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	gcc-c++

%description
Spotify third-party client written in Qt

%prep
%autosetup -p1

%build
#cd "%{name}-%{version}"
ls /usr/lib64/cmake/Qt5
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}

%install
#cd "%{name}-%{version}"
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/spotify-qt
%{_datadir}/icons/hicolor/scalable/apps/spotify-qt.svg
%{_datadir}/applications/spotify-qt.desktop
