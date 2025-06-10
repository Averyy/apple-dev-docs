# WKWebExtension.TabChangedProperties

**Framework**: WebKit  
**Kind**: struct

Constants the web extension controller and web extension context use to indicate tab changes.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct TabChangedProperties
```

## Topics

### Initializers
- [init(rawValue: UInt)](wkwebextension/tabchangedproperties/init(rawvalue:).md)
### Type Properties
- [static var URL: WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties/url.md)
  Indicates the URL changed.
- [static var loading: WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties/loading.md)
  Indicates the loading state changed.
- [static var muted: WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties/muted.md)
  Indicates the muted state changed.
- [static var pinned: WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties/pinned.md)
  Indicates the pinned state changed.
- [static var playingAudio: WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties/playingaudio.md)
  Indicates the audio playback state changed.
- [static var readerMode: WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties/readermode.md)
  Indicates the reader mode state changed.
- [static var size: WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties/size.md)
  Indicates the size changed.
- [static var title: WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties/title.md)
  Indicates the title changed.
- [static var zoomFactor: WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties/zoomfactor.md)
  Indicates the zoom factor changed.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [WKWebExtension.DataType](wkwebextension/datatype.md)
  Constants for specifying data types for a [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md).
- [WKWebExtension.Error](wkwebextension/error.md)
  Constants that indicate errors in the [`WKWebExtension`](wkwebextension.md) domain.
- [WKWebExtension.Permission](wkwebextension/permission.md)
  Constants for specifying permission in a [`WKWebExtensionContext`](wkwebextensioncontext.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/tabchangedproperties)*