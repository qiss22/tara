//! Post and thread management

use anyhow::Result;
use tracing::info;

#[tokio::main]
async fn main() -> Result<()> {
    tracing_subscriber::init();
    
    info!("Starting web-service...");
    
    // TODO: Initialize service
    
    Ok(())
}
