Name:       lepapyrusnoir
Version:    1.1.9
Release:    0
Summary:    RPM package for Studio Le Papyrus Noir
License:    GPL-3.0
Requires:   gtk3 libxcb1 libXfixes3 alsa-utils libXtst6 libva2 gstreamer-plugins-base gstreamer-plugin-pipewire
Recommends: libayatana-appindicator3-1 xdotool

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
Solution de bureau à distance développée pour Studio Le Papyrus Noir.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%global __python %{__python3}

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/lepapyrusnoir/
mkdir -p %{buildroot}/usr/share/lepapyrusnoir/files/
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -m 755 $HBB/target/release/lepapyrusnoir %{buildroot}/usr/bin/lepapyrusnoir
install $HBB/libsciter-gtk.so %{buildroot}/usr/share/lepapyrusnoir/libsciter-gtk.so
install $HBB/res/rustdesk.service %{buildroot}/usr/share/lepapyrusnoir/files/
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/lepapyrusnoir.png
install $HBB/res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/lepapyrusnoir.svg
install $HBB/res/rustdesk.desktop %{buildroot}/usr/share/lepapyrusnoir/files/
install $HBB/res/rustdesk-link.desktop %{buildroot}/usr/share/lepapyrusnoir/files/

%files
/usr/bin/lepapyrusnoir
/usr/share/lepapyrusnoir/libsciter-gtk.so
/usr/share/lepapyrusnoir/files/rustdesk.service
/usr/share/icons/hicolor/256x256/apps/lepapyrusnoir.png
/usr/share/icons/hicolor/scalable/apps/lepapyrusnoir.svg
/usr/share/lepapyrusnoir/files/rustdesk.desktop
/usr/share/lepapyrusnoir/files/rustdesk-link.desktop

%changelog
# let's skip this for now

%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop lepapyrusnoir || true
  ;;
esac

%post
cp /usr/share/lepapyrusnoir/files/rustdesk.service /etc/systemd/system/lepapyrusnoir.service
cp /usr/share/lepapyrusnoir/files/rustdesk.desktop /usr/share/applications/lepapyrusnoir.desktop
cp /usr/share/lepapyrusnoir/files/rustdesk-link.desktop /usr/share/applications/lepapyrusnoir-link.desktop
systemctl daemon-reload
systemctl enable lepapyrusnoir
systemctl start lepapyrusnoir
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop lepapyrusnoir || true
    systemctl disable lepapyrusnoir || true
    rm /etc/systemd/system/lepapyrusnoir.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/share/applications/lepapyrusnoir.desktop || true
    rm /usr/share/applications/lepapyrusnoir-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac
