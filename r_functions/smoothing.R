# Moving Average Smoothing
moving_average <- function(series, window) {
  # series: numeric vector
  # window: integer, size of moving window
  if(window < 1) stop("Window size must be at least 1")
  
  # Use stats::filter for simple moving average
  ma <- stats::filter(series, rep(1/window, window), sides = 2)
  return(as.numeric(ma))
}

# Exponential Smoothing
exponential_smoothing <- function(series, alpha = 0.3) {
  # series: numeric vector
  # alpha: smoothing factor (0 < alpha <= 1)
  if(alpha <= 0 | alpha > 1) stop("Alpha must be between 0 and 1")
  
  smoothed <- numeric(length(series))
  smoothed[1] <- series[1] # initialize first value
  
  for(i in 2:length(series)) {
    smoothed[i] <- alpha * series[i] + (1 - alpha) * smoothed[i-1]
  }
  
  return(smoothed)
}