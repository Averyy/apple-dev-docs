# kVTMultiPassStorageCreationOption_DoNotDelete

**Framework**: Videotoolbox  
**Kind**: var

Indicates that the multipass storage object’s backing store should not be deleted when finalized.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTMultiPassStorageCreationOption_DoNotDelete: CFString
```

#### Discussion

If the backing store file did not exist when the storage was created, the file will be deleted when the multipass storage object is finalized, unless you set this option to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) in the options dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtmultipassstoragecreationoption_donotdelete)*