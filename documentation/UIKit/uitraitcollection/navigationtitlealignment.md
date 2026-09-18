# navigationTitleAlignment

**Framework**: UIKit  
**Kind**: property

The alignment the navigation bar resolved for its title.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)

## Declaration

```swift
var navigationTitleAlignment: UINavigationItem.TitleAlignment { get }
```

#### Discussion

When the system has resolved an alignment for the title, this reports that concrete alignment, Leading or Center, even when the client has not set a preference. Otherwise it reports Automatic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/navigationtitlealignment)*