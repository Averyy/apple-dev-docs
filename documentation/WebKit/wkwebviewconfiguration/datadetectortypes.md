# dataDetectorTypes

**Framework**: Webkit  
**Kind**: property

The types of data detectors to apply to the web view’s content.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var dataDetectorTypes: WKDataDetectorTypes { get set }
```

#### Discussion

Data detectors add interactivity to web content by creating links for specially formatted text. For example, the `WKDataDetectorTypeLink` type causes the `apple.com` portion of the text “Visit apple.com” to become a link to the Apple website.

The default value of this property is [`WKDataDetectorTypeNone`](wkdatadetectortypes/wkdatadetectortypenone.md). For other possible values, see [`WKDataDetectorTypes`](wkdatadetectortypes.md).

## See Also

- [struct WKDataDetectorTypes](wkdatadetectortypes.md)
  The data detector types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/datadetectortypes)*