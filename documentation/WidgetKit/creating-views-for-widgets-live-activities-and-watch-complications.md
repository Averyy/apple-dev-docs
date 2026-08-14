# Creating views for widgets, Live Activities, and watch complications

**Framework**: WidgetKit

Implement glanceable views with WidgetKit and SwiftUI.

#### Overview

SwiftUI and WidgetKit power widgets, Live Activities, and watch complications. Because they use the same technology and share design similarities, plan your WidgetKit adoption before you start creating these features. Start simple and add complexity later; for example, start by adding a widget extension as described in [`Creating a widget extension`](creating-a-widget-extension.md) and support one widget size. Spend time to make sure it offers a focused, glanceable experience. Then, add support for additional widget sizes and features like configurability, animations, and interactivity.

> **Note**: [`Session 10027: Bring widgets to new places`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10027)

If you’re new to using WidgetKit, see [`Developing a WidgetKit strategy`](developing-a-widgetkit-strategy.md).

##### Use System Font Styles

Widgets, Live Activities, and watch complications appear adjacent to other widgets or complications. As a result, a consistent look for your content that fits in well with the other elements needs to be a priority. To achieve a consistent look for your widgets and complications, use system fonts, default font parameters, and the following font styles:

- [`Font.TextStyle.headline`](https://developer.apple.com/documentation/swiftui/font/textstyle/headline)
- [`Font.TextStyle.title`](https://developer.apple.com/documentation/swiftui/font/textstyle/title)
- [`Font.TextStyle.body`](https://developer.apple.com/documentation/swiftui/font/textstyle/body)
- [`Font.TextStyle.caption`](https://developer.apple.com/documentation/swiftui/font/textstyle/caption)

##### Make Sure Text Fits the Available Space

Widgets and watch complications offer limited space for content — especially on the Lock Screen or on Apple Watch. Give careful consideration to the amount of text you display. For example, say you support the [`WidgetFamily.accessoryInline`](widgetfamily/accessoryinline.md) widget. It can include an image and text. However, the amount of displayable characters varies depending on the context where the widget appears. On Apple Watch, the size of the inline complication varies depending on the watch face. Include it in a [`ViewThatFits`](https://developer.apple.com/documentation/swiftui/viewthatfits) view to make sure text always fits the available space.

> **Note**: Test your widgets with every language you support, especially if you support languages that commonly have words with a lot of characters, such as German.

##### Use Content Margins Instead of Safe Areas

watchOS 9, iOS 16, iPadOS 16, macOS 13, and earlier use system-defined safe areas to keep content from getting too close to the edge of the widget, complication, or Live Activity. You likely don’t change the safe areas that the system defines. However, you might use the [`ignoresSafeArea(_:edges:)`](https://developer.apple.com/documentation/swiftui/view/ignoressafearea(_:edges:)) view modifier to extend content farther than the safe area.

WidgetKit complications, and Live Activities use content margins instead of safe areas. As a result, `ignoresSafeArea(_:edges:)` has no effect. Instead, use the [`contentMarginsDisabled()`](https://developer.apple.com/documentation/swiftui/widgetconfiguration/contentmarginsdisabled()) view modifier to define custom content margins.

If you use `ignoresSafeArea(_:edges:)`, follow these steps:

1. Add the `contentMarginsDisabled()` view modifier to your widget configuration.
2. For any content that you intend to remain inside system-defined content margins, make use of [`padding(_:)`](https://developer.apple.com/documentation/swiftui/view/padding(_:)) as needed.

> 💡 **Tip**: To access the system’s default content margins for an environment, use the [`widgetContentMargins`](https://developer.apple.com/documentation/swiftui/environmentvalues/widgetcontentmargins) environment variable.

## See Also

- [SwiftUI views for widgets](swiftui-views.md)
  Present your app’s content in widgets with SwiftUI views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/creating-views-for-widgets-live-activities-and-watch-complications)*