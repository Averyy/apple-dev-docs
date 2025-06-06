# iOS & iPadOS 13.3 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 13.3 SDK provides support for developing apps for iPhone, iPad, and iPod touch devices running iOS & iPadOS 13.3. The SDK comes bundled with Xcode 11.3 available from the Mac App Store. For information on the compatibility requirements for Xcode 11.3, see [`Xcode 11.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-11_3-release-notes).

##### Networking

###### New Features

- Certain top-level domains (TLDs) such as `.dev` and `.app` are now in the Foundation [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) and [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection) HTTP Strict Transport Security (HSTS) preload list. An app which uses [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) to visit a matching URL will always navigate to the URL as `https://`, and never as cleartext `http://`. See the [`HTTP Strict Transport Security (HSTS) Specification`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6797) for more information about HSTS. (56247242)

##### Safari

###### New Features

- Now supports NFC, USB, and Lightning FIDO2-compliant security keys in Safari, [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController), and [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) using the WebAuthn standard, on devices with the necessary hardware capabilities.

## See Also

- [iOS & iPadOS 13.7 Release Notes](ios-ipados-13_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.6 Release Notes](ios-ipados-13_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.5 Release Notes](ios-ipados-13_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.4 Release Notes](ios-ipados-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.3.1 Release Notes](ios-ipados-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.2 Release Notes](ios-ipados-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.1 Release Notes](ios-ipados-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS 13 Release Notes](ios-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-13_3-release-notes)*