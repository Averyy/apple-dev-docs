# scaleFactor

**Framework**: Core Image  
**Kind**: structdata

A key for the scale factor. The associated value is a floating-point value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object that specifies the desired scale factor at which the image will be drawn. Setting this value can greatly improve the drawing performance. A value of `1` is the identity. In some cases, if you change the scale factor and enable draft mode, performance can decrease. See [`allowDraftMode`](cirawfilteroption/1438010-allowdraftmode.md).

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.5+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
static let scaleFactor: CIRAWFilterOption
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437936-scalefactor)*