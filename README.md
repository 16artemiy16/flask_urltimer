# flask_urltimer

A Flask extension for app endpoints execution time measurement.

## Config
The next configuration is available.

- **URLTIMER_URL_PATH** *(default="timings-ui")* - the url under which ui will be 
exposed
- **URLTIMER_STORAGE_ENGINE** *(default="txt")* (available: ['txt']) - points
how to store the data
- **URLTIMER_CLEANUP_ON_SHUTDOWN** (default=True) - if True the storage will be
cleared on each app shutdown 
