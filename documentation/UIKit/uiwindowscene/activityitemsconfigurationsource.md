# activityItemsConfigurationSource

**Framework**: UIKit  
**Kind**: property

An object that can provide shareable items for a scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var activityItemsConfigurationSource: (any UIActivityItemsConfigurationProviding)? { get set }
```

#### Discussion

When a user asks Siri to “share this” on iOS, or clicks an [`NSSharingServicePickerToolbarItem`](https://developer.apple.com/documentation/AppKit/NSSharingServicePickerToolbarItem) in the toolbar of an app built with Mac Catalyst, the system asks the current scene or view controller what to share. You can supply multiple representations of the current content, such as a file, image, and URL.

You can implement this property or provide configurations from view controllers with [`activityItemsConfiguration`](uiactivityitemsconfigurationproviding/activityitemsconfiguration.md).

If you don’t provide a [`UIActivityItemsConfiguration`](uiactivityitemsconfiguration.md) in either of these ways, the system may fall back to sharing either the [`webpageURL`](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) of your app’s current user activity or a screenshot of the scene.

## See Also

- [protocol UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
  An interface that provides a source for shareable content to fulfill user requests to share current content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activityitemsconfigurationsource)*