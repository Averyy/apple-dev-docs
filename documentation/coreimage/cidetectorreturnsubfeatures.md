# CIDetectorReturnSubFeatures

**Framework**: Core Image  
**Kind**: data

An option specifying whether to return feature information for components of detected features.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorReturnSubFeatures: String
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object with a Boolean value. Use this option with the [`CIDetectorTypeText`](cidetectortypetext.md) detector type to choose whether to detect only regions likely to contain text ([`false`](https://developer.apple.com/documentation/swift/false), the default) or to also identify sub-regions likely to contain individual characters of text ([`true`](https://developer.apple.com/documentation/swift/true)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectorreturnsubfeatures)*