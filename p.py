#!/usr/bin/env python3
"""
Taracol Project Scaffolding Script
Creates the full private workspace structure for Tarantula Protocol development.
"""

import os
import json
from pathlib import Path
from textwrap import dedent

class TaracolScaffolder:
    def __init__(self, project_name="taracol", base_dir=None):
        self.project_name = project_name
        self.base_dir = Path(base_dir) if base_dir else Path.cwd() / project_name
        
    def create_directory_structure(self):
        """Create the full directory structure"""
        directories = [
            # Root level
            "docs",
            
            # Protocol definitions (will be open sourced later)
            "protocol/lexicons/tara/identity",
            "protocol/lexicons/tara/web", 
            "protocol/lexicons/tara/migration",
            "protocol/lexicons/tara/feed",
            "protocol/lexicons/com.atproto/server",
            "protocol/lexicons/com.atproto/repo",
            "protocol/lexicons/com.atproto/sync",
            "protocol/specs",
            "protocol/reference-types",
            
            # Core implementation (hybrid - some will be open sourced)
            "core/taracol-types/src/identity",
            "core/taracol-types/src/web",
            "core/taracol-types/src/migration", 
            "core/taracol-types/src/crypto",
            "core/taracol-types/tests",
            "core/taracol-crypto/src",
            "core/taracol-crypto/tests",
            "core/taracol-protocol/src/transport",
            "core/taracol-protocol/src/federation",
            "core/taracol-protocol/src/storage",
            "core/taracol-protocol/tests",
            
            # Private microservices (business logic)
            "services/identity-service/src/handlers",
            "services/identity-service/src/storage",
            "services/identity-service/proto",
            "services/identity-service/migrations/postgresql",
            "services/web-service/src/handlers",
            "services/web-service/src/storage", 
            "services/web-service/proto",
            "services/web-service/migrations/postgresql",
            "services/relay-service/src/handlers",
            "services/relay-service/src/quic",
            "services/relay-service/proto",
            "services/pds-service/src/handlers",
            "services/pds-service/src/storage",
            "services/pds-service/proto",
            "services/ai-service/src/handlers",
            "services/ai-service/src/models",
            "services/ai-service/proto",
            "services/federation-service/src/handlers",
            "services/federation-service/src/quic",
            "services/federation-service/proto",
            
            # API Gateway
            "gateway/src/routes",
            "gateway/src/grpc_clients",
            "gateway/src/adapters",
            "gateway/src/lexicon_generator",
            "gateway/src/middleware",
            "gateway/config",
            
            # Client applications
            "tara-client/web/src/components",
            "tara-client/web/src/api",
            "tara-client/web/src/stores", 
            "tara-client/web/src/utils",
            "tara-client/web/public",
            "tara-client/mobile/ios",
            "tara-client/mobile/android",
            "tara-client/mobile/shared",
            "tara-client/desktop/src",
            
            # SDK packages
            "packages/tara-api/src/client",
            "packages/tara-api/src/lexicons/tara",
            "packages/tara-api/src/lexicons/atproto",
            "packages/tara-api/src/utils",
            "packages/tara-pro/src",
            "packages/migration-tools/src/importers",
            "packages/migration-tools/src/exporters",
            "packages/migration-tools/cli",
            
            # Development tools
            "tools/lexicon-codegen/src",
            "tools/benchmarks/src",
            "tools/monitoring/src",
            "tools/deployment/src",
            
            # Infrastructure
            "infrastructure/docker",
            "infrastructure/kubernetes/services",
            "infrastructure/kubernetes/ingress", 
            "infrastructure/kubernetes/monitoring",
            "infrastructure/terraform/aws",
            "infrastructure/terraform/gcp",
            "infrastructure/terraform/monitoring",
            
            # Business strategy (private)
            "business/market-research",
            "business/competitive-analysis",
            "business/monetization-experiments",
            "business/legal",
            "business/partnerships",
            
            # Examples and references
            "examples/basic-node/src",
            "examples/federation-demo/node1",
            "examples/federation-demo/node2", 
            "examples/migration-example/src",
            
            # Testing
            "tests/protocol-compliance",
            "tests/integration",
            "tests/performance",
            "tests/security",
            
            # Scripts and utilities
            "scripts",
        ]
        
        for directory in directories:
            (self.base_dir / directory).mkdir(parents=True, exist_ok=True)
            
    def create_workspace_cargo_toml(self):
        """Create the main workspace Cargo.toml"""
        content = '''[workspace]
resolver = "2"
members = [
    "core/taracol-types",
    "core/taracol-crypto",
    "core/taracol-protocol",
    "services/identity-service",
    "services/web-service",
    "services/relay-service",
    "services/pds-service", 
    "services/ai-service",
    "services/federation-service",
    "gateway",
    "tools/lexicon-codegen",
    "tools/benchmarks",
    "examples/basic-node",
]

[workspace.package]
version = "0.1.0"
edition = "2021"
license = "PROPRIETARY"
authors = ["Your Name <your.email@domain.com>"]

[workspace.dependencies]
# Core dependencies
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
tokio = { version = "1.0", features = ["full"] }
anyhow = "1.0"
uuid = { version = "1.0", features = ["v4"] }
chrono = { version = "0.4", features = ["serde"] }
tracing = "0.1"
tracing-subscriber = "0.3"

# Crypto
ed25519-dalek = "2.0"
bs58 = "0.5"
ring = "0.17"
rand = "0.8"

# Network
quinn = "0.10"
rustls = "0.21"
tonic = "0.10"
prost = "0.12"
axum = "0.7"
hyper = "0.14"
reqwest = { version = "0.11", features = ["json"] }

# Database
sqlx = { version = "0.7", features = ["postgres", "runtime-tokio-native-tls", "uuid", "chrono"] }
redis = { version = "0.24", features = ["tokio-comp"] }

# Utilities
clap = { version = "4.0", features = ["derive"] }
config = "0.13"
dotenv = "0.15"
'''
        
        with open(self.base_dir / "Cargo.toml", "w") as f:
            f.write(content)
            
    def create_core_crates(self):
        """Create the core crate files"""
        
        # taracol-types
        types_cargo = '''[package]
name = "taracol-types"
version.workspace = true
edition.workspace = true
license.workspace = true

[dependencies]
serde.workspace = true
serde_json.workspace = true
chrono.workspace = true
uuid.workspace = true
anyhow.workspace = true
'''
        with open(self.base_dir / "core/taracol-types/Cargo.toml", "w") as f:
            f.write(types_cargo)
            
        types_lib = '''//! Core types for the Taracol protocol

pub mod identity;
pub mod web;
pub mod migration;
pub mod crypto;
pub mod errors;

pub use identity::*;
pub use web::*;
pub use migration::*;
pub use errors::*;
'''
        with open(self.base_dir / "core/taracol-types/src/lib.rs", "w") as f:
            f.write(types_lib)
            
        # taracol-crypto
        crypto_cargo = '''[package]
name = "taracol-crypto"
version.workspace = true
edition.workspace = true
license.workspace = true

[dependencies]
ed25519-dalek.workspace = true
bs58.workspace = true
ring.workspace = true
rand.workspace = true
serde.workspace = true
anyhow.workspace = true
'''
        with open(self.base_dir / "core/taracol-crypto/Cargo.toml", "w") as f:
            f.write(crypto_cargo)
            
        crypto_lib = '''//! Cryptographic primitives for Taracol

pub mod signatures;
pub mod keys;
pub mod migration_proofs;

pub use signatures::*;
pub use keys::*;
'''
        with open(self.base_dir / "core/taracol-crypto/src/lib.rs", "w") as f:
            f.write(crypto_lib)
            
        # taracol-protocol
        protocol_cargo = '''[package]
name = "taracol-protocol"
version.workspace = true
edition.workspace = true
license.workspace = true

[dependencies]
taracol-types = { path = "../taracol-types" }
taracol-crypto = { path = "../taracol-crypto" }
quinn.workspace = true
rustls.workspace = true
tokio.workspace = true
serde.workspace = true
anyhow.workspace = true
tracing.workspace = true
'''
        with open(self.base_dir / "core/taracol-protocol/Cargo.toml", "w") as f:
            f.write(protocol_cargo)
            
        protocol_lib = '''//! Core Taracol protocol implementation

pub mod transport;
pub mod federation;  
pub mod storage;

pub use transport::*;
pub use federation::*;
'''
        with open(self.base_dir / "core/taracol-protocol/src/lib.rs", "w") as f:
            f.write(protocol_lib)
            
    def create_service_crates(self):
        """Create microservice crate files"""
        
        services = [
            ("identity-service", "Identity management and authentication"),
            ("web-service", "Post and thread management"), 
            ("relay-service", "Relay and data aggregation"),
            ("pds-service", "Personal Data Server"),
            ("ai-service", "AI features and recommendations"),
            ("federation-service", "Federation and node communication"),
        ]
        
        for service_name, description in services:
            service_cargo = f'''[package]
name = "{service_name}"
version.workspace = true
edition.workspace = true
license.workspace = true

[dependencies]
taracol-types = {{ path = "../../core/taracol-types" }}
taracol-crypto = {{ path = "../../core/taracol-crypto" }}
taracol-protocol = {{ path = "../../core/taracol-protocol" }}
tonic.workspace = true
prost.workspace = true
tokio.workspace = true
sqlx.workspace = true
serde.workspace = true
anyhow.workspace = true
tracing.workspace = true
uuid.workspace = true
config.workspace = true

[build-dependencies]
tonic-build = "0.10"
'''
            
            service_main = f'''//! {description}

use anyhow::Result;
use tracing::info;

#[tokio::main]
async fn main() -> Result<()> {{
    tracing_subscriber::init();
    
    info!("Starting {service_name}...");
    
    // TODO: Initialize service
    
    Ok(())
}}
'''
            
            service_lib = f'''//! {description}

pub mod handlers;
pub mod storage;
pub mod config;

pub use handlers::*;
'''
            
            build_rs = '''fn main() -> Result<(), Box<dyn std::error::Error>> {
    tonic_build::compile_protos("proto/service.proto")?;
    Ok(())
}
'''
            
            service_path = self.base_dir / "services" / service_name
            with open(service_path / "Cargo.toml", "w") as f:
                f.write(service_cargo)
            with open(service_path / "src/main.rs", "w") as f:
                f.write(service_main)
            with open(service_path / "src/lib.rs", "w") as f:
                f.write(service_lib)
            with open(service_path / "build.rs", "w") as f:
                f.write(build_rs)
                
    def create_gateway(self):
        """Create the API gateway"""
        
        gateway_cargo = '''[package]
name = "gateway"
version.workspace = true
edition.workspace = true
license.workspace = true

[dependencies]
taracol-types = { path = "../core/taracol-types" }
axum.workspace = true
tokio.workspace = true
tonic.workspace = true
serde.workspace = true
serde_json.workspace = true
anyhow.workspace = true
tracing.workspace = true
tower = "0.4"
tower-http = { version = "0.4", features = ["cors"] }
'''
        
        gateway_main = '''//! Taracol API Gateway
//! Provides REST API compatible with Bluesky while routing to internal gRPC services

use anyhow::Result;
use axum::{Router, routing::get};
use tracing::info;

#[tokio::main]
async fn main() -> Result<()> {
    tracing_subscriber::init();
    
    let app = Router::new()
        .route("/", get(|| async { "Taracol API Gateway" }));
        
    info!("Starting gateway on :3000");
    
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await?;
    axum::serve(listener, app).await?;
    
    Ok(())
}
'''
        
        gateway_lib = '''//! API Gateway library

pub mod routes;
pub mod grpc_clients;
pub mod adapters;
pub mod middleware;
pub mod lexicon_generator;

pub use routes::*;
'''
        
        gateway_path = self.base_dir / "gateway"
        with open(gateway_path / "Cargo.toml", "w") as f:
            f.write(gateway_cargo)
        with open(gateway_path / "src/main.rs", "w") as f:
            f.write(gateway_main)
        with open(gateway_path / "src/lib.rs", "w") as f:
            f.write(gateway_lib)
            
    def create_client_files(self):
        """Create client application files"""
        
        # Web client package.json
        web_package = {
            "name": "tara-web",
            "version": "0.1.0",
            "private": True,
            "dependencies": {
                "react": "^18.0.0",
                "react-dom": "^18.0.0",
                "@tara/api": "workspace:*"
            },
            "devDependencies": {
                "typescript": "^5.0.0",
                "@types/react": "^18.0.0",
                "@types/react-dom": "^18.0.0",
                "vite": "^5.0.0"
            },
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview"
            }
        }
        
        with open(self.base_dir / "tara-client/web/package.json", "w") as f:
            json.dump(web_package, f, indent=2)
            
        # Mobile React Native package.json
        mobile_package = {
            "name": "tara-mobile",
            "version": "0.1.0",
            "private": True,
            "dependencies": {
                "react-native": "^0.73.0",
                "@tara/api": "workspace:*"
            },
            "scripts": {
                "android": "react-native run-android",
                "ios": "react-native run-ios",
                "start": "react-native start"
            }
        }
        
        with open(self.base_dir / "tara-client/mobile/package.json", "w") as f:
            json.dump(mobile_package, f, indent=2)
            
    def create_sdk_packages(self):
        """Create SDK package files"""
        
        # @tara/api package.json
        api_package = {
            "name": "@tara/api",
            "version": "0.1.0",
            "description": "TypeScript client library for Taracol protocol",
            "main": "dist/index.js",
            "types": "dist/index.d.ts",
            "files": ["dist/"],
            "scripts": {
                "build": "tsc",
                "test": "jest",
                "generate": "node scripts/generate-from-lexicons.js"
            },
            "keywords": ["taracol", "tarantula", "decentralized", "social"],
            "license": "PROPRIETARY",
            "dependencies": {
                "axios": "^1.6.0"
            },
            "devDependencies": {
                "typescript": "^5.0.0",
                "@types/node": "^20.0.0",
                "jest": "^29.0.0"
            }
        }
        
        with open(self.base_dir / "packages/tara-api/package.json", "w") as f:
            json.dump(api_package, f, indent=2)
            
        # @tara/pro package.json
        pro_package = {
            "name": "@tara/pro",
            "version": "0.1.0",
            "description": "Premium features SDK for Taracol",
            "main": "dist/index.js",
            "types": "dist/index.d.ts",
            "license": "PROPRIETARY",
            "dependencies": {
                "@tara/api": "workspace:*"
            }
        }
        
        with open(self.base_dir / "packages/tara-pro/package.json", "w") as f:
            json.dump(pro_package, f, indent=2)
            
    def create_infrastructure_files(self):
        """Create infrastructure and deployment files"""
        
        # Docker compose for development
        docker_compose = '''version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: taracol_dev
      POSTGRES_USER: taracol
      POSTGRES_PASSWORD: development
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  gateway:
    build:
      context: .
      dockerfile: infrastructure/docker/gateway.Dockerfile
    ports:
      - "3000:3000"
    depends_on:
      - postgres
      - redis
      - identity-service
      - web-service

  identity-service:
    build:
      context: .
      dockerfile: infrastructure/docker/identity-service.Dockerfile
    depends_on:
      - postgres
      - redis
    environment:
      DATABASE_URL: postgresql://taracol:development@postgres/taracol_dev
      REDIS_URL: redis://redis

  web-service:
    build:
      context: .
      dockerfile: infrastructure/docker/web-service.Dockerfile  
    depends_on:
      - postgres
      - redis
    environment:
      DATABASE_URL: postgresql://taracol:development@postgres/taracol_dev
      REDIS_URL: redis://redis

volumes:
  postgres_data:
'''
        
        with open(self.base_dir / "docker-compose.yml", "w") as f:
            f.write(docker_compose)
            
        # Development environment file
        env_example = '''# Taracol Development Environment

# Database
DATABASE_URL=postgresql://taracol:development@localhost/taracol_dev
REDIS_URL=redis://localhost

# Services
IDENTITY_SERVICE_URL=http://localhost:50001
WEB_SERVICE_URL=http://localhost:50002
RELAY_SERVICE_URL=http://localhost:50003

# Gateway
GATEWAY_PORT=3000

# Logging
RUST_LOG=info
TRACING_SUBSCRIBER=pretty

# JWT
JWT_SECRET=your-jwt-secret-change-in-production

# External APIs (for later)
# OPENAI_API_KEY=
# AWS_ACCESS_KEY_ID=
# AWS_SECRET_ACCESS_KEY=
'''
        
        with open(self.base_dir / ".env.example", "w") as f:
            f.write(env_example)
            
    def create_scripts(self):
        """Create utility scripts"""
        
        # Development setup script
        dev_setup = '''#!/bin/bash
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
'''
        
        with open(self.base_dir / "scripts/setup-dev.sh", "w") as f:
            f.write(dev_setup)
        os.chmod(self.base_dir / "scripts/setup-dev.sh", 0o755)
        
        # Build script
        build_script = '''#!/bin/bash
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
'''
        
        with open(self.base_dir / "scripts/build.sh", "w") as f:
            f.write(build_script)
        os.chmod(self.base_dir / "scripts/build.sh", 0o755)
        
    def create_gitignore(self):
        """Create comprehensive .gitignore"""
        
        gitignore_content = '''# Rust
/target
**/*.rs.bk
Cargo.lock

# Node.js
node_modules/
.npm/
.pnpm-store/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment files
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Logs
logs/
*.log

# Database
*.db
*.sqlite
*.db-journal

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Build outputs
dist/
build/
*.tgz
*.tar.gz

# Coverage
coverage/
*.lcov

# Docker
.dockerignore
docker-compose.override.yml

# Terraform
*.tfstate
*.tfstate.*
.terraform/
.terraform.lock.hcl

# Secrets
secrets/
*.key
*.pem
*.crt
*.p12
*.pfx

# Business sensitive
business/contracts/
business/financials/
business/partnerships/*.pdf
business/partnerships/*.docx

# Generated code
**/*_pb.rs
**/*_pb.js
**/*_pb.ts

# Temporary files
*.tmp
*.temp
.cache/
'''
        
        with open(self.base_dir / ".gitignore", "w") as f:
            f.write(gitignore_content)
            
    def create_root_files(self):
        """Create root project files"""
        
        # Root package.json for workspace
        root_package = {
            "name": "taracol-workspace",
            "private": True,
            "workspaces": [
                "packages/*",
                "tara-client/*"
            ],
            "scripts": {
                "build": "./scripts/build.sh",
                "dev": "./scripts/setup-dev.sh",
                "test": "cargo test && npm run test --workspaces"
            },
            "devDependencies": {
                "concurrently": "^8.0.0"
            }
        }
        
        with open(self.base_dir / "package.json", "w") as f:
            json.dump(root_package, f, indent=2)
            
        # Simple README
        readme = '''# Taracol - Tarantula Protocol Implementation

🕷️ Private workspace for Tarantula Protocol development.

## Quick Start

```bash
# Setup development environment
./scripts/setup-dev.sh

# Build everything
./scripts/build.sh

# Run services
cargo run --bin gateway
```

## Architecture

- `core/` - Core protocol implementation
- `services/` - Microservices (gRPC)
- `gateway/` - REST API gateway  
- `tara-client/` - Client applications
- `packages/` - SDK packages

## Development

See individual service README files for specific instructions.
'''
        
        with open(self.base_dir / "README.md", "w") as f:
            f.write(readme)
            
    def create_placeholder_files(self):
        """Create placeholder files to maintain directory structure"""
        
        placeholder_files = [
            "core/taracol-types/src/identity.rs",
            "core/taracol-types/src/web.rs", 
            "core/taracol-types/src/migration.rs",
            "core/taracol-types/src/crypto.rs",
            "core/taracol-types/src/errors.rs",
            "core/taracol-crypto/src/signatures.rs",
            "core/taracol-crypto/src/keys.rs",
            "core/taracol-crypto/src/migration_proofs.rs",
            "core/taracol-protocol/src/transport.rs",
            "core/taracol-protocol/src/federation.rs",
            "core/taracol-protocol/src/storage.rs",
            "gateway/src/routes.rs",
            "gateway/src/grpc_clients.rs",
            "gateway/src/adapters.rs",
            "gateway/src/middleware.rs",
            "gateway/src/lexicon_generator.rs",
        ]
        
        for file_path in placeholder_files:
            full_path = self.base_dir / file_path
            if not full_path.exists():
                with open(full_path, "w") as f:
                    f.write("// TODO: Implement\n")
                    
        # Create handler and storage modules for services
        services = ["identity-service", "web-service", "relay-service", "pds-service", "ai-service", "federation-service"]
        for service in services:
            handler_file = self.base_dir / "services" / service / "src" / "handlers.rs"
            storage_file = self.base_dir / "services" / service / "src" / "storage.rs"
            config_file = self.base_dir / "services" / service / "src" / "config.rs"
            
            with open(handler_file, "w") as f:
                f.write("// TODO: Implement service handlers\n")
            with open(storage_file, "w") as f:
                f.write("// TODO: Implement storage layer\n")  
            with open(config_file, "w") as f:
                f.write("// TODO: Implement configuration\n")
                
    def scaffold(self):
        """Run the complete scaffolding process"""
        
        print(f"🕷️  Scaffolding Taracol project at {self.base_dir}")
        
        # Create base directory
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        print("📁 Creating directory structure...")
        self.create_directory_structure()
        
        print("📦 Creating workspace configuration...")
        self.create_workspace_cargo_toml()
        
        print("🦀 Creating core crates...")
        self.create_core_crates()
        
        print("🔧 Creating microservices...")
        self.create_service_crates()
        
        print("🌐 Creating API gateway...")
        self.create_gateway()
        
        print("💻 Creating client files...")
        self.create_client_files()
        
        print("📚 Creating SDK packages...")
        self.create_sdk_packages()
        
        print("🐳 Creating infrastructure files...")
        self.create_infrastructure_files()
        
        print("📜 Creating utility scripts...")
        self.create_scripts()
        
        print("🚫 Creating .gitignore...")
        self.create_gitignore()
        
        print("📄 Creating root files...")
        self.create_root_files()
        
        print("📝 Creating placeholder files...")
        self.create_placeholder_files()
        
        print(f"✅ Taracol project scaffolded successfully!")
        print(f"📍 Project location: {self.base_dir}")
        print(f"🚀 Next steps:")
        print(f"   1. cd {self.base_dir}")
        print(f"   2. ./scripts/setup-dev.sh")
        print(f"   3. Start building! 🕷️")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Scaffold Taracol project structure")
    parser.add_argument("--name", default="taracol", help="Project name")
    parser.add_argument("--dir", help="Base directory (default: current dir)")
    
    args = parser.parse_args()
    
    scaffolder = TaracolScaffolder(args.name, args.dir)
    scaffolder.scaffold()

if __name__ == "__main__":
    main()
