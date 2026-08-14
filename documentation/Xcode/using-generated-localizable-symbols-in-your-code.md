# Using generated localizable symbols in your code

**Framework**: Xcode

Add keys directly to your string catalog that you can reference in your code using Xcode generated localizable symbols.

#### Overview

If you add keys to your string catalogs, Xcode can automatically generate symbols that you can use to reference the localizable strings in your code. For strings without format specifiers, Xcode creates static variables; for strings with format specifiers, Xcode creates functions with parameters.

First, you internationalize your app and use localizable strings in your code and interface files. Populate string catalogs when you build your targets and automatically generate comments to provide more context to translators. Then, optionally, generate localizable symbols to separate keys from their values so that you can iterate on your text without changing your code. You can use both of these approaches separately or in combination throughout your project.

For more information on creating string catalogs from localizable strings in your code, see [`Localizing and varying text with a string catalog`](localizing-and-varying-text-with-a-string-catalog.md).

##### Enable Automatic Symbol Generation

For older projects, you may need to enable Generate String Catalog Symbols in build settings. In the project editor, select the project in the sidebar and click Build Settings in the editor area. Enter “Generate String” in the filter field, and under Localization, set the Generate String Catalog Symbols setting to `Yes`.

##### Add Keys to Your String Catalog

You can add localizable strings directly to your string catalog and then use symbols that Xcode generates for them in your code.

1. In the string catalog editor, select the source localization (English in this example) or another language in the sidebar.
2. Click the Add button (+) in the toolbar of the string catalog editor (on the far left of the filter field).
3. In the table, enter the key name, translation, and comment for translators.

![An Xcode screenshot showing the Discover file selected in the Project navigator, the English language selected on the left, a key without variables entered in the middle, and the inspector with example usages on the right.](/images/com.apple.Xcode/add-keys-to-your-string-file@2x.png)

For the other languages in the sidebar, Xcode shows a New icon in the State column.

##### Add Localizable Strings with Variables

To add localizable strings with variables, enter the `%` character in the language column, and choose a string from the code completion menu that matches the type of the variable. For example, choose the format specifier for an integer or double placeholder from the menu. Then enter a name for the variable in the `variableName` placeholder text that Xcode highlights in the table. Press Return to finish typing and confirm the string.

![An Xcode screenshot showing the Discover file selected in the Project navigator, the English language selected on the left, and the % character entered in the English column in the middle. The code completion menu appears under the % character with the integer variable menu item choosen.](/images/com.apple.Xcode/add-localizable-strings-with-variables@2x.png)

You can add multiple variables of different types to the localizable string, but you can only use a variable name once.

##### Use Generated Localizable Symbols in Your Code

Xcode generates symbols from the keys and translations that you enter in your string catalog so that you can access keys from your code. For localizable strings without variables, Xcode creates static properties, and for localizable strings containing format specifiers, Xcode creates functions with appropriate parameters.

For keys in the default `Localizable` file, the symbol starts with a period (.) followed by the symbol name. Otherwise, it’s followed by the table name, period, and then the symbol name, as in `.[table name].[symbol name]`.

For example, for a `TITLE` key without variables that you add to a `Discover` string catalog, Xcode creates a `.Discover.title` static property of type [`LocalizedStringResource`](https://developer.apple.com/documentation/foundation/localizedstringresource). For a `SUBTITLE` key with `%1$(friendsPosts)lld - %2$(curatedPosts)lld` as the translation, Xcode creates a `.Discover.subtitle(friendsPosts: Int, curatedPosts: Int)` function that returns a `LocalizedStringResource`.

In SwiftUI, you can use the `LocalizedStringResource` type wherever you use localizable strings. Otherwise, you can use the generated static property or function in the `String`  [`init(localized:)`](https://developer.apple.com/documentation/swift/string/init(localized:)) or `AttributedString`  [`init(localized:)`](https://developer.apple.com/documentation/foundation/attributedstring/init(localized:)) initializer.

First, become familiar with the style of generated localizable symbols and how to use them in your code. Select the key in the string catalog and open the Attributes inspector. If a Generate Swift Symbol checkbox appears selected under String, then the string has a symbol. Code snippets for both SwiftUI and non-SwiftUI apps appear under Example Usages.

![An Xcode screenshot showing the Discover file selected in the Project navigator, the English source localization selected on the left, the SUBTITLE key selected in the string catalog editor, and example usages of the generated symbol in the inspector.](/images/com.apple.Xcode/inspector-example-usages@2x.png)

Then, use code completion to quickly enter these symbols while writing code in the source editor. Begin by entering a period followed by the key path. Then choose the symbol from the code completion menu that appears. For strings with format specifiers, replace the placeholder text with your variables.

![An Xcode screenshot showing a Swift file selected in the Project navigator and a code completion menu that appears when you enter .Discover. with the generated symbol menu item chosen.](/images/com.apple.Xcode/insert-localizable-symbols-in-code@2x.png)

##### Refactor Code to Use Generated Symbols

You can explicitly convert localizable strings in your code and interface files to generated symbols.

In the string catalog editor, select one or more keys in the table, Control-click a selected key, and choose Refactor > Convert Strings to Symbols. The generated symbol preview shows the changes to the key in the string catalog and the location where Xcode adds the symbol in the source code. To toggle between the current and modified code, click the highlighted code. To generate the symbol and apply the code changes, click Convert in the upper right corner.

![An Xcode screenshot showing a generate symbol preview in the project editor that displays the changes to the string catalog and source code with the Convert button in the upper-right corner.](/images/com.apple.Xcode/generate-symbols-for-specific-strings@2x.png)

Optionally, change the signature of the symbol by editing the localizable string that appears under Convert to Symbol. For example, change the signature to have a more semantic meaning or match your style if needed. For strings with format specifiers, you can also change the parameter names.

To undo your changes, select one or more keys and choose Convert Symbols to Strings from the pop-up menu. You can also switch existing generated symbols back to strings.

## See Also

- [Supporting multiple languages in your app](supporting-multiple-languages-in-your-app.md)
  Internationalize your app’s strings, images, and other resource types to prepare for localization.
- [Localizing your app using agents](localizing-your-app-using-agents.md)
  Use agentic coding tools to translate the strings in your app into multiple languages and regions.
- [Localizing and varying text with a string catalog](localizing-and-varying-text-with-a-string-catalog.md)
  Use string catalogs to manage localizable strings, add languages, translate text, handle plurals, and vary text by device.
- [Localizing Landmarks](localizing-landmarks.md)
  Add localizations to the Landmarks sample code project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/using-generated-localizable-symbols-in-your-code)*