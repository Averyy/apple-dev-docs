# isActivated

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to display the system selection UI.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isActivated: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite, getter=isActivated) BOOL activated;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) when you want the system to display the selection UI. Set the property to [`false`](../../Swift/false.md) to hide the selection UI again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/isactivated)*