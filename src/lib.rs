use pyo3::prelude::*;

#[pyfunction]
fn example_function(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pymodule]
fn _internal(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(example_function, m)?)?;
    Ok(())
}
