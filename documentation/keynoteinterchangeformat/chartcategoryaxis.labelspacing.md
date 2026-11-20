# ChartCategoryAxis.LabelSpacing

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The spacing of the category labels along the axis.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(object | string("auto_fit" | "none" | "show_all")) ChartCategoryAxis.LabelSpacing
```



**Allowed Types**: `object`, `string("auto_fit" | "none" | "show_all")`

## Overview

A label can be shown for every category, or for a reduced set chosen to fit the space available.

Every Nth category label is shown, where N is the given value. An N of `0` is written as `auto_fit` instead, and an N of `1` as `show_all`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.chart-category-axis.label-spacing`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `custom` (integer) *(required)*: Every Nth category label is shown, where N is the given value. An N of `0` is written as `auto_fit` instead, and an N of `1` as `show_all`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartcategoryaxis.labelspacing)*