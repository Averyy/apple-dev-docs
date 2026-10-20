# init(application:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates a CPU metric that records data for the requested app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(application: XCUIApplication)
```

```objc
- (instancetype) initWithApplication:(XCUIApplication *) application;
```

## Parameters

- `application`: The application to be tested.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Creates a CPU metric that records data for the current process.
- [init(limitingToCurrentThread: Bool)](./init%28limitingtocurrentthread%29.md)
  Creates a CPU metric that optionally records data only for the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctcpumetric/init(application:))*