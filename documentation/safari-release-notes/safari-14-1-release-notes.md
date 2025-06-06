# Safari 14.1 Release Notes

**Framework**: Safari Release Notes

Released April 26, 2021 — Version 14.1 (16611.1.21)

#### Overview

Safari 14.1 ships with iOS & iPadOS 14.5 and macOS Big Sur 11.3.

##### Authentication and Passwords

###### New Features

- Added support for Touch ID and Face ID via WebAuthentication to all WKWebViews. See [`Web Authentication`](https://developer.apple.comhttps://www.w3.org/TR/webauthn/) for more information.

##### Css and Web Animations

###### New Features

- Added support for [`CSS individual transform properties: translate, rotate, and scale`](https://developer.apple.comhttps://drafts.csswg.org/css-transforms-2/#individual-transforms).
- Web Animations now support animating discrete properties and pseudo-elements, see [`Web Animations`](https://developer.apple.comhttps://drafts.csswg.org/web-animations-1/).
- Safari now supports flexbox gaps with `row-gap` and `column-gap`, see [`Gap Shorthand: the gap property`](https://developer.apple.comhttps://drafts.csswg.org/css-align/#gap-flex).

##### Javascript and Webassembly

###### New Features

- Added support for static instance class fields, private instance class fields, and static public class fields — public instance class fields were already supported. See [`Public and private instance fields proposal`](https://developer.apple.comhttps://tc39.es/proposal-class-fields/) for more information.
- Added support for new ECMAScript Internationalization API features: - Added [`Intl.NumberFormat updates`](https://developer.apple.comhttps://github.com/tc39/proposal-unified-intl-numberformat).
- Added [`Intl.DisplayNames updates`](https://developer.apple.comhttps://github.com/tc39/proposal-intl-displaynames).
- Added [`Intl.ListFormat updates`](https://developer.apple.comhttps://github.com/tc39/proposal-intl-list-format).
- Added [`Intl.Segmenter`](https://developer.apple.comhttps://github.com/tc39/proposal-intl-segmenter).
- Added `Intl.DateTimeFormat` updates to [`dateStyle and timeStyle options on the Intl.DateTimeFormat API Specification`](https://developer.apple.comhttps://github.com/tc39/proposal-intl-datetime-style), [`Intl.DateTimeFormat.prototype.formatRange`](https://developer.apple.comhttps://github.com/tc39/proposal-intl-DateTimeFormat-formatRange), [`Add dayPeriod option`](https://developer.apple.comhttps://github.com/tc39/ecma402/pull/346), and [`Add fractionalSecondDigits option`](https://developer.apple.comhttps://github.com/tc39/ecma402/pull/347).
- Added support for [`WeakRefs and FinalizationRegistry`](https://developer.apple.comhttps://tc39.es/proposal-weakrefs/).
- Added support for [`Arbitrary module namespace identifier names`](https://developer.apple.comhttps://github.com/tc39/ecma262/pull/2154).
- Added support for WebAssembly atomic instructions in the [`Threading specification`](https://developer.apple.comhttps://webassembly.github.io/threads/core/).
- Added support for [`WebAssembly BigInt integration`](https://developer.apple.comhttps://github.com/WebAssembly/JS-BigInt-integration).
- Added support for [`WebAssembly Sign-extension instructions`](https://developer.apple.comhttps://github.com/WebAssembly/sign-extension-ops).

##### Media

###### New Features

- Added support for WebM files containing VP8 or VP9 video tracks and Vorbis audio tracks in macOS, see [`WebM Container Guidelines`](https://developer.apple.comhttps://www.webmproject.org/docs/container/).
- Added support for MediaStream Recording to enable websites to record audio and video, see [`MediaStream Recording`](https://developer.apple.comhttps://w3c.github.io/mediacapture-record/MediaRecorder.html).
- Added support for [`getUserMedia`](https://developer.apple.comhttps://w3c.github.io/mediacapture-main/#dom-mediadevices-getusermedia) from MediaStream and Capture API in WKWebView.

##### Safari Web Extensions

###### New Features

- Added support for WebExtensions API to replace the new tab page.
- Added support for non-persistent background pages.

##### Security and Privacy

###### New Features

- Improved Storage Access API interoperability and specification compliance, see [`Storage Access API`](https://developer.apple.comhttps://webkit.org/blog/11545/updates-to-the-storage-access-api/).
- Added support for [`Private Click Measurement`](https://developer.apple.comhttps://webkit.org/blog/11529/introducing-private-click-measurement-pcm/), enabling privacy-preserving ad attribution for web-to-web and app-to-web flows.

##### Webkit Framework

###### New Features

- Added support for HTML `date`, `time`, and `datetime-local` input types in macOS, enabling date and time controls in forms. For more information, see [`Date state (type=date)`](https://developer.apple.comhttps://html.spec.whatwg.org/#date-state-(type=date)).
- Added support for Web Audio API, now unprefixed, compliant, and including Audio Worklets. This enables better compatibility for advanced audio processing, see [`Web Audio API`](https://developer.apple.comhttps://www.w3.org/TR/webaudio/) for more information.
- Added support for [`Web Speech API`](https://developer.apple.comhttps://wicg.github.io/speech-api/) that enables speech recognition and speech synthesis for websites.
- Improved mouse support in iPadOS and in apps built with Mac Catalyst, including scrolling events and hover/pointer media queries.
- Added support for Paint Timing, a Web API that measures how quickly a webpage is displayed.  See [`Paint Timing 1`](https://developer.apple.comhttps://w3c.github.io/paint-timing/) for more information.

## See Also

- [Safari 14 Release Notes](safari-14-release-notes.md)
  Released September 16, 2020 — Version 14 (16610.1.28)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-14_1-release-notes)*