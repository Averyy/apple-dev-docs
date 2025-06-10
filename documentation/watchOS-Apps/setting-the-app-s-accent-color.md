# Setting the app’s accent color

**Framework**: watchOS apps

Set your app’s accent color.

#### Overview

Every Apple Watch app has an accent color that the system applies to the following UI elements:

- The app’s title string in the status bar
- The app’s name in short-look notifications

You can access the accent color from the [`accentColor`](https://developer.apple.com/documentation/SwiftUI/Color/accentColor) property.

> **Note**: If your accent color is dark, your text may not be legible against the black background. Consider lightening or saturating your accent color to improve the contrast.

##### Set the Accent Color

Xcode automatically configures an asset catalog that includes the accent color when you create a new project. To set the color, open the WatchKit App’s `Assets.xcassets` file, select the AccentColor color set, and then select the AccentColor cell. You can then change the color using the Color section of the Attributes inspector. For example, to specify the RGB values for a color, change the Content to sRGB and then modify the values using the sliders.

![A screenshot showing how to set the accent color using the sRGB controls.](https://docs-assets.developer.apple.com/published/83ee257cfcf8a8fa85aac7ef02171352/setting-the-app-s-accent-color-1%402x.png)

Alternatively, you can click the Show Color Panel button, and select a color from the system color panel.

##### Update Existing Projects

If you’re updating an older project, you can manually set up the asset catalog.

To set the accent color:

1. Open the WatchKit App’s asset catalog.
2. Select the Editor > Add New Asset > Color Set menu item to add a new color set to the asset catalog.
3. In the WatchKit app’s Build Settings, set the Global Accent Color Name to your color set’s name.

![An Xcode screenshot that shows the Global Accent Color Name in the WatchKit app’s Build Settings.](https://docs-assets.developer.apple.com/published/a3a6378b5dcb6a455adfc38d68b13da8/setting-the-app-s-accent-color-2%402x.png)

##### Support Older Operating Systems

In watchOS 6 and earlier, set the Global Tint property instead of the Global Accent Color. To set this property, open the storyboard, and select the File inspector.

![An Xcode screenshot that shows the Global Tint property in the storyboard’s File inspector.](https://docs-assets.developer.apple.com/published/d3ec257de01ef104571965a076d5c94c/setting-the-app-s-accent-color-3%402x.png)

Click the Global Tint pop-up button to display a menu with several preexisting colors, plus the option to open a color picker and specify a custom color.

## See Also

- [Building a productivity app for Apple Watch](building-a-productivity-app-for-apple-watch.md)
  Create a watch app to manage and share a task list and visualize the status with a chart.
- [Supporting multiple watch sizes](supporting-multiple-watch-sizes.md)
  Customize the layout of your user interface to support all Apple Watch sizes.
- [Designing your app for the Always On state](designing-your-app-for-the-always-on-state.md)
  Customize your watchOS app’s user interface for continuous display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/setting-the-app-s-accent-color)*