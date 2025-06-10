# Understanding a drag item as a promise

**Framework**: UIKit

Use drag items to convey data representation promises between a source app and a destination app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

#### Overview

When a user drags an onscreen visual representation of an item in your app, such as a photo, a Maps location, a Calendar event, or a text selection, your app associates the underlying data with a . The drag item, in turn, uses an . Your app populates the item provider’s [`registeredTypeIdentifiers`](https://developer.apple.com/documentation/Foundation/NSItemProvider/registeredTypeIdentifiers) array with [`uniform type identifiers (UTIs)`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html).

![A drag item with its contained item provider and array of uniform type identifiers](https://docs-assets.developer.apple.com/published/f3295ba2321f55ef49342ac6d5c16a6e/media-2903721%402x.png)

The array of UTIs constitutes the source app’s promise about the specific data representations it can deliver, on request, to a destination app. The term  means that, at the time your app constructs a drag item, it commits to providing certain data representations but doesn’t yet perform the work to create them. Although it appears to the user that the item itself is being dragged, the drag item instead consists of promises along with a preview image that remains under the user’s touch point onscreen.

The portion of your app that constructs the drag item is the  ([`UIDragInteractionDelegate`](uidraginteractiondelegate.md)). On the destination side, an app’s  ([`UIDropInteractionDelegate`](uidropinteractiondelegate.md)) interacts with the drag item to consume promised data.

This table shows the protocols you implement to support constructing or consuming a drag item, depending on whether a view in your app is acting as a source or destination:

| Drag-and-drop role | Protocol | Your implementation |
| --- | --- | --- |
| Source app | [`NSItemProviderWriting`](https://developer.apple.com/documentation/Foundation/NSItemProviderWriting) | Register UTIs |
| Destination app | [`NSItemProviderReading`](https://developer.apple.com/documentation/Foundation/NSItemProviderReading) | Request items |

The following classes automatically support these protocols: [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString), [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL), [`UIColor`](uicolor.md), and [`UIImage`](uiimage.md).

## See Also

- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
  Adopt drag interaction APIs to provide items for dragging.
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)
  Adopt drop interaction APIs to selectively consume dragged content.
- [Adopting drag and drop in a custom view](adopting-drag-and-drop-in-a-custom-view.md)
  Demonstrates how to enable drag and drop for a `UIImageView` instance.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md)
  Demonstrates how to enable and implement drag and drop for a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/understanding-a-drag-item-as-a-promise)*