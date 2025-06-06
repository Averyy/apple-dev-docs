# Safari 15.6 Release Notes

**Framework**: Safari Release Notes

Released July 20, 2022 — Version 15.6 (17613.3.9)

#### Overview

Safari 15.6 ships with the iOS & iPadOS 15.6 and macOS 12.5.

##### Css

###### New Features

- Added support for `:modal` CSS pseudo-class.

###### Resolved Issues

- Fixed `object-fit` causing iframe contents to shift.
- Fixed inert behavior to apply to `::after`, `::before`, and `::marker` pseudo-elements.
- Fixed `:focus-visible` matching a mouse click after a second `element.focus()` call.
- Fixed logical inline and logical block viewport units to be based on the current element’s `writing-mode`.

##### Editing

###### Resolved Issues

- Fixed resetting writing direction when inserting a new paragraph breaks out of a quoted reply block.
- Fixed managed pasteboard on iOS to work for all managed locations including managed Safari domains.

##### Fonts

###### Resolved Issues

- Fixed automatically updating page layout when new fonts are installed.

##### Html

###### Resolved Issues

- Fixed `<link rel=preconnect>` to respect `crossorigin=anonymous` and prevent sending credentials to different-origin links.

##### Media

###### Resolved Issues

- Fixed blank video playback with only audio.
- Fixed replaceTrack with different constraints preventing sending packets.
- Fixed WebAudio playback rate speeding up for a few seconds when using `createMediaElementSource`.
- Fixed stalled playback when seeking in a xHE-AAC track backed by a SourceBuffer.
- Fixed starting audio playback in Safari when the device is locked.
- Fixed playback for video when the timeline sometimes goes backward at the start of playback.
- Fixed capturing and rendering audio simultaneously.

##### Rendering

###### Resolved Issues

- Fixed flickering when rendering overlapping negative `z-index` layers.
- Fixed disappearing multi-column content inside a fixed position container when scrolling.
- Fixed images displayed in Reader not appearing in a print job or PDF export.

##### Webauthn

###### Resolved Issues

- Fixed missing text in a sign-in sheet when registering a passkey with syncing platform authenticator disabled, if Touch ID isn’t configured.

##### Web Animations

###### Resolved Issues

- Fixed computing implicit keyframes when either a 0 percent or 100 percent keyframe (or both) define only a timing function.

##### Web Api

###### Resolved Issues

- Fixed communication between BroadcastChannel instances in distinct opaque origins.

##### Web Inspector

###### Resolved Issues

- Fixed resources from memory cache showing empty content in Network, Sources, and Search tabs.

## See Also

- [Safari 15.5 Release Notes](safari-15_5-release-notes.md)
  Released May 16, 2022 — Version 15.5 (17613.2.7)
- [Safari 15.4 Release Notes](safari-15_4-release-notes.md)
  Released March 14, 2022 — Version 15.4 (17613.1.17)
- [Safari 15.2 Release Notes](safari-15_2-release-notes.md)
  Released December 13, 2021 — Version 15.2 (17612.3.6)
- [Safari 15 Release Notes](safari-15-release-notes.md)
  Released September 20, 2021 — Version 15 (17612.1.27)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-15_6-release-notes)*