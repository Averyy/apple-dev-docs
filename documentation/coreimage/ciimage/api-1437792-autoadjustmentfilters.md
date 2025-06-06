# autoAdjustmentFilters(options:)

**Framework**: Core Image  
**Kind**: instm

Returns a subset of automatically selected and configured filters for adjusting the image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func autoAdjustmentFilters(options: [CIImageAutoAdjustmentOption : Any]? = nil) -> [CIFilter]
```

#### Return_value

An array of [`CIFilter`](cifilter.md) instances preconfigured for correcting deficiencies in the supplied image.

## Parameters

- `options`: The options dictionary can also contain a   key. Because some autoadjustment filters rely on face detection, you should specify an image orientation if you want to enable these filters for an image containing face whose orientation does not match that of the image.

## See Also

- [func autoAdjustmentFilters() -> [CIFilter]](ciimage/1645889-autoadjustmentfilters.md)
  Returns all possible automatically selected and configured filters for adjusting the image.
- [Autoadjustment Keys](ciimage/autoadjustment_keys.md)
  Constants used as keys in the options dictionary for the [`autoAdjustmentFilters(options:)`](ciimage/1437792-autoadjustmentfilters.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1437792-autoadjustmentfilters)*