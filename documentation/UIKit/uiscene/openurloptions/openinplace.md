# openInPlace

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you should open the URL at its current location instead of copying it to your app’s container.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var openInPlace: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL openInPlace;
```

#### Discussion

When the value of this property is [`false`](../../../Swift/false.md), copy the document to your app’s container before opening the file. When the value of this property is [`true`](../../../Swift/true.md), open the existing URL in its current location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openurloptions/openinplace)*