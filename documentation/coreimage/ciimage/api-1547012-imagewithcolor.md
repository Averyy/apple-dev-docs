# imageWithColor:

**Framework**: Core Image  
**Kind**: clm

Creates and returns an image of infinite extent whose entire content is the specified color. 

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
+ (CIImage *)imageWithColor:(CIColor *)color;
```

#### Return_value

The image object initialized with the color represented by the [`CIColor`](cicolor.md) object.

## Parameters

- `color`: A color object.

## See Also

- [- initWithColor:](ciimage/1437947-initwithcolor.md)
  Initializes an image of infinite extent whose entire content is the specified color.
- [blackImage](ciimage/3074421-blackimage.md)
- [blueImage](ciimage/3074422-blueimage.md)
- [clearImage](ciimage/3074423-clearimage.md)
- [cyanImage](ciimage/3074424-cyanimage.md)
- [grayImage](ciimage/3074425-grayimage.md)
- [greenImage](ciimage/3074426-greenimage.md)
- [magentaImage](ciimage/3074427-magentaimage.md)
- [redImage](ciimage/3074428-redimage.md)
- [whiteImage](ciimage/3074429-whiteimage.md)
- [yellowImage](ciimage/3074430-yellowimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1547012-imagewithcolor)*