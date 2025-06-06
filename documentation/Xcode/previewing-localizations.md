# Previewing localizations

**Framework**: Xcode

Test localizations in the SwiftUI preview or the Interface Builder preview.

#### Overview

You can preview localizations early in development while you lay out your app’s interface for both SwiftUI and Interface Builder apps. For SwiftUI apps, you need to add the language or import the localization before you preview it, described in [`Adding support for languages and regions`](adding-support-for-languages-and-regions.md) and [`Importing localizations`](importing-localizations.md). For Interface Builder apps, you can first preview the interface in pseudolanguages and then later in the localizations you add.

##### Add Localizations to a Swiftui Preview

For SwiftUI apps, you can preview a localization by setting the [`locale`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/locale) environment variable in your code. Use the [`environment(_:_:)`](https://developer.apple.com/documentation/SwiftUI/View/environment(_:_:)) function to set the locale for all views in the view hierarchy of a SwiftUI preview. For example, if you add German to your project, you can set the locale to German (`de`):

```swift
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
                .environment(\.locale, .init(identifier: "de"))
    }
}
```

To preview right-to-left languages, also set the [`layoutDirection`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/layoutDirection) key to [`LayoutDirection.rightToLeft`](https://developer.apple.com/documentation/SwiftUI/LayoutDirection/rightToLeft).

To preview multiple localizations, add additional previews to your code and set the [`locale`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/locale) environment value for each. The localizations appear in the SwiftUI preview.

![Screenshot of the project editor with the ContentView.swift file selected in the navigator and the line of code that sets the locale highlighted, and its preview on the right.](https://docs-assets.developer.apple.com/published/caed099e42d282474b9c755cf3df1f9e/previewing-localizations-1%402x.png)

##### Preview Localizations in Interface Builder

For Interface Builder, you can preview localizations any time during development by choosing localizations including pseudolanguages in the preview. You don’t need to build and run your app to see the preview.

In Interface Builder, select the desired view controller. Click the Adjust Editor Options button in the upper-right corner, then choose Preview. A preview of the layout appears to the right of the canvas.

In the preview area, select a preview or click in the background to deselect all previews. If you don’t select a preview, you’ll change the language of all previews. Click the language button—for example, English—in the lower-right corner. In the pop-up menu that appears, choose a localization or pseudolanguage.

![Screenshot of Interface Builder showing previews of a view controller scene and the location of the language pop-up menu in the lower-right corner.](https://docs-assets.developer.apple.com/published/c1674e7c2bbc8d7d5f93484a58d70768/previewing-localizations-2%402x.png)

## See Also

- [Adding support for languages and regions](adding-support-for-languages-and-regions.md)
  Select the resources that you want to localize for each language and region you support.
- [Importing localizations](importing-localizations.md)
  Import the files that you translate or adapt for a language and region into your project.
- [struct EnvironmentValues](../SwiftUI/EnvironmentValues.md)
  A collection of environment values propagated through a view hierarchy.
- [Testing localizations when running your app](testing-localizations-when-running-your-app.md)
  Run your app in each language and region you support to thoroughly test your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/previewing-localizations)*