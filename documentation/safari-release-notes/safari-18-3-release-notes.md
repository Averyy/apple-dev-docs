# Safari 18.3 Release Notes

**Framework**: Safari Release Notes

Released January 27, 2025 — 18.3 (20620.2.4)

#### Overview

Safari 18.3 is available for iOS 18.3, iPadOS 18.3, visionOS 2.3, macOS 15.3, macOS Sonoma, and macOS Ventura.

##### Accessibility

###### Resolved Issues

- Fixed VoiceOver to not announce the content of `<script>` elements inside containers with `display: contents`.  (141174582)

##### Css

###### Resolved Issues

- Fixed the `::view-transition` pseudo-element to create a stacking context.  (138196100)
- Fixed an issue where SVG text was not displayed in a `content-visibility: auto` subtree.  (139667754)
- Fixed `:not(:has(...))` invalidation.  (140215464)
- Fixed the default `background-origin` to `border-box` for the `border-area` in shorthand.  (141167096)
- Fixed `text-box` not working correctly on buttons.  (141556699)

##### Editing

###### Resolved Issues

- Fixed duplicated and offset highlights in iCloud Notes.  (140215491)
- Fixed `getRangeAt(0)` returning the same JavaScript object even after selection changes.  (141232989)
- Fixed the inability to tap to place the cursor at end of the line if last word was autocorrected.  (141233042)
- Fixed the drag preview remaining after dragging multiple items and then cancelling the drag.  (141233047)

##### Media

###### Resolved Issues

- Fixed an incorrect aspect ratio for WebM files with non-1:1 source pixels and a `sample-aspect-ratio` setting.  (140352350)

##### Rendering

###### Resolved Issues

- Fixed dynamically changing `scrollbar-width` causing horizontal scrollbars to be painted incorrectly.  (139287706)
- Fixed `<img>` element with `height: min-content` getting stretched vertically.  (139717026)

##### Scrolling

###### Resolved Issues

- Fixed scrollbar appearance when changing to light or dark appearance.  (140215544)

##### Security

###### Deprecations

- Removed support for `Clear-Site-Data: "executionContexts"`.  (138673776)

##### Svg

###### Resolved Issues

- Fixed SVG paths getting clipped at tile boundaries.  (141294412)

##### Web Api

###### Resolved Issues

- Fixed touching or clicking outside of the popover not closing it on iOS or iPadOS.  (139078745)
- Fixed coalesced and predicted events of a given pointer event to have the same pointer identifier as their parent.  (141662290)

##### Web Extensions

###### Resolved Issues

- Fixed an issue where the permissions alert would still appear after clicking the extension icon, even though the user had granted the extension access to all sites.  (139078231)
- Fixed `browser.tabs.create` ignoring the `pinned` and `openerTabId` attributes, also occurring with `browser.tabs.duplicate` on iOS.  (141320890)

##### Web Inspector

###### Resolved Issues

- Fixed the DOM tree view in the Elements tab reducing deeply-nested nodes to one character wide.  (140221149)
- Fixed: Improved the reliability of `safaridriver` connecting to remote devices, especially immediately after toggling the “Remote Automation” setting.  (141166533)

##### Webassembly

###### Resolved Issues

- Fixed memory leaks in WebAssembly Table objects for JSWebAssemblyInstance to improve resource management in WebAssembly instances. This change enhances the stability and performance of WebAssembly in Safari by ensuring proper lifecycle management of internal Table references. No action is required by web developers, but you may notice reduced memory usage in applications that create and manage WebAssembly instances extensively.  (142713278)

##### Wkwebview

###### Resolved Issues

- Fixed an issue where entering full screen in WKWebView on iOS could fail, even with `isElementFullscreenEnabled` enabled.  (140804572)

## See Also

- [Safari 18.5 Release Notes](safari-18_5-release-notes.md)
  Released May 12, 2025 — 18.5 (20621.2.5)
- [Safari 18.4 Release Notes](safari-18_4-release-notes.md)
  Released March 31, 2025 — 18.4 (20621.1.15)
- [Safari 18.2 Release Notes](safari-18_2-release-notes.md)
  Released December 11, 2024 — 18.2 (20620.1.16)
- [Safari 18.1 Release Notes](safari-18_1-release-notes.md)
  Released October 28, 2024 — 18.1 (20619.2.8)
- [Safari 18.0.1 Release Notes](safari-18_0_1-release-notes.md)
  Released October 3, 2024 — 18.0.1 (20619.1.26.30)
- [Safari 18.0 Release Notes](safari-18-release-notes.md)
  Released September 16, 2024 — 18.0 (20619.1.26)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-18_3-release-notes)*