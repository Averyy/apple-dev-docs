# Safari 17.5 Release Notes

**Framework**: Safari Release Notes

Released May 13, 2024 — 17.5 (19618.2.12)

#### Overview

Safari 17.5 is available for iOS 17.5, iPadOS 17.5, visionOS 1.2, macOS Sonoma, macOS Monterey, and macOS Ventura.

##### Accessibility

###### Resolved Issues

- Fixed a bug preventing VoiceOver word echoing in some text fields.  (122451549) (FB13592798)

##### Animations

###### Resolved Issues

- Fixed flickering with multiple accelerated animations and direction changes.  (117815004)

##### Authentication

###### Resolved Issues

- Fixed `excludeCredentials` property being ignored during a passkey registration request.  (124405037)

##### Css

###### New Features

- Added support for the `light-dark()` color function.  (123854183)
- Added support for `text-wrap-style: auto/balance/stable`.  (123854373)
- Added support for `@starting-style`.  (123854536)
- Added support for `@supports()` syntax for `@import` rules.  (123854667)

###### Resolved Issues

- Fixed the proximity calculation for implicit `@scope`.  (124640124)
- Fixed the Grid track sizing algorithm logical height computation avoid unnecessary grid item updates.  (124713418)
- Fixed any `@scope` limit making the element out of scope.  (124956673)

##### Forms

###### Resolved Issues

- Fixed native text fields becoming invisible in dark mode.  (123658326)
- Fixed fallback native `<select>` rendering in dark mode.  (123845293)

##### Media

###### New Features

- Added support for WebCodecs AV1 when an AV1 hardware decoder is available.  (123433815)

###### Resolved Issues

- Fixed scrolling for an element when a video element with `pointer-events: none` is placed over it.  (118936715)
- Fixed HTML5 `<audio>` playback to continue to the next media activity when in the background.  (121268089) (FB13551577)
- Fixed AV1 to decode in hardware on iPhone 15 Pro.  (121924090)
- Fixed audio distortion over internal speakers when streaming content in web browsers.  (122590884)
- Fixed firing `loadeddata` events for `<audio>` and `<video>` on page load.  (124079735) (FB13675360)

##### Rendering

###### Resolved Issues

- Fixed adjusting the size of the scrollable area when changing betwen non-overlay and overlay scrollbars.  (117507268)
- Fixed flickering when showing a layer on a painted background for the first time by avoiding async image decoding.  (117533495)
- Fixed line breaking before or between ruby sequences.  (122663646)

##### Web Api

###### Resolved Issues

- Fixed `mousemove` events in an `iframe` when the mouse is clicked from outside the `iframe` and then moves into it while the button is held down.  (120540148) (FB13517196)

##### Web Apps

###### Resolved Issues

- Fixed several issues that caused Web Push to not show notifications when the web app or Safari was not already running.  (124075358)

##### Web Inspector

###### Resolved Issues

- Fixed info and debug buttons not appearing in the Console Tab until new console messages are displayed.  (122923625)

##### Webgl

###### New Features

- Added support for `EXT_conservative_depth` and `NV_shader_noperspective_interpolation`.  (123854629)

##### Webrtc

###### Resolved Issues

- Fixed WebCodecs to correctly use the VP9 hardware decoder.  (123475343)
- Fixed no incoming video in Teams VA.  (124406255)
- Fixed the camera pausing occasionally when torch is enabled.  (124434403)

##### Wkwebview

###### New Features

- Added logging MarketplaceKit errors to the JavaScript console to make errors easier to debug.  (123475774)

## See Also

- [Safari 17.6 Release Notes](safari-17_6-release-notes.md)
  Released July 29, 2024 — 17.6 (19618.3.11)
- [Safari 17.4 Release Notes](safari-17_4-release-notes.md)
  Released March 5, 2024 — 17.4  (19618.1.15)
- [Safari 17.3 Release Notes](safari-17_3-release-notes.md)
  Released January 22, 2024 — Version 17.3 (19617.2.4)
- [Safari 17.2 Release Notes](safari-17_2-release-notes.md)
  Released December 11, 2023 — Version 17.2 (19617.1.17)
- [Safari 17.1 Release Notes](safari-17_1-release-notes.md)
  Released October 25, 2023 — Version 17.1 (19616.2.9)
- [Safari 17 Release Notes](safari-17-release-notes.md)
  Released September 18, 2023 — Version 17 (19616.1.27)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-17_5-release-notes)*