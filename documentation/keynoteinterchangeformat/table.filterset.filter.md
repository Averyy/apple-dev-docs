# Table.FilterSet.Filter

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The filter for a single column.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.FilterSet.Filter
```

## Overview

It names the column being filtered and holds the ordered rules applied to its values. A row passes the filter when at least one of `rules` matches; the rules within a single-column filter are always combined with OR.

## Topics

### Objects
- [object Table.FilterSet.Filter.Rule](./table.filterset.filter.rule.md)
  A single predicate evaluated against a row’s value in the enclosing filter’s column.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.filter-set.filter`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `column_identifier` (string) *(required)*: The stable identifier of the column whose values every rule in this filter is evaluated against. It matches a `Table.ColumnHeader.column_identifier`.
- `rules` ([Table.FilterSet.Filter.Rule]) *(required)*: The ordered list of predicates applied to the column’s values. A row passes this filter when at least one rule’s predicate matches; within a single-column filter, rules are implicitly combined with OR.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.filterset.filter)*