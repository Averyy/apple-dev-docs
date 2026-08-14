# appEntityIdentifier

**Framework**: UIKit  
**Kind**: property

The identifier of an app entity that you associate with a custom view.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency var appEntityIdentifier: EntityIdentifier? { get set }
```

#### Discussion

Associate your view with one app entity to make it discoverable by Apple Intelligence and Siri when the view appears onscreen. For example, when a person taps an item in a list to view the detail view for the item, expose the item to Apple Intelligence and Siri using the `appEntityIdentifier`. If your custom view shows several separate items; for example, if you use a custom list implementation that manages selection states itself; use [`appEntityUIElementProvider`](uiview/appentityuielementprovider.md) to provide the system with a list of items.

To clear the association with the app entity, set `appEntityIdentifier` to `nil`.

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [`App Intents`](https://developer.apple.com/documentation/appintents).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/appentityidentifier)*