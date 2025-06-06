# Remote Process Dictionary Keys

**Framework**: Application Services

Used to extract information from dictionaries with entries that describe remote processes.

## Topics

### Constants
- [let kAERemoteProcessURLKey: CFString!](../coreservices/kaeremoteprocessurlkey.md)
  Use this key to obtain the full URL to the remote process, as a `CFURLRef`.
- [let kAERemoteProcessNameKey: CFString!](../coreservices/kaeremoteprocessnamekey.md)
  Use this key to obtain the visible name of the remote process, in the localization supplied by the server, as a `CFStringRef`.
- [let kAERemoteProcessUserIDKey: CFString!](../coreservices/kaeremoteprocessuseridkey.md)
  Use this key to obtain the user ID of the remote process, if available; if so, returned as a `CFNumberRef`.
- [let kAERemoteProcessProcessIDKey: CFString!](../coreservices/kaeremoteprocessprocessidkey.md)
  Use this key to obtain the process ID of the remote process, if available; if so, returned as a `CFNumberRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/remote_process_dictionary_keys)*