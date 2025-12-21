# XCTHitchMetric

**Framework**: XCTest  
**Kind**: class

A metric to measure the number of hitches your UI encounters in a performance test.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class XCTHitchMetric
```

#### Discussion

A hitch occurs when your app doesn’t prepare the content it displays in time for the system to render it in the next screen update. For more information, see [`Understanding hitches in your app`](https://developer.apple.com/documentation/Xcode/understanding-hitches-in-your-app).

## Topics

### Creating a hitch metric
- [init(application: XCUIApplication)](xcthitchmetric/init(application:).md)
  Initializes a metric that measures hitches metric in the specified app.

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
- [class XCTApplicationLaunchMetric](xctapplicationlaunchmetric.md)
  A metric to record the application launch duration for a performance test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xcthitchmetric)*