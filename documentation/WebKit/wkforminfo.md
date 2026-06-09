# WKFormInfo

**Framework**: WebKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
class WKFormInfo
```

#### Overview

A WKFormInfo object contains information about an in-progress form submission happening in a WKWebView

An instance of this class is a transient, data-only object; it does not uniquely identify a form across multiple delegate method calls.

## Topics

### Instance Properties
- [var formValues: [String : String]](wkforminfo/formvalues.md)
- [var httpMethod: String](wkforminfo/httpmethod.md)
- [var sourceFrame: WKFrameInfo](wkforminfo/sourceframe.md)
- [var submissionURL: URL](wkforminfo/submissionurl.md)
- [var targetFrame: WKFrameInfo](wkforminfo/targetframe.md)

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
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkforminfo)*