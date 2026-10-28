# traitCollection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The traits that describe the current environment of the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var traitCollection: UITraitCollection { get }
```

```objc
@property (nonatomic, readonly) UITraitCollection * traitCollection;
```

## Discussion

Use this property to get additional information about the current scene, such as the size class and scale factor. For more information about the available traits, see [`UITraitCollection`](../uitraitcollection.md).

## See Also

### Getting the interface attributes
- [var sizeRestrictions: UISceneSizeRestrictions?](./sizerestrictions.md)
  The minimum and maximum size of the app’s windows.
- [class UISceneSizeRestrictions](../uiscenesizerestrictions.md)
  An object that specifies the minimum and maximum sizes for resizable windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/traitcollection)*