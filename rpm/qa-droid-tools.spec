
Name:       qa-droid-tools
Summary:    QA android tools
Version:    4.4.4_r2
Release:    1
Group:      Tools
License:    Apache 2.0
Source0:    qa-droid-tools-%{version}.tar.gz
Source1:    adb.mk
Source2:    fastboot.mk
Source3:    udev-rule-builder.sh
Patch0:     0001-Ignore-selinux-android-header.patch
Patch1:     0001-Add-vendors.patch
Patch2:     0001-Use-mmap-for-fastboot-data.patch
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
%patch0 -p1 -d extras
%patch1 -p1 -d core
%patch2 -p1 -d core

%build
make -f %{SOURCE1} -C core/adb
make -f %{SOURCE2} -C core/fastboot
%{SOURCE3} > 51-android.rules

%install
rm -rf %{buildroot}
install -D -m 755  core/adb/adb %{buildroot}%{_bindir}/adb
install -D -m 755  core/fastboot/fastboot %{buildroot}%{_bindir}/fastboot
install -D -m 0644 51-android.rules %{buildroot}%{_udevprefix}/udev/rules.d/51-android.rules

%files
%defattr(-,root,root,-)
%{_bindir}/adb
%{_bindir}/fastboot
%{_udevprefix}/udev/rules.d/51-android.rules
