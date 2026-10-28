# activityItemsConfigurationSource

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that can provide shareable items for a scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var activityItemsConfigurationSource: (any UIActivityItemsConfigurationProviding)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIActivityItemsConfigurationProviding> activityItemsConfigurationSource;
```

## Discussion

When a user asks Siri to “share this” on iOS, or clicks an [`NSSharingServicePickerToolbarItem`](../../AppKit/nssharingservicepickertoolbaritem.md) in the toolbar of an app built with Mac Catalyst, the system asks the current scene or view controller what to share. You can supply multiple representations of the current content, such as a file, image, and URL.

You can implement this property or provide configurations from view controllers with [`activityItemsConfiguration`](../uiactivityitemsconfigurationproviding/activityitemsconfiguration.md).

If you don’t provide a [`UIActivityItemsConfiguration`](../uiactivityitemsconfiguration.md) in either of these ways, the system may fall back to sharing either the [`webpageURL`](../../Foundation/nsuseractivity/webpageurl.md) of your app’s current user activity or a screenshot of the scene.

## See Also

### Sharing content
- [protocol UIActivityItemsConfigurationProviding](../uiactivityitemsconfigurationproviding.md)
  An interface that provides a source for shareable content to fulfill user requests to share current content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activityitemsconfigurationsource)*