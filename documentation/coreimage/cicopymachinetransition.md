# CICopyMachineTransition

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a copy machine transition filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CICopyMachineTransition
```

## Topics

### Instance Properties
- [var angle: Float](cicopymachinetransition/3228189-angle.md)
  The angle of the copier light.
- [var color: CIColor](cicopymachinetransition/3228190-color.md)
  The color of the copier light.
- [var extent: CGRect](cicopymachinetransition/3228191-extent.md)
  A rectangle that defines the extent of the effect.
- [var opacity: Float](cicopymachinetransition/3228192-opacity.md)
  The opacity of the copier light.
- [var width: Float](cicopymachinetransition/3228193-width.md)
  The width of the copier light.

## Relationships

### Inherits From
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func copyMachineTransition() -> any CIFilter & CICopyMachineTransition](cifilter/3228304-copymachinetransition.md)
  Simulates the effect of a copy machine scanner light to transiton between two images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicopymachinetransition)*