# statusBarVisibility

**Framework**: Webkit  
**Kind**: property

A Boolean value that indicates whether the webpage requested a visible status bar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var statusBarVisibility: NSNumber? { get }
```

#### Discussion

If the webpage didn’t request a visible status bar, this property is `nil`.

## See Also

- [var menuBarVisibility: NSNumber?](wkwindowfeatures/menubarvisibility.md)
  A Boolean value that indicates whether the webpage requests a visible menu bar.
- [var toolbarsVisibility: NSNumber?](wkwindowfeatures/toolbarsvisibility.md)
  A Boolean value that indicates whether the webpage requested a visible toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwindowfeatures/statusbarvisibility)*