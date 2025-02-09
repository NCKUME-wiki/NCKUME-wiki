#!/usr/bin/env bash
# This script needs to be "source"-d since it sets LD_LIBRARY_PATH and PATH

# Since we don't have root access on netlify, we could only install Python in current user's env
# This script installs Python binary from PPA and Pipenv, with APT prefix
PYTHON_VERSION="3.10"

APT_PACKAGES=(
  "python$PYTHON_VERSION"
  "python$PYTHON_VERSION-distutils"
)

APT_PREFIX="$HOME/.apt_prefix"
APT_PREFIX_MAKE_DIRS=(
  /etc/apt
  /usr/lib
  /var/lib/dpkg
  /var/lib/dpkg/triggers
  /var/lib/dpkg/alternatives
  /var/lib/dpkg/info
  /var/lib/dpkg/parts
  /var/lib/dpkg/updates
  /var/lib/apt/lists/partial
  /var/cache/apt/archives/partial
  /var/log/apt
)
#  manually exclude trigger file...
APT_PREFIX_COPY_DIRS=(
  /etc/apt
  # /var/lib/dpkg
  /var/lib/dpkg/alternatives
  /var/lib/dpkg/info
  /var/lib/dpkg/parts
  /var/lib/dpkg/updates

)
APT_PREFIX_COPY_FILES=(
  /var/lib/dpkg/available
  /var/lib/dpkg/cmethopt
  /var/lib/dpkg/diversions
  /var/lib/dpkg/diversions-old
  /var/lib/dpkg/lock
  /var/lib/dpkg/lock-frontend
  /var/lib/dpkg/statoverride
  /var/lib/dpkg/statoverride-old
  /var/lib/dpkg/status
  /var/lib/dpkg/status-old
# 
  /var/lib/dpkg/triggers/File
  /var/lib/dpkg/triggers/Unincorp
  /var/lib/dpkg/triggers/aspell-autobuildhash
  /var/lib/dpkg/triggers/ispell-autobuildhash
  /var/lib/dpkg/triggers/ldconfig
  /var/lib/dpkg/triggers/lib32
  /var/lib/dpkg/triggers/libo32
  /var/lib/dpkg/triggers/libx32
  /var/lib/dpkg/triggers/update-ca-certificates
  /var/lib/dpkg/triggers/update-ca-certificates-fresh
  /var/lib/dpkg/triggers/update-ca-certificates-java
  /var/lib/dpkg/triggers/update-ca-certificates-java-fresh
  /var/lib/dpkg/triggers/update-default-ispell
  /var/lib/dpkg/triggers/update-default-wordlist
  /var/lib/dpkg/triggers/update-sgmlcatalog
)
APT_PREFIX_LD_LIBRARY_PATHS=(
  /lib
  /lib/x86_64-linux-gnu
  /usr/lib
  /usr/lib/x86_64-linux-gnu
)
APT_PREFIX_PATHS=(
  /usr/local/bin
  /usr/bin
  /bin
)

# npm install netlify-cli
for DIR in "${APT_PREFIX_MAKE_DIRS[@]}"; do mkdir -p "$APT_PREFIX$DIR"; done
# for DIR in "${APT_PREFIX_COPY_DIRS[@]}"; do cp -r "$DIR/." "$APT_PREFIX$DIR/" || true; done
# for DIR in "${APT_PREFIX_COPY_FILES[@]}"; do cp -r "$DIR" "$APT_PREFIX$DIR" || true; done
  # rsync -av --exclude="./triggers/Lock" "$DIR/." "$APT_PREFIX$DIR/" || true
  # cp -r --exclude='triggers/Lock' "$DIR/." "$APT_PREFIX$DIR/" || true
for DIR in "${APT_PREFIX_COPY_DIRS[@]}"; do rsync -av "$DIR/." "$APT_PREFIX$DIR/" || true; done
for DIR in "${APT_PREFIX_COPY_FILES[@]}"; do rsync -av "$DIR" "$APT_PREFIX$DIR" || true; done
echo "copy done"
# cat /etc/apt/sources.list :
# Ubuntu sources have moved to the /etc/apt/sources.list.d/ubuntu.sources
# file, which uses the deb822 format. Use deb822-formatted .sources files
# to manage package sources in the /etc/apt/sources.list.d/ directory.
# See the sources.list(5) manual page for details.
cat /etc/apt/sources.list.d/ubuntu.sources | grep 'ubuntu\.com' > "$APT_PREFIX/etc/apt/sources.list.d/ubuntu.sources"
echo "cat done"
rm -rf "$APT_PREFIX/etc/apt/sources.list.d"/*
echo "rm done"

# Download packages from PPA deadsnakes/ppa
UBUNTU_CODENAME="$(source /etc/os-release && echo "$UBUNTU_CODENAME")"
echo "deb [trusted=yes] https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu $UBUNTU_CODENAME main" > "$APT_PREFIX"/etc/apt/sources.list.d/python.list
apt-get -o "Dir=$APT_PREFIX" -o Debug::NoLocking=1 update
apt-get -o "Dir=$APT_PREFIX" -o Debug::NoLocking=1 install -y --download-only "${APT_PACKAGES[@]}"

# Install (extract) packages
for PACKAGE in "$APT_PREFIX"/var/cache/apt/archives/*.deb; do dpkg -x "$PACKAGE" "$APT_PREFIX"; done

# Append LD_LIBRARY_PATH and PATH (after current)
for LIBPATH in "${APT_PREFIX_LD_LIBRARY_PATHS[@]}"; do export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$APT_PREFIX$LIBPATH"; done
for BINPATH in "${APT_PREFIX_PATHS[@]}"; do export PATH="$PATH:$APT_PREFIX$BINPATH"; done

# Install Pipenv
pip install pipenv