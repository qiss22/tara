#!/bin/bash
# Build all components

set -e

echo "🔨 Building Taracol..."

# Build Rust workspace
echo "Building Rust services..."
cargo build --release

# Build TypeScript packages  
echo "Building TypeScript packages..."
cd packages/tara-api
npm run build
cd ../..

# Build web client
echo "Building web client..."
cd tara-client/web
npm run build
cd ../..

echo "✅ Build complete!"
