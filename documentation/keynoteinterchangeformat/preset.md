# Preset

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A reusable, named set of properties that other objects inherit.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Preset
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)

## Overview

This set is stored in `presets.json`.

## Topics

### Dictionaries
- [object Preset.PresetProperties](./preset/presetproperties.md)
  The properties that objects adopting this preset inherit.

## Properties

- `identifier` (string) *(required)*: The unique identifier used to refer to the preset.
- `display_name` (string): The name of the preset as shown in Keynote.
- `parent_identifier` (string): The identifier of a preset that this one inherits from. If no preset has that identifier, a warning is reported and the parent is treated as empty.
- `properties` (Preset.PresetProperties) *(required)*: The properties that objects adopting this preset inherit.

## See Also

### File format
- [object Presentation](./presentation.md)
  A document’s root object, which describes one Keynote presentation.
- [object Manifest](./manifest.md)
  An object that declares which version of Keynote Interchange Format a .keyx file uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/preset)*