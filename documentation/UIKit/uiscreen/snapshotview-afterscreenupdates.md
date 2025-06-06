# snapshotView(afterScreenUpdates:)

**Framework**: UIKit  
**Kind**: method

Returns a snapshot view based on the current screen contents.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func snapshotView(afterScreenUpdates afterUpdates: Bool) -> UIView
```

#### Return Value

A new view object containing a snapshot of the screen’s rendered contents.

#### Discussion

This method captures the current visual contents of the screen from the render server and uses them to build a new snapshot view. You can use the returned snapshot view as a visual stand-in for the screen’s contents in your app. For example, you might use a snapshot view to facilitate a full screen animation. Because the content is captured from the already rendered content, this method reflects the current visual appearance of the screen and is not updated to reflect animations that are scheduled or in progress. However, this method is faster than trying to render the contents of the screen into a bitmap image yourself.

Because the returned snapshot view is still a view object, you may modify it and its layer object as needed. However, you cannot change the [`contents`](https://developer.apple.com/documentation/QuartzCore/CALayer/contents) property of the snapshot view’s layer and attempts to do so will fail silently. If any onscreen views have not yet been committed to the render server, that portion of the snapshot will have no content.

## Parameters

- `afterUpdates`: A Boolean value that indicates whether the snapshot should be taken after recent changes have been incorporated. Specify the value   if you want to capture the screen in its current state, which might not include recent changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/snapshotview(afterscreenupdates:))*