# Safari 12 Release Notes

**Framework**: Safari Release Notes

Released September 17, 2018 — Version 12 (14606.1.36)

#### Overview

Safari 12 is included with iOS 12 and macOS 10.14. It’s also available for macOS 10.13.6 and 10.12.6.

New features of Safari 12 include:

-  Show website icons in tabs.
-  Automatically generate strong, unique passwords when you sign up for accounts or change passwords on websites.
-  View 3D models or jump into an AR viewing experience in Safari on iOS 12.

##### Web on Watchos

###### New Features

- Added support for viewing web pages and HTML from Mail and Messages on watchOS 5 with Apple Watch Series 3 or later.

##### Authentication and Passwords

###### New Features

- Added support for automatically generating unique strong passwords when creating an account and updating passwords.
- Added support for compatibility with the `passwordrules` attribute when generating passwords.
- Added support for suggesting user names during sign-up flows.
- Added support for using `username`, `current-password`, and `new-passwordvalues` for the `autocomplete` attribute in credential-related forms. For example, `<input type="password" autocomplete="new-password">`.
- Added support for filling security codes delivered over SMS.
- Added support for tagging text fields using the `one-time-code` value of the `autocomplete` attribute to ensure that Security Code AutoFill is offered.
- Added support for using security codes from text messages with a numeric sequence near the word “code”, such as “Your secure login code is: 123456.”

##### Media

###### New Features

- Added support for viewing USDZ models embedded in websites in 3D and AR.
- Added support for viewing HTML elements in full screen on iPad.

##### Css and Text

###### New Features

- Added support for font collections in WOFF2 and TTC files.
- Added support for defining letterforms in OpenType fonts using SVG.
- Added support for the `font-display` CSS property to declaratively control web font loading behaviors.
- Improved HSL and HSLA parsing to match the [`CSS Color Module Level 4 specification`](https://developer.apple.comhttps://drafts.csswg.org/css-color-4/#the-hsl-notation).

##### Security and Privacy

###### New Features

- Added improvements to Intelligent Tracking Prevention including: permanently partitioning cookie access in third-party contexts, adding a user prompt to the Storage Access API, detecting bounce trackers and purging their website data, identifying tracker collusion, and sending origin-only headers for third-party tracker requests.
- Added support for specifying cookies that shouldn’t be sent for cross-site requests.
- Added support for `cross-origin-window-policy` and `cross-origin-resource-policy` to defend against Cross Site Script Inclusion attacks.

##### Web Inspector and Tools

###### New Features

- Added support for debugging WebGL shaders in the Canvas tab.
- Updated Safari WebDriver to implement the protocol as defined by the [`W3C WebDriver`](https://developer.apple.comhttps://www.w3.org/TR/webdriver/) specification

##### Safari Extensions

###### Deprecations

- Deprecated support for `.safariextz` Safari Extensions installed from the Safari Extensions Gallery with Safari 12 on macOS. Submissions to the Safari Extensions Gallery will no longer be accepted after December 2018. Developers are encouraged to transition to Safari App Extensions.
- Disabled `canLoad` Safari Extensions on first launch. Safari Extensions that make use of the `canLoad` event are disabled on first launch and users are notified with a warning that their use is harmful to performance. These extensions can be enabled in Safari Extensions preferences. Developers are encouraged to move to Content Blocker Extensions.
- Removed Support for Developer-signed `.safariextz` Safari Extensions in Safari 12 on macOS. They no longer appear in Safari preferences and cannot be enabled. If a user has one of these extensions installed, they receive a warning notification on first launch.

##### Legacy Npapi Plugins

###### Deprecations

- Removed support for running legacy NPAPI plugins other than Adobe Flash.

## See Also

- [Safari 12.1 Release Notes](safari-12_1-release-notes.md)
  Released March 25, 2019 — Version 12.1 (14607.1.40)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-12-release-notes)*