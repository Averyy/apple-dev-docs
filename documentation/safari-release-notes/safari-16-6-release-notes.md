# Safari 16.6 Release Notes

**Framework**: Safari Release Notes

Released July 24, 2023 — Version 16.6 (18615.3.12)

#### Overview

Safari 16.6 is available for macOS Big Sur, macOS Monterey, macOS Ventura, iPadOS 16.6, and iOS 16.6.

##### Css

###### Resolved Issues

- Fixed using `currentcolor` with `color-mix()`.
- Fixed content at `block-start` edge to have their trimmed margins reflected in the computed style.
- Fixed trimmed `block-end` margins for block containers to be reflected in the computed style in a horizontal writing mode.
- Fixed compression streams to handle large outputs during the flush stage.
- Fixed trimming nested self-collapsing children at `block-end`.
- Fixed the CSS `hypot()` function sometimes returning the result squared.
- Fixed container query length units to use the content box instead of the border box.
- Fixed serializing properties directly in the parent group rule only for the first nested style rule.

##### Forms

###### Resolved Issues

- Fixed the value not updating on `<meter>` and `<progress>` elements.

##### Web Api

###### Resolved Issues

- Fixed `putImageData` to draw on the correct canvas.

## See Also

- [Safari 16.5 Release Notes](safari-16_5-release-notes.md)
  Released May 18, 2023 — Version 16.5 (18615.2.9)
- [Safari 16.4 Release Notes](safari-16_4-release-notes.md)
  Released March 27, 2023 — Version 16.4 (18615.1.26)
- [Safari 16.3 Release Notes](safari-16_3-release-notes.md)
  Released January 23, 2023 — Version 16.3 (18614.4.6)
- [Safari 16.2 Release Notes](safari-16_2-release-notes.md)
  Released December 13, 2022 — Version 16.2 (18614.3.7)
- [Safari 16.1 Release Notes](safari-16_1-release-notes.md)
  Released October 24, 2022 — Version 16.1 (18614.2.9)
- [Safari 16 Release Notes](safari-16-release-notes.md)
  Released September 12, 2022 — Version 16 (18614.1.25)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-16_6-release-notes)*