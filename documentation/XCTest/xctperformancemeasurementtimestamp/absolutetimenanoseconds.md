# absoluteTimeNanoSeconds

**Framework**: XCTest  
**Kind**: property

The nanoseconds component of the absolute time.

## Declaration

```swift
var absoluteTimeNanoSeconds: UInt64 { get }
```

#### Discussion

This property reflects the number of nanoseconds since an arbitrary reference time. It doesn’t update while the system is sleeping.

## See Also

- [var absoluteTime: UInt64](xctperformancemeasurementtimestamp/absolutetime.md)
  The absolute time of the timestamp, which is the value of the mach absolute time clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurementtimestamp/absolutetimenanoseconds)*