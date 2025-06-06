# macOS Catalina 10.15.2 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 10.15.2 SDK provides support for developing apps for Macs running macOS Catalina 10.15.2. The SDK comes bundled with Xcode 11.3 available from the Mac App Store. For information on the compatibility requirements for Xcode 11.3, see [`Xcode 11.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-11_3-release-notes).

##### Networking

###### New Features

- Certain top-level domains (TLDs) such as `.dev` and `.app` are now in the Foundation [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) and [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection) HTTP Strict Transport Security (HSTS) preload list. An app which uses [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) to visit a matching URL will always navigate to the URL as `https://`, and never as cleartext `http://`. See the [`HTTP Strict Transport Security (HSTS) Specification`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6797) for more information about HSTS. (56247242)

## See Also

- [macOS Catalina 10.15.6 Release Notes](macos-catalina-10_15_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.5 Release Notes](macos-catalina-10_15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.4 Release Notes](macos-catalina-10_15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.3 Release Notes](macos-catalina-10_15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.1 Release Notes](macos-catalina-10_15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15 Release Notes](macos-catalina-10_15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-catalina-10_15_2-release-notes)*