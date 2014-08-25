
Name:       qa-droid-tools
Summary:    QA android tools
Version:    4.4.4_r2
Release:    1
Group:      Tools
License:    Apache 2.0
Source0:    qa-droid-tools-%{version}.tar.gz
Source1:    adb.mk
Source2:    fastboot.mk
BuildRequires:  pkgconfig(openssl)
BuildRequires:  libselinux-devel
BuildRequires:  zlib

%description
qa-droid-tools for Mer

The upstream tarball is based of these upstream Android git repos:
  git clone https://android.googlesource.com/platform/system/core
  git clone https://android.googlesource.com/platform/system/extras

with unneeded files removed.

%prep
%setup -q

%build
make -f %{SOURCE1} -C core/adb
make -f %{SOURCE2} -C core/fastboot

%install
rm -rf %{buildroot}
install -D -m 755  core/adb/adb %{buildroot}%{_bindir}/adb
install -D -m 755  core/fastboot/fastboot %{buildroot}%{_bindir}/fastboot

%files
%defattr(-,root,root,-)
%{_bindir}/adb
%{_bindir}/fastboot
