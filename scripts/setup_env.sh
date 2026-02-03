#!/usr/bin/env bash

# Ballpark environment bootstrapper (inspired by HAFiscal-Latest)
# Creates a platform/architecture-specific virtual environment that lives
# at .venv-${platform}-${arch} and installs dependencies via uv.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

detect_platform() {
    case "$(uname -s)" in
        Darwin) printf "darwin" ;;
        Linux) printf "linux" ;;
        *) printf "" ;;
    esac
}

detect_arch() {
    case "$(uname -s)" in
        Darwin)
            if sysctl -n hw.optional.arm64 2>/dev/null | grep -q 1; then
                printf "arm64"
            else
                printf "x86_64"
            fi
            ;;
        *)
            printf "%s" "$(uname -m)"
            ;;
    esac
}

ensure_uv_available() {
    if command -v uv >/dev/null 2>&1; then
        return 0
    fi

    echo "❌ uv is not installed."
    echo "Install uv first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "or:"
    echo "  brew install uv"
    exit 1
}

platform="$(detect_platform)"
arch="$(detect_arch)"

if [[ -z "$platform" || -z "$arch" ]]; then
    echo "Unsupported platform: $(uname -s)"
    exit 1
fi

VENV_DIR="$REPO_ROOT/.venv-${platform}-${arch}"

echo "Ballpark environment setup"
echo "Platform: $platform"
echo "Architecture: $arch"
echo "Environment directory: ${VENV_DIR/$REPO_ROOT\//}"
echo "----------------------------------------"

ensure_uv_available

# Ensure uv-managed Python 3.12 is present
if ! uv python list 2>/dev/null | grep -q "cpython-3.12"; then
    echo "Installing Python 3.12 via uv..."
    uv python install 3.12
fi

# Create venv if missing
if [[ ! -d "$VENV_DIR" ]]; then
    echo "Creating virtual environment..."
    uv venv --python 3.12 "$VENV_DIR"
fi

# Point uv at this environment and install deps
export UV_PROJECT_ENVIRONMENT="$VENV_DIR"

echo "Installing dependencies with uv..."
uv sync --python 3.12

cat <<EOF

✅ Environment ready!

To activate it in this shell:
  source ${VENV_DIR/$REPO_ROOT\//}/bin/activate

Once activated you can launch Jupyter Lab with:
  uv run jupyter lab

EOF
