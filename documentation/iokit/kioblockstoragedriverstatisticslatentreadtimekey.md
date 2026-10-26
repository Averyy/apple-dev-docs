# kIOBlockStorageDriverStatisticsLatentReadTimeKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Describes the number of nanoseconds of latency during reads since the block storage driver was instantiated.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define kIOBlockStorageDriverStatisticsLatentReadTimeKey
```

#### Discussion

This property describes the number of nanoseconds of latency during reads since the block storage driver was instantiated. It is one of the statistic entries listed under the top-level kIOBlockStorageDriverStatisticsKey property table. It has an OSNumber value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kioblockstoragedriverstatisticslatentreadtimekey)*