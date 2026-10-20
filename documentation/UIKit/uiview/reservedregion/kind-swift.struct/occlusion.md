# occlusion

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A region that covers part of your view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
static let occlusion: UIView.ReservedRegion.Kind
```

#### Discussion

An occlusion region is an area where an element, such as the Dynamic Island, a camera, or window controls, cover your content. Place important views and controls outside this area so people can see and use them.

## See Also

### Getting reserved region kinds
- [static let division: UIView.ReservedRegion.Kind](./division.md)
  A region that splits your view into separate parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregion/kind-swift.struct/occlusion)*