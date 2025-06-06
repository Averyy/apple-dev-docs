# kLSQuarantineTimeStampKey

**Framework**: Core Services  
**Kind**: data

The date and time of the item’s quarantine.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kLSQuarantineTimeStampKey: CFString
```

#### Discussion

When setting quarantine properties, this property is set automatically to the current date and time if this key is not present in the caller’s dictionary.

## See Also

- [let kLSQuarantineAgentBundleIdentifierKey: CFString](klsquarantineagentbundleidentifierkey.md)
  The bundle identifier of the quarantining agent.
- [let kLSQuarantineAgentNameKey: CFString](klsquarantineagentnamekey.md)
  The app name of the quarantining agent.
- [let kLSQuarantineTypeKey: CFString](klsquarantinetypekey.md)
  A symbolic string identifying the reason for the quarantine.
- [let kLSQuarantineDataURLKey: CFString](klsquarantinedataurlkey.md)
  The actual URL of the quarantined item.
- [let kLSQuarantineOriginURLKey: CFString](klsquarantineoriginurlkey.md)
  The URL of the resource originally hosting the quarantined item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/klsquarantinetimestampkey)*