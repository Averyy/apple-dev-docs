# typeApplicationBundleID

**Framework**: Application Services

For specifying a target application by bundle ID.

#### Overview

This address mode is preferred for targeting specific applications. For example, you should target the Finder by sending an event whose target address descriptor uses the bundle ID `"com.apple.finder"` rather than the application signature `'MACS'`.

## Topics

### Constants
- [var typeApplicationBundleID: DescType](../coreservices/typeapplicationbundleid.md)
  Indicates a descriptor containing UTF-8 characters that specify the bundle ID of an application. Bundle IDs should be constructed similarly to `"com.company.directorylocation.ApplicationName"`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/1542896-typeapplicationbundleid)*