# Editing XLIFF and string catalog files

**Framework**: Xcode

Translate or adapt the localizable files for a language and region that you export from your project.

#### Overview

After you export localizations, you can give the Xcode Localization Catalog to localizers for translation, or edit the XLIFF files located in the `Localized Contents` folder yourself.

##### Add Translations to Xliff Files

To find the user-facing strings that need translation, including the app name, search for the `<trans-unit>` element in the XLIFF file. To insert a translation of a string, add a `<target>` element to the `<trans-unit>` element containing the localized text as in:

```other
<trans-unit id="Hello, world!" xml:space="preserve">
        <source>Hello, world!</source>
        <target>Hallo, Welt!</target>
        <note>A friendly greeting.</note>
</trans-unit>
```

##### Group Related Strings Using Tables

If you specify a table name when you internationalize your code — in other words, if you use the `Text` [`init(_:tableName:bundle:comment:)`](https://developer.apple.com/documentation/SwiftUI/Text/init(_:tableName:bundle:comment:)) method or the [`NSLocalizedString(_:tableName:bundle:value:comment:)`](https://developer.apple.com/documentation/foundation/1418095-nslocalizedstring) function with the `tableName` parameter — Xcode groups the strings into separate `<file>` elements with `[table name].strings` as the filename. If you don’t specify a table name, Xcode uses the default `Localizable.strings` as the filename.

When you import the localizations, Xcode adds a version of the strings file for each localization to your project. In the following SwiftUI code listing, the first `Text` string appears in the default `Localized.strings` file while the Button label that specifies a table name appears in the `Buttons.strings` file:

```swift
VStack {
    Text("Hello, world!", comment:"A friendly greeting.")
        .font(.largeTitle)
        .padding()
    Button(action: pushMe){
        Text("Push Me", tableName:"Buttons", comment:"Push Me button label.")
    }
    .font(.title)
}
```

##### Edit String Catalogs in Xcode

After you import localizations, you can edit the string catalog file in your project and the next time you export localizations, Xcode includes your changes in the XLIFF files.

For more information about editing string catalogs in Xcode, see [`Localizing and varying text with a string catalog`](localizing-and-varying-text-with-a-string-catalog.md).

## See Also

- [Creating screenshots of your app for localizers](creating-screenshots-of-your-app-for-localizers.md)
  Share screenshots of your app with localizers to provide context for translation.
- [Exporting localizations](exporting-localizations.md)
  Provide the localizable files from your project to localizers.
- [Importing localizations](importing-localizations.md)
  Import the files that you translate or adapt for a language and region into your project.
- [Locking views in storyboard and XIB files](locking-views-in-storyboard-and-xib-files.md)
  Prevent changes to your Interface Builder files while localizing human-facing strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/editing-xliff-and-string-catalog-files)*