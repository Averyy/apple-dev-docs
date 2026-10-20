# init(absoluteTime:date:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Intitializes a timestamp that represents the provided time.

## Declaration

```swift
init(absoluteTime: UInt64, date: Date)
```

```objc
- (instancetype) initWithAbsoluteTime:(uint64_t) absoluteTime date:(NSDate *) date;
```

## Parameters

- `absoluteTime`: The time, as returned by the [`mach_absolute_time`](../../kernel/api-1462446-mach_absolute_time.md) system call.
- `date`: The time, represented as a [`Date`](../../Foundation/date.md).

## See Also

### Initializers
- [convenience init()](./init%28%29.md)
  Intitializes a timestamp that represents the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurementtimestamp/init(absolutetime:date:))*