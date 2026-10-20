# containerTraitCollection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The trait collection of the sheet’s container view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var containerTraitCollection: UITraitCollection { get }
```

```objc
@property (nonatomic, readonly) UITraitCollection * containerTraitCollection;
```

#### Discussion

The value of this property is the same as the window’s [`traitCollection`](../uiwindowscene/traitcollection.md), and doesn’t include overrides from the sheet’s [`overrideTraitCollection`](../uipresentationcontroller/overridetraitcollection.md).

## See Also

### Accessing the properties of the context
- [var maximumDetentValue: CGFloat](./maximumdetentvalue.md)
  The maximum value of a detent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdetentresolutioncontext/containertraitcollection)*