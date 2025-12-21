# Localizing strings that contain plurals

**Framework**: Xcode

Use a strings dictionary file to ensure correct localization of strings that contain language plurals.

#### Overview

> ❗ **Important**: In Xcode 15 and later, string catalogs are the recommended way to localize strings that contain plurals. In earlier versions of Xcode, use strings and `stringsdict` files. For more information about string catalogs, see [`Localizing and varying text with a string catalog`](localizing-and-varying-text-with-a-string-catalog.md).

Languages have different grammatical rules for handling plurals of nouns and units. So if you localize formatted strings that contain variable amounts, use a `.stringsdict` file to provide a different translation for each plural form in the language.

For example, if you pass the `%d home(s) found` formatted string to the [`NSLocalizedString`](https://developer.apple.com/documentation/Foundation/NSLocalizedString) macro or similar API, such as the [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) structure, you can use the a `.stringsdict` file to return different versions of the string. In English, you can return `one home found` or `1 home found` when `d` is `1`, and `%d homes found` when `d` is greater than `1`. For other languages, the `.stringsdict` file can have more or fewer plural variants of a formatted string.

Xcode automatically handles `.stringsdict` files for you when you export and import localizations. However, you need to know the format of a `.stringsdict` file to localize it in the development language and other languages if you don’t use a localization service.

##### Add a Strings Dictionary File to Your Project

To add a `.stringsdict` file to your project, choose File > New > File from Template. In the sheet that appears, select the platform, enter `strings` in the Filter field, select Stringsdict File, and click Next. In the dialog that appears, enter a name for the file, choose a location, and click Create.

A `.stringsdict` file is a resource file in your project, but Xcode doesn’t automatically localize it. While the file is in a selected state in the Project navigator, open the inspector, and click Localize under Localization. In the dialog that appears, choose a language and click Localize. Choose Base to localize the file in all languages.

If you previously added localizations to your project, select the other localizations in the inspector under Localization. If you select multiple localizations, the `.stringsdict` file becomes a group in the Project navigator that contains a version for each language.

Later when you add more localizations, be sure to include the `.stringsdict` file when you select resources for the localization.

##### Localize the Strings Dictionary File in the Development Language

Next, add the plural rules and variants to the development language version of the `.stringsdict` file.

In the Project navigator, select the `.stringsdict` file. If it appears as a group, select the development language version of the file (the language appears in parentheses). Because a `.stringsdict` file is a property list, it appears in the property editor by default. To edit the `.stringsdict` file using the source editor, Control-click it and choose Open As > Source Code.

A new `.stringsdict` file contains a dictionary with plural variants for a single formatted string. For each formatted string in your app that contains a numeric value, enter the formatted string as the key and a  dictionary as the value with the following key-value pairs:

| Key | Value |
| --- | --- |
| `NSStringLocalizedFormatKey` | A formatted string that contains variables. To replace the string with a plural rule, precede the variable with the %#@ characters and follow it by the @ character, as in `%#@homes@` where `homes` is the variable. |
| `[variable]` | A dictionary that specifies the plural variants for a variable in the formatted string. |

For example, enter separate dictionaries for the user-facing formatted strings you use in your code. If the formatted string contains multiple variables, enter a separate subdictionary for each variable. In the following `.stringsdict` file, the formatted strings are: `%d home(s) found`, `%d service hour(s)`, and `%d award(s)`:

```other
<plist version="1.0">
    <dict>
        <key>%d home(s) found</key>
        <dict>
            <key>NSStringLocalizedFormatKey</key>
            <string>%#@homes@</string>
            <key>homes</key>
            <dict>
                ...
            </dict>
        </dict>
        <key>%d service hour(s)</key>
        <dict>
            …
        </dict>
        <key>%d award(s)</key>
        <dict>
            …
        </dict>
    </dict>
</plist>
```

The variable dictionary for each formatted string determines which string returns from the [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) structure, [`NSLocalizedString`](https://developer.apple.com/documentation/Foundation/NSLocalizedString) macro, or similar API in your code. It contains a key-value pair for each grammatical plural variant in the language, called a .

For example, the following `.stringsdict` file with English localization contains plural variants for the `zero`, `one`, and `other` categories. For the `%d home(s) found` formatted string, the API returns `No homes found` for `0`, `%d home found `for` 1`, and `%d homes found` for `other` values.

```other
<plist version="1.0">
    <dict>
        <key>%d home(s) found</key>
        <dict>
            <key>NSStringLocalizedFormatKey</key>
            <string>%#@homes@</string>
            <key>homes</key>
            <dict>
                <key>NSStringFormatSpecTypeKey</key>
                <string>NSStringPluralRuleType</string>
                <key>NSStringFormatValueTypeKey</key>
                <string>d</string>
                <key>zero</key>
                <string>No homes found</string>
                <key>one</key>
                <string>%d home found</string>
                <key>other</key>
                <string>%d homes found</string>
            </dict>
        </dict>
    </dict>
</plist>
```

A variable dictionary can contain the following key-value pairs:

| Key | Value |
| --- | --- |
| `NSStringFormatSpecTypeKey` | Specifies the type of language rule. The only possible value is `NSStringPluralRuleType`, which indicates a language plural variant. |
| `NSStringFormatValueTypeKey` | A string format specifier for a number, as in the letter `d` for an integer. |
| `zero, one, two, few, many, other` | The formatted string for the language-specific plural category. Using the format specifier in the string is optional. The `other` category is a requirement. |

The meaning of the plural categories is language-dependent, and not all languages have the same categories. For example, the English language only requires the `one` and `other` categories to represent plural forms, and `zero` is optional. Arabic has different plural forms for the `zero`, `one`, `two`, `few`, `many`, and `other` categories. Although Russian also uses the `many` category, the rules for which numbers are in the `many` category aren’t the same as the Arabic rules.

For the categories and plural rules for each language, see [`CLDR Language Plural Rules`](https://developer.apple.comhttp://cldr.unicode.org/index/cldr-spec/plural-rules).

##### Localize the Strings Dictionary File in Other Languages

After you localize the `.stringsdict` files in the development langauge and add the other localizations to your project, you export the localizations.

When you export localizations, Xcode automatically adds the language-specific categories for each formatted string to the exported XLIFF files. Localizers just need to enter the translations for each category in the XLIFF file. Then when you import localizations, Xcode updates the localized `.stringsdict` files in your project.

For example, if you export a Russian localization containing the `%d home(s) found` formatted string in a `.stringsdict` file, Xcode adds the `one`, `many`, and `other` categories to the Russian version of the XLIFF file. The localizer inserts the translations and when you import the localization, the `.stringsdict` file contains the correct variable dictionary key-value pairs for Russian.

```other
<plist version="1.0">
    <dict>
       <key>%d home(s) found</key>
         <dict>
            <key>NSStringLocalizedFormatKey</key>
            <string>%#@homes@</string>
            <key>homes</key>
            <dict>
                <key>NSStringFormatSpecTypeKey</key>                
                <string>NSStringPluralRuleType</string>
                <key>NSStringFormatValueTypeKey</key>
                <string>d</string>
                <key>one</key>
                <string>найден %d дом</string>
                <key>many</key>
                <string>найдены %d дома</string>
                <key>other</key>
                <string>найдены %d домов</string>
            </dict>
        </dict>
    </dict>
</plist>
```

You can edit the `.stringsdict` files in Xcode yourself, but keep in mind that all of the categories are optional except the `other` category. Also the localized text may be grammatically incorrect if you don’t supply a rule for all the language-specific categories. Conversely, if you provide a rule for a category that a language doesn’t use, the system ignores it and uses the `other` category format string instead.

Furthermore, using the `NSStringFormatValueTypeKey` format specifier in the localized formatted strings is optional. For example, the format string for the `one` category in English can be `One home found`, while the `other` category can be `%d homes found`.

You can use the format specifier (`%d`)` `or spell out numbers (`one`)` `in the plural variants, but don’t use a numeric value (`1`) in the string because it may not have the correct localization if the user changes regions.

## See Also

- [Adding support for languages and regions](adding-support-for-languages-and-regions.md)
  Select the resources that you want to localize for each language and region you support.
- [Exporting localizations](exporting-localizations.md)
  Provide the localizable files from your project to localizers.
- [Importing localizations](importing-localizations.md)
  Import the files that you translate or adapt for a language and region into your project.
- [Creating width and device variants of strings](creating-width-and-device-variants-of-strings.md)
  Change a localized string for different interface widths and devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/localizing-strings-that-contain-plurals)*