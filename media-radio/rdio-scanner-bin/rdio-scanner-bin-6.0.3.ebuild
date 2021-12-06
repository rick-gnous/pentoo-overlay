# Copyright 1999-2021 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=8

DESCRIPTION="ingest and distribute audio files generated by various software-defined radio recorders"
HOMEPAGE="https://github.com/chuot/rdio-scanner"

SRC_URI="amd64? ( https://github.com/chuot/rdio-scanner/releases/download/v${PV}-beta/rdio-scanner-linux-amd64-v${PV}.zip )
		x86? ( https://github.com/chuot/rdio-scanner/releases/download/v${PV}-beta/rdio-scanner-linux-386-v${PV}.zip )
		arm? ( https://github.com/chuot/rdio-scanner/releases/download/v${PV}-beta/rdio-scanner-linux-arm-v${PV}.zip )
		arm64? ( https://github.com/chuot/rdio-scanner/releases/download/v${PV}-beta/rdio-scanner-linux-arm64-v${PV}.zip )"

LICENSE="GPL-3"
SLOT="0"
KEYWORDS="~amd64 ~arm ~arm64 ~x86"
S="${WORKDIR}"
QA_PREBUILD='opt/rdio-scanner-bin/rdio-scanner-bin'

src_install() {
	exeinto "/opt/${PN}"
	newexe rdio-scanner "${PN}"
	insinto "/usr/share/doc/${PN}-${PVR}"
	newins "rdio-scanner.pdf" "rdio-scanner-${PVF}.pdf"
}