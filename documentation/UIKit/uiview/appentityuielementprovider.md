# appEntityUIElementProvider

**Framework**: UIKit  
**Kind**: property

A closure that provides app entity identifiers to make custom view content discoverable by Apple Intelligence and Siri when it appears onscreen.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency var appEntityUIElementProvider: ((UIView, AppEntityUIElementsContext) -> [AppEntityUIElement])? { get set }
```

#### Discussion

Dynamically provide app entity identifiers for a custom view where your app manages state for the user interface or you use custom drawing to render the interface. For example, you might use a custom list or tab implementation and manage selection and other states in the app, or you might use Metal to render the interface. If either applies to your app’s interface, make content discoverable by Apple Intelligence and Siri using `appEntityUIElementProvider` and provide the system with a list of `AppEntityUIElements`.

For example, a web browser with tabs might provide context to Apple Intelligence like this:

```swift

class BrowserTabView: UIView {

    // Call this methid when the tab or selection state changes.
    func updateEntityAnnotation() {
        // This example stores state from self as local variables that are then
        // captured by the closure. Setting a new closure when any captured state
        // changes is inexpensive, making this a good option. Alternatively, weakly
        /// capture `self` or cast the `view` in the closure to `BrowserTabView`
        // and read state directly from the view when the closure executes.
        let browserTab: BrowserTab = self.browserTab // model object
        let isSelected: Bool = self.isSelected // whether tab is selected

        self.appEntityUIElementProvider = { view, context in
           [AppEntityUIElement(
                identifier: EntityIdentifier(
                    for: BrowserTabEntity.self,
                    identifier: browserTab.id
                ),
                bounds: view.bounds,
                state: State(isSelected: isSelected)
            )]
        }
    }
}
```

A photo viewing app that uses Metal to render a photo grid might make content discoverable by Apple Intelligence and Siri like this:

```swift
class MetalPhotoGridController: UIViewController {

    // Call this method when the set of displayed photos changes, or when a photo's UI state
    // changes; for example, when a person selects photos int the grid.
    func updateEntityProvider() {
        // This example stores state from self as local variables that are then
        // captured by the closure. Setting a new closure when any captured state
        // changes is inexpensive, making this a good option. Alternatively, weakly
        /// capture `self` or cast the `view` in the closure to `BrowserTabView`
        // and read state directly from the view when the closure executes.
        let displayedPhotos: [PhotoModel] = self.displayedPhotos // model objects

        self.view.appEntityUIElementProvider = { view, context in
            displayedPhotos.compactMap { photo in
                // Note: `photo.frame` assumed to be in `view` coordinates already!
                guard photo.frame.intersects(context.queryRect) ||
                      photo.isSelected else {
                    return nil
                }

                return AppEntityUIElement(
                    identifier: EntityIdentifier(
                        for: PhotoModel.self,
                        identifier: photo.id
                    ),
                    bounds: photo.frame,
                    state: State(isSelected: photo.isSelected)
                )
            }
        }
    }
}
```

> **Note**: The order of the returned elements isn’t relevant.

If your custom view shows content you can describe with a single app entity, use the [`appEntityIdentifier`](uiview/appentityidentifier.md) property instead to associate the app entity with your custom view.

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [`App Intents`](https://developer.apple.com/documentation/appintents).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/appentityuielementprovider)*