# Safari 18.1 Release Notes

**Framework**: Safari Release Notes

Released October 28, 2024 — 18.1 (20619.2.8)

#### Overview

Safari 18.1 is available for iOS 18.1, iPadOS 18.1, visionOS 2.1, macOS 15.1, macOS Sonoma, and macOS Ventura.

##### Accessibility

###### Resolved Issues

- Fixed `display: contents` on `tbody` elements preventing table rows from being properly exposed in the accessibility tree.  (129131780)
- Fixed the handling of ElementInternals’s `ariaValueNow` null values so the right value is exposed to assistive technologies.  (129218234)
- Fixed tables with hidden rows reporting wrong counts and blocking access to some rows in VoiceOver.  (129612387)
- Fixed `role="menu"` elements to allow child groups with `menuitem` children.  (131838275)
- Fixed updating the accessibility tree when text underneath an `aria-describedby` element changes.  (131877635)
- Fixed text exposed to assistive technologies when `display: contents` directly wraps a `display: block` text container.  (132265522)
- Fixed VoiceOver not finding any content in a table when `display: table` is applied to `tbody` elements.  (132820485)

##### Authentication

###### Resolved Issues

- Fixed an issue using large credential lists with security keys.  (133711978)

##### Css

###### Resolved Issues

- Fixed style container queries querying the root element.  (124875999)

##### Editing

###### Resolved Issues

- Fixed deleting content immediately before a `<picture>` element unexpectedly removing `<source>` elements.  (128100106)
- Fixed inserting text before a `<picture>` element inserting the text after the element instead.  (134378236)

##### Javascript

###### Resolved Issues

- Fixed incorrect optimization and random non-updated values.  (135851156)

##### Media

###### Resolved Issues

- Fixed a bug in WebCodecs where audio and video codecs with pending work could be prematurely garbage collected.  (134297589)

##### Networking

###### Resolved Issues

- Fixed a bug where `Cross-Origin-Opener-Policy` header fields in the response of iframe elements were not ignored, resulting in `window.opener` being null after multiple cross-origin navigations of the embedder document.  (132840366)

##### Rendering

###### Resolved Issues

- Fixed `content-visibility` to not apply to elements with `display: contents` or `display: none`.  (134436437)
- Fixed float clearing in the WordPress Classic Editor sidebar layout.  (136988841)

##### Security

###### Resolved Issues

- Fixed the `ping` attribute for `<a>` elements to be controlled by the `connect-src` CSP directive.  (131054895)

##### Web Extensions

###### Resolved Issues

- Fixed blob URL downloads failing to trigger from an extension.  (78929424)

##### Webrtc

###### Resolved Issues

- Fixed blurry screen sharing for some sites.  (133611004)

##### Wkwebview

###### New Features

- Added support for the Writing Tools API to enable and customize the behavior in apps.  (128340967)

###### Resolved Issues

- Fixed AVIF in WKWebView on macOS.  (133272264) (FB14678252)

## See Also

- [Safari 18.6 Release Notes](safari-18_6-release-notes.md)
  Released July 29, 2025 — 18.6 (20621.3.11)
- [Safari 18.5 Release Notes](safari-18_5-release-notes.md)
  Released May 12, 2025 — 18.5 (20621.2.5)
- [Safari 18.4 Release Notes](safari-18_4-release-notes.md)
  Released March 31, 2025 — 18.4 (20621.1.15)
- [Safari 18.3 Release Notes](safari-18_3-release-notes.md)
  Released January 27, 2025 — 18.3 (20620.2.4)
- [Safari 18.2 Release Notes](safari-18_2-release-notes.md)
  Released December 11, 2024 — 18.2 (20620.1.16)
- [Safari 18.0.1 Release Notes](safari-18_0_1-release-notes.md)
  Released October 3, 2024 — 18.0.1 (20619.1.26.30)
- [Safari 18.0 Release Notes](safari-18-release-notes.md)
  Released September 16, 2024 — 18.0 (20619.1.26)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-18_1-release-notes)*