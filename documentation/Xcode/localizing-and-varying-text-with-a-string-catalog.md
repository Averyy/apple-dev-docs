# Localizing and varying text with a string catalog

**Framework**: Xcode

Use a string catalog to translate text, handle plurals, and vary the text your app displays on specific devices.

#### Overview

Your app delivers the best experience when it runs well in a person’s locale and displays content in their native language. Supporting multiple languages is more than translating text. It includes handling plurals for nouns and units, as well as displaying the right form of text on specific devices.

![None](https://docs-assets.developer.apple.com/published/ca1cd2ff0166df7b3fb34dee9d839e39/localizing-and-varying-text-with-a-string-catalog-0-hero%402x.png)

Use a string catalog to localize and translate all your app’s text in a visual editor right in Xcode. A string catalog automatically tracks all the localizable strings from your code, and keeps your translations in one place.

Use string catalogs to host translations, configure pluralization messages for different regions and locales, and change how text appears on different devices.

> **Note**: Session 10155: [`Discover String Catalogs`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10155)

##### Localize Your Apps Text

Before you can translate text, you need to make it localizable. This involves wrapping the user-facing strings in your app in constructs that make them translatable.

In SwiftUI, all string literals within a view are automatically localizable.

```swift
// SwiftUI localizable text.
Text("Welcome")
```

Make general text localizable using the `String(localized:)` initializer. For apps targeting older platforms, use the `NSLocalizedString` macro.

```swift
// General localizable text.
String(localized: "Buy a book"))
```

Add comments to give context and assist localizers when translating your text.

```swift
// Localizable text with comments.
Text("Explore", comment: "The title of the tab bar item that navigates to the Explore screen.")
String(localized: "Get Started", comment: "The label on the Get Started button that appears after they sign in.")
```

##### Add a String Catalog to Your Project

To add a string catalog to your project, choose File > New > File.

In the sheet that appears, select the platform, enter `string` into the filter field, select String Catalog, and click Next. In the dialog that appears, accept the default name `Localizable`, choose a location, and click Create.

![An Xcode screenshot showing the new file template with a string catalog file selected and highlighted.](https://docs-assets.developer.apple.com/published/6f463d0afd212879f7b1fa591e5311e2/localizing-and-varying-text-with-a-string-catalog-1-add-a-string-catalog%402x.png)

If your string catalog gets too big, you can create multiple string catalog files within a single Xcode project, and give each a unique name. Then choose which string catalog to use for each translation by passing the string catalog name to the `tableName` or `table` parameter to the respective localization API as follows:

```swift
// A SwiftUI localization example pointing to a specific string catalog.
Text("Explore", tableName: "Navigation")

// A general text localization example pointing to a specific string catalog.
String(localized: "Get Started", table: "MainScreen")
```

##### Add a Language to Your Project

To support multiple languages in your app, add additional languages to your project. For each language, select the string catalog in the Project navigator, click the Add button (+) near the bottom of the string catalog editor, and select a language to add.

![An Xcode screenshot of the string catalog editor with a callout for the Add button near the bottom of the Language pane.](https://docs-assets.developer.apple.com/published/d9b2dd71764863073381f716e731724f/localizing-and-varying-text-with-a-string-catalog-2-add-language%402x.png)

##### Add Your Localizable Text to the String Catalog

Xcode automatically keeps your string catalog and app in sync each time you build your project. To populate your string catalog with the localizable text from your app, choose Product > Build. Xcode identifies strings in your app that support localization, and then adds them to your string catalog.

![An Xcode screenshot of the string catalog editor showing a newly added language setting with a 0 percent indicator beside it.](https://docs-assets.developer.apple.com/published/90c67fb32bc0afc57298f407f3c2b963/localizing-and-varying-text-with-a-string-catalog-2a-add-text%402x.png)

Use the percent symbol beside each language to track your string catalog’s percentage of translation.

##### Add Your Translations Using the String Catalog Editor

After identifying your localizable strings and adding them to a string catalog, you can either manually translate them, or you can export them, send them to a third-party for translation, and then import them.

To enter your app’s translations manually, select the string catalog and click the language you want to add translations for. Then click the text field of the Language column for each key in the table and enter the translation for that key.

Newly added strings that require translation appear with a New icon in the State column. When you add a translation, the New icon changes to a green checkmark. As you add translations, the percent symbol beside the language updates, displaying the translation percentage for that language. When a string catalog language reaches full translation, the percent symbol changes to a green checkmark.

![An Xcode screenshot showing the Project navigator on the left with a string catalog selected. The string catalog editor on the right contains English strings with Swedish translations.](https://docs-assets.developer.apple.com/published/29cc3c4fe487c6f2f40766b359841eba/localizing-and-varying-text-with-a-string-catalog-3-add-translations%402x.png)

For information about exporting and importing translations in Xcode, see [`Exporting localizations`](exporting-localizations.md) and [`Importing localizations`](importing-localizations.md).

##### Add Pluralizations

Languages have different grammatical rules for handling plurals of nouns and units. For example, in English, you can return `1 Book` when the value of `%lld` is `1`. And you can return `%lld Books` for all other cases. Other languages can have fewer or more plural variants, depending on their region and locale.

| Plural | Text |
| --- | --- |
| One | `%lld Book` |
| Other | `%lld Books` |

To add a plural variant, first localize the text using the value the string is dependent on, using string interpolation.

```swift
@State private var itemCount = 0
Text("\(itemCount) Books")
```

Then, in the string catalog editor, select the language you want to add pluralization for, Control-click the variant key, and select the Vary by Plural option.

![An Xcode screenshot of the string catalog editor showing one of the localized strings selected with a contextual menu. The Vary by Plural option is selected.](https://docs-assets.developer.apple.com/published/479cd9130764b79f80fe677fa5448e1f/localizing-and-varying-text-with-a-string-catalog-4-add-pluralization%402x.png)

When you add a plural variant, the system does the following:

- Adds all the plural forms for that language into the string catalog editor.
- Determines which specifier to use for the interpolated string (`%lld` representing a 64-bit integer in this case).
- Prepopulates the variant fields with the value of that key.

> **Note**: If you add pluralization to the source language (English in this case), the system propagates the variation to the other languages, if possible. If you add pluralization to a nonsource language, that change affects only that language.

Click the text field in the Language column for each variation of that string key, and enter the text for the system to use when that plural displays.

When you run the app, the pluralized variants update based on the value of the interpolated string.

##### Vary Strings By Device

When you need to alter the text that displays on a device due to the available space, or because it has a different interaction, use the Vary by Device option in the string catalog editor.

For example, suppose you want to display two different messages depending on whether your app is running on iPhone or a Mac.

| Operating system | Message |
| --- | --- |
| iOS | Tap to learn more |
| macOS | Click to learn more |

To vary the text string based on device, select the string catalog file, along with the language and key representing the message you want to vary. Control-click the key, select Vary by Device, and then select the device you want to add a specific message for.

![An Xcode screenshot showing the string catalog editor with one of the localized strings selected with a contextual menu. The Vary by Device option is selected with the Mac option highlighted.](https://docs-assets.developer.apple.com/published/0f9d14bc3f55b166e1e599db4568119c/localizing-and-varying-text-with-a-string-catalog-5-vary-by-device%402x.png)

Enter the text you want to display for that selected device, while retaining the existing text for all other devices. Add more devices if you need more variations.

When the app runs on the selected device, the system displays the new message for that device.

##### Test Your Translations

To test your translations in the simulator:

1. Change the app language of your current scheme by choosing Product > Scheme > Edit Scheme.
2. In the dialog that appears, select the Run action on the left and click the Options tab.
3. Click the App Language drop-down, select the language you want to test, and click Close.

![An Xcode screenshot showing an open scheme editor with the Swedish language selected in the App Language drop-down.](https://docs-assets.developer.apple.com/published/6161a4b408dc8e1233459fd277c55ad1/localizing-and-varying-text-with-a-string-catalog-6-testing%402x.png)

You can also navigate to Settings on the simulated device and change the deviceʼs language there. When your app runs, the translations for the selected language appear in the simulator.

## See Also

- [Supporting multiple languages in your app](supporting-multiple-languages-in-your-app.md)
  Internationalize your app’s strings, images, and other resource types to prepare for the translation process.
- [Localizing Landmarks](localizing-landmarks.md)
  Add localizations to the Landmarks sample code project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog)*