# rect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The rectangle that encloses the text selection rectangle’s text range.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var rect: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect rect;
```

#### Discussion

The returned rectangle is in the coordinate system of the text input view that created the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectionrect/rect)*