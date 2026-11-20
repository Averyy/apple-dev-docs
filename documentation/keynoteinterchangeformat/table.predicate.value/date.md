# Table.Predicate.Value.date

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Absolute date value, used by absolute date predicates.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Predicate.Value.date
```

## Overview

Examples of these values are `date_is_before`, `date_is_after`, `date_is_between`, `date_is_exactly`, and `date_is_the_date`.

Written as `{"date": …}`: the `date` form of `Table.Predicate.Value`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.predicate.value`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `date` (Table.Date) *(required)*: Absolute date value, used by absolute date predicates. Examples of these values are `date_is_before`, `date_is_after`, `date_is_between`, `date_is_exactly`, and `date_is_the_date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.predicate.value/date)*