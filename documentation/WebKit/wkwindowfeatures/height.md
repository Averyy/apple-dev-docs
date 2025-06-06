# height

**Framework**: Webkit  
**Kind**: property

The requested height of the containing window.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var height: NSNumber? { get }
```

#### Discussion

The object in this property contains a [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) value. If the webpage didn’t request a specific window height, this property is `nil`.

## See Also

- [var allowsResizing: NSNumber?](wkwindowfeatures/allowsresizing.md)
  A Boolean value that indicates whether to make the containing window window resizable.
- [var width: NSNumber?](wkwindowfeatures/width.md)
  The requested width of the containing window.
- [var x: NSNumber?](wkwindowfeatures/x.md)
  The requested x-coordinate of the containing window.
- [var y: NSNumber?](wkwindowfeatures/y.md)
  The requested y-coordinate of the containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwindowfeatures/height)*