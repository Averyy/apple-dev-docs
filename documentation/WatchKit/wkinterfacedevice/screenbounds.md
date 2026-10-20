# screenBounds

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The bounding rectangle of the screen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var screenBounds: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect screenBounds;
```

#### Discussion

The rectangle represents the dimensions of the screen and may be different from the rectangle used to display your app’s content.

## See Also

### Reading the Screen Information
- [var screenScale: CGFloat](./screenscale.md)
  The number of pixels per point for the current screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/screenbounds)*