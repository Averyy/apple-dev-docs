# navigationTitleAlignment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The alignment the navigation bar resolved for its title.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```swift
var navigationTitleAlignment: UINavigationItem.TitleAlignment { get }
```

```objc
@property (nonatomic, assign, readonly) UINavigationItemTitleAlignment navigationTitleAlignment;
```

#### Discussion

When the system has resolved an alignment for the title, this reports that concrete alignment, Leading or Center, even when the client has not set a preference. Otherwise it reports Automatic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/navigationtitlealignment)*