
Name:       qa-droid-tools
Summary:    QA android tools
Version:    5.1.1_r38
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
BuildRequires:  zlib-devel
BuildRequires:  udev
Requires:       udev

Provides:       adb
Provides:       fastboot
Conflicts:      android-tools

%description
qa-droid-tools (fastboot and adb) for Mer QA

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
chmod a+x %{SOURCE3}
%{SOURCE3} > 51-android.rules

%install
rm -rf %{buildroot}
install -D -m 755  core/adb/adb %{buildroot}%{_bindir}/adb
install -D -m 755  core/fastboot/fastboot %{buildroot}%{_bindir}/fastboot
install -D -m 0644 51-android.rules %{buildroot}/lib/udev/rules.d/51-android.rules

%files
%defattr(-,root,root,-)
%{_bindir}/adb
%{_bindir}/fastboot
/lib/udev/rules.d/51-android.rules
