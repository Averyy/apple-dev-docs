# allowsResizing

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to make the containing window window resizable.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var allowsResizing: NSNumber? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSNumber * allowsResizing;
```

#### Discussion

If the webpage didn’t request a resizable window, this property is `nil`.

## See Also

### Inspecting Window Position and Dimensions
- [var height: NSNumber?](./height.md)
  The requested height of the containing window.
- [var width: NSNumber?](./width.md)
  The requested width of the containing window.
- [var x: NSNumber?](./x.md)
  The requested x-coordinate of the containing window.
- [var y: NSNumber?](./y.md)
  The requested y-coordinate of the containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwindowfeatures/allowsresizing)*