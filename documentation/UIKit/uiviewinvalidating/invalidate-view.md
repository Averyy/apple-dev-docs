# invalidate(view:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Indicates to the system that an aspect of a view is invalid and triggers the necessary update.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
func invalidate(view: UIView)
```

#### Discussion

A type that conforms to [`UIViewInvalidating`](uiviewinvalidating.md) implements this method to perform any actions necessary to notify the system that an aspect of your view is invalid. For more info, see [`UIView.Invalidating`](uiview/invalidating.md).

## Parameters

- `view`: The view that requires invalidating.

## See Also

- [UIView.Invalidations](uiview/invalidations.md)
  Changes that cause an aspect of a view to be invalid and require an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewinvalidating/invalidate(view:))*