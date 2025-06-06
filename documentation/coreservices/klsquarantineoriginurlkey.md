# kLSQuarantineOriginURLKey

**Framework**: Coreservices  
**Kind**: data

The URL of the resource originally hosting the quarantined item.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kLSQuarantineOriginURLKey: CFString
```

#### Discussion

For web downloads, this property is the URL of the web page on which the user initiated the download. For attachments, this property is the URL of the resource to which the quarantined item was attached (e.g. the email message, calendar event, etc.). The origin URL may be a file URL for local resources, or a custom URL to which the quarantining app will respond when asked to open it. The quarantining app should respond by displaying the resource to the user. 

> **Note**: The origin URL should not be set to the data URL, or the quarantining app may start downloading the file again if the user choses to view the origin URL while resolving a quarantine warning.

## See Also

- [let kLSQuarantineAgentBundleIdentifierKey: CFString](klsquarantineagentbundleidentifierkey.md)
  The bundle identifier of the quarantining agent.
- [let kLSQuarantineAgentNameKey: CFString](klsquarantineagentnamekey.md)
  The app name of the quarantining agent.
- [let kLSQuarantineTimeStampKey: CFString](klsquarantinetimestampkey.md)
  The date and time of the item’s quarantine.
- [let kLSQuarantineTypeKey: CFString](klsquarantinetypekey.md)
  A symbolic string identifying the reason for the quarantine.
- [let kLSQuarantineDataURLKey: CFString](klsquarantinedataurlkey.md)
  The actual URL of the quarantined item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/klsquarantineoriginurlkey)*