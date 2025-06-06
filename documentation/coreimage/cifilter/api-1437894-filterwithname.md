# filterWithName:withInputParameters:

**Framework**: Core Image  
**Kind**: clm

Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter and initializes the input values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
+ (CIFilter *)filterWithName:(NSString *)name withInputParameters:(NSDictionary<NSString *,id> *)params;
```

#### Return_value

A [`CIFilter`](cifilter.md) object whose input values are initialized.

#### Discussion

Use this method to quickly create and configure a [`CIFilter`](cifilter.md) instance, as in the example below.

```occ
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

- [+ filterWithName:](cifilter/1438255-filterwithname.md)
  Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter. 
- [+ filterWithName:keysAndValues:](cifilter/1562057-filterwithname.md)
  Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter and initializes the input values with a `nil`-terminated list of arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1437894-filterwithname)*