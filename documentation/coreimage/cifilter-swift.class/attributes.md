# attributes

**Framework**: Core Image  
**Kind**: property

A dictionary of key-value pairs that describe the filter.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var attributes: [String : Any] { get }
```

#### Discussion

This dictionary contains two kinds of key-value pairs:

- Keys listed in [`Filter Attribute Keys`](filter-attribute-keys.md) describe the filter, providing information such as a human-readable name and categories you can use to organize filters in your app’s UI.
- Other keys, including those listed in [`Filter Parameter Keys`](filter-parameter-keys.md) and those starting with “input” or “output”, describe parameters that control the filter’s behavior. For each parameter key, the corresponding value is another dictionary describing possible values for that parameter, such as the value class and minimum/maximum values. You can use this information to build a UI to control the filter.

For example, the attributes dictionary for the `CIColorControls` filter contains the following information:

```objc
CIColorControls:
{
    CIAttributeFilterCategories = (
        CICategoryColorAdjustment,
        CICategoryVideo,
        CICategoryStillImage,
        CICategoryInterlaced,
        CICategoryNonSquarePixels,
        CICategoryBuiltIn
    );
    CIAttributeFilterDisplayName = "Color Controls";
    CIAttributeFilterName = CIColorControls;
    inputBrightness = {
        CIAttributeClass = NSNumber;
        CIAttributeDefault = 0;
        CIAttributeIdentity = 0;
        CIAttributeMin = -1;
        CIAttributeSliderMax = 1;
        CIAttributeSliderMin = -1;
        CIAttributeType = CIAttributeTypeScalar;
    };
    inputContrast = {
        CIAttributeClass = NSNumber;
        CIAttributeDefault = 1;
        CIAttributeIdentity = 1;
        CIAttributeMin = 0.25;
        CIAttributeSliderMax = 4;
        CIAttributeSliderMin = 0.25;
        CIAttributeType = CIAttributeTypeScalar;
    };
    inputImage = {CIAttributeClass = CIImage; };
    inputSaturation = {
        CIAttributeClass = NSNumber;
        CIAttributeDefault = 1;
        CIAttributeIdentity = 1;
        CIAttributeMin = 0;
        CIAttributeSliderMax = 3;
        CIAttributeSliderMin = 0;
        CIAttributeType = CIAttributeTypeScalar;
    };
    outputImage = {CIAttributeClass = CIImage; };
}
```

## See Also

- [var name: String](cifilter-swift.class/name.md)
  A name associated with a filter.
- [var isEnabled: Bool](cifilter-swift.class/isenabled.md)
  A Boolean value that determines whether the filter is enabled. Animatable.
- [var inputKeys: [String]](cifilter-swift.class/inputkeys.md)
  The names of all input parameters to the filter.
- [var outputKeys: [String]](cifilter-swift.class/outputkeys.md)
  The names of all output parameters from the filter.
- [var outputImage: CIImage?](cifilter-swift.class/outputimage.md)
  Returns a [`CIImage`](ciimage.md) object that encapsulates the operations configured in the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/attributes)*