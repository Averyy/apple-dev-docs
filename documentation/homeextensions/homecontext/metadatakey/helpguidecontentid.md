# helpGuideContentId

**Framework**: HomeExtensions  
**Kind**: property  
**Role**: Type Property

The key for the content identifier of the help guide entry that a person opened.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
static let helpGuideContentId: String
```

#### Discussion

Use this value to distinguish entries when several help guide entries in your `metadata.json` file share one [`HomeAccessoryHelpGuide`](../../homeaccessoryhelpguide.md) identifier. The metadata omits this key if the entry has no `ContentId`.

## See Also

### Keys
- [static let accessoryErrorCode: String](./accessoryerrorcode.md)
  The key for the code of the accessory’s top error.
- [static let accessoryErrorDetails: String](./accessoryerrordetails.md)
  The key for additional details about the accessory’s top error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homecontext/metadatakey/helpguidecontentid)*