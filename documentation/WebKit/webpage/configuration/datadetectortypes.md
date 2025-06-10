# dataDetectorTypes

**Framework**: WebKit  
**Kind**: property

The types of data detectors to apply to the webpage’s content.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

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