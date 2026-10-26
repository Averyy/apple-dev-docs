# supportedColorSpaces()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the supported color spaces in an extension.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func supportedColorSpaces() -> [NSNumber]!
```

```objc
- (NSArray<NSNumber *> *) supportedColorSpaces;
```

#### Return Value

An array of supported color spaces from the [`eCEColorSpace`](../ececolorspace.md) enumeration.

#### Discussion

If there is no implementation for this method, the Compressor app assumes [`eCEColorSpaceDeviceRGB`](../ececolorspacedevicergb.md), [`eCEColorSpace601NTSC`](../ececolorspace601ntsc.md), and [`eCEColorSpace709`](../ececolorspace709.md) for the supported color spaces.

## See Also

### Supporting Color Spaces
- [struct eCEColorSpace](../ececolorspace.md)
  The list of color spaces an encoder extension can support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensioncolorspaces/supportedcolorspaces())*