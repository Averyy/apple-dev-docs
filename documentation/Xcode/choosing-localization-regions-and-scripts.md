# Choosing localization regions and scripts

**Framework**: Xcode

Add a language-only localization or localizations specific to regional variants and scripts.

#### Overview

When you localize your app, you add localizations by choosing a language, and then, optionally, a region and script from Xcode’s menus. Apple recommends that you choose the most specific localization, not just the language. For example, if you only support English and it is American English, choose English (United States) (en-US) instead of English (en).

In Xcode menus, you choose a human-readable name for a localization, but in the project and exported files, a language identifier understood by localizers specifies the language, region, and script. The Xcode Localization Catalog (a folder with a `.xcloc` file extension) uses the language identifier as the suffix, as in `en.xcloc` and `de.xcloc` for the English and German catalog names, respectively.

For information about how the `Bundle` object finds the best match between the localizations your app supports and the user’s language and region settings, see [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle).

##### Understand the Language Identifier

A  is a compound syntax that represents a combination of a language, regional variant, and script. It contains a language code, and, optionally, a region code, and a script code.

For a language used in many regions, use just the  that represents the language (`[language code]`). For example, to specify Serbian, use the `sr` language code. Use the two-letter ISO 639-1 standard (preferred) or, if no code is available for a particular language, use the ISO 639-2 standard instead.

To distinguish between different languages and regional variants, use a language code with a region code separated by hyphens (`[language code]-[region code]`). A  represents a country or region. Use the ISO 3166-1 standard, a two-letter, capitalized code, such as, `US`, `GB`, `AU`, and `FR`. For example, to specify the Swiss variant of the German language, use `de-CH`. If it’s not possible to create a language identifier using the ISO 3166-1 standard, use the United Nations M.49 standard, which is a numeric code.

To specify a script, combine a language code with a script code in the ISO 3166-1 standard, separated by a hyphen (`[language code]-[script code]`), as in `az-Cyrl` for Azerbaijani in the Cyrillic script. To represent Chinese spoken in Taiwan and written in traditional Chinese script, use `zh-Hant-TW`.

This table shows some common language identifiers with their language, region, and script codes:

| Syntax | Description | Examples |
| --- | --- | --- |
| [language code] | Specifies a language only | `en` for English |
|  |  | `fr` for French |
|  |  | `de` for German |
| [language code]-[region code] | Specifies a regional variant of a language | `en-AU` for English in Australia |
|  |  | `en-GB` for English in United Kingdom |
|  |  | `fr-FR` for French in France |
|  |  | `fr-CA` for French in Canada |
|  |  | `de-AT` for German in Austria |
|  |  | `de-CH` for German in Switzerland |
| [language code]-[script code] | Specifies a script of a language | `az-Cyrl` for Azerbaijani in the Cyrillic script |
|  |  | `sr-Latn` for Serbian in the Latin script |
|  |  | `uz-Cyrl` for Uzbek in the Cyrillic script |
|  |  | `zh-Hans` for Chinese in the simplified script |
|  |  | `zh-Hant` for Chinese in the traditional script |

## See Also

- [Adding support for languages and regions](adding-support-for-languages-and-regions.md)
  Select the resources that you want to localize for each language and region you support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/choosing-localization-regions-and-scripts)*