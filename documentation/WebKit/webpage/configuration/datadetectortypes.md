# dataDetectorTypes

**Framework**: WebKit  
**Kind**: property

The types of data detectors to apply to the webpage’s content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var dataDetectorTypes: WKDataDetectorTypes
```

#### Discussion

Data detectors add interactivity to web content by creating links for specially formatted text. For example, the `.link` type causes the apple.com portion of the text “Visit apple.com” to become a link to the Apple website.

The default value of this property is an empty OptionSet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/datadetectortypes)*