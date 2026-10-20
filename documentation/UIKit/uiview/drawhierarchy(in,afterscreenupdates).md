# drawHierarchy(in:afterScreenUpdates:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Renders a snapshot of the complete view hierarchy as visible onscreen into the current context.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func drawHierarchy(in rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool
```

```objc
- (BOOL) drawViewHierarchyInRect:(CGRect) rect afterScreenUpdates:(BOOL) afterUpdates;
```

#### Return Value

Returns [`true`](../../Swift/true.md) if the snapshot is complete, or [`false`](../../Swift/false.md) if the snapshot is missing image data for any view in the hierarchy.

#### Discussion

Use this method when you want to apply a graphical effect, such as a blur, to a view snapshot. This method is not as fast as the [`snapshotView(afterScreenUpdates:)`](./snapshotview%28afterscreenupdates%29.md) method.

## Parameters

- `rect`: A rectangle specified in the local coordinate system (bounds) of the view.
- `afterUpdates`: A Boolean value that indicates whether the snapshot should be rendered after recent changes have been incorporated. Specify the value [`false`](../../Swift/false.md) if you want to render a snapshot in the view hierarchy’s current state, which might not include recent changes.

## See Also

### Capturing a view snapshot
- [func snapshotView(afterScreenUpdates: Bool) -> UIView?](./snapshotview%28afterscreenupdates%29.md)
  Returns a snapshot view based on the contents of the current view.
- [func resizableSnapshotView(from: CGRect, afterScreenUpdates: Bool, withCapInsets: UIEdgeInsets) -> UIView?](./resizablesnapshotview%28from,afterscreenupdates,withcapinsets%29.md)
  Returns a snapshot view based on the specified contents of the current view, with stretchable insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/drawhierarchy(in:afterscreenupdates:))*