# Safari 26.6 Release Notes

**Framework**: Safari Release Notes

Released July 27, 2026 — 26.6 (20624.4.5)

#### Overview

Safari 26.6 is available for iOS 26.6, iPadOS 26.6, visionOS 26.6, macOS 26.6, macOS Sequoia, and macOS Sonoma.

##### Css

###### Resolved Issues

- Fixed an issue where the `ic` length unit scaled incorrectly with page zoom, causing it to no longer equal `1em` as expected by the CSS specification. (174857144)
- Fixed an issue where fixed-positioned elements using `position-area` did not fall back properly when the body was scrollable. (175544079)
- Fixed an issue where CSS `zoom` interacted incorrectly with `font-size`, `font-weight`, `font-variant`, and `font-style` on iPad when requesting the desktop website. (176647969)

##### Networking

###### Resolved Issues

- Fixed an issue where partitioned cookies could not be deleted using `WKHTTPCookieStore`. (176097960)

##### Service Workers

###### Resolved Issues

- Fixed an issue where service worker registrations with missing main scripts were not automatically unregistered, preventing pages from re-registering new service workers. (175522651)
- Fixed an issue where service worker registrations with missing imported scripts were not automatically unregistered. (175522816)

##### Web Extensions

###### Resolved Issues

- Fixed an issue where web extension service worker registration database files accumulated on each Safari launch, causing performance degradation. (175810627)

##### Webassembly

###### New Features

- Added `compileOptions` parameter to `WebAssembly.compileStreaming` and `WebAssembly.instantiateStreaming` for JS String Builtins support. (174858653)

##### Webrtc

###### Resolved Issues

- Fixed an issue where `RTCPeerConnection` configured with `iceTransportPolicy: "relay"` failed to gather any ICE candidates on macOS Sequoia. (175009190)

## See Also

- [Safari 26.5 Release Notes](safari-26_5-release-notes.md)
  Released May 11, 2026 — 26.5 (20624.2.5)
- [Safari 26.4 Release Notes](safari-26_4-release-notes.md)
  Released March 24, 2026 — 26.4 (20624.1.16)
- [Safari 26.3 Release Notes](safari-26_3-release-notes.md)
  Released February 11, 2026 — 26.3 (20623.2.7)
- [Safari 26.2 Release Notes](safari-26_2-release-notes.md)
  Released December 12, 2025 — 26.2 (20623.1.14)
- [Safari 26.1 Release Notes](safari-26_1-release-notes.md)
  Released November 3, 2025 — 26.1 (20622.2.11)
- [Safari 26.0 Release Notes](safari-26-release-notes.md)
  Released September 15, 2025 — 26 (20622.1.22)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-26_6-release-notes)*