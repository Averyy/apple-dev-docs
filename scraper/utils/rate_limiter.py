"""Rate limiting utilities for polite web scraping."""

import asyncio
import random
import time
from typing import Optional

from scraper.utils.logger import get_logger

logger = get_logger(__name__)


class RateLimiter:
    """Async rate limiter with randomized delays."""
    
    def __init__(
        self, 
        requests_per_second: float = 0.5,
        randomize_delay: bool = True,
        min_delay: Optional[float] = None,
        max_delay: Optional[float] = None
    ) -> None:
        """Initialize rate limiter.
        
        Args:
            requests_per_second: Maximum requests per second
            randomize_delay: Whether to add random jitter to delays
            min_delay: Minimum delay between requests (overrides requests_per_second)
            max_delay: Maximum delay between requests (for randomization)
        """
        self.min_interval = 1.0 / requests_per_second
        self.randomize_delay = randomize_delay
        self.min_delay = min_delay or self.min_interval
        self.max_delay = max_delay or (self.min_delay * 1.5)
        self.last_request_time = 0.0
        self._lock = asyncio.Lock()
        
        logger.info(
            "rate_limiter_initialized",
            min_delay=self.min_delay,
            max_delay=self.max_delay,
            randomize=self.randomize_delay
        )
    
    async def acquire(self) -> None:
        """Wait if necessary to maintain rate limit."""
        async with self._lock:
            current_time = time.time()
            elapsed = current_time - self.last_request_time
            
            # Calculate required delay
            if self.randomize_delay:
                required_delay = random.uniform(self.min_delay, self.max_delay)
            else:
                required_delay = self.min_delay
            
            if elapsed < required_delay:
                wait_time = required_delay - elapsed
                logger.debug("rate_limit_wait", wait_time=f"{wait_time:.2f}s")
                await asyncio.sleep(wait_time)
            
            self.last_request_time = time.time()
    
    def reset(self) -> None:
        """Reset the rate limiter."""
        self.last_request_time = 0.0
        logger.debug("rate_limiter_reset")


class AdaptiveRateLimiter(RateLimiter):
    """Rate limiter that adapts based on response times and errors."""
    
    def __init__(
        self,
        initial_delay: float = 0.2,
        min_delay: float = 0.1,
        max_delay: float = 10.0,
        success_decrease_factor: float = 0.9,
        error_increase_factor: float = 2.0,
        slow_response_threshold: float = 5.0
    ) -> None:
        """Initialize adaptive rate limiter.
        
        Args:
            initial_delay: Starting delay between requests
            min_delay: Minimum allowed delay
            max_delay: Maximum allowed delay
            success_decrease_factor: Factor to decrease delay on success
            error_increase_factor: Factor to increase delay on error
            slow_response_threshold: Response time to consider "slow"
        """
        super().__init__(requests_per_second=1/initial_delay, randomize_delay=True)
        self.current_delay = initial_delay
        self.min_delay_limit = min_delay
        self.max_delay_limit = max_delay
        self.success_decrease_factor = success_decrease_factor
        self.error_increase_factor = error_increase_factor
        self.slow_response_threshold = slow_response_threshold
        
        # Update parent class delays
        self.min_delay = self.current_delay
        self.max_delay = self.current_delay * 1.5
    
    def record_success(self, response_time: float) -> None:
        """Record a successful request and adjust delay.
        
        Args:
            response_time: Time taken for the request
        """
        if response_time > self.slow_response_threshold:
            # Server is slow, don't decrease delay
            logger.debug(
                "slow_response_detected",
                response_time=f"{response_time:.2f}s",
                current_delay=f"{self.current_delay:.2f}s"
            )
        else:
            # Decrease delay on success
            self.current_delay = max(
                self.min_delay_limit,
                self.current_delay * self.success_decrease_factor
            )
            self._update_delays()
            logger.debug(
                "rate_limit_decreased",
                new_delay=f"{self.current_delay:.2f}s",
                response_time=f"{response_time:.2f}s"
            )
    
    def record_error(self, error_type: str = "unknown") -> None:
        """Record an error and increase delay.
        
        Args:
            error_type: Type of error encountered
        """
        self.current_delay = min(
            self.max_delay_limit,
            self.current_delay * self.error_increase_factor
        )
        self._update_delays()
        logger.warning(
            "rate_limit_increased",
            new_delay=f"{self.current_delay:.2f}s",
            error_type=error_type
        )
    
    def _update_delays(self) -> None:
        """Update internal delay values."""
        self.min_delay = self.current_delay
        self.max_delay = min(self.current_delay * 1.5, self.max_delay_limit)