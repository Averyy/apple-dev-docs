# CIFlashTransition

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a flash transition filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIFlashTransition
```

## Topics

### Instance Properties
- [var center: CGPoint](ciflashtransition/3228436-center.md)
  The x and y position to use as the center of the effect.
- [var color: CIColor](ciflashtransition/3228437-color.md)
  The color of the light rays emanating from the flash.
- [var extent: CGRect](ciflashtransition/3228438-extent.md)
  The extent of the flash.
- [var fadeThreshold: Float](ciflashtransition/3228439-fadethreshold.md)
  The amount of fade between the flash and the target image.
- [var maxStriationRadius: Float](ciflashtransition/3228440-maxstriationradius.md)
  The radius of the light rays emanating from the flash.
- [var striationContrast: Float](ciflashtransition/3228441-striationcontrast.md)
  The contrast of the light rays emanating from the flash.
- [var striationStrength: Float](ciflashtransition/3228442-striationstrength.md)
  The strength of the light rays emanating from the flash.

## Relationships

### Inherits From
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func flashTransition() -> any CIFilter & CIFlashTransition](cifilter/3228326-flashtransition.md)
  Creates a flash of light to transition between two images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciflashtransition)*