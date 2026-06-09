# Localizing and varying text with a string catalog

**Framework**: Xcode

Use string catalogs to manage localizable strings, add languages, translate text, handle plurals, and vary text by device.

#### Overview

Your app delivers the best experience when it runs well in a person’s locale and displays content in their native language. Supporting multiple languages and regions is more than translating text. It includes handling plurals for nouns and units, as well as displaying the right form of text on specific devices.

![None](https://docs-assets.developer.apple.com/published/ca1cd2ff0166df7b3fb34dee9d839e39/localizing-and-varying-text-with-a-string-catalog-0-hero%402x.png)

Use string catalogs to manage your localizable strings in one place using a visual editor in Xcode. Take advantage of the localization tasks that Xcode performs for you, such as extracting the localizable strings from your app, generating comments and translations, and adding plural variants for each language.

To get started using string catalogs:

1. Add a string catalog to your project.
2. Build your app to populate the string catalog.
3. Add a language to the string catalog.
4. Generate the translations for that language.

Then, fine tune your code and translations, add plural and device variants as needed, and test your app in each language and region you support. Also, explore the other features of string catalogs, such as generating comments for people localizing and using localizable symbols instead of string literals in your code.

For more information on internationalizing your app, see [`Supporting multiple languages in your app`](supporting-multiple-languages-in-your-app.md), and for testing, see [`Previewing localizations`](previewing-localizations.md) and [`Testing localizations when running your app`](testing-localizations-when-running-your-app.md).

> **Note**: Session 225: [`Code-along: Explore localization with Xcode`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/225)

##### Add a String Catalog to Your Project

Add one or more string catalog files to your project. You can start with the default `Localizable.xcstrings` file and later, add more depending on the complexity of your code.

To add a string catalog to your project:

1. Choose File > New > File from Template.
2. In the sheet that appears, select the platform, enter `string` in the filter field, select String Catalog under Resource, and click Next.
3. In the dialog that appears, accept the default name `Localizable` or enter another name, choose a folder in your project as the location, and click Create.

If you add multiple string catalogs, choose which string catalog to use for each localizable string by passing its name to the localizable APIs in your code. For more information, see [`Organize localizable strings into tables`](preparing-your-apps-text-for-translation#Organize-localizable-strings-into-tables.md).

##### Add Your Localizable Text to the String Catalog

To populate your string catalog with the localizable text from your app, choose Product > Build. Xcode discovers the localizable strings in your app and adds them to string catalogs in your project automatically. Each time you build your project, Xcode updates your string catalogs with changes you make to localizable strings in your code.

Most SwiftUI strings inside views are automatically localizable and appear in the string catalog files. If some strings are missing, verify that you are using localizable APIs in your code so that Xcode finds all the user-facing text. For more information, see [`Preparing your app’s text for translation`](preparing-your-apps-text-for-translation.md) and [`Preparing dates, currencies, and numbers for translation`](preparing-dates-numbers-with-formatters.md).

##### Review the Source of Localizable Text in the Assistant

After you populate your string catalog, you can review the location of localizable text in your app before you add languages and translations.

In the Project navigator, select the string catalog file and choose Editor > Assistant. Then select a key in the catalog to see the source of the localizable text in the assistant.

If necessary, make edits to the localizable text in the source editor and choose Product > Build to update the string catalog.

To jump to the text in the source editor, click the arrow button that appears next to a key when you hover over it in the string catalog. You can also jump to the code and see example usages in the Attributes inspector for a key.

##### Add Variants for Strings That Contain Plurals

If you use string interpolation in your localizable strings, Xcode can add plural variants for you to string catalogs.

Languages have different grammatical rules for handling plurals of nouns and units. For example, in English, you can return `1 item` when the value of `%lld` is `1`. And you can return `%lld items` for all other cases. Other languages can have fewer or more plural variants, depending on their region and locale.

| Plural | Text |
| --- | --- |
| One | `%lld item` |
| Other | `%lld items` |

First pass the string with the interpolated variable to a localizable API so that Xcode discovers it and adds it to the string catalog.

```swift
Text("\(collection.landmarks.count) items")
```

In the string catalog editor, Control-click the key that contains variables and select Vary by Plural from the contextual menu. Xcode adds plural variants to the source localization.

Then enter the translations for the different plurals in the source localization. Click the language in the sidebar, click the text field in the Language column for each variation of that string key, and then enter the translation for the system to use when that plural displays.

Later, when you add other languages to a string catalog, Xcode automatically adds the language-specific variations for those languages to the string catalog too. For example, Xcode adds One and Other variants for English when it’s the source localization, and One, Few, Many, and Other variants for Russian when you add Russian.

When you select Vary by Plural, Xcode:

- Adds all the plural forms for that language to the string catalog editor.
- Determines which specifier to use for the interpolated string (`%lld` representing a 64-bit integer in this case).
- Prepopulates the variant fields with the value of that key.

You can add plural variants to the source localization before or after you add languages and Xcode keeps all the plural variants in sync. If you add plural variants to a language other than the source localization, that change affects only that language.

##### Vary Strings By Device

When you need to alter the text that displays on a device due to the available space, or because it has a different interaction, use the Vary by Device option in the string catalog editor.

For example, suppose you want to display two different messages depending on whether your app is running on iPhone or a Mac.

| Operating system | Message |
| --- | --- |
| iOS | Tap to learn more |
| macOS | Click to learn more |

To vary the text string based on device, select the string catalog file, along with the language and key representing the message you want to vary. Control-click the key, select Vary by Device, and then select the device you want to add a specific message for.

Enter the text you want to display for that selected device, while retaining the existing text for all other devices. Add more devices if you need more variations.

When the app runs on the selected device, the system displays the new message for that device.

##### Generate Comments Automatically

You can let Xcode automatically create comments for your localizable strings to provide more context for localizers. These comments describe the interface element, surrounding interface, placeholder content, and variables in the string.

To generate a comment for a specific key:

1. In the string catalog editor, Control-click the key you want to add a comment to.
2. Choose Generate Comment from the context menu.

You can also enable automatic comment generation for all projects. In Xcode > Settings > Editing, turn on “Automatically generate string catalog comments.” under Localized Strings.

Later, when you export your localization files, an “auto-generated” note appears next to any automatically generated comments to distinguish them from human-written comments.

Alternatively, pass comments to the localizable APIs in your code. For more information, see [`Add comments to your localizable strings`](preparing-your-apps-text-for-translation#Add-comments-to-your-localizable-strings.md).

##### Add Localizations to Your Project

Add the language and region combinations you want to support to your string catalogs.

For each localization, select the string catalog in the Project navigator, click the Add button (+) at the bottom of the sidebar in the string catalog editor, and select a language and optionally, a region, from the pop-up menu.

For example, select a language and region, such as Portuguese (Brazil) (pt-BR) or Portuguese (Portugal) (pt-PT), or just a language, such as French (fr) or Greek (el). For more information on languages and regions, see [`Choosing localization regions and scripts`](choosing-localization-regions-and-scripts.md).

You can also add and remove languages using the Info pane in the project editor. Under Localizations, click the Add button, or select a localization and click the Remove button (-).

##### Add Translations to the String Catalog

If you know the translations for the languages that you add, you can enter them directly in the string catalog editor. To enter translations, select the language that you want to add translations for in the sidebar. Then click the text field for each key in that language’s column and enter the translation for that key.

Newly added strings that require translation appear with a New icon in the State column. When you add a translation, the state changes from new to translated indicated by a green checkmark. As you add translations, the percent symbol beside the language updates, displaying the translation percentage for that language. When a string catalog language reaches full translation, the percent symbol changes to a green checkmark.

## See Also

- [Localizing your app using agents](localizing-your-app-using-agents.md)
  Use agentic coding tools to translate the strings in your app into multiple languages and regions.
- [Supporting multiple languages in your app](supporting-multiple-languages-in-your-app.md)
  Internationalize your app’s strings, images, and other resource types to prepare for localization.
- [Localizing your app using agents](localizing-your-app-using-agents.md)
  Use agentic coding tools to translate the strings in your app into multiple languages and regions.
- [Using generated localizable symbols in your code](using-generated-localizable-symbols-in-your-code.md)
  Add keys directly to your string catalog that you can reference in your code using Xcode generated localizable symbols.
- [Localizing Landmarks](localizing-landmarks.md)
  Add localizations to the Landmarks sample code project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog)*