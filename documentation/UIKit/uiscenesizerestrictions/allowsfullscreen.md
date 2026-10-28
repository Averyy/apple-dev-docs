# allowsFullScreen

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the scene can appear full screen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 16.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var allowsFullScreen: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsFullScreen;
```

## Discussion

The system only checks the value of this property in Mac Catalyst apps.

## See Also

### Setting the size restrictions
- [var minimumSize: CGSize](./minimumsize.md)
  The minimum width and height supported by your app’s windows.
- [var maximumSize: CGSize](./maximumsize.md)
  The maximum width and height supported by your app’s windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesizerestrictions/allowsfullscreen)*