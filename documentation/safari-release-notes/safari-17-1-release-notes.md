# Safari 17.1 Release Notes

**Framework**: Safari Release Notes

Released October 25, 2023 — Version 17.1 (19616.2.9)

#### Overview

Safari 17.1 is available for iOS 17.1, iPadOS 17.1, macOS Sonoma, macOS Ventura, and macOS Monterey.

##### Accessibility

###### Resolved Issues

- Fixed properly exposing the expanded state of `<details>` elements on iOS.  (109684906)
- Fixed exposing column headers of cells within `role="row"` elements with `display: contents` to assistive technologies.  (115190637)
- Fixed empty accessibility label for `role="treeitem"` elements with `display: contents` who have child text starting with a newline.  (115226509)

##### Authentication

###### Resolved Issues

- Fixed a bug that could cause authentication through Extensible Enterprise Single Sign-On to hang if the authentication was canceled on the server side.  (105809792)

##### Css

###### Resolved Issues

- Fixed `font-size-adjust` toggling font sizes for `system-ui` font.  (111709567)
- Fixed counter values to prevent them from overflowing or underflowing.  (111743827)
- Fixed `auto none` support for `contain-intrinsic-size`.  (112479718)
- Fixed fine-grained invalidation for `:host` pseudo-class in non-subject position.  (114560066)

##### Javascript

###### Resolved Issues

- Fixed a positive look-behind RegExp with alternatives of different minimum lengths.  (112952197)

##### Loading

###### Resolved Issues

- Fixed an issue with a workaround to handle cases where websites serve Data URLs with malformed padding. This issue prevented some images in Word documents from failing to display when hosted by Box and Sharepoint.  (114573089)

##### Media

###### New Features

- Added support for Managed MediaSource on iOS.  (114270414)

###### Resolved Issues

- Fixed fullscreen ready check to remove the hierarchy requirement.  (110004138)
- Fixed an issue where HTTP Live Streaming (HLS) videos may be offset and clipped within their video element’s frame.  (110467872)
- Fixed videos disappearing when switching from landscape to portrait.  (112416568)
- Fixed vertical multiline WebVTT captions getting cut off.  (112951878)
- Fixed an issue where AirPods spatial audio quality is degraded after loading sites that request user media in Safari.  (113604970)
- Fixed an issue where media will play with sound but no video after pressing the back button in Safari.  (113605284)
- Fixed an issue where media of type `application/x-mpegURL; codecs="avc1.42E01E"` does not play in Safari.  (113608345)
- Fixed an issue where a media element backed by MediaSource may not receive the `seeked` event.  (114594559)

##### Performance

###### Resolved Issues

- Fixed a bug that caused poor performance when resuming WebKit-based apps, including causing a black screen or a blurry snapshot of the app’s prior state to be temporarily visible to users.  (114795818)

##### Rendering

###### Resolved Issues

- Fixed handling iframes with `display: none`.  (112494003)
- Fixed an issue where scrollbars would sometimes show unexpectedly in fullscreen content.  (113605155)
- Fixed a bug that could cause sites to layout improperly in Private Browsing mode.  (113607432)

##### Safari Extensions

###### New Features

- Added support for `storage.session.setAccessLevel` and updated `storage.session` to be accessed only by `TRUSTED_CONTEXTS` by default.  (105952676)

##### Web Api

###### Resolved Issues

- Fixed an issue that could trigger a crash when web content uses WebSockets.  (75425816)
- Fixed intermittent removal of `adoptedStyleSheet` CSSStyleSheet instances when assigning an `adoptedStyleSheet` array.  (107768559)
- Fixed: Improved the performance of IntersectionObserver operations during scrolling.  (111120491)
- Fixed `ElementInternals.setFormValue(<nullish value>)` to clear the submission value.  (111802198)
- Fixed keyboard scroll not stopping after pressing the down arrow if `keyup` is default prevented.  (112396756) (FB12647732)
- Fixed `window.postMessage` with OffscreenCanvas with an isolated world message listener.  (112618195)
- Fixed a bug that could cause a nested popover element within a shadow DOM to improperly dismiss its ancestor popover.  (113604250)

##### Web Apps

###### Resolved Issues

- Fixed handling dismissed notifications on macOS.  (113756668)

##### Web Inspector

###### Resolved Issues

- Fixed objects logged to the console with multiple private fields that use the same name.  (109215331)
- Fixed: Stopped using `Number.prototype.toLocaleString()` for numeric console format specifiers.  (112170843)

##### Webgl

###### Resolved Issues

- Fixed an issue which would cause unnecessary “WebGL: context lost.” errors after Safari has been moved to the background on iPadOS.  (115500744)

## See Also

- [Safari 17.6 Release Notes](safari-17_6-release-notes.md)
  Released July 29, 2024 — 17.6 (19618.3.11)
- [Safari 17.5 Release Notes](safari-17_5-release-notes.md)
  Released May 13, 2024 — 17.5 (19618.2.12)
- [Safari 17.4 Release Notes](safari-17_4-release-notes.md)
  Released March 5, 2024 — 17.4  (19618.1.15)
- [Safari 17.3 Release Notes](safari-17_3-release-notes.md)
  Released January 22, 2024 — Version 17.3 (19617.2.4)
- [Safari 17.2 Release Notes](safari-17_2-release-notes.md)
  Released December 11, 2023 — Version 17.2 (19617.1.17)
- [Safari 17 Release Notes](safari-17-release-notes.md)
  Released September 18, 2023 — Version 17 (19616.1.27)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-17_1-release-notes)*