# isHandlingWriting

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user is actively writing in a text view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isHandlingWriting: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isHandlingWriting) BOOL handlingWriting;
```

#### Discussion

This property is [`true`](../../Swift/true.md) in between calls to [`scribbleInteractionWillBeginWriting(_:)`](../uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting%28_%29.md) and [`scribbleInteractionDidFinishWriting(_:)`](../uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting%28_%29.md) when the user is writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteraction/ishandlingwriting)*