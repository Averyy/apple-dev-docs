# Table.ConditionalStyleSet.Rule

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A single conditional highlighting rule with a predicate and styling to apply when the predicate is true.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.ConditionalStyleSet.Rule
```

## Topics

### Enumerations
- [type Table.ConditionalStyleSet.Rule.PresetKind](./table.conditionalstyleset.rule.presetkind.md)
  The built-in conditional-highlighting preset that a rule represents.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.conditional-style-set.rule`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `predicate` (Table.Predicate) *(required)*: The condition that determines when this rule applies.
- `cell_style` (Table.CellProperties): The cell styling to apply when the predicate is true.
- `text_style` (ParagraphProperties): The text styling to apply when the predicate is true.
- `preset_kind` (Table.ConditionalStyleSet.Rule.PresetKind): The built-in conditional-highlighting preset this rule represents. A named preset supplies the styling when `cell_style` and `text_style` are omitted; when either is present, it overrides the preset. `custom`, or no value at all, makes the rule fully custom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.conditionalstyleset.rule)*