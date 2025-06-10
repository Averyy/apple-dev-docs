# primaryBackgroundStyle

**Framework**: UIKit  
**Kind**: property

The background style of the primary view controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var primaryBackgroundStyle: UISplitViewController.BackgroundStyle { get set }
```

## Mentions

- [Optimizing your iPad app for Mac](optimizing-your-ipad-app-for-mac.md)

#### Discussion

In macOS, the sidebar of a split view shows a blurred desktop behind its view. To achieve this effect in your iPad app when it runs in macOS, set [`primaryBackgroundStyle`](uisplitviewcontroller/primarybackgroundstyle.md) to [`UISplitViewController.BackgroundStyle.sidebar`](uisplitviewcontroller/backgroundstyle/sidebar.md). Set the style to [`UISplitViewController.BackgroundStyle.none`](uisplitviewcontroller/backgroundstyle/none.md) when you want to control the background appearance of the primary view controller.

> **Note**:  Setting the background style to [`UISplitViewController.BackgroundStyle.sidebar`](uisplitviewcontroller/backgroundstyle/sidebar.md) has no effect when your app is running in iOS or tvOS.

## See Also

- [UISplitViewController.BackgroundStyle](uisplitviewcontroller/backgroundstyle.md)
  Styles that apply a visual effect to the background of a primary view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/primarybackgroundstyle)*