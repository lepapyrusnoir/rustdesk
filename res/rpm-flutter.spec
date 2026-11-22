Name:       lepapyrusnoir
Version:    1.5.3
Release:    0
Summary:    RPM package for Studio Le Papyrus Noir
License:    GPL-3.0
URL:        https://www.lepapyrusnoir.com/
Vendor:     Studio Le Papyrus Noir <lepapyrusnoir@gmail.com>
Requires:   gtk3 libxcb libXfixes alsa-lib libva gstreamer1-plugins-base
Recommends: libayatana-appindicator3-1 libxdo
Provides:   libdesktop_drop_plugin.so()(64bit), libdesktop_multi_window_plugin.so()(64bit), libfile_selector_linux_plugin.so()(64bit), libflutter_custom_cursor_plugin.so()(64bit), libflutter_linux_gtk.so()(64bit), libscreen_retriever_plugin.so()(64bit), libtray_manager_plugin.so()(64bit), liburl_launcher_linux_plugin.so()(64bit), libwindow_manager_plugin.so()(64bit), libwindow_size_plugin.so()(64bit), libtexture_rgba_renderer_plugin.so()(64bit)

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
Version configurée et packagée pour Studio Le Papyrus Noir (basée sur RustDesk sous licence GPL-3.0).

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

# %global __python %{__python3}

%install

mkdir -p "%{buildroot}/usr/share/lepapyrusnoir" && cp -r ${HBB}/flutter/build/linux/x64/release/bundle/* -t "%{buildroot}/usr/share/lepapyrusnoir"
mkdir -p "%{buildroot}/usr/bin"
install -Dm 644 $HBB/res/rustdesk.service -t "%{buildroot}/usr/share/lepapyrusnoir/files"
install -Dm 644 $HBB/res/rustdesk.desktop -t "%{buildroot}/usr/share/lepapyrusnoir/files"
install -Dm 644 $HBB/res/rustdesk-link.desktop -t "%{buildroot}/usr/share/lepapyrusnoir/files"
install -Dm 644 $HBB/res/128x128@2x.png "%{buildroot}/usr/share/icons/hicolor/256x256/apps/lepapyrusnoir.png"
install -Dm 644 $HBB/res/scalable.svg "%{buildroot}/usr/share/icons/hicolor/scalable/apps/lepapyrusnoir.svg"

%files
/usr/share/lepapyrusnoir/*
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
ln -sf /usr/share/lepapyrusnoir/lepapyrusnoir /usr/bin/lepapyrusnoir
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
    rm /usr/bin/lepapyrusnoir || true
    rmdir /usr/lib/lepapyrusnoir || true
    rmdir /usr/local/lepapyrusnoir || true
    rmdir /usr/share/lepapyrusnoir || true
    rm /usr/share/applications/lepapyrusnoir.desktop || true
    rm /usr/share/applications/lepapyrusnoir-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
    rmdir /usr/lib/lepapyrusnoir || true
    rmdir /usr/local/lepapyrusnoir || true
  ;;
esac
