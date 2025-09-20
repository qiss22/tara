//! Personal Data Server

use anyhow::Result;
use tracing::info;

#[tokio::main]
async fn main() -> Result<()> {
    tracing_subscriber::init();
    
    info!("Starting pds-service...");
    
    // TODO: Initialize service
    
    Ok(())
}
