# Localization

**Framework**: Xcode

Expand the market for your app by supporting multiple languages and regions.

#### Overview

Localization is the process of translating and adapting your app into multiple languages and regions. Localize your app so it adapts for people who speak a variety of languages, and who download your app from different App Store territories.

First, use localizable APIs that format and translate strings correctly for the language and region setting on the device. For more information, see [`Supporting multiple languages in your app`](supporting-multiple-languages-in-your-app.md).

Then, you have several options for localizing your app that you can use separately or in combination:

- Let agents in the coding assistant add languages, string catalog files, and translations for you. For more information, see [`Localizing your app using agents`](localizing-your-app-using-agents.md).
- Add string catalogs to your app and manage languages, comments, and translations using the string catalog editor. For more information, see [`Localizing and varying text with a string catalog`](localizing-and-varying-text-with-a-string-catalog.md).
- Export localizations and send the files to *localizers*, who translate the strings and adapt resources. For more information, see [`Exporting localizations`](exporting-localizations.md) and [`Importing localizations`](importing-localizations.md).

Next, test your app in the languages and regions you support in Xcode previews and by running your app on simulated and physical devices. For more information, see [`Previewing localizations`](previewing-localizations.md) and [`Testing localizations when running your app`](testing-localizations-when-running-your-app.md).

To get the best feedback on your translations, distribute your app to native speakers in the languages that you support. For more information on using TestFlight, see [`Distributing your app for beta testing and releases`](distributing-your-app-for-beta-testing-and-releases.md).

Finally, when you release a localized version of your app, localize the App Store information in App Store Connect for the specific territories where you offer your app. For more information, see [`Localize app information`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-information/).

For other localization tips, tools, and resources, see [`Expand your app to new markets`](https://developer.apple.comhttps://developer.apple.com/localization/).

## Topics

### Essentials
- [Supporting multiple languages in your app](supporting-multiple-languages-in-your-app.md)
  Internationalize your app’s strings, images, and other resource types to prepare for localization.
- [Localizing your app using agents](localizing-your-app-using-agents.md)
  Use agentic coding tools to translate the strings in your app into multiple languages and regions.
- [Localizing and varying text with a string catalog](localizing-and-varying-text-with-a-string-catalog.md)
  Use string catalogs to manage localizable strings, add languages, translate text, handle plurals, and vary text by device.
- [Using generated localizable symbols in your code](using-generated-localizable-symbols-in-your-code.md)
  Add keys directly to your string catalog that you can reference in your code using Xcode generated localizable symbols.
- [Localizing Landmarks](localizing-landmarks.md)
  Add localizations to the Landmarks sample code project.
### Strings and text
- [Preparing your interface for localization](preparing-your-interface-for-localization.md)
  Find text in your app that needs translation and verify that your interface adapts to translated text.
- [Preparing your app’s text for translation](preparing-your-apps-text-for-translation.md)
  Use localizable APIs to populate string catalogs automatically with your app’s user-facing text.
- [Preparing dates, currencies, and numbers for translation](preparing-dates-numbers-with-formatters.md)
  Ensure that dates, currencies, and numbers display correctly across multiple languages and locales by using formatters.
### Layouts and views
- [Preparing views for localization](../swiftui/preparing-views-for-localization.md)
  Specify hints and add strings to localize your SwiftUI views.
- [Autosizing views for localization in iOS](autosizing-views-for-localization-in-ios.md)
  Add auto layout constraints to your app to achieve localizable views.
- [Localization-friendly layouts in macOS](localization-friendly-layouts-in-macos.md)
  This project demonstrates localization-friendly auto layout constraints.
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
- [Accessibility Inspector](../accessibility/accessibility-inspector.md)
  Reveal how your app represents itself to people using accessibility features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/localization)*