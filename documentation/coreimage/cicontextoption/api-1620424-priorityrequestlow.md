# priorityRequestLow

**Framework**: Core Image  
**Kind**: structdata

A key for enabling low-priority GPU use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let priorityRequestLow: CIContextOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a Boolean value. If this value is [`true`](https://developer.apple.com/documentation/swift/true), use of the Core Image context from a background thread takes lower priority than GPU usage from the main thread, allowing your app to perform Core Image rendering without disturbing the frame rate of UI animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/1620424-priorityrequestlow)*