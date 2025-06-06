# kMDItemTextContent

**Framework**: Core Services  
**Kind**: data

Contains a text representation of the content of the document. Data in multiple fields should be combined using a whitespace character as a separator. A CFString.

**Availability**:
- macOS 10.4+

## Declaration

```swift
let kMDItemTextContent: CFString!
```

#### Discussion

An application's Spotlight importer provides the content of this attribute. Applications can search for values in this attribute, but are not able to read the content of this attribute directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kmditemtextcontent)*