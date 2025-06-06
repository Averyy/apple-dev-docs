# filterWithName:

**Framework**: Core Image  
**Kind**: clm

Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter. 

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
+ (CIFilter *)filterWithName:(NSString *)name;
```

#### Return_value

A [`CIFilter`](cifilter.md) object whose input values are undefined.

#### Discussion

In macOS, after creating a filter with this method you must call [`setDefaults`](cifilter/1437902-setdefaults.md) or set parameters individually by calling [`setValue(_:forKey:)`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forkey:)). In iOS, the filter’s parameters are automatically set to default values.

## Parameters

- `name`: The name of the filter. You must make sure the name is spelled correctly, otherwise your app will run but not produce any output images. For that reason, you should check for the existence of the filter after calling this method. 

## See Also

- [+ filterWithName:withInputParameters:](cifilter/1437894-filterwithname.md)
  Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter and initializes the input values.
- [+ filterWithName:keysAndValues:](cifilter/1562057-filterwithname.md)
  Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter and initializes the input values with a `nil`-terminated list of arguments.
- [Image Unit Tutorial](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004531)
- [Core Image Filter Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346)
- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1438255-filterwithname)*