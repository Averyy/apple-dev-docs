# Locale indicator

**Framework**: QuickTime File Format

A four-byte value that indicates a locale.

#### Overview

The locale indicator is formatted as a four-byte value. It is formed from two two-byte values: a country indicator, and a language indicator. In each case, the two-byte field has the possible values shown in the following table.

| Value | Meaning |
| --- | --- |
| `0` | This atom provides the default value of this datum for any locale not explicitly listed. |
| `1` to `255` | The value is an index into the country or language list (the upper byte is 0). |
| otherwise | The value is an ISO 3166 code (for the country code) or a packed ISO 639-2/T code (for the language). |

Note that both ISO 3166 and ISO 639-2/T codes have a nonzero value in their top byte, and so will have a value > `255`.

Software applications that read metadata may be customized for a specific set of countries or languages. If a metadata writer does not want to limit a metadata item to a specific set of countries, it should use the reserved value `ZZ` from ISO 3166 as its country code. Similarly if the metadata writer does not want to limit the user’s language (this is not recommended) it uses the value ‘und’ (undetermined) from the ISO 639-2/T specification.

A software application matches a country code if either (a) the value to be matched to is `0` (default) or (b) the codes are equal. A software application matches to a list of codes if its value is a member of that list. A software application matches to a locale if both country and language match.

The following table shows some example metadata tags.

| Country | Language | Meaning |
| --- | --- | --- |
| `0` | `eng` | All speakers of English, regardless of country |
| `GB` | `0` | All people in the United Kingdom, regardless of language |
| `CA` | `fra` | French speakers in Canada |
| `DE,GB,FR,IT` | `0` | People in Germany, France, United Kingdom, and Italy, regardless of language |
| `DE,GB,FR,IT` | `deu,fra` | People in Germany, France, United Kingdom, and Italy, who speak German or French |
| `0` | `0` | Default, all speakers in all countries |

To reiterate, if the country_indicator value is in the range `1` to `255`, it is interpreted as the 1-based index for a country list in the Country Language atom in the Metadata atom. If the language_indicator value is in the range `1` to `255`, it is interpreted as the 1-based index for a language list in the Language List atom in the Metadata atom. Otherwise, the country_indicator or language_indicator is unspecified (`0`) or holds the immediate value for a single country or language.

## See Also

- [Extensibility](extensibility.md)
  Avoid issues building extensibility into your file.
- [Localization list sets](localization_list_sets.md)
  Provide metadata for more than one country or language.
- [Type indicator](type_indicator.md)
  Four bytes that indicate a type of data that QuickTime supports.
- [Data ordering](data_ordering.md)
  Represent multiple representations of the same information, differing either by language or storage type or by the size or nature of the data.
- [Well-known types](well-known_types.md)
  Basic data types.
- [Location metadata](location_metadata.md)
  Storing the location coordinates, as well as several auxiliary pieces of information about a location, as metadata.
- [QuickTime metadata keys](quicktime_metadata_keys.md)
  Use QuickTime keys to hold data in a Metadata atom.
- [Direction definition](direction_definition.md)
  Define a direction in metadata keys.
- [Metadata handling](appendix_d_metadata_handling.md)
  Handling metadata in other file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/locale_indicator)*