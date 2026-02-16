import logging
from typing import Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class DataProcessor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.data_sources = config["data_sources"]
        self.cache = {}
        
    def fetch_data(self) -> Dict[str, Any]:
        """Fetches raw data from configured sources."""
        try:
            data = {}
            for source in self.data_sources:
                # Simulated API call
                response = self._make_api_request(source)
                
                if not response:
                    logger.error(f"Failed to fetch data from {source['name']}")
                    continue
                
                data[source["name"]] = response
            return data
        except Exception as e:
            logger.error(f"Data fetching failed: {str(e)}")
            raise DataFetchingError("Unable to fetch required data")

    def _make_api_request(self, source: Dict[str, str]) -> Dict[str, Any]:
        """Makes API requests with retry logic and logging."""
        attempts = 3
        for attempt in range(attempts):
            try:
                # Simulated API call
                response = {"status": "success", "data": {"metrics": {}}}
                return response
            except Exception as e:
                logger.warning(f"API request failed (attempt {attempt + 1}/{attempts}): {str(e)}")
        return None

    def process_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Processes and transforms raw data into a usable format."""
        processed = {}
        
        for source in self.data_sources:
            if source["name"] not in raw_data:
                logger.warning(f"Missing data from {source['name']}")
                continue
                
            # Simulated transformation
            transformed = {
                "metrics": {"revenue": 100, "expenses": 50},
                "timestamp": datetime.now().isoformat()
            }
            
            processed[source["name"]] = transformed
            
        return processed

    def cache_data(self, data: Dict[str, Any]) -> None:
        """Caches processed data for future use."""
        self.cache = data