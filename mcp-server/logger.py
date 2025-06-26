"""
Logging configuration for Apple Docs MCP Server
"""

import logging
import sys
from config import LOG_LEVEL

def get_logger(name: str) -> logging.Logger:
    """Get a configured logger instance"""
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(getattr(logging, LOG_LEVEL))
    
    return logger