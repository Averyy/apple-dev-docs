# DOMApplicationCache

**Framework**: Webkitjs  
**Kind**: cl

A `DOMApplicationCache` object is used to store resources—such as, HTML, JavaScript, CSS, and images—locally. This allows your web application to continue running offline when there is no network connection. The cache persists after Safari exits, so it can be used by multiple browser sessions. There is one application cache per browsing context. 

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 2.1+

## Declaration

```swift
interface DOMApplicationCache
```

## Topics

### Accessing Properties
- [status](domapplicationcache/1634227-status.md)
  The current status of the application cache. One of the values described in "Constants.”
### Handling Events
- [onchecking](domapplicationcache/1634093-onchecking.md)
  Sent when the cache update process begins.
- [onerror](domapplicationcache/1629048-onerror.md)
  Sent when an error occurs.
- [onnoupdate](domapplicationcache/1631877-onnoupdate.md)
  Sent when the update process finishes but the manifest file does not change.
- [ondownloading](domapplicationcache/1632146-ondownloading.md)
  Sent when the update process begins downloading resources in the manifest file.
- [onprogress](domapplicationcache/1631599-onprogress.md)
  Sent when each resource in the manifest file begins to download.
- [onupdateready](domapplicationcache/1629348-onupdateready.md)
  Sent when there is an existing application cache, the update process finishes, and there is a new application cache ready for use.
- [oncached](domapplicationcache/1632145-oncached.md)
  Sent when the update process finishes for the first time—that is, the first time an application cache is saved.
### Updating the Cache
- [add](domapplicationcache/1804703-add.md)
  Forthcoming
- [update](domapplicationcache/1632530-update.md)
  Manually triggers the update process.
- [swapCache](domapplicationcache/1633375-swapcache.md)
  Replaces the active cache with the latest version.
### Constants
- [UNCACHED](domapplicationcache/1632990-uncached.md)
  The object isn’t associated with an application cache. This can occur if the update process fails and there is no previous cache to revert to, or if there is no manifest file.
- [IDLE](domapplicationcache/1633733-idle.md)
  The cache is idle.
- [CHECKING](domapplicationcache/1629519-checking.md)
  The update has started but the resources are not downloaded yet—for example, this can happen when the manifest file is fetched.
- [DOWNLOADING](domapplicationcache/1630071-downloading.md)
  The resources are being downloaded into the cache.
- [UPDATEREADY](domapplicationcache/1630598-updateready.md)
  Resources have finished downloading and the new cache is ready to be used.
### Instance Properties
- [onobsolete](domapplicationcache/1631339-onobsolete.md)
### Instance Methods
- [abort](domapplicationcache/1630974-abort.md)
### Miscellaneous
- [OBSOLETE](domapplicationcache/1629288-obsolete.md)

## Relationships

### Inherits From
- [EventTarget](../tvmljs/eventtarget.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/domapplicationcache)*