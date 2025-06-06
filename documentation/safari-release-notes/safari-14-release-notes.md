# Safari 14 Release Notes

**Framework**: Safari Release Notes

Released September 16, 2020 — Version 14 (16610.1.28)

#### Overview

Safari 14 ships with iOS & iPadOS 14 and macOS Big Sur 11.

##### General

###### New Features

- Added Safari Web Extensions support for macOS.
- Added Webpage Translation for English, Spanish, Simplified Chinese, French, German, Russian, and Brazilian Portuguese. Safari will automatically detect if a translation is available based on your Preferred Languages list.
- Added support for HTTP/3.
- Improved Web Platform Tests pass rate for WebDriver, XHR+Fetch, Service Workers, CSS, and SVG.

###### Removed Features

- Safari no longer supports Flash.

##### Performance

###### New Features

- Supported incremental loading of PDF files.
- Implemented asynchronous scrolling for `overflow: scroll`, and `<iframe>` on macOS.
- Improved tab closing performance.
- Improved `IndexedDB` performance.
- Improved JavaScript cookie access performance.
- Improved `for-of` performance.

##### Privacy

###### New Features

- Added a Privacy Report that shows the trackers that Intelligent Tracking Prevention prevented from accessing identifying information.
- Enabled full third-party cookie blocking, and the Storage Access API in Private Browsing mode.

##### Authentication and Passwords

###### New Features

- Added a Web Authentication platform authenticator using Face ID or Touch ID, depending on which capability is present.
- Added support for PIN entry and account selection on external Web Authentication security keys.
- Added notifying users when one of their saved passwords in iCloud Keychain has shown up in a data breach; requesting a password change uses the [`well-known URL for changing passwords`](https://developer.apple.comhttps://wicg.github.io/change-password-url/) (https://example.com/.well-known/change-password), enabling websites to specify the page to open for updating a password.
- Added support to Security Code AutoFill for [`domain-bound, one-time codes sent over SMS`](https://developer.apple.comhttps://wicg.github.io/sms-one-time-codes/); in the following 2FA SMS, Safari  only offers to fill the code on example.com, and no other domain. ```None
Your Example code is 123446.

@example.com #123446
```

##### Javascript

###### New Features

- Added support for the `BigInt` data type.
- Added support for creating custom instances of `EventTarget`.
- Added logical assignment operator support.
- Added public class fields support.

##### Media

###### New Features

- Added WebP image support.
- Added HDR video playback support.
- Changed to derive `<img>` aspect ratio from size attributes.
- Support for the Picture-in-Picture API is now available in iOS on iPhone.

##### Css

###### New Features

- Updated `image-set()` to support all other image functions including `image()`, `-webkit-canvas()`, `-webkit-cross-fade()`, and `-webkit-*-gradient()`.
- Added `:is()` pseudo-selector support as a synonym for `:matches()`.
- Added `:where()` pseudo-selector support for specificity adjustment.
- Added support for `image-orientation`.

##### Web Inspector

###### New Features

- Added support for a bootstrap script.
- Added a Sources Tab that combines the Resources tab and Debugger tab.
- Added an HSL color picker with P3 support.
- Added information about Web Animations, CSS animations, and CSS transitions to the Timelines tab.
- Improved VoiceOver support.

## See Also

- [Safari 14.1 Release Notes](safari-14_1-release-notes.md)
  Released April 26, 2021 — Version 14.1 (16611.1.21)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-14-release-notes)*