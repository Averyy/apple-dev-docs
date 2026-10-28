# init(systemImageName:)

**Framework**: User Notifications  
**Kind**: init  
**Role**: Initializer

Creates an action icon by using a system symbol image.

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
convenience init(systemImageName: String)
```

```objc
+ (instancetype) iconWithSystemImageName:(NSString *) systemImageName;
```

## Return Value

An action icon that the system initializes with the system symbol image that your app specifies.

## Parameters

- `systemImageName`: The name of the system symbol image. Use the SF Symbols app to look up the names of system symbol images. Download this app from the design resources page at [developer.apple.com](https://developer.apple.com/design/resources/).

## See Also

### Essentials
- [convenience init(templateImageName: String)](./init%28templateimagename%29.md)
  Creates an action icon based on an image in your app’s bundle, preferably in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationactionicon/init(systemimagename:))*