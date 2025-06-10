# Localization

**Framework**: Xcode

Expand the market for your app by supporting multiple languages and regions.

#### Overview

Localization is the process of translating and adapting your app into multiple languages and regions. Localize your app to provide access for users who speak a variety of languages, and who download from different App Store territories.

First,  your code with APIs that automatically format and translate strings correctly for the language and region. Then add support for content that includes plural nouns and verbs by following language plural rules to increase the accuracy of your translations.

##### Translate and Adapt Your App

In Xcode, localization refers specifically to the set of resources for a specific language and region that you support.

You add a localization to your project and select the resources you want to include for that language and region. Export the localization and send the files to , who translate the user-facing text and adapt resources for particular cultures and regions. Finally, you import the localized files and test the app in that language and region directly in Xcode.

When you release a localized version of your app, you can also localize the App Store information in App Store Connect for the specific territories where you offer your app.

For other localization tips, tools, and resources, see [`Expanding Your App to New Markets`](https://developer.apple.comhttps://developer.apple.com/localization/).

> ❗ **Important**: In Xcode 15 and later, string catalogs are the recommended way to localize strings. In earlier versions of Xcode, use strings and `stringsdict` files. For more information about string catalogs, see [`Localizing and varying text with a string catalog`](localizing-and-varying-text-with-a-string-catalog.md).

## Topics

### Essentials
- [Supporting multiple languages in your app](supporting-multiple-languages-in-your-app.md)
  Internationalize your app’s strings, images, and other resource types to prepare for the translation process.
- [Localizing and varying text with a string catalog](localizing-and-varying-text-with-a-string-catalog.md)
  Use a string catalog to translate text, handle plurals, and vary the text your app displays on specific devices.
- [Localizing Landmarks](localizing-landmarks.md)
  Add localizations to the Landmarks sample code project.
### Strings and text
- [Preparing your interface for localization](preparing-your-interface-for-localization.md)
  Find text in your app that needs translation and verify that your interface adapts to translated text.
- [Preparing your app’s text for translation](preparing-your-apps-text-for-translation.md)
  Make your app’s text translatable by leveraging the localization APIs in the Foundation framework.
- [Preparing dates, currencies, and numbers for translation](preparing-dates-numbers-with-formatters.md)
  Ensure that dates, currencies, and numbers display correctly across multiple languages and locales by using formatters.
### Layouts and views
- [Preparing views for localization](../SwiftUI/Preparing-views-for-localization.md)
  Specify hints and add strings to localize your SwiftUI views.
- [Autosizing Views for Localization in iOS](autosizing_views_for_localization_in_ios.md)
  Add auto layout constraints to your app to achieve localizable views.
- [Localization-Friendly Layouts in macOS](localization-friendly_layouts_in_macos.md)
  This project demonstrates localization-friendly auto layout constraints. It uses `NSGridView` as a container view to achieve localized layouts.
### Languages and regions
- [Adding support for languages and regions](adding-support-for-languages-and-regions.md)
  Select the resources that you want to localize for each language and region you support.
- [Choosing localization regions and scripts](choosing-localization-regions-and-scripts.md)
  Add a language-only localization or localizations specific to regional variants and scripts.
### Resources and assets
- [Adding resources to localizations](adding-resources-to-localizations.md)
  Include more resources in the localizations you add to your project.
- [Localizing assets in a catalog](localizing-assets-in-a-catalog.md)
  Use asset catalogs to localize colors, images, symbols, watch complications, and more.
### Translation and adaptation
- [Creating screenshots of your app for localizers](creating-screenshots-of-your-app-for-localizers.md)
  Share screenshots of your app with localizers to provide context for translation.
- [Exporting localizations](exporting-localizations.md)
  Provide the localizable files from your project to localizers.
- [Editing XLIFF and string catalog files](editing-xliff-and-string-catalog-files.md)
  Translate or adapt the localizable files for a language and region that you export from your project.
- [Importing localizations](importing-localizations.md)
  Import the files that you translate or adapt for a language and region into your project.
- [Locking views in storyboard and XIB files](locking-views-in-storyboard-and-xib-files.md)
  Prevent changes to your Interface Builder files while localizing human-facing strings.
### Testing
- [Previewing localizations](previewing-localizations.md)
  Test localizations in the SwiftUI preview or the Interface Builder preview.
- [Testing localizations when running your app](testing-localizations-when-running-your-app.md)
  Run your app in each language and region you support to thoroughly test your app.
### Legacy localization techniques
- [Localizing strings that contain plurals](localizing-strings-that-contain-plurals.md)
  Use a strings dictionary file to ensure correct localization of strings that contain language plurals.
- [Creating width and device variants of strings](creating-width-and-device-variants-of-strings.md)
  Change a localized string for different interface widths and devices.

## See Also

- [Asset management](asset-management.md)
  Add app icons, images, strings, data files, machine learning models, and other resources to your projects, and manage how you load them at runtime.
- [Accessibility Inspector](../Accessibility/accessibility-inspector.md)
  Reveal how your app represents itself to people using accessibility features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/localization)*