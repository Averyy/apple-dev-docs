# typeFileURL

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

A file URL. That is, the associated data consists of the bytes of a UTF-8 encoded URL with a scheme of "file". This type is appropriate for describing a file that may not yet exist—see [Technical Note 2022](http://developer.apple.com/technotes/tn/tn2022.html) for more information.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
typeFileURL = 'furl'
```

#### Discussion

You can translate between a descriptor of this type and an instance of `CFURL` by calling [`CFURLCreateWithBytes(_:_:_:_:_:)`](../../CoreFoundation/cfurlcreatewithbytes%28_,_,_,_,_%29.md) and specifying `kCFStringEncodingUTF8` for the encoding. Or, if you have a [`CFURL`](../../CoreFoundation/cfurl.md), you can call [`CFURLCreateData(_:_:_:_:)`](../../CoreFoundation/cfurlcreatedata%28_,_,_,_%29.md) to get the data as an instance of `CFData` (again specifying an encoding of `kCFStringEncodingUTF8`), and[`CFDataGetBytes(_:_:_:)`](../../CoreFoundation/cfdatagetbytes%28_,_,_%29.md) to get the actual bytes to insert into a descriptor of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants/typefileurl)*