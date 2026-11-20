# Table.CustomFormat.CustomFormatCondition

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A conditional rule on a custom number format.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.CustomFormat.CustomFormatCondition
```

## Overview

The rule swaps in a different `format_string` when the comparison of the cell value with `condition_value` is true, for example, to show negative values in parentheses.

## Topics

### Enumerations
- [type Table.CustomFormat.CustomFormatCondition.ConditionType](./table.customformat.customformatcondition.conditiontype.md)
  A comparison operator used by a custom-format condition.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.custom-format.custom-format-condition`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `condition_type` (Table.CustomFormat.CustomFormatCondition.ConditionType) *(required)*: The comparison operator (`equal`, `less_than`, `greater_than`, `less_than_or_equal_to`, or `greater_than_or_equal_to`) applied between the cell value and `condition_value`.
- `condition_value` (number) *(required)*: The numeric threshold the cell value is compared against using `condition_type` (for example, `0` to test for negative values).
- `format_string` (string) *(required)*: The format pattern applied when the condition is true. It uses the same syntax as `Table.CustomFormat.format_string`.
- `number_format_data` (Table.CustomFormat.NumberFormatData): The precomputed parse details of `format_string`, used at render time when this condition is active. See `Table.CustomFormat.NumberFormatData`.

## See Also

### Objects
- [object Table.CustomFormat.NumberFormatData](./table.customformat.numberformatdata.md)
  Details that the reader precomputes from a custom number format’s format string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.customformat.customformatcondition)*