# watchOS 5 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 5 SDK provides support for developing watchOS apps for Apple Watch devices running watchOS 5. For information about new features in watchOS 5, see [`What’s New in watchOS`](https://developer.apple.comhttps://developer.apple.com/watchos/whats-new/). The SDK comes bundled with Xcode 10 available from the Mac App Store. For information about Xcode 10, see [`Xcode 10 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-10-release-notes).

##### Networking

###### New Features

- The [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) HTTP/2 implementation has been updated to support HTTP/2 connection reuse per RFC 7540 Section 9.1.1. This requires an HTTP/2 server to present a certificate which covers more than one server hostname. The certificate may use the Subject Alternative Name extension or wildcarded domain names. In addition, [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) requires name resolution to resolve the different hostnames to the same IP address. [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) might reuse HTTP/2 connections across different domain names when these conditions are satisfied. (37507838)

###### Deprecations

- The `ftp://` and `file://` URL schemes for Proxy Automatic Configuration (PAC) are deprecated. HTTP and HTTPS are the only supported URL schemes for PAC. This affects all PAC configurations including, but not limited to, configurations set via Settings, System Preferences, profiles, and [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) APIs such as [`connectionProxyDictionary`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/connectionProxyDictionary), and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](https://developer.apple.com/documentation/CFNetwork/CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)). (37811761)

##### Watchkit

###### New Features

- The tint color of a [`WKInterfaceVolumeControl`](https://developer.apple.com/documentation/WatchKit/WKInterfaceVolumeControl) can now be set by calling the [`setTintColor(_:)`](https://developer.apple.com/documentation/WatchKit/WKInterfaceVolumeControl/setTintColor(_:)) method. (40565782)

###### Deprecations

- The [`updateUserActivity(_:userInfo:webpageURL:)`](https://developer.apple.com/documentation/WatchKit/WKInterfaceController/updateUserActivity(_:userInfo:webpageURL:)) method doesn’t properly register activities. Use [`update(_:)`](https://developer.apple.com/documentation/WatchKit/WKInterfaceController/update(_:)) instead. (39840960)
- The [`didReceive(_:withCompletion:)`](https://developer.apple.com/documentation/WatchKit/WKUserNotificationInterfaceController/didReceive(_:withCompletion:)) method doesn’t receive grouped updates for threaded notifications. Use [`didReceive(_:)`](https://developer.apple.com/documentation/WatchKit/WKUserNotificationInterfaceController/didReceive(_:)) instead.

## See Also

- [watchOS 5.3 Release Notes](watchos-5_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 5.1.3 Release Notes](watchos-5_1_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 5.1 Release Notes](watchos-5_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-5-release-notes)*