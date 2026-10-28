# toolbarsVisibility

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the webpage requested a visible toolbar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var toolbarsVisibility: NSNumber? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSNumber * toolbarsVisibility;
```

## Discussion

If the webpage didn’t request a visible toolbar, this property is `nil`.

## See Also

### Inspecting Visibility Properties
- [var menuBarVisibility: NSNumber?](./menubarvisibility.md)
  A Boolean value that indicates whether the webpage requests a visible menu bar.
- [var statusBarVisibility: NSNumber?](./statusbarvisibility.md)
  A Boolean value that indicates whether the webpage requested a visible status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwindowfeatures/toolbarsvisibility)*