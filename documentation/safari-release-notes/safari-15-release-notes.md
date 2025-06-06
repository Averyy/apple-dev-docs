# Safari 15 Release Notes

**Framework**: Safari Release Notes

Released September 20, 2021 — Version 15 (17612.1.27)

#### Overview

Safari 15 ships with iOS and iPadOS 15 and macOS 12.

##### General

###### New Features

- Redesigned the Safari user interface in macOS 12, iOS and iPadOS 15, along with adding Tab Groups and customization sync.

##### Authentication and Passwords

###### New Features

- Added support for Verification Codes to the iCloud Keychain Password Manager. To use verification codes with Safari and Autofill: - Use `autocomplete=one-time-code` to make an `<input>` eligible for AutoFill.
- Use a standard `otpauth` URL and replace the scheme with `apple-otpauth` to link directly to the password manager for setup.
- Use a raster image to enable contextual menus on `otpauth` QR codes that offer to set up a verification code generator.
- Added technology preview of passkeys in iCloud Keychain: - Passkeys are WebAuth credentials intended to replace passwords for website and apps with device sync and backup.
- To Enable the technology preview, in Safari choose Develop > Enable Syncing Platform Authenticator.

##### Css

###### New Features

- Added support for `aspect-ratio` for box elements.
- Added support for `lab()`, `lch()`, `hwb()` color syntaxes.
- Added support for predefined color spaces using the `color()` syntax: [`srgb`](https://developer.apple.comhttps://drafts.csswg.org/css-color-4/#valdef-color-srgb), [`display-p3`](https://developer.apple.comhttps://drafts.csswg.org/css-color-4/#valdef-color-display-p3), [`a98-rgb`](https://developer.apple.comhttps://drafts.csswg.org/css-color-4/#valdef-color-a98-rgb), [`prophoto-rgb`](https://developer.apple.comhttps://drafts.csswg.org/css-color-4/#valdef-color-prophoto-rgb), [`rec2020`](https://developer.apple.comhttps://drafts.csswg.org/css-color-4/#valdef-color-rec2020), [`xyz`](https://developer.apple.comhttps://drafts.csswg.org/css-color-4/#valdef-color-xyz).
- Adjusted environment variable calculations where appropriate to adjust for the safe area of the new iOS design.

##### Html

###### New Features

- Redesigned form controls in iOS.
- Added support for the `theme-color` meta tag to change the tab bar background and over-scroll area in macOS and iPadOS, and the status bar in iOS.
- Added support for the `media` attribute to specify `theme-color` meta tags for Dark Mode and light appearance. ```None
<meta name="theme-color" 
      content="#ecd96f" 
      media="(prefers-color-scheme: light)">
<meta name="theme-color" 
      content="#0b3e05" 
      media="(prefers-color-scheme: dark)">
```

##### Javascript

###### New Features

- Added top-level `await`.
- Added support for ES6 Modules in Workers and ServiceWorkers.
- Added support for `Error.cause`.
- Added support for private class methods and accessors (Safari 14.1 added support for private data member syntax).
- Added support for `BigInt64Array` and `BigUint64Array`.

##### Media

###### New Features

- Added support for the MediaSession API to enable SharePlay experiences.
- Added Playback Speed and Chapters menus to built-in media controls.
- Added hardware accelerated VP9 and WebM in MSE on all iPads that support iPadOS 15.
- Added support for the Opus audio codec in WebM containers.

##### Security Privacy

###### New Features

- Added support for automatic HTTPS upgrades.
- Added IP address hiding from known trackers which users can enable in Safari Preferences.
- Private Click Measurement enhancements for privacy-preserving ad click attribution: - Updated attribution reporting to also send reports to the click destination.
- Added click fraud prevention with un-linkable tokens.
- Added IP address protection for attribution reports.

##### Payments

###### New Features

- Added support for indicating an estimated arrival date for shipping methods.
- Added support for the user to enter a coupon code.
- Added support for marking the shipping method as in-store pickup.

##### Webassembly

###### New Features

- Added support for streaming compilation.
- Added support for bulk memory operations.
- Added support for reference types.
- Added support for non-trapping conversions from `float` to `int`.

##### Web Apis

###### New Features

- Added support for WebGL 2. The implementation of WebGL runs on top of [`Metal`](https://developer.apple.com/documentation/Metal) for better performance.
- Added support for Web Share level 2 enhancements to Web Share that enable sharing files from a web page to an app. See [`Web Share API`](https://developer.apple.comhttps://w3c.github.io/web-share/) for more information.
- User gestures now propagate through `requestAnimationFrame` with a one second time limit.

##### Web Extensions

###### New Features

- Added support for Safari Web Extensions in iOS and iPadOS.
- Added support for `declarativeNetRequest` in Safari Web Extensions.

##### Web Inspector

###### New Features

- Added an inspected page overlay for visualizing and debugging CSS grid contexts.

## See Also

- [Safari 15.6 Release Notes](safari-15_6-release-notes.md)
  Released July 20, 2022 — Version 15.6 (17613.3.9)
- [Safari 15.5 Release Notes](safari-15_5-release-notes.md)
  Released May 16, 2022 — Version 15.5 (17613.2.7)
- [Safari 15.4 Release Notes](safari-15_4-release-notes.md)
  Released March 14, 2022 — Version 15.4 (17613.1.17)
- [Safari 15.2 Release Notes](safari-15_2-release-notes.md)
  Released December 13, 2021 — Version 15.2 (17612.3.6)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-15-release-notes)*