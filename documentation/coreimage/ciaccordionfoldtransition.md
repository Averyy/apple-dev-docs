# CIAccordionFoldTransition

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure an accordion fold transition filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIAccordionFoldTransition
```

## Topics

### Instance Properties
- [var bottomHeight: Float](ciaccordionfoldtransition/3228050-bottomheight.md)
  The height of the accordion-fold part of the transition.
- [var foldShadowAmount: Float](ciaccordionfoldtransition/3228051-foldshadowamount.md)
  A value that specifies the intensity of the shadow in the transtion.
- [var numberOfFolds: Float](ciaccordionfoldtransition/3228052-numberoffolds.md)
  The number of folds used in the transition.

## Relationships

### Inherits From
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition](cifilter/3228263-accordionfoldtransition.md)
  Transitions by folding and crossfading an image to reveal the target image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciaccordionfoldtransition)*