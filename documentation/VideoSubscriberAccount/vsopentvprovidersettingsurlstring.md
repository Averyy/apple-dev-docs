# VSOpenTVProviderSettingsURLString

**Framework**: Video Subscriber Account  
**Kind**: var  
**Role**: Global Variable

A URL string you use to deep link to the system’s TV Provider settings.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
let VSOpenTVProviderSettingsURLString: String
```

```c
extern NSString * const VSOpenTVProviderSettingsURLString;
```

#### Discussion

Pass this URL to [`open(_:options:completionHandler:)`](../UIKit/uiapplication/open%28_,options,completionhandler%29.md) to open the Settings app and show the TV Provider settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsopentvprovidersettingsurlstring)*