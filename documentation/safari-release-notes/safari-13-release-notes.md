# Safari 13 Release Notes

**Framework**: Safari Release Notes

Released September 19, 2019 — Version 13 (15608.2.11)

#### Overview

Safari 13 ships with iOS 13 and macOS 10.15. It’s also available for macOS 10.14.5 and 10.13.6.

##### General

###### New Features

- Added Desktop-class Browsing to Safari for iPad. Safari for iPad displays the same desktop websites as Safari for macOS, and provides the same capabilities. In addition it has more keyboard shortcuts, a download manager with background downloads, and support for top productivity websites.
- Added opt-in dark mode support for websites in Safari for iOS.
- Added support for aborting Fetch requests.

##### Authentication and Passwords

###### New Features

- Updated Safari to prompt the user to change weak passwords when signing into a website. Requesting a password change uses the well-known URL for changing passwords, enabling websites to specify the page to open for updating a password.
- Added support for FIDO2-compliant USB security keys with the Web Authentication standard in Safari on macOS.
- Added support for Sign in With Apple to Safari and to [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView).

##### Security and Privacy

###### New Features

- Added a permission API on iOS for [`DeviceMotionEvent`](https://developer.apple.com/documentation/webkitjs/devicemotionevent) and [`DeviceOrientationEvent`](https://developer.apple.com/documentation/webkitjs/deviceorientationevent).
- Changed the behavior for third party iframes to prevent them automatically navigating the page.
- Updated Intelligent Tracking Prevention to prevent cross-site tracking through referrer and through link decoration.
- Improved the privacy of local WebRTC data connections with mDNS ICE candidates.
- Increased the security for WebKit sandboxes on iOS and macOS.

##### Layout and Rendering

###### New Features

- Added support for one-finger accelerated scrolling to all frames and `overflow:scroll` elements eliminating the need to `set-webkit-overflow-scrolling: touch`.
- Changed the default behavior on iPad for wide web pages with responsive meta-tags that require horizontal scrolling. Pages are scaled to prevent horizontal scrolling and any text is resized to preserve legibility.
- Added support for CSS conic gradients.

##### Performance

###### New Features

- Reduced the initial rendering time for webpages on iOS.
- Added automatic support for Fast Tap to desktop websites on iPad.
- Reduced load time up to 50% for webpages on watchOS.
- Reduced the amount of memory used by JavaScript, including for non-web clients.
- Improved the MotionMark graphics performance benchmark score by 10%.

##### Web Api

###### New Features

- Added support for the `__Secure-` and `__Host-` cookie prefixes in beta 3.
- Improved iPad hardware keyboard support for websites including focus navigation and scrolling with the arrow keys.
- Added support for the Pointer Events API enabling consistent access to mouse, trackpad, touch, and Apple Pencil events.
- Added support for the Visual Viewport API for adjusting web content to avoid overlays, such as the onscreen keyboard.
- Added support for programmatic paste with user consent to Safari for iOS.
- Updated editing callouts to avoid in-page controls.
- Added intelligent whitespace to editable WebViews and editable areas of webpages.

##### Payment Request Api

###### New Features

- Added support for Apple Pay on the Web to [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView). Note that using script injection APIs, such as [`WKUserScript`](https://developer.apple.com/documentation/WebKit/WKUserScript) or [`evaluateJavaScript(_:completionHandler:)`](https://developer.apple.com/documentation/WebKit/WKWebView/evaluateJavaScript(_:completionHandler:)) disables Apple Pay for that view.

##### Media

###### New Features

- Added support for the `decodingInfo()` method of the Media Capabilities API for checking supported codecs, efficiently supported codecs, and optional codec features including alpha.
- Added the ability to Safari for macOS to share your screen with others using only web technologies. Plug-ins are no longer required.
- Updated Safari for iPad to support Media Source Extensions.
- Added support for the `navigator.mediaDevices` property of the Media Capture and Streams API to [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController).

###### Resolved Issues

- Transparency in video with an alpha channel now works correctly for all supported video formats.

##### Safari App Extension Api

###### New Features

- Added an API for page navigation notifications.
- Added support for associated Safari App Extensions receiving blocked content notifications from Content Blocker Safari Extensions.

##### Web Inspector and Tools

###### New Features

- Added Safari WebDriver to iOS.
- Added importing and exporting of recorded timeline data.
- Added the CPU Usage Timeline for analyzing and improving the power efficiency of websites.
- Added the Audit tab for running tests against web content including a built-in accessibility audit, importing and exporting results, and creating custom audits.
- Added the Changes sidebar in the Elements tab to track CSS changes in the Styles sidebar.
- Added the Device Settings menu to override developer-related Safari settings when Web Inspector is connected to an iOS device.
- Added a Security tab to the resources view of the Network tab to review certificates and TLS settings.
- Increased the performance of Web Inspector for large sites.

###### Removed Features

- Removed support for WebSQL.
- Removed support for Legacy Safari Extensions.
- Disabled `-webkit-overflow-scrolling: touch `on iPad. All frames and scrollable overflow areas now use accelerated one-finger scrolling without changing stacking.
- Disabled frame flattening on iOS. Frames now render in the same way as a desktop browser.

##### Authenticationservices Framework

###### New Features

- Added [`ASAuthorizationController`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationController) to implement Sign In with Apple and to use a system-provided sign-in account picker for accounts stored in iCloud Keychain.
- Added [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) to the SDK for macOS.
- Added support for using web browsers other than Safari to [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) on macOS. For more information, see [`ASWebAuthenticationSessionWebBrowserSessionManager`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSessionWebBrowserSessionManager).

##### Webkit Framework

###### New Features

- Added API to control desktop and mobile content modes.

##### Javascriptcore Framework

###### New Features

- Added an API for loading ES6 modules.

##### Linkpresentation Framework

###### New Features

- Added LinkPresentation to the SDKs, enabling presentation of web links and better share sheet integration.

##### Mac Catalyst

###### Differences From Ios

- [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) opens the URL in the user’s web browser and immediately calls [`safariViewControllerDidFinish(_:)`](https://developer.apple.com/documentation/SafariServices/SFSafariViewControllerDelegate/safariViewControllerDidFinish(_:)).

## See Also

- [Safari 13.1 Release Notes](safari-13_1-release_notes.md)
  Released March 24, 2020 — Version 13.1 (15609.1.20)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-13-release-notes)*