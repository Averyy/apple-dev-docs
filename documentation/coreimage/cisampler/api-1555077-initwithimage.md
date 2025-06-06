# initWithImage:keysAndValues:

**Framework**: Core Image  
**Kind**: instm

Initializes the sampler with an image object using options specified as key-value pairs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
- (instancetype)initWithImage:(CIImage *)im keysAndValues:(id)key0, ...;
```

## Parameters

- `im`: The image object to initialize the sampler with.
- `key0`: A list of key-value pairs that represent options.  Each key needs to be followed by that appropriate value. You can supply one or more key-value pairs. Use   to specify the end of the key-value options. See  .

## See Also

- [- initWithImage:](cisampler/1438117-initwithimage.md)
  Initializes a sampler with an image object.
- [- initWithImage:options:](cisampler/1437963-initwithimage.md)
  Initializes the sampler with an image object using options specified in a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler/1555077-initwithimage)*