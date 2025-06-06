# kMDItemContentType

**Framework**: Core Services  
**Kind**: data

The UTI pedigree of a file. A CFString.

**Availability**:
- macOS 10.4+

## Declaration

```swift
let kMDItemContentType: CFString!
```

#### Discussion

 For example, a jpeg image file will have a value of public.jpeg/public.image/public.data. The value of this attribute is set by the MDImporter. Changes to this value are lost when the file attributes are next imported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kmditemcontenttype)*