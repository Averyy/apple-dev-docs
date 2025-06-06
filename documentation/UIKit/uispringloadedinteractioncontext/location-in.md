# location(in:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the location of the drag activity within the specified view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func location(in view: UIView?) -> CGPoint
```

#### Return Value

A point in the local coordinate system of `view`.

#### Discussion

To get the location of the drag activity within the window, use `nil` for the view.

## Parameters

- `view`: The view that is used to determine the location of the drag activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractioncontext/location(in:))*