# Safari 16.2 Release Notes

**Framework**: Safari Release Notes

Released December 13, 2022 — Version 16.2 (18614.3.7)

#### Overview

Safari 16.2 is available for macOS Big Sur, macOS Monterey, macOS Ventura, iPadOS 16.2, and iOS 16.2.

##### Css

###### New Features

- Added support for additional values for the  `font-variant-alternates` property: `annotation(value-name)`, `character-variant(value-name)`, `ornaments(value-name)`, `styleset(value-name)`, `stylistic(value-name)`, `swash(value-name)`, along with the associated `@font-feature-values` at-rule.
- Added support for `last baseline` alignment for Flexbox and Grid.
- Added support for `color-mix()`.
- Added support for Gradient Interpolation Color Spaces.

###### Resolved Issues

- Fixed backgrounds with a `fixed` attachment to behave like `scroll` inside transformed elements.
- Fixed calculating inline `min-content` size to include the `aspect-ratio` and add the `min-content` block computation.
- Fixed flexbox cases where border and padding are added twice to the computed min and max sizes.
- Fixed flex base size width calculation to not consider min and max sizes.
- Fixed focus behavior to not take into account scroll margin when checking visibility.
- Fixed layout containment to not propagate forced breaks to the parent.
- Fixed percentage based translations not working with SVG `<text>` elements.
- Fixed `perspective: 0` behavior.
- Fixed re-snap to follow scroll snap target if necessary.
- Fixed scroll snap to choose the closest snap target if targets on each axes aren’t visible.
- Fixed `text-decoration-thickness` property to not be inherited.
- Fixed transforms on SVG shapes and groups when the root element size is changed.
- Fixed `text-decoration` location for superscripts and subscripts when the text string contains both regular text and either superscript or subscript.
- Fixed `text-decoration` pixel alignment when the content is truncated.
- Fixed removing the intrinsic margin when specifying the width or height of an `<input>` element.
- Fixed rounding for `rgba()` channels.
- Fixed `font-variant` shorthand parsing to allow the `font-variant-east-asian` property in any position.
- Fixed scroll snapping on a date input with `scroll-margin` applied.

##### Rendering

###### Resolved Issues

- Fixed applying `lineWidth` and `strokeStyle` when drawing on .
- Fixed `contain: content` breaking scrolling when applied to the body.
- Fixed applying `transform-origin` with a z-component.
- Fixed computing the baseline position for tables when margins are applied.
- Fixed applying transforms to table sections: `tbody`, `thead`, and `tfoot`.
- Fixed: transform changes recompute overflow.

##### Media

###### Resolved Issues

- Fixed updating MediaSessionInfo for a media element when a `srcObject` is used.

##### Web Api

###### Resolved Issues

- Fixed SharedWorker to honor `Upgrade-Insecure-Request`.

##### Webdriver

###### Resolved Issues

- Fixed Element Click command failing on iOS.
- Fixed: Enabled `touch` pointer input source subtype on iOS.

## See Also

- [Safari 16.6 Release Notes](safari-16_6-release-notes.md)
  Released July 24, 2023 — Version 16.6 (18615.3.12)
- [Safari 16.5 Release Notes](safari-16_5-release-notes.md)
  Released May 18, 2023 — Version 16.5 (18615.2.9)
- [Safari 16.4 Release Notes](safari-16_4-release-notes.md)
  Released March 27, 2023 — Version 16.4 (18615.1.26)
- [Safari 16.3 Release Notes](safari-16_3-release-notes.md)
  Released January 23, 2023 — Version 16.3 (18614.4.6)
- [Safari 16.1 Release Notes](safari-16_1-release-notes.md)
  Released October 24, 2022 — Version 16.1 (18614.2.9)
- [Safari 16 Release Notes](safari-16-release-notes.md)
  Released September 12, 2022 — Version 16 (18614.1.25)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-16_2-release-notes)*