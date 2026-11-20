# Table.Predicate.Value.number

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Numeric value, used by value-comparison predicates, for example, `value_equal`, `value_greater_than`, and `value_between`, and by relative date predicates that take a unit count, for example, `date_is_in_the_last`.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Predicate.Value.number
```

## Overview

Written as `{"number": …}`: the `number` form of `Table.Predicate.Value`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.predicate.value`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `number` (number) *(required)*: Numeric value, used by value-comparison predicates, for example, `value_equal`, `value_greater_than`, and `value_between`, and by relative date predicates that take a unit count, for example, `date_is_in_the_last`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.predicate.value/number)*