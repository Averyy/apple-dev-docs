# openInPlace

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether you should open the URL at its current location instead of copying it to your app’s container.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var openInPlace: Bool { get }
```

#### Discussion

When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), copy the document to your app’s container before opening the file. When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), open the existing URL in its current location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openurloptions/openinplace)*