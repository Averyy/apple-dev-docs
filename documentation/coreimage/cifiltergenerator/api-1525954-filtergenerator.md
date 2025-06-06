# filterGenerator

**Framework**: Core Image  
**Kind**: clm

Creates and returns an empty filter generator object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
+ (CIFilterGenerator *)filterGenerator;
```

#### Return_value

A [`CIFilterGenerator`](cifiltergenerator.md) object.

#### Discussion

You use the returned object to connect two or more [`CIFilter`](cifilter.md) objects and input images. It is also valid to have only one [`CIFilter`](cifilter.md) object in a filter generator.

## See Also

- [+ filterGeneratorWithContentsOfURL:](cifiltergenerator/1525950-filtergeneratorwithcontentsofurl.md)
  Creates and returns a filter generator object and initializes it with the contents of a filter generator file.
- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [Core Image Filter Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1525954-filtergenerator)*