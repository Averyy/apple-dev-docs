# WKSnapshotConfiguration

**Framework**: WebKit  
**Kind**: class

The configuration data to use when generating an image from a web view’s contents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKSnapshotConfiguration
```

#### Overview

Create a [`WKSnapshotConfiguration`](wksnapshotconfiguration.md) object when you want to generate an image based on your web view’s content. Use this object to specify the portion of the web view to capture and the capture behavior. To generate the snapshot, pass the configuration object to the [`takeSnapshot(with:completionHandler:)`](wkwebview/takesnapshot(with:completionhandler:).md) method of [`WKWebView`](wkwebview.md), which returns a platform-native image for you to use.

## Topics

### Specifying the snapshot dimensions
- [var rect: CGRect](wksnapshotconfiguration/rect.md)
  The portion of your web view to capture, specified as a rectangle in the view’s coordinate system.
- [var snapshotWidth: NSNumber?](wksnapshotconfiguration/snapshotwidth.md)
  The width of the captured image, in points.
### Configuring the capture behavior
- [var afterScreenUpdates: Bool](wksnapshotconfiguration/afterscreenupdates.md)
  A Boolean value that indicates whether to take the snapshot after incorporating any pending screen updates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKPDFConfiguration](wkpdfconfiguration.md)
  The configuration data to use when generating a PDF representation of a web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wksnapshotconfiguration)*