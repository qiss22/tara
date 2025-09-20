//! API Gateway library

pub mod routes;
pub mod grpc_clients;
pub mod adapters;
pub mod middleware;
pub mod lexicon_generator;

pub use routes::*;
