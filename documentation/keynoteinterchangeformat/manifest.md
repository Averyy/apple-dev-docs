# Manifest

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An object that declares which version of Keynote Interchange Format a .keyx file uses.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Manifest
```

## Overview

This version information is stored in `manifest.json`.

## Properties

- `package_version` (string): The package format version, in major.minor format. Keynote also reads it as a number or as a `{major, minor}` object.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`

## See Also

### File format
- [object Presentation](./presentation.md)
  A document’s root object, which describes one Keynote presentation.
- [object Preset](./preset.md)
  A reusable, named set of properties that other objects inherit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/manifest)*