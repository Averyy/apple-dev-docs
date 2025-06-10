# XCTPerformanceMeasurementTimestamp

**Framework**: XCTest  
**Kind**: class

A point in time that captures the start or finish of a performance test iteration.

## Declaration

```swift
class XCTPerformanceMeasurementTimestamp
```

## Topics

### Initializers
- [convenience init()](xctperformancemeasurementtimestamp/init.md)
  Intitializes a timestamp that represents the current time.
- [init(absoluteTime: UInt64, date: Date)](xctperformancemeasurementtimestamp/init(absolutetime:date:).md)
  Intitializes a timestamp that represents the provided time.
### Mach Absolute Time
- [var absoluteTimeNanoSeconds: UInt64](xctperformancemeasurementtimestamp/absolutetimenanoseconds.md)
  The nanoseconds component of the absolute time.
- [var absoluteTime: UInt64](xctperformancemeasurementtimestamp/absolutetime.md)
  The absolute time of the timestamp, which is the value of the mach absolute time clock.
### Date
- [var date: Date](xctperformancemeasurementtimestamp/date.md)
  The timestamp’s representation as a date.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class XCTPerformanceMeasurement](xctperformancemeasurement.md)
  A measurement from a single iteration of a performance test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurementtimestamp)*