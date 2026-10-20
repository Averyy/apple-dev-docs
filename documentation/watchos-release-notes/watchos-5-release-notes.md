# watchOS 5 Release Notes

**Framework**: watchOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 5 SDK provides support for developing watchOS apps for Apple Watch devices running watchOS 5. For information about new features in watchOS 5, see [What’s New in watchOS](https://developer.apple.com/watchos/whats-new/). The SDK comes bundled with Xcode 10. For information about Xcode 10, see [Xcode 10 Release Notes](../Xcode-Release-Notes/xcode-10-release-notes.md).

##### Networking

###### New Features

- The [`URLSession`](../Foundation/urlsession.md) HTTP/2 implementation has been updated to support HTTP/2 connection reuse per RFC 7540 Section 9.1.1. This requires an HTTP/2 server to present a certificate which covers more than one server hostname. The certificate may use the Subject Alternative Name extension or wildcarded domain names. In addition, [`URLSession`](../Foundation/urlsession.md) requires name resolution to resolve the different hostnames to the same IP address. [`URLSession`](../Foundation/urlsession.md) might reuse HTTP/2 connections across different domain names when these conditions are satisfied. (37507838)

###### Deprecations

- The `ftp://` and `file://` URL schemes for Proxy Automatic Configuration (PAC) are deprecated. HTTP and HTTPS are the only supported URL schemes for PAC. This affects all PAC configurations including, but not limited to, configurations set via Settings, System Preferences, profiles, and [`URLSession`](../Foundation/urlsession.md) APIs such as [`connectionProxyDictionary`](../Foundation/urlsessionconfiguration/connectionproxydictionary.md), and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](../CFNetwork/cfnetworkexecuteproxyautoconfigurationurl%28_,_,_,_%29.md). (37811761)

##### WatchKit

###### New Features

- The tint color of a [`WKInterfaceVolumeControl`](../WatchKit/wkinterfacevolumecontrol.md) can now be set by calling the [`setTintColor(_:)`](../WatchKit/wkinterfacevolumecontrol/settintcolor%28_%29.md) method. (40565782)

###### Deprecations

- The [`updateUserActivity(_:userInfo:webpageURL:)`](../WatchKit/wkinterfacecontroller/updateuseractivity%28_,userinfo,webpageurl%29.md) method doesn’t properly register activities. Use [`update(_:)`](../WatchKit/wkinterfacecontroller/update%28_%29.md) instead. (39840960)
- The [`didReceive(_:withCompletion:)`](../WatchKit/wkusernotificationinterfacecontroller/didreceive%28_,withcompletion%29.md) method doesn’t receive grouped updates for threaded notifications. Use [`didReceive(_:)`](../WatchKit/wkusernotificationinterfacecontroller/didreceive%28_%29.md) instead.

## See Also

### watchOS 5
- [watchOS 5.3 Release Notes](./watchos-5_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 5.1.3 Release Notes](./watchos-5_1_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 5.1 Release Notes](./watchos-5_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-5-release-notes)*