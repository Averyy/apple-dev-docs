# setJobSourceAttributes(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the source media attributes based on the given values.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func setJobSourceAttributes(_ sourceProperties: [AnyHashable : Any]!)
```

```objc
- (void) setJobSourceAttributes:(NSDictionary *) sourceProperties;
```

#### Discussion

The Compressor app calls this method when users update the source media attributes for an encoding job. Use the source media attributes to compute encoding values for the encoder settings, such as height, width, and frame rate, that have values set to automatic. See [`kCEAutoHeightKey`](../kceautoheightkey.md), [`kCEAutoWidthKey`](../kceautowidthkey.md), and [`kCEAutoRateKey`](../kceautoratekey.md).

## Parameters

- `sourceProperties`: A dictionary of key-value pairs that provide information about the source media, such as size and frame rate. The dictionary has same keys as defined in Encoder Attribute Keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionsettingsoptional/setjobsourceattributes(_:))*