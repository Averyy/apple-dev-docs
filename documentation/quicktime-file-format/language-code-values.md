# Language code values

**Framework**: Quicktime File Format

Indicate the language associated with a particular object using language codes.

#### Overview

Some elements of a QuickTime file may be associated with a particular spoken language. To indicate the language associated with a particular object, the QuickTime file format uses either language codes from the Macintosh Script Manager or ISO language codes (as specified in ).

QuickTime stores language codes as unsigned 16-bit fields. All Macintosh language codes have a value that is less than `0x400` except for the single value `0x7FFF` indicating an unspecified language. ISO language codes are three-character codes, and are stored inside the 16-bit language code field as packed arrays, as described in [`Language code values`](language_code_values.md). If treated as an unsigned 16-bit integer, an ISO language code always has a value of `0x400` or greater unless the code is equal to the value `0x7FFF` indicating an Unspecified Macintosh language code.

If the language is specified using a Macintosh language code, any associated text uses Macintosh text encoding.

If the language is specified using an ISO language code, any associated text uses Unicode text encoding. When Unicode is used, the text is in UTF-8 unless it starts with a byte-order-mark (BOM, `0xFEFF`), whereupon the text is in UTF-16. Both the BOM and the UTF-16 text should be big-endian.

> **Note**: ISO language codes cannot be used for all elements of a QuickTime file. ISO language codes can be used . All other elements, including text tracks, must be specified using Macintosh language codes.

> **Note**: ISO 639-2/T codes do not distinguish between certain language variations. Use an extended language tag atom (`'elng'`) to make these distinctions. For example, ISO 639-2T does not distinguish between traditional and simplified Chinese, so also use `'elng'` with the value `"zh-Hant"` or `"zh-Hans"`, respectively. See [`Extended language tag atom ('elng')`](extended_language_tag_atom.md).

#### Macintosh Language Codes

The following table lists QuickTime language code values.

| Language | Value |
| --- | --- |
| English | `0` |
| French | `1` |
| German | `2` |
| Italian | `3` |
| Dutch | `4` |
| Swedish | `5` |
| Spanish | `6` |
| Danish | `7` |
| Portuguese | `8` |
| Norwegian | `9` |
| Hebrew | `10` |
| Japanese | `11` |
| Arabic | `12` |
| Finnish | `13` |
| Greek | `14` |
| Icelandic | `15` |
| Maltese | `16` |
| Turkish | `17` |
| Croatian | `18` |
| Traditional Chinese | `19` |
| Urdu | `20` |
| Hindi | `21` |
| Thai | `22` |
| Korean | `23` |
| Lithuanian | `24` |
| Polish | `25` |
| Hungarian | `26` |
| Estonian | `27` |
| Lettish | `28` |
| Latvian | `28` |
| Saami | `29` |
| Sami | `29` |
| Faroese | `30` |
| Farsi | `31` |
| Russian | `32` |
| Simplified Chinese | `33` |
| Flemish | `34` |
| Irish | `35` |
| Albanian | `36` |
| Romanian | `37` |
| Czech | `38` |
| Slovak | `39` |
| Slovenian | `40` |
| Yiddish | `41` |
| Serbian | `42` |
| Macedonian | `43` |
| Bulgarian | `44` |
| Ukrainian | `45` |
| Belarusian | `46` |
| Uzbek | `47` |
| Kazakh | `48` |
| Azerbaijani | `49` |
| AzerbaijanAr | `50` |
| Armenian | `51` |
| Georgian | `52` |
| Moldavian | `53` |
| Kirghiz | `54` |
| Tajiki | `55` |
| Turkmen | `56` |
| Mongolian | `57` |
| MongolianCyr | `58` |
| Pashto | `59` |
| Kurdish | `60` |
| Kashmiri | `61` |
| Sindhi | `62` |
| Tibetan | `63` |
| Nepali | `64` |
| Sanskrit | `65` |
| Marathi | `66` |
| Bengali | `67` |
| Assamese | `68` |
| Gujarati | `69` |
| Punjabi | `70` |
| Oriya | `71` |
| Malayalam | `72` |
| Kannada | `73` |
| Tamil | `74` |
| Telugu | `75` |
| Sinhala | `76` |
| Burmese | `77` |
| Khmer | `78` |
| Lao | `79` |
| Vietnamese | `80` |
| Indonesian | `81` |
| Tagalog | `82` |
| MalayRoman | `83` |
| MalayArabic | `84` |
| Amharic | `85` |
| Galla | `87` |
| Oromo | `87` |
| Somali | `88` |
| Swahili | `89` |
| Kinyarwanda | `90` |
| Rundi | `91` |
| Nyanja | `92` |
| Malagasy | `93` |
| Esperanto | `94` |
| Welsh | `128` |
| Basque | `129` |
| Catalan | `130` |
| Latin | `131` |
| Quechua | `132` |
| Guarani | `133` |
| Aymara | `134` |
| Tatar | `135` |
| Uighur | `136` |
| Dzongkha | `137` |
| JavaneseRom | `138` |
| Unspecified | `32767` |

#### Iso Language Codes

Because the language codes specified by ISO 639-2/T are three characters long, they must be packed to fit into a 16-bit field. The packing algorithm must map each of the three characters, which are always lowercase, into a 5-bit integer and then concatenate these integers into the least significant 15 bits of a 16-bit integer, leaving the 16-bit integer’s most significant bit set to zero.

One algorithm for performing this packing is to treat each ISO character as a 16-bit integer. Subtract `0x60` from the first character and multiply by 2^10 (`0x400`), subtract `0x60` from the second character and multiply by 2^5 (`0x20`), subtract 0x60 from the third character, and add the three 16-bit values. This will result in a single 16-bit value with the three codes correctly packed into the 15 least significant bits and the most significant bit set to zero.

Example: The ISO language code `'jpn'` consists of the three hexadecimal values `0x6A`, `0x70`, `0x6E`. Subtracting `0x60` from each value yields the values `0xA`, `0x10`, `0xE`, as shown in the following table.

| Character | UTF-8 code | 5-bit value | Shifted value |
| --- | --- | --- | --- |
| `j` | `0x6A` | `0xA (01010)` | `0x2800 (01010..........)` |
| `p` | `0x70` | `0x10 (10000)` | `0x200 (.....10000.....)` |
| `n` | `0x6E` | `0xE (01110)` | `0xE (..........01110)` |

The first value is shifted 10 bits to the left (multiplied by `0x400`) and the second value is shifted 5 bits to the left (multiplied by `0x20`). This yields the values `0x2800`, `0x200`, `0xE`. When added, this results in the 16-bit packed language code value of `0x2A0E`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/language_code_values)*