# init(templateImageName:)

**Framework**: User Notifications  
**Kind**: init  
**Role**: Initializer

Creates an action icon based on an image in your app’s bundle, preferably in an asset catalog.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(templateImageName: String)
```

```objc
+ (instancetype) iconWithTemplateImageName:(NSString *) templateImageName;
```

#### Return Value

An action icon initialized with the specified template image provided by your app.

## Parameters

- `templateImageName`: The name of a custom image in the app’s asset catalog. If the image isn’t in your app’s asset catalog, this method searches the app bundle for the image.

  You don’t need to specify the filename extension or the `@2x` or `@3x` modifiers for this name. This method retrieves the appropriate image based on the system and the available image resources.

## See Also

### Essentials
- [convenience init(systemImageName: String)](./init%28systemimagename%29.md)
  Creates an action icon by using a system symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationactionicon/init(templateimagename:))*