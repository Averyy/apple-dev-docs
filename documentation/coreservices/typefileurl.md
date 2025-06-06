# typeFileURL

**Framework**: Core Services  
**Kind**: data

A file URL. That is, the associated data consists of the bytes of a UTF-8 encoded URL with a scheme of "file". This type is appropriate for describing a file that may not yet exist—see [`Technical Note 2022`](https://developer.apple.comhttp://developer.apple.com/technotes/tn/tn2022.html) for more information.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```swift
var typeFileURL: DescType { get }
```

#### Discussion

You can translate between a descriptor of this type and an instance of `CFURL` by calling [`CFURLCreateWithBytes(_:_:_:_:_:)`](https://developer.apple.com/documentation/corefoundation/cfurlcreatewithbytes(_:_:_:_:_:)) and specifying `kCFStringEncodingUTF8` for the encoding. Or, if you have a [`CFURL`](https://developer.apple.com/documentation/corefoundation/cfurl), you can call [`CFURLCreateData(_:_:_:_:)`](https://developer.apple.com/documentation/corefoundation/cfurlcreatedata(_:_:_:_:)) to get the data as an instance of `CFData` (again specifying an encoding of `kCFStringEncodingUTF8`), and[`CFDataGetBytes(_:_:_:)`](https://developer.apple.com/documentation/corefoundation/cfdatagetbytes(_:_:_:)) to get the actual bytes to insert into a descriptor of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/typefileurl)*