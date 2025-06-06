# nrNoiseLevel

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

The noise level of the image, used with camera data, that's removed before tracing the edges of the image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var nrNoiseLevel: Float { get set }
```

#### Discussion

Increasing the noise level helps to clean up the traced edges of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay/3228529-nrnoiselevel)*