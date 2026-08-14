# Supporting multiple languages in your app

**Framework**: Xcode

Internationalize your app’s strings, images, and other resource types to prepare for localization.

#### Overview

Multilingual apps are apps that can run in more than one language and region. Making your app multilingual widens your audience and gives your customers a better overall experience. People are more comfortable using apps when the text and assets adapt to the language and region settings on their device.

![A banner containing the word hello in multiple languages.](/images/com.apple.Xcode/supporting-multiple-languages-in-your-app-hero@2x.png)

To make your app multilingual, you first *internationalize* it by preparing your code and assets for translation into different languages and regions. For example, dates in some regions appear in a day-month-year format, while in others, dates appear in month-day-year format.

After you internationalize your app, you *localize* it by translating your strings and varying your assets for multiple languages and regions. For more information, see [`Localizing and varying text with a string catalog`](localizing-and-varying-text-with-a-string-catalog.md).

#### Internationalize Your Code

Write your code so your app automatically adapts to the language and region settings of the device. Use specific localizable APIs and these Xcode tools that support internationalization:

- **User-facing text**. Use localized versions of the string formatters to prepare your app’s text for localization. For more information about user-facing text, see [`Preparing your app’s text for translation`](preparing-your-apps-text-for-translation.md).
- **Dates, currencies, and numbers**. Different regions have different formats for dates, currencies, and numbers. For more information, see [`Preparing dates, currencies, and numbers for translation`](preparing-dates-numbers-with-formatters.md).
- **Grammatical agreement**. Use the automatic grammar agreement APIs in Foundation, such as [`TermOfAddress`](https://developer.apple.com/documentation/foundation/termofaddress), to represent grammatical gender correctly in localized text. For more information about grammatical agreement, see [`Unlock the power of grammatical agreement`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10153/).
- **Text direction**. Use the layout tools in SwiftUI and Xcode to control text and UI element orientation, and to flip image direction when necessary for right-to-left languages. For more information about text direction, see [`Get it right (to left)`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10107/).
- **Tall languages**. Use Dynamic Type to prevent clipping of words and letters, and to ensure proper spacing of text for some languages that require significantly more vertical space and other that have specific conventions for wrapping and hyphenation. For more information about Dynamic Type, see [`Scaling fonts automatically`](https://developer.apple.com/documentation/uikit/scaling-fonts-automatically) and [`What’s new with text and text interactions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10058/).
- **Sounds, images, and assets**. Use an asset catalog to localize colors, images, and sounds in your app. For more information about adding resources to asset catalogs, see [`Adding resources to localizations`](adding-resources-to-localizations.md) and [`Localizing assets in a catalog`](localizing-assets-in-a-catalog.md).

## See Also

- [Localizing your app using agents](localizing-your-app-using-agents.md)
  Use agentic coding tools to translate the strings in your app into multiple languages and regions.
- [Localizing and varying text with a string catalog](localizing-and-varying-text-with-a-string-catalog.md)
  Use string catalogs to manage localizable strings, add languages, translate text, handle plurals, and vary text by device.
- [Using generated localizable symbols in your code](using-generated-localizable-symbols-in-your-code.md)
  Add keys directly to your string catalog that you can reference in your code using Xcode generated localizable symbols.
- [Localizing Landmarks](localizing-landmarks.md)
  Add localizations to the Landmarks sample code project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/supporting-multiple-languages-in-your-app)*