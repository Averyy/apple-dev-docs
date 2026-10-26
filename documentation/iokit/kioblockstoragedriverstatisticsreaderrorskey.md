# kIOBlockStorageDriverStatisticsReadErrorsKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Describes the number of read errors encountered since the block storage driver was instantiated.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define kIOBlockStorageDriverStatisticsReadErrorsKey
```

#### Discussion

This property describes the number of read errors encountered since the block storage driver was instantiated. It is one of the statistic entries listed under the top-level kIOBlockStorageDriverStatisticsKey property table. It has an OSNumber value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kioblockstoragedriverstatisticsreaderrorskey)*