Name:		vgabios
Version:	0.6b
Release:	3.8%{?dist}
Summary:	LGPL implementation of a vga video bios

Group:		Applications/Emulators		
License:	LGPLv2
URL:		http://www.nongnu.org/vgabios/
Source0:	http://savannah.gnu.org/download/%{name}/%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch: x86_64 noarch

Provides: vgabios-qxl
Provides: vgabios-stdvga
Provides: vgabios-vmware

BuildRequires:	dev86
BuildArch: noarch
Patch1:		%{name}-provide-high-res.patch
# For bz#569473 - spice: Need vgabios for qxl device
Patch2: vgabios-use-VBE-LFB-address-from-PCI-base-address-if-present.patch
# For bz#569473 - spice: Need vgabios for qxl device
Patch3: vgabios-qxl-vgabios.patch
# For bz#654639 - [vgabios] bochs vga lfb @ 0xe0000000 causes trouble for hot-plug
Patch4: vgabios-Revert-qxl-vgabios.patch
# For bz#654639 - [vgabios] bochs vga lfb @ 0xe0000000 causes trouble for hot-plug
Patch5: vgabios-Makefile-cleanup.patch
# For bz#654639 - [vgabios] bochs vga lfb @ 0xe0000000 causes trouble for hot-plug
Patch6: vgabios-Add-defines-for-PCI-IDs.patch
# For bz#654639 - [vgabios] bochs vga lfb @ 0xe0000000 causes trouble for hot-plug
Patch7: vgabios-Add-qemu-stdvga-pci-bios.patch
# For bz#654639 - [vgabios] bochs vga lfb @ 0xe0000000 causes trouble for hot-plug
Patch8: vgabios-update-pci_get_lfb_addr-for-vmware-vga.patch
# For bz#654639 - [vgabios] bochs vga lfb @ 0xe0000000 causes trouble for hot-plug
Patch9: vgabios-Add-qemu-vmware-vga-pci-bios.patch
# For bz#654639 - [vgabios] bochs vga lfb @ 0xe0000000 causes trouble for hot-plug
Patch10: vgabios-Add-qemu-qxl-vga-pci-bios.patch
# For bz#691344 - vgabios is missing DPMS support (for S3 support for Win guests)
Patch11: vgabios-add-DPMS-support-to-cirrus-vgabios.patch
# For bz#840087 - Unable to boot rhev-hypervisor6.iso in virtual machine for testing.
Patch12: vgabios-Fix-get-video-mode-vgabios-call.patch
# For bz#1421574 - [virtio-win][svvp][ws2016] cannot generate dump file when using nmi on ws2016
Patch13: vgabios-Reorder-video-modes-to-work-around-a-Windows.patch

%description
vgabios is an LPGL implementation of a bios for a video card.
It is tied to plex86/bochs, althoug it will likely work on other
emulators. It is not intended for use in real cards.


%prep 
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build 
make clean
make biossums %{?_smp_mflags}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vgabios
install -m 0644 VGABIOS-lgpl-*.bin $RPM_BUILD_ROOT%{_datadir}/vgabios 


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/vgabios/
%doc README COPYING
%{_datadir}/vgabios/VGABIOS-lgpl-latest.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.cirrus.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.cirrus.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.qxl.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.qxl.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.stdvga.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.stdvga.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.vmware.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.vmware.debug.bin


%changelog
* Tue Feb 14 2017 Danilo Cesar Lemes de Paula <ddepaula@redhat.com> - 0.6b-3.7.el6
- vgabios-Reorder-video-modes-to-work-around-a-Windows.patch [bz#1421574]
- Resolves: bz#1421574
  ([virtio-win][svvp][ws2016] cannot generate dump file when using nmi on ws2016)

* Thu Nov 08 2012 Michal Novotny <minovotn@redhat.com> - vgabios-0.6b-3.7.el6
- vgabios-Fix-get-video-mode-vgabios-call.patch [bz#840087]
- Resolves: bz#840087
  (Unable to boot rhev-hypervisor6.iso in virtual machine for testing.)

* Tue Apr 12 2011 Eduardo Habkost <ehabkost@redhat.com> - vgabios-0.6b-3.6.el6
- vgabios-add-DPMS-support-to-cirrus-vgabios.patch [bz#691344]
- Resolves: bz#691344
  (vgabios is missing DPMS support (for S3 support for Win guests))

* Mon Feb 07 2011 Eduardo Habkost <ehabkost@redhat.com> - vgabios-0.6b-3.5.el6
- vgabios-Revert-qxl-vgabios.patch [bz#654639]
- vgabios-Makefile-cleanup.patch [bz#654639]
- vgabios-Add-defines-for-PCI-IDs.patch [bz#654639]
- vgabios-Add-qemu-stdvga-pci-bios.patch [bz#654639]
- vgabios-update-pci_get_lfb_addr-for-vmware-vga.patch [bz#654639]
- vgabios-Add-qemu-vmware-vga-pci-bios.patch [bz#654639]
- vgabios-Add-qemu-qxl-vga-pci-bios.patch [bz#654639]
- Include stdvga and vmware bios images in the package
- Resolves: bz#654639
  ([vgabios] bochs vga lfb @ 0xe0000000 causes trouble for hot-plug)

* Thu Mar 18 2010 Eduardo Habkost <ehabkost@redhat.com> - vgabios-0.6b-3.4.el6
- Add VGABIOS-lgpl-latest.qxl.bin to file list
- Add Provides: vgabios-qxl to allow other packages to require vgabios.qxl
- Related: bz#569473
  (spice: Need vgabios for qxl device)

* Thu Mar 18 2010 Eduardo Habkost <ehabkost@redhat.com> - vgabios-0.6b-3.3.el6
- vgabios-use-VBE-LFB-address-from-PCI-base-address-if-present.patch [bz#569473]
- vgabios-qxl-vgabios.patch [bz#569473]
- Resolves: bz#569473
  (spice: Need vgabios for qxl device)

* Wed Jan 13 2010 Eduardo Habkost <ehabkost@redhat.com> - vgabios-0.6b-3.2.el6
- Build only on x86_64
- Resolves: bz#554862
  (vgabios should not be shipped on i686/ppc64/s390x, only on x86_64)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.6b-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Glauber Costa <glommer@redhat.com> - 0.6b-2
- properly add the patch

* Fri Jun 19 2009 Glauber Costa <glommer@redhat.com> - 0.6b-1
- applied vgabios-provide-high-res.patch, that should fix #499060
- Changed versioning naming, since the "b" in 0.6b does not stand for beta.

* Mon Mar 02 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.5.b
- fixed naming to comply with guidelines.

* Tue Feb 17 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.4beta
- removed leftovers and fixed rpmlint errors.

* Mon Feb 16 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.3beta
- using dev86 to build directly on all arches, made package noarch.
  No more binaries \o/

* Fri Feb 13 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.2beta
- Addressing BZ 485418: added doc section, clean build root before
  we proceed, own vgabios directory
* Fri Feb 13 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.1beta
- Created initial package
