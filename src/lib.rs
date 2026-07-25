use adblock::lists::ParseOptions;
use adblock::request::Request;
use adblock::{Engine, FilterSet};
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
struct Adblocker {
    engine: Engine,
}

#[pymethods]
impl Adblocker {
    #[new]
    fn new(rules: Vec<String>) -> Self {
        // Build a FilterSet and hand it to `Engine::from_filter_set`. The `true`
        // args enable debug info (so the engine can report which filter matched)
        // and optimization, respectively.
        let mut filter_set = FilterSet::new(true);
        filter_set.add_filters(&rules, ParseOptions::default());

        Adblocker { engine: Engine::from_filter_set(filter_set, true) }
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
    ///         source_url="http://example.com/",
    ///         request_type="image",
    ///     )
    fn check_network_urls(
        &mut self,
        url: &str,
        source_url: &str,
        request_type: &str,
    ) -> bool {
        // adblock 0.7 replaced `Engine::check_network_urls` with
        // `check_network_request`, which takes a pre-parsed `Request`. Building
        // the request can fail on a malformed url; treat that as "not blocked",
        // matching the old behaviour where unparseable urls never matched.
        let request = match Request::new(url, source_url, request_type) {
            Ok(request) => request,
            Err(_) => return false,
        };

        self.engine.check_network_request(&request).matched
    }
}

/// Braveblock is a python library that implemented an adblocker based on Brave's browser adblocker written in Rust
/// This library is a bindings for the original adblocker written by Brave's team
/// Original code can be found here https://github.com/brave/adblock-rust
#[pymodule]
fn braveblock(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Adblocker>()?;

    Ok(())
}
