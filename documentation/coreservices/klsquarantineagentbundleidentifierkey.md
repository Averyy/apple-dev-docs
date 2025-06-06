# kLSQuarantineAgentBundleIdentifierKey

**Framework**: Core Services  
**Kind**: data

The bundle identifier of the quarantining agent.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kLSQuarantineAgentBundleIdentifierKey: CFString
```

#### Discussion

When setting quarantine properties, the bundle identifier is set automatically to the main bundle identifier of the current process if the key is not present in the caller’s dictionary.

## See Also

- [let kLSQuarantineAgentNameKey: CFString](klsquarantineagentnamekey.md)
  The app name of the quarantining agent.
- [let kLSQuarantineTimeStampKey: CFString](klsquarantinetimestampkey.md)
  The date and time of the item’s quarantine.
- [let kLSQuarantineTypeKey: CFString](klsquarantinetypekey.md)
  A symbolic string identifying the reason for the quarantine.
- [let kLSQuarantineDataURLKey: CFString](klsquarantinedataurlkey.md)
  The actual URL of the quarantined item.
- [let kLSQuarantineOriginURLKey: CFString](klsquarantineoriginurlkey.md)
  The URL of the resource originally hosting the quarantined item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/klsquarantineagentbundleidentifierkey)*