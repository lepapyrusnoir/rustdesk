# arg 1:  the new package version
#pre_install() {
#}

# arg 1:  the new package version
post_install() {
	# do something here
	cp /usr/share/lepapyrusnoir/files/rustdesk.service /etc/systemd/system/lepapyrusnoir.service
	cp /usr/share/lepapyrusnoir/files/rustdesk.desktop /usr/share/applications/lepapyrusnoir.desktop
	cp /usr/share/lepapyrusnoir/files/rustdesk-link.desktop /usr/share/applications/lepapyrusnoir-link.desktop
	systemctl daemon-reload
	systemctl enable lepapyrusnoir
	systemctl start lepapyrusnoir
	update-desktop-database
}

# arg 1:  the new package version
# arg 2:  the old package version
pre_upgrade() {
    systemctl stop lepapyrusnoir || true
}

# arg 1:  the new package version
# arg 2:  the old package version
post_upgrade() {
	cp /usr/share/lepapyrusnoir/files/rustdesk.service /etc/systemd/system/lepapyrusnoir.service
	cp /usr/share/lepapyrusnoir/files/rustdesk.desktop /usr/share/applications/lepapyrusnoir.desktop
	cp /usr/share/lepapyrusnoir/files/rustdesk-link.desktop /usr/share/applications/lepapyrusnoir-link.desktop
	systemctl daemon-reload
	systemctl enable lepapyrusnoir
	systemctl start lepapyrusnoir
	update-desktop-database
}

# arg 1:  the old package version
pre_remove() {
	systemctl stop lepapyrusnoir || true
	systemctl disable lepapyrusnoir || true
	rm /etc/systemd/system/lepapyrusnoir.service || true
}

# arg 1:  the old package version
post_remove() {
	rm /usr/share/applications/lepapyrusnoir.desktop || true
	rm /usr/share/applications/lepapyrusnoir-link.desktop || true
	update-desktop-database
}
