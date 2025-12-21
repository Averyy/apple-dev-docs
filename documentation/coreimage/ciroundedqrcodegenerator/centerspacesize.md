# centerSpaceSize

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The fraction of the center space of the QRCode to fill with Color 1. If the size is 0.0 or the Correction Level is L or M, the center of the QRCode will be unaltered. The size will be limited to 0.25 if the Correction Level is Q. The size will be limited to 0.33 if the Correction Level is H.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var centerSpaceSize: Float { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciroundedqrcodegenerator/centerspacesize)*