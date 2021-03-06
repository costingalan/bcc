#!/bin/bash

set -x
set -e

PARALLEL=${PARALLEL:-1}
TMP=$(mktemp -d /tmp/debuild.XXXXXX)

function cleanup() {
  [[ -d $TMP ]] && rm -rf $TMP
}
trap cleanup EXIT

mkdir $TMP/bcc
cp -a * $TMP/bcc
pushd $TMP
tar zcf bcc_0.1.7.orig.tar.gz bcc/
cd bcc
DEB_BUILD_OPTIONS="nocheck parallel=${PARALLEL}" debuild -us -uc
popd

cp $TMP/*.deb .
