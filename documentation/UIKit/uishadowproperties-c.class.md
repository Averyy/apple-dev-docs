# UIShadowProperties

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```objc
@interface UIShadowProperties : NSObject
```

## Topics

### Instance Properties
- [color](./uishadowproperties-c.class/color.md)
  The color to use when rendering the shadow. Defaults to `UIColor.blackColor`.
- [offset](./uishadowproperties-c.class/offset.md)
  The offset, in points, of the layer’s shadow. Defaults to `CGSizeZero`.
- [opacity](./uishadowproperties-c.class/opacity.md)
  The shadow’s opacity. Defaults to `0.0`.
- [path](./uishadowproperties-c.class/path.md)
  The path that is used to create the shadow. When `nil`, the shadow will be rendered to match the bounds of the view that it is applied to. Defaults to `nil`.
- [radius](./uishadowproperties-c.class/radius.md)
  The blur radius, in points, used to render the shadow. Defaults to `0.0`.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Customizing the background
- [customView](./uibackgroundconfiguration-c.class/customview.md)
  A custom view for the background.
- [cornerRadius](./uibackgroundconfiguration-c.class/cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the background and stroke.
- [backgroundInsets](./uibackgroundconfiguration-c.class/backgroundinsets.md)
  The insets (or outsets, if negative) for the background and stroke, relative to the edges of the containing view.
- [edgesAddingLayoutMarginsToBackgroundInsets](./uibackgroundconfiguration-c.class/edgesaddinglayoutmarginstobackgroundinsets.md)
  The edges on which the configuration adds the containing view’s layout margins to the background insets.
- [backgroundColor](./uibackgroundconfiguration-c.class/backgroundcolor.md)
  The color of the background.
- [backgroundColorTransformer](./uibackgroundconfiguration-c.class/backgroundcolortransformer.md)
  The color transformer for resolving the background color.
- [- resolvedBackgroundColorForTintColor:](./uibackgroundconfiguration-c.class/resolvedbackgroundcolorfortintcolor_.md)
  Generates the resolved background color for the specified tint color, using the background color and color transformer.
- [visualEffect](./uibackgroundconfiguration-c.class/visualeffect.md)
  The visual effect that the configuration applies to the background.
- [shadowProperties](./uibackgroundconfiguration-c.class/shadowproperties.md)
  Describes a shadow applied by the background. Defaults to no shadow (i.e. a shadow with an opacity of 0.0).
- [strokeColor](./uibackgroundconfiguration-c.class/strokecolor.md)
  The color of the stroke.
- [strokeColorTransformer](./uibackgroundconfiguration-c.class/strokecolortransformer.md)
  The color transformer for resolving the stroke color.
- [- resolvedStrokeColorForTintColor:](./uibackgroundconfiguration-c.class/resolvedstrokecolorfortintcolor_.md)
  Generates the resolved stroke color for the specified tint color, using the stroke color and color transformer.
- [strokeWidth](./uibackgroundconfiguration-c.class/strokewidth.md)
  The width of the stroke.
- [strokeOutset](./uibackgroundconfiguration-c.class/strokeoutset.md)
  The outset (or inset, if negative) for the stroke.
- [image](./uibackgroundconfiguration-c.class/image.md)
  The image displayed in the view’s background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishadowproperties-c.class)*