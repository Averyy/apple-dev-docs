# Table.Predicate.Value.reference

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The comparison operand is another cell rather than a literal value (for example, “date is before [B2]”). A reader compares the referenced cell’s value at evaluation time. A version 1.0 reader doesn’t support a cell operand: a rule that compares against a `reference` in `value1` or `value2` is dropped and a warning is reported, and a `reference` entry in `value_list` is skipped.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Predicate.Value.reference
```

## Overview

Written as `{"reference": …}`: the `reference` form of `Table.Predicate.Value`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.predicate.value`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `reference` (Table.Predicate.Reference) *(required)*: The comparison operand is another cell rather than a literal value (for example, “date is before [B2]”). A reader compares the referenced cell’s value at evaluation time. A version 1.0 reader doesn’t support a cell operand: a rule that compares against a `reference` in `value1` or `value2` is dropped and a warning is reported, and a `reference` entry in `value_list` is skipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.predicate.value/reference)*