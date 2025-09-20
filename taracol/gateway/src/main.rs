//! Taracol API Gateway
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
