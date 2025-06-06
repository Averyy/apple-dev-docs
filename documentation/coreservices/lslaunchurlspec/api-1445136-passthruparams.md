# passThruParams

**Framework**: Core Services  
**Kind**: structp

A pointer to an Apple event descriptor that is passed untouched as an optional parameter, with keyword `keyAEPropData` (`'prdt'`), in the Apple event sent to each application launched or activated (whether individual preferred applications or the application designated by `appURL`). See the  in the Carbon Interapplication Communication Documentation for a description of the `AEDesc` data type. The value of this field can be `NULL`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var passThruParams: UnsafePointer<AEDesc>?
```

## See Also

- [var appURL: Unmanaged<CFURL>?](lslaunchurlspec/1443566-appurl.md)
  A Core Foundation URL reference designating the application to launch; see the  in the Core Foundation Reference Documentation for a description of the `CFURLRef` data type.The URL must have scheme `file` and contain a valid path to an application file or application bundle. Set this field to `NULL` to request that each item in the `itemURLs` array be opened in its own preferred application.
- [var asyncRefCon: UnsafeMutableRawPointer?](lslaunchurlspec/1448168-asyncrefcon.md)
  A pointer to an arbitrary application-defined value, passed in the Carbon event notifying you of an application’s launch or termination (if you have registered for such notification). The value of this field can be `NULL`.
- [var itemURLs: Unmanaged<CFArray>?](lslaunchurlspec/1443759-itemurls.md)
  A reference to an array of Core Foundation URL references designating the item or items to open; see the  in the Core Foundation Reference Documentation for a description of the `CFArrayRef` data type. The value of this field can be `NULL`, in which case the application designated by `appURL` will be launched without opening any items.
- [var launchFlags: LSLaunchFlags](lslaunchurlspec/1443957-launchflags.md)
  Launch flags specifying how to launch each application (including whether to print or merely open documents); see [`LSLaunchFlags`](lslaunchflags.md) for a description of these flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lslaunchurlspec/1445136-passthruparams)*