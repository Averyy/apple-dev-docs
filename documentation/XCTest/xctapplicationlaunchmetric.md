# XCTApplicationLaunchMetric

**Framework**: Xctest  
**Kind**: class

A metric to record the application launch duration for a performance test.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class XCTApplicationLaunchMetric
```

## Topics

### Initializers
- [init()](xctapplicationlaunchmetric/init.md)
  Initializes a metric that records the time for an app to display its first frame to screen and complete all extended launch tasks.
- [init(waitUntilResponsive: Bool)](xctapplicationlaunchmetric/init(waituntilresponsive:).md)
  Initializes a metric that records the time for an app to display its first frame to screen and complete all extended launch tasks, or to display its first frame and wait until the app is responsive.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [XCTMetric](xctmetric.md)

## See Also

- [protocol XCTMetric](xctmetric.md)
  A protocol that defines the methods that objects must provide when gathering metrics during performance tests.
- [class XCTCPUMetric](xctcpumetric.md)
  A metric to record information about CPU activity during a performance test.
- [class XCTClockMetric](xctclockmetric.md)
  A metric to record the time that elapses during a performance test.
- [class XCTMemoryMetric](xctmemorymetric.md)
  A metric to record the physical memory that a performance test uses.
- [class XCTOSSignpostMetric](xctossignpostmetric.md)
  A metric to record the time that a performance test spends executing a signposted region of code.
- [class XCTStorageMetric](xctstoragemetric.md)
  A metric to record the amount of data that a performance test logically writes to storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctapplicationlaunchmetric)*