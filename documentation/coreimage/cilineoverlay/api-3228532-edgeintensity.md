# edgeIntensity

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

The accentuation factor of the Sobel gradient information when tracing the edges of the image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var edgeIntensity: Float { get set }
```

#### Discussion

Higher values find more edges, although typically, you’d use a low value (such as 1.0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay/3228532-edgeintensity)*