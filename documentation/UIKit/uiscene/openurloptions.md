# UIScene.OpenURLOptions

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Options that UIKit provides when asking your app to open a URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class OpenURLOptions
```

```objc
@interface UISceneOpenURLOptions : NSObject
```

## Overview

Don’t create a [`UIScene.OpenURLOptions`](./openurloptions.md) object directly. UIKit creates one for you when your app receives a request to open a URL. Use the information in the object to determine how to respond to the URL.

## Topics

### Specifying the URL details
- [var sourceApplication: String?](./openurloptions/sourceapplication.md)
  The bundle ID of the app that originated the request.
- [var annotation: Any?](./openurloptions/annotation.md)
  A property-list object that contains the annotation data provided by a document interaction controller.
- [var eventAttribution: UIEventAttribution?](./openurloptions/eventattribution.md)
  An event attribution associated with the URL to open.
### Specifying the behavior options
- [var openInPlace: Bool](./openurloptions/openinplace.md)
  A Boolean value that indicates whether you should open the URL at its current location instead of copying it to your app’s container.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Getting the URL
- [var url: URL](../uiopenurlcontext/url.md)
  The URL to open.
- [var options: UIScene.OpenURLOptions](../uiopenurlcontext/options.md)
  Additional information for determining how to open the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openurloptions)*