# initWithRect:

**Framework**: Core Image  
**Kind**: instm

Initializes a filter shape object with a rectangle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
- (instancetype)initWithRect:(CGRect)r;
```

#### Return_value

An initialized CIFilterShape object, or `nil` if the method fails.

## Parameters

- `r`: A rectangle. Core Image uses the rectangle specified by integer parts of the values in the   data structure.

## See Also

- [+ shapeWithRect:](cifiltershape/1562074-shapewithrect.md)
  Creates a filter shape object and initializes it with a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltershape/1437921-initwithrect)*