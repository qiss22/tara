#!/bin/bash
# Development environment setup

set -e

echo "🕷️  Setting up Taracol development environment..."

# Copy environment file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env file"
fi

# Start databases
echo "🐘 Starting databases..."
docker-compose up -d postgres redis

# Wait for postgres
echo "⏳ Waiting for PostgreSQL..."
sleep 5

# Run database migrations (when implemented)
# cargo run --bin migrate

# Build all services
echo "🔨 Building services..."
cargo build

echo "✅ Development environment ready!"
echo ""
echo "Next steps:"
echo "1. Run services: cargo run --bin identity-service"
echo "2. Run gateway: cargo run --bin gateway"
echo "3. Start web client: cd tara-client/web && npm run dev"
