# isEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the UI update link is monitoring UI updates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

#### Discussion

By default, the value of this property is [`true`](../../Swift/true.md), which means the system invokes the actions of the UI update link for each UI update.

When the value is [`false`](../../Swift/false.md), the UI update link has no effect. Set the value to [`false`](../../Swift/false.md) if you want to temporarily turn off the UI update link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/isenabled)*