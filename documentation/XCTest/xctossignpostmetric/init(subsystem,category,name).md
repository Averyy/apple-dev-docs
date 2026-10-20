# init(subsystem:category:name:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithSubsystem:(NSString *) subsystem category:(NSString *) category name:(NSString *) name;
```

#### Discussion

Create an `XCTOSSignpostMetric` that records the time that elapses between the beginning and end of the named signpost in a particular log subsystem and category.

## Parameters

- `subsystem`: The [`OSLog`](../../os/oslog.md) subsystem that logs the signpost events.
- `category`: The log category for the logged signpost events.
- `name`: The name of the signpost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctossignpostmetric/init(subsystem:category:name:))*