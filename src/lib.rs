use adblock::engine::Engine;
use adblock::lists::FilterFormat;
use pyo3::prelude::*;

/// Adblocker class
/// Hold the adblocker engine loaded with the rules
///
/// input:
///     rules: List[str] -> list of strings that represent the rules to be applied
///
/// example:
///     braveblock.Adblocker(
///         rules=[
///             "-advertisement-icon.",
///             "-advertisement/script.",
///         ]
///     )
#[pyclass]
#[text_signature = "(rules, /)"]
struct Adblocker {
    engine: Engine,
}

#[pymethods]
impl Adblocker {
    #[new]
    fn new(rules: Vec<String>) -> Self {
        Adblocker { engine: Engine::from_rules(&rules, FilterFormat::Standard) }
    }

    /// The function that should tell whether a specific request should be blocked according to the loaded rules
    ///
    /// input:
    ///     url: str -> The inspected url that should be tested
    ///     source_url: str -> The source url that made the request to the inspected url
    ///     request_type: str -> The type of the resource that is being requested. Can be one of the following:
    ///         "beacon", "csp_report", "document", "font", "image", "imageset", "main_frame",
    ///         "media", "object_subrequest", "object", "other", "ping", "script", "speculative",
    ///         "stylesheet", "sub_frame", "subdocument", "web_manifest", "websocket", "xbl",
    ///         "xhr", "xml_dtd", "xmlhttprequest", "xslt"
    ///
    /// returns:
    ///     bool -> Whether the request should be blocked or not
    ///
    /// example:
    ///     adblocker.check_network_urls(
    ///         url="http://example.com/-advertisement-icon.",
    ///         source_url="http://example.com/helloworld",
    ///         request_type="image",
    ///     )
    #[text_signature = "(url, source_url, request_type, /)"]
    fn check_network_urls(
        &mut self,
        url: &str,
        source_url: &str,
        request_type: &str,
    ) -> PyResult<bool> {
        let blocker_result = self.engine.check_network_urls(
            url,
            source_url,
            request_type
        );

        Ok(blocker_result.matched)
    }
}

/// Braveblock is a python library that implemented an adblocker based on Brave's browser adblocker written in Rust
/// This library is a bindings for the original adblocker written by Brave's team
/// Original code can be found here https://github.com/brave/adblock-rust
#[pymodule]
fn braveblock(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Adblocker>()?;

    Ok(())
}
