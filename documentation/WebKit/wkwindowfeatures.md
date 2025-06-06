# WKWindowFeatures

**Framework**: Webkit  
**Kind**: class

Display-related attributes that a webpage requests for its window.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKWindowFeatures
```

#### Overview

A [`WKWindowFeatures`](wkwindowfeatures.md) object contains the attributes that a webpage requests from its containing web view. You don’t create a [`WKWindowFeatures`](wkwindowfeatures.md) object directly. When a navigation action results in the display of a new web view, [`WKWebView`](wkwebview.md) creates this object and passes it to the [`webView(_:createWebViewWith:for:windowFeatures:)`](wkuidelegate/webview(_:createwebviewwith:for:windowfeatures:).md) method of its UI delegate object. The delegate uses the information in this object to configure and return the new web view.

## Topics

### Inspecting Window Position and Dimensions
- [var allowsResizing: NSNumber?](wkwindowfeatures/allowsresizing.md)
  A Boolean value that indicates whether to make the containing window window resizable.
- [var height: NSNumber?](wkwindowfeatures/height.md)
  The requested height of the containing window.
- [var width: NSNumber?](wkwindowfeatures/width.md)
  The requested width of the containing window.
- [var x: NSNumber?](wkwindowfeatures/x.md)
  The requested x-coordinate of the containing window.
- [var y: NSNumber?](wkwindowfeatures/y.md)
  The requested y-coordinate of the containing window.
### Inspecting Visibility Properties
- [var menuBarVisibility: NSNumber?](wkwindowfeatures/menubarvisibility.md)
  A Boolean value that indicates whether the webpage requests a visible menu bar.
- [var statusBarVisibility: NSNumber?](wkwindowfeatures/statusbarvisibility.md)
  A Boolean value that indicates whether the webpage requested a visible status bar.
- [var toolbarsVisibility: NSNumber?](wkwindowfeatures/toolbarsvisibility.md)
  A Boolean value that indicates whether the webpage requested a visible toolbar.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKWebViewConfiguration](wkwebviewconfiguration.md)
  A collection of properties that you use to initialize a web view.
- [class WKProcessPool](wkprocesspool.md)
  An opaque token that you use to run multiple web views in a single process.
- [class WKPreferences](wkpreferences.md)
  An object that encapsulates the standard behaviors to apply to websites.
- [class WKWebpagePreferences](wkwebpagepreferences.md)
  An object that specifies the behaviors to use when loading and rendering page content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwindowfeatures)*