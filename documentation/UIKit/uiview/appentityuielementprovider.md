# appEntityUIElementProvider

**Framework**: UIKit  
**Kind**: property

return AppEntityUIElement( identifier: EntityIdentifier( for: PhotoModel.self, identifier: photo.id ), bounds: photo.frame, state: State(isSelected: photo.isSelected) ) } } } }

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

```None

> Note: The order of the returned elements isn't relevant.

If your custom view shows content you can describe with a single app entity, use the ``appEntityIdentifier`` property instead to
associate the app entity with your custom view.

For more information, refer to <doc:Making-onscreen-content-available-to-siri-and-apple-intelligence> and
<doc://com.apple.documentation/documentation/appintents>.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/appentityuielementprovider)*