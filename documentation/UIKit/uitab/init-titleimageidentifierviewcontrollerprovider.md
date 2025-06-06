# init(title:image:identifier:viewControllerProvider:)

**Framework**: UIKit  
**Kind**: init

Creates a tab object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
init(title: String, image: UIImage?, identifier: String, viewControllerProvider: ((UITab) -> UIViewController)? = nil)
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

## Parameters

- `title`: The tab’s title.
- `image`: The tab’s image.
- `identifier`: An identifier string for the tab. Each identifier must be unique across all the tabs managed by a  .
- `viewControllerProvider`: The view controller that the system presents when someone selects the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitab/init(title:image:identifier:viewcontrollerprovider:))*