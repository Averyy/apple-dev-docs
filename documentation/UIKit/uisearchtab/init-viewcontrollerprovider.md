# init(viewControllerProvider:)

**Framework**: UIKit  
**Kind**: init

Creates a search tab with a system localized title and image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
init(viewControllerProvider: ((UITab) -> UIViewController)? = nil)
```

## Parameters

- `viewControllerProvider`: The view controller that the system presents when someone selects the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtab/init(viewcontrollerprovider:))*