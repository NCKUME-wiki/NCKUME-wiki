#!/usr/bin/env bash

# dummy comment (only "chmod +x"ing it is not detectable to git hub? kindof)
set -e

DIRNAME="$(dirname -- "${BASH_SOURCE[0]}")"

chmod +x "$DIRNAME"/install-python.sh
source "$DIRNAME"/install-python.sh

# Install dependencies
pipenv install
yarn --frozen-lockfile --production

# Install themes and etc.
PREBUILD_NETLIFY=1 scripts/pre-build/pre-build.sh

pipenv run mkdocs build -v

# Post-build scripts
export NODE_OPTIONS="--max_old_space_size=3072"
node --loader ts-node/esm scripts/post-build/html-postprocess.ts commits-info math external-links
