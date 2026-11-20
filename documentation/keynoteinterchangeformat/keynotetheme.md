# KeynoteTheme

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The Keynote theme a presentation is based on.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object KeynoteTheme
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)

## Overview

A theme provides the presentation’s default slide layouts, styles, and background. It’s chosen by its `name`, as shown in Keynote, and `slide_layouts` can replace the layouts it provides.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.keynote-theme`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `name` (string): The name of the theme to base the presentation on, as shown in Keynote’s theme chooser (for example, `White` or `Gradient`). Because the name is localized, pair it with `locale`. Themes in My Themes are matched before built-in ones, and a name that matches nothing, like an absent name, falls back to the White theme. When Keynote exports a presentation whose custom theme isn’t in My Themes, it writes `White` here, so the presentation opens in the White theme even where that theme is available.
- `locale` (string): The locale of the theme name given in `name`. If it’s absent, the system locale is used. The value is a BCP 47 language identifier, such as `en_US` or `en-u-nu-thai-ca-buddhist`, or an ICU-style identifier, such as `en@calendar=buddhist;numbers=thai`.
- `slide_layouts` ([SlideLayout]): The slide layouts to use in place of the ones the theme provides. If it’s present, the list replaces the theme’s own layouts entirely and must contain at least one entry. Each entry’s `name` must be unique within the theme, because a slide selects its layout by identifier or name. If it’s absent, it defaults to the theme’s layouts. Validation: minimum `1` item.

## See Also

### Styling
- [object Stylesheet](./stylesheet.md)
  A collection of styles to use as presets for various objects in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/keynotetheme)*