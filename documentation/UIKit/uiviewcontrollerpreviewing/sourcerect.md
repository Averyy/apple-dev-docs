# sourceRect

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var sourceRect: CGRect { get set }
```

#### Discussion

Use this property if you want to specify a preview indication area that is different than the bounds of the view in the [`sourceView`](uiviewcontrollerpreviewing/sourceview.md) property. Set this property’s value in your object’s [`previewingContext(_:viewControllerForLocation:)`](uiviewcontrollerpreviewingdelegate/previewingcontext(_:viewcontrollerforlocation:).md) method.

The default value of this property corresponds to the bounds of the view in the [`sourceView`](uiviewcontrollerpreviewing/sourceview.md) property.

For example, if your source view is a table view, you can set the `sourceRect` property to the frame of the row under the user’s touch. The row then remains visually sharp when a user presses it, while surrounding content blurs, thereby indicating to the user that it is the row being touched that has a preview available.

You can change the value of this property at runtime.

## See Also

- [var sourceView: UIView](uiviewcontrollerpreviewing/sourceview.md)
  A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user.
- [var previewingGestureRecognizerForFailureRelationship: UIGestureRecognizer](uiviewcontrollerpreviewing/previewinggesturerecognizerforfailurerelationship.md)
  A gesture recognizer suitable for setting up failure requirements for a preview’s (peek’s) gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/sourcerect)*