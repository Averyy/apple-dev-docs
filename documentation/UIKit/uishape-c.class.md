# UIShape

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An abstract representation of a shape.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```objc
@interface UIShape : NSObject
```

#### Overview

A [`UIShape`](./uishape-swift.struct.md) can represent different types of shapes, including:

- A simple shape like a rectangle or circle that resolves into a concrete shape according to context (like size and position)
- A Bézier path
- A dynamic shape that resolves using a custom closure

You typically use a [`UIShape`](./uishape-swift.struct.md) with APIs like [`UIHoverStyle`](./uihoverstyle.md) to represent the shape of an effect.

## Topics

### Creating a hover shape
- [rectShape](./uishape-c.class/rectshape.md)
  Creates a rectangular shape.
- [capsuleShape](./uishape-c.class/capsuleshape.md)
  Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.
- [circleShape](./uishape-c.class/circleshape.md)
  Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.
- [+ rectShapeWithCornerRadius:](./uishape-c.class/rectshapewithcornerradius_.md)
  Creates a rectangular shape with rounded corners, using the provided corner radius.
- [+ rectShapeWithCornerRadius:cornerCurve:](./uishape-c.class/rectshapewithcornerradius_cornercurve_.md)
  Creates a rectangular shape with rounded corners, using the provided corner radius and corner curve.
- [+ rectShapeWithCornerRadius:cornerCurve:maskedCorners:](./uishape-c.class/rectshapewithcornerradius_cornercurve_maskedcorners_.md)
  Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [+ fixedRectShapeWithRect:](./uishape-c.class/fixedrectshapewithrect_.md)
  Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.
- [+ fixedRectShapeWithRect:cornerRadius:](./uishape-c.class/fixedrectshapewithrect_cornerradius_.md)
  Creates a fixed rectangular shape with the provided corner radius, using the provided rectangle as its shape.
- [+ fixedRectShapeWithRect:cornerRadius:cornerCurve:maskedCorners:](./uishape-c.class/fixedrectshapewithrect_cornerradius_cornercurve_maskedcorners_.md)
  Creates a fixed rectangular shape with the provided corner radius and corner curve, using the provided rectangle as its shape.
- [enum UICornerCurve](./uicornercurve.md)
  The corner curve to apply to a view.
### Creating a hover shape from a custom path
- [+ shapeWithBezierPath:](./uishape-c.class/shapewithbezierpath_.md)
  Creates a shape with a custom Bézier path.
### Creating a dynamic hover shape
- [+ shapeWithProvider:](./uishape-c.class/shapewithprovider_.md)
  Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [UIShapeProvider](./uishapeprovider-31jrf.md)
  An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [- resolvedShapeInContext:](./uishape-c.class/resolvedshapeincontext_.md)
  Resolves the shape in the provided context.
- [UIShapeResolutionContext](./uishaperesolutioncontext.md)
  The context for resolving a dynamic shape.
- [UIResolvedShape](./uiresolvedshape.md)
  A shape that has completely resolved based on a context.
### Creating a shape by applying insets
- [- shapeByApplyingInsets:](./uishape-c.class/shapebyapplyinginsets_.md)
  Creates a new modified shape by applying the provided insets to this shape.
- [- shapeByApplyingInset:](./uishape-c.class/shapebyapplyinginset_.md)
  Creates a new modified shape by applying the provided inset to this shape.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [UIShapeProvider](./uishapeprovider-31jrf.md)

## See Also

### Specifying a hover shape
- [shape](./uihoverstyle/shape-55cmq.md)
  The shape to use for the hover effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-c.class)*