# Table.CustomFormat.NumberFormatData

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Details that the reader precomputes from a custom number format’s format string.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CustomFormat.NumberFormatData
```

## Overview

They include placeholder counts, padding widths, the scale factor, and currency and separator settings, and they let a reader render the format without having to re-parse the `format_string`. They’re shared between `Table.CustomFormat` and `Table.CustomFormat.CustomFormatCondition`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.custom-format.number-format-data`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `scale_factor` (number): The multiplier applied to the value before it’s rendered, used for unit-suffixed formats. For example, `#,###K` has a `scale_factor` of 0.001, so 1500 displays as “1.5K”, and a percentage uses 100. The default is 1.0, which means no scaling.

  **Default**: `1`
- `fraction_accuracy` (Table.CellFormat.FractionFormat.Accuracy): The fraction display granularity. It’s set only when the `format_string` includes a fraction token such as `# ?/?`.
- `interstitial_strings` ([string]): The literal text fragments embedded in the format string between digit placeholders (for example, the `,`, the `K`, or any quoted text). They’re indexed against `interstitial_string_insertion_indexes`.
- `interstitial_string_insertion_indexes` ([integer]): The digit positions at which each `interstitial_strings` entry is inserted. It parallels `interstitial_strings`, so their length and order must match.
- `minimum_integer_width` (integer): The minimum number of integer digits to render. A value with fewer digits is padded with zeros; for example, `0000` displays 42 as “0042”.

  **Default**: `0`
- `decimal_width` (integer): The number of decimal-side digit placeholders in the format string, which is the count of `0`, `#`, and `?` characters after the decimal point.

  **Default**: `0`
- `number_of_non_space_integer_placeholder_digits` (integer): The number of integer-side digit placeholders that aren’t space-padded (that is, `0` and `#` but not `?`). It’s used to decide which digit positions are filled and which are left blank.

  **Default**: `0`
- `number_of_non_space_decimal_placeholder_digits` (integer): The number of decimal-side digit placeholders that aren’t space-padded (that is, `0` and `#` but not `?`).

  **Default**: `0`
- `index_from_right_of_last_digit_placeholder` (integer): The position of the rightmost digit placeholder, counted from the right of the `format_string`. It’s used to locate where digits stop and trailing literal text begins.

  **Default**: `0`
- `number_of_hash_decimal_placeholders` (integer): The number of `#` placeholders after the decimal point, which suppress trailing zeros.

  **Default**: `0`
- `total_number_of_decimal_placeholders_in_format` (integer): The total number of decimal-side digit placeholders: `0`, `#`, and `?` combined.

  **Default**: `0`
- `currency_code` (string): The ISO 4217 currency code, such as `USD` or `EUR`, when the `format_string` contains a currency symbol token. It determines the symbol that’s shown.
- `show_thousands_separator` (boolean): Whether the `format_string` includes a thousands separator (typically a `,` between integer placeholders).

  **Default**: `false`
- `use_accounting_style` (boolean): Whether to render in accounting style: currency symbol left-aligned with padding, negative values in parentheses.

  **Default**: `false`
- `requires_fraction_replacement` (boolean): Whether the `format_string` contains a fraction token, such as `?/?`, that must be replaced with a computed fraction at render time.

  **Default**: `false`
- `format_contains_integer_token` (boolean): Whether the `format_string` includes at least one integer-side digit placeholder (`0`, `#`, or `?` before the decimal point).

  **Default**: `false`
- `is_complex_format` (boolean): Whether the format needs custom rendering rather than a standard number formatter (for fractions, space-padded placeholders, or interstitial literal strings).

  **Default**: `false`

## See Also

### Objects
- [object Table.CustomFormat.CustomFormatCondition](./table.customformat.customformatcondition.md)
  A conditional rule on a custom number format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.customformat.numberformatdata)*