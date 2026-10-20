# OSLog.Category

**Framework**: os  
**Kind**: struct  
**Role**: Structure

System-defined categories that identify well-known parts of your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS
- watchOS 5.0+

## Declaration

```swift
struct Category
```

## Topics

### Logging Signposts
- [static let pointsOfInterest: OSLog.Category](./category/pointsofinterest.md)
  The category you use to log signposts.
- [static let dynamicStackTracing: OSLog.Category](./category/dynamicstacktracing.md)
  The category for dynamic stack tracing.
- [static let dynamicTracing: OSLog.Category](./category/dynamictracing.md)
  The category for dynamic tracing.
### Inspecting Log Categories
- [let rawValue: String](./category/rawvalue.md)
  A string that uniquely identifies a logging category.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Log
- [convenience init(subsystem: String, category: String)](./init%28subsystem,category%29-17gyy.md)
  Creates a log using the specified subsystem and category.
- [convenience init(subsystem: String, category: OSLog.Category)](./init%28subsystem,category%29-72ghw.md)
  Creates a log using the specified subsystem and system-defined category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslog/category)*