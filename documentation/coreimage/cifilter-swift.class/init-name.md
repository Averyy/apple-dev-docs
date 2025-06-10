# init(name:)

**Framework**: Core Image  
**Kind**: init

Creates a [`CIFilter`](cifilter-swift.class.md) object for a specific kind of filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init?(name: String)
```

#### Return Value

A [`CIFilter`](cifilter-swift.class.md) object whose input values are undefined.

#### Discussion

In macOS, after creating a filter with this method you must call [`setDefaults()`](cifilter-swift.class/setdefaults().md) or set parameters individually by calling doc://com.apple.documentation/documentation/objectivec/nsobject/1415969-setvalue. In iOS, the filter’s parameters are automatically set to default values.

## Parameters

- `name`: The name of the filter. You must make sure the name is spelled correctly, otherwise your app will run but not produce any output images. For that reason, you should check for the existence of the filter after calling this method.

## See Also

- [Image Unit Tutorial](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004531)
- [Core Image Filter Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346)
- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [init?(name: String, withInputParameters: [String : Any]?)](cifilter-swift.class/init(name:withinputparameters:).md)
  Creates a [`CIFilter`](cifilter-swift.class.md) object for a specific kind of filter and initializes the input values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(name:))*