# menuBarVisibility

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the webpage requests a visible menu bar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var menuBarVisibility: NSNumber? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSNumber * menuBarVisibility;
```

#### Discussion

If the webpage didn’t request a visible menu bar, this property is `nil`.

## See Also

### Inspecting Visibility Properties
- [var statusBarVisibility: NSNumber?](./statusbarvisibility.md)
  A Boolean value that indicates whether the webpage requested a visible status bar.
- [var toolbarsVisibility: NSNumber?](./toolbarsvisibility.md)
  A Boolean value that indicates whether the webpage requested a visible toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwindowfeatures/menubarvisibility)*