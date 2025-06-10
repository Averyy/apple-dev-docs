# init(name:withInputParameters:)

**Framework**: Core Image  
**Kind**: init

Creates a [`CIFilter`](cifilter-swift.class.md) object for a specific kind of filter and initializes the input values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init?(name: String, parameters params: [String : Any]?)
```

#### Return Value

A [`CIFilter`](cifilter-swift.class.md) object whose input values are initialized.

#### Discussion

Use this method to quickly create and configure a [`CIFilter`](cifilter-swift.class.md) instance, as in the example below.

```objc
CIFilter *f = [CIFilter filterWithName: @"CIColorControls"
                   withInputParameters: @{
                             @"inputImage"      : inImage,
                             @"inputSaturation" : @0.5,
                             @"inputBrightness" : @1.2,
                             @"inputContrast"   : @1.3
                                         }];
```

## Parameters

- `name`: The name of the filter. You must make sure the name is spelled correctly, otherwise your app will run but not produce any output images. For that reason, you should check for the existence of the filter after calling this method.
- `params`: A list of key-value pairs to set as input values to the filter. Each key is a constant that specifies the name of an input parameter for the filter, and the corresponding value is the value for that parameter. See   for built-in filters and their allowed parameters.

## See Also

- [init?(name: String)](cifilter-swift.class/init(name:).md)
  Creates a [`CIFilter`](cifilter-swift.class.md) object for a specific kind of filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(name:withinputparameters:))*