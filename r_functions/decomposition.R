
# Convert numeric vector to ts object (helper)
to_ts <- function(series, frequency) {
  ts(series, frequency = frequency)
}

# Multiplicative decomposition - trend component
get_trend <- function(series, frequency) {
  ts_series <- to_ts(series, frequency)
  decomposed <- decompose(ts_series, type = "multiplicative")
  return(decomposed$trend)
}

# Multiplicative decomposition - seasonal component
get_seasonal <- function(series, frequency) {
  ts_series <- to_ts(series, frequency)
  decomposed <- decompose(ts_series, type = "multiplicative")
  return(decomposed$seasonal)
}

# Multiplicative decomposition - residual component
get_residual <- function(series, frequency) {
  ts_series <- to_ts(series, frequency)
  decomposed <- decompose(ts_series, type = "multiplicative")
  return(decomposed$random)
}