# WKWebExtension.TabChangedProperties

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum WKWebExtensionTabChangedProperties : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./tabchangedproperties/init%28rawvalue%29.md)
### Type Properties
- [static var URL: WKWebExtension.TabChangedProperties](./tabchangedproperties/url.md)
  Indicates the URL changed.
- [static var loading: WKWebExtension.TabChangedProperties](./tabchangedproperties/loading.md)
  Indicates the loading state changed.
- [static var muted: WKWebExtension.TabChangedProperties](./tabchangedproperties/muted.md)
  Indicates the muted state changed.
- [static var pinned: WKWebExtension.TabChangedProperties](./tabchangedproperties/pinned.md)
  Indicates the pinned state changed.
- [static var playingAudio: WKWebExtension.TabChangedProperties](./tabchangedproperties/playingaudio.md)
  Indicates the audio playback state changed.
- [static var readerMode: WKWebExtension.TabChangedProperties](./tabchangedproperties/readermode.md)
  Indicates the reader mode state changed.
- [static var size: WKWebExtension.TabChangedProperties](./tabchangedproperties/size.md)
  Indicates the size changed.
- [static var title: WKWebExtension.TabChangedProperties](./tabchangedproperties/title.md)
  Indicates the title changed.
- [static var zoomFactor: WKWebExtension.TabChangedProperties](./tabchangedproperties/zoomfactor.md)
  Indicates the zoom factor changed.
### Enumeration Cases
- [WKWebExtensionTabChangedPropertiesNone](../wkwebextensiontabchangedproperties/wkwebextensiontabchangedpropertiesnone.md)
  Indicates nothing changed.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Structures
- [WKWebExtension.DataType](./datatype.md)
  Constants for specifying data types for a [`WKWebExtension.DataRecord`](./datarecord.md).
- [WKWebExtension.Error](./error.md)
  Constants that indicate errors in the [`WKWebExtension`](../wkwebextension.md) domain.
- [WKWebExtension.Permission](./permission.md)
  Constants for specifying permission in a [`WKWebExtensionContext`](../wkwebextensioncontext.md).
### Enumerations
- [WKWebExtensionWindowState](./windowstate.md)
  Constants used by [`WKWebExtensionWindow`](../wkwebextensionwindow.md) to indicate possible states of a window.
- [WKWebExtensionWindowType](./windowtype.md)
  Constants used by [`WKWebExtensionWindow`](../wkwebextensionwindow.md) to indicate the type of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/tabchangedproperties)*