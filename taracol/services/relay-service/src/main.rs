//! Relay and data aggregation

use anyhow::Result;
use tracing::info;

#[tokio::main]
async fn main() -> Result<()> {
    tracing_subscriber::init();
    
    info!("Starting relay-service...");
    
    // TODO: Initialize service
    
    Ok(())
}
