# traitCollection

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The traits, such as the size class and scale factor, that describe the current environment of the object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var traitCollection: UITraitCollection { get }
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Discussion

[`UIViewController`](uiviewcontroller.md) and [`UIView`](uiview.md) adopt the [`UITraitEnvironment`](uitraitenvironment.md) protocol and expose this property.

> ❗ **Important**:  Don’t implement this property in your own objects. Instead, use the [`traitCollection`](uitraitenvironment/traitcollection.md) property associated with a view, view controller, or other object to determine the currently available trait information.

 Don’t implement this property in your own objects. Instead, use the [`traitCollection`](uitraitenvironment/traitcollection.md) property associated with a view, view controller, or other object to determine the currently available trait information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitenvironment/traitcollection)*