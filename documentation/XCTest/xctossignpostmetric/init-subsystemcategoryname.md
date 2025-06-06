# init(subsystem:category:name:)

**Framework**: Xctest  
**Kind**: init

Creates a metric to record a specific signpost.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(subsystem: String, category: String, name: String)
```

#### Discussion

Create an `XCTOSSignpostMetric` that records the time that elapses between the beginning and end of the named signpost in a particular log subsystem and category.

## Parameters

- `subsystem`: The   subsystem that logs the signpost events.
- `category`: The log category for the logged signpost events.
- `name`: The name of the signpost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctossignpostmetric/init(subsystem:category:name:))*