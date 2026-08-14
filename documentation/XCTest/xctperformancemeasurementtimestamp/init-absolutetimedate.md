# init(absoluteTime:date:)

**Framework**: XCTest  
**Kind**: init

Intitializes a timestamp that represents the provided time.

## Declaration

```swift
init(absoluteTime: UInt64, date: Date)
```

## Parameters

- `absoluteTime`: The time, as returned by the [`mach_absolute_time`](https://developer.apple.com/documentation/kernel/1462446-mach_absolute_time) system call.
- `date`: The time, represented as a [`Date`](https://developer.apple.com/documentation/foundation/date).

## See Also

- [convenience init()](xctperformancemeasurementtimestamp/init.md)
  Intitializes a timestamp that represents the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurementtimestamp/init(absolutetime:date:))*